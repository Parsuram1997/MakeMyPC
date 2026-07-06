"""
remove_orphan_nav_junk.py
--------------------------
Removes two specific orphan blocks left over from old nav scripts:

BLOCK A (lines after <!-- ═══ NAVBAR END ═══ -->):
  <!-- TopNavBar -->
  <div class="flex flex-col gap-6 ..."> ... </div></div>

BLOCK B (old Mobile Menu Logic script):
  <script>
      // Mobile Menu Logic
      document.addEventListener('DOMContentLoaded', ...
  </script>
"""

import os, glob, re

SKIP_FILES = {
    'admin-dashboard.html',
    'admin-dashboard-overview.html',
    'orders-management.html',
    'product-management.html',
}

# Pattern A: <!-- TopNavBar --> ... </div>\n</div>
# This is the leftover mobile menu body content visible on desktop
PATTERN_A = re.compile(
    r'\s*<!--\s*TopNavBar\s*-->\r?\n'
    r'<div class="flex flex-col gap-6[^"]*"[^>]*>.*?</div>\r?\n</div>',
    re.DOTALL
)

# Pattern B: Old "Mobile Menu Logic" script
PATTERN_B = re.compile(
    r'\r?\n?<script>\r?\n\s*// Mobile Menu Logic\r?\n.*?</script>',
    re.DOTALL
)

html_files = sorted(glob.glob('c:/Projects/MakeMyPC/*.html'))
changed = 0
skipped = 0

for fpath in html_files:
    basename = os.path.basename(fpath)
    if basename in SKIP_FILES:
        skipped += 1
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove Block A
    content = PATTERN_A.sub('', content)

    # Remove Block B
    content = PATTERN_B.sub('', content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  CLEANED  {basename}")
        changed += 1
    else:
        print(f"  clean    {basename}")

print(f"\nDone. {changed} files had orphan junk removed, {skipped} skipped.")
