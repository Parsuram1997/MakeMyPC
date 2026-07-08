import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    def filter_details(match):
        block = match.group(0)
        # Verify it is actually the PC Builder dropdown (and not some other details that happens to contain the text)
        if '>PC Builder</span>' in block and 'class="material-symbols-outlined' in block:
            return '' # delete it
        return block

    new_content = re.sub(
        r'<details[^>]*>.*?</details>',
        filter_details,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed PC Builder menu from {fname}")

print(f"Total files updated: {count}")
