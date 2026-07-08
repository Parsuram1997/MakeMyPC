import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add style="row-gap:2px" to nav if missing
    new_content = re.sub(
        r'<nav\s+class="flex flex-col gap-0\.5 px-4 flex-1 overflow-y-auto custom-scrollbar pb-4"(?!\s*style=)>',
        '<nav class="flex flex-col gap-0.5 px-4 flex-1 overflow-y-auto custom-scrollbar pb-4" style="row-gap:2px">',
        content
    )
    
    # 2. Fix old submenu divs (space-y-1, gap-1, padding, margins)
    # Old variant 1: ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2
    # Old variant 2: flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2
    # We want ALL submenu wrappers to be: ml-6 pl-4 border-l border-white/10 flex flex-col space-y-0.5 mt-0.5 mb-1
    # But wait, we can just replace anything matching space-y-1 mt-1 mb-2
    new_content = re.sub(
        r'class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1[^"]*"',
        'class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-0.5 mt-0.5 mb-1"',
        new_content
    )
    new_content = re.sub(
        r'class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2"',
        'class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-0.5 mt-0.5 mb-1"',
        new_content
    )
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Fixed spacing in {fname}")

print(f"Total files updated: {count}")
