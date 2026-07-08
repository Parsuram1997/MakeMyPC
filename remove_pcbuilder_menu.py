import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to remove the entire PC Builder <details> block
    # Pattern: <details class="group" name="sidebar-menu"...> ... <span class="...">PC Builder</span> ... </details>
    
    def remove_pcbuilder_block(match):
        return "" # Remove the whole block

    new_content = re.sub(
        r'<details[^>]*name="sidebar-menu"[^>]*>\s*<summary[^>]*>.*?<span[^>]*>PC Builder</span>.*?</details>\s*',
        remove_pcbuilder_block,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed PC Builder menu from {fname}")

print(f"Total files updated: {count}")
