"""
Fix: Reduce excessive vertical spacing in admin sidebar across ALL admin HTML pages.

Changes:
  - nav gap-2 -> gap-0.5
  - nav item py-3 -> py-1.5  (all <a> and <summary> in nav)
  - submenu items py-2 -> py-1
  - aside py-6 -> py-4
  - logo mb-8 -> mb-4
  - section label mt-6 mb-2 -> mt-3 mb-1
"""

import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"

def fix_sidebar_spacing(content):
    changed = False

    # 1. nav gap: flex flex-col gap-2 px-4 flex-1 -> gap-0.5
    new = content.replace(
        'class="flex flex-col gap-2 px-4 flex-1 overflow-y-auto custom-scrollbar pb-6"',
        'class="flex flex-col gap-0.5 px-4 flex-1 overflow-y-auto custom-scrollbar pb-4"'
    )
    if new != content: changed = True
    content = new

    # 2. aside py-6 -> py-4
    new = content.replace(
        'class="h-screen w-64 fixed left-0 top-0 border-r border-white/10 bg-surface-deep z-50 flex flex-col py-6"',
        'class="h-screen w-64 fixed left-0 top-0 border-r border-white/10 bg-surface-deep z-50 flex flex-col py-4"'
    )
    if new != content: changed = True
    content = new

    # 3. Logo wrapper mb-8 -> mb-4
    new = content.replace(
        'class="px-6 mb-8 shrink-0"',
        'class="px-6 mb-4 shrink-0"'
    )
    if new != content: changed = True
    content = new

    # 4. All plain nav <a> items: py-3 rounded-xl -> py-1.5 rounded-lg (both normal and active states)
    # Pattern: px-4 py-3 rounded-xl (nav items)
    new = re.sub(
        r'(class="flex items-center gap-3 px-4 )py-3( rounded-xl)',
        r'\1py-1.5\2',
        content
    )
    if new != content: changed = True
    content = new

    # 5. <summary> items: px-4 py-3 rounded-xl cursor-pointer
    new = re.sub(
        r'(class="flex items-center justify-between px-4 )py-3( rounded-xl cursor-pointer)',
        r'\1py-1.5\2',
        content
    )
    if new != content: changed = True
    content = new

    # 6. Submenu child items: py-2 rounded-lg -> py-1 rounded-lg
    # These are the <a> links inside the details dropdown divs
    new = re.sub(
        r'(class="(?:text-sm|text-[a-z\[\]0-9]+) (?:text-on-surface-variant|text-primary)[^"]*?px-4 )py-2( rounded-lg)',
        r'\1py-1\2',
        content
    )
    if new != content: changed = True
    content = new

    # 7. Section label spacing: mt-6 mb-2 -> mt-3 mb-1
    new = content.replace(
        'class="px-4 mt-6 mb-2"',
        'class="px-4 mt-3 mb-1"'
    )
    if new != content: changed = True
    content = new

    # 8. Active state items that also have py-3
    new = re.sub(
        r'(class="flex items-center gap-3 px-4 )py-3( rounded-xl[^"]*bg-primary/10)',
        r'\1py-1.5\2',
        content
    )
    if new != content: changed = True
    content = new

    # 9. mt-auto mb-4 Settings item (has extra margin)
    new = content.replace(
        'rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary mt-auto mb-4',
        'rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary mt-auto mb-2'
    )
    if new != content: changed = True
    content = new

    return content, changed

fixed_files = []
skipped_files = []

for fname in os.listdir(PAGES_DIR):
    if not (fname.startswith("admin-") and fname.endswith(".html")):
        continue

    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, changed = fix_sidebar_spacing(content)

    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_files.append(fname)
        print(f"  [FIXED] {fname}")
    else:
        skipped_files.append(fname)
        print(f"  [SKIP]  {fname}")

print(f"\nDone. Fixed {len(fixed_files)}, skipped {len(skipped_files)}.")
