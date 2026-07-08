import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the dropdown block and tighten the vertical spacing extremely
    # Currently it has: class="... p-1.5 flex flex-col gap-0.5"
    # And the links have: class="... px-3 py-1.5 rounded-lg ..."
    
    # We will target specifically the Profile Settings, Security, Preferences, Sign out links
    
    def reduce_padding(match):
        text = match.group(0)
        # reduce container padding and gap
        text = text.replace('p-1.5 flex flex-col gap-0.5', 'p-1 flex flex-col gap-0')
        # reduce vertical padding on links
        text = text.replace('py-1.5 rounded-lg', 'py-0.5 rounded-lg')
        # reduce my-1 to my-0.5 for the divider
        text = text.replace('my-1 mx-2', 'my-0.5 mx-2')
        return text

    new_content = re.sub(
        r'<div class="bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl p-1.5 flex flex-col gap-0.5">.*?</div>\s*</details>',
        reduce_padding,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Tightened profile spacing in {fname}")

print(f"Total files updated: {count}")
