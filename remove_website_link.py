import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # The regex matches the full <a> tag that contains 'language' and 'Website'
    # We will remove the whole <a> tag.
    new_content = re.sub(
        r'<a[^>]*>\s*<span[^>]*>language</span>\s*<span[^>]*>Website</span>\s*</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed Website link from {fname}")

print(f"Total files updated: {count}")
