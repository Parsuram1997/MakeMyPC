import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Base replace for ALL pages to default inactive state
    new_content = content.replace(
        'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-white bg-primary">\n            <span class="material-symbols-outlined">manage_accounts</span>',
        'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\n            <span class="material-symbols-outlined">manage_accounts</span>'
    )
    
    # Also handle the case where it might be on a single line or slightly different spacing
    new_content = re.sub(
        r'class="[^"]*text-white bg-primary[^"]*"(>\s*<span[^>]*>manage_accounts)',
        r'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary"\1',
        new_content
    )

    # If this is the admin-users.html page, make it the standard active state
    if fname == 'admin-users.html':
        new_content = re.sub(
            r'class="[^"]*text-on-surface-variant hover:bg-white/5 hover:text-primary[^"]*"(>\s*<span[^>]*>manage_accounts)',
            r'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 bg-primary/10 text-primary"\1',
            new_content
        )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Fixed Admin Users button style in {fname}")

print(f"Total files updated: {count}")
