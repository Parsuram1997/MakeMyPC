import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # The regex matches the full <a> tag that contains 'shield_person' and 'Roles & Permissions'
    new_content = re.sub(
        r'<a[^>]*>\s*<span[^>]*>shield_person</span>\s*<span[^>]*>Roles &amp; Permissions</span>\s*</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Some files might have 'Roles & Permissions' without the &amp; html entity
    new_content = re.sub(
        r'<a[^>]*>\s*<span[^>]*>shield_person</span>\s*<span[^>]*>Roles & Permissions</span>\s*</a>',
        '',
        new_content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed Roles & Permissions link from {fname}")

print(f"Total files updated: {count}")
