"""
clean_orphan_mobile_content.py
-------------------------------
Removes orphan legacy mobile menu content that got left behind in all pages.

The old v1 script left behind this pattern after the </nav> tag:
- <!-- TopNavBar --> comment + dangling div with flex-col gap-6 content
- Old <script> Mobile Menu Logic blocks
These need to be removed from all public pages.
"""

import os, glob, re

# Files to process
SKIP_FILES = {
    'admin-dashboard.html',
    'admin-dashboard-overview.html',
    'orders-management.html',
    'product-management.html',
}

# Pattern 1: The orphan div block (Search + Shop/Builder/Resources links without a wrapper)
# Matches: <!-- TopNavBar --> ... </div></div> block that's the old mobile menu body
ORPHAN_PATTERN_1 = re.compile(
    r'\s*<!--\s*TopNavBar\s*-->\s*'
    r'<div[^>]*flex[^>]*flex-col[^>]*gap-6[^>]*>.*?</div>\s*</div>',
    re.DOTALL
)

# Pattern 2: Old mobile menu script block (Mobile Menu Logic with classList)
ORPHAN_SCRIPT_PATTERN = re.compile(
    r'<script>\s*\n\s*//\s*Mobile Menu Logic\s*\n\s*document\.addEventListener.*?</script>',
    re.DOTALL
)

# Pattern 3: Catch any stray old mobile-menu div that has the OLD format (class-based)
# These are divs OUTSIDE of our new NAVBAR block that contain the old menu body
STRAY_MENU_PATTERN = re.compile(
    r'(?<=<!-- \u2550\u2550\u2550 NAVBAR END \u2550\u2550\u2550 -->)\s*'  # after our nav end marker
    r'.*?'
    r'(?=<main\b|<section\b|<div\s+class="[^"]*(?:breadcrumb|container|page|wrapper)|<!--\s*(?:Main|Page|Content))',
    re.DOTALL
)

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')
changed = 0
skipped = 0
errors  = []

for fpath in sorted(html_files):
    basename = os.path.basename(fpath)
    if basename in SKIP_FILES:
        skipped += 1
        continue

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Remove orphan TopNavBar comment + div block
        content = ORPHAN_PATTERN_1.sub('', content)

        # Remove old Mobile Menu Logic script
        content = ORPHAN_SCRIPT_PATTERN.sub('', content)

        # More aggressive: find NAVBAR END marker and remove everything between it
        # and the next meaningful tag (<main, breadcrumb wrapper, etc.)
        nav_end_idx = content.find('<!-- ═══ NAVBAR END ═══ -->')
        if nav_end_idx != -1:
            after_nav = nav_end_idx + len('<!-- ═══ NAVBAR END ═══ -->')
            rest = content[after_nav:]

            # Find where real content starts
            # Look for <main, or a <div that has a breadcrumb/page class, or a known section
            real_content_match = re.search(
                r'(?=<main\b|<section\b(?!\s+id=["\']mobile)|'
                r'<div[^>]*(?:max-w-container|pb-20|page-wrapper|content-wrapper|breadcrumb|mx-auto px-)[^>]*>)',
                rest
            )

            if real_content_match:
                garbage = rest[:real_content_match.start()]
                # Only strip if it's whitespace/comments/old menu divs (not real content)
                # Check it doesn't contain important tags
                has_important = re.search(r'<(?:form|table|article|header|aside|footer)\b', garbage)
                if not has_important:
                    cleaned_garbage = re.sub(
                        r'<div[^>]*(?:flex-col|mobile|menu)[^>]*>.*?</div>|'
                        r'<script>.*?</script>|'
                        r'<!--[^>]*-->|'
                        r'\s+',
                        lambda m: '\n' if m.group().strip() == '' else '',
                        garbage,
                        flags=re.DOTALL
                    )
                    content = content[:after_nav] + '\n\n' + content[after_nav + real_content_match.start():]

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  CLEANED  {basename}")
            changed += 1
        else:
            print(f"  NO CHANGE  {basename}")

    except Exception as e:
        errors.append(f"{basename}: {e}")
        import traceback; traceback.print_exc()

print(f"\nDone. {changed} files cleaned, {skipped} skipped.")
if errors:
    for e in errors: print(f"  ERROR: {e}")
