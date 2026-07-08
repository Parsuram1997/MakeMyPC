"""
Fix sidebar vertical spacing in ALL non-admin pages that have a sidebar.
Applies the same compact spacing as admin pages.
"""

import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"

# Pages to fix (non-admin pages with sidebar spacing issues)
TARGET_PAGES = [
    "product-add.html",
    "product-inventory.html",
    "product-categories.html",
    "product-brands.html",
    "product-compatibility.html",
    "product-reviews.html",
    "compatibility-manager.html",
    "account-settings.html",
    "compare-products.html",
    "my-builds.html",
    "submit-ticket.html",
]

def fix_sidebar_spacing(content):
    changed = False

    # 1. nav gap-2 -> gap-0.5, pb-6 -> pb-4
    new = re.sub(
        r'(class="flex flex-col )gap-2( px-4 flex-1 overflow-y-auto[^"]*)"',
        r'\1gap-0.5\2"',
        content
    )
    if new != content: changed = True; content = new

    # 2. aside py-6 -> py-4
    new = re.sub(
        r'(<aside[^>]*?)py-6([^>]*?>)',
        r'\1py-4\2',
        content
    )
    if new != content: changed = True; content = new

    # 3. Logo wrapper mb-8 -> mb-4
    new = content.replace('class="px-6 mb-8 shrink-0"', 'class="px-6 mb-4 shrink-0"')
    if new != content: changed = True; content = new

    # Also handle px-4 mb-8
    new = content.replace('class="px-4 mb-8 shrink-0"', 'class="px-4 mb-4 shrink-0"')
    if new != content: changed = True; content = new

    # 4. Nav items: px-4 py-3 rounded-xl -> px-4 py-1.5 rounded-xl
    new = re.sub(
        r'(class="flex items-center[^"]*?px-4 )py-3( rounded-xl)',
        r'\1py-1.5\2',
        content
    )
    if new != content: changed = True; content = new

    # 5. Summary items: px-4 py-3 rounded-xl cursor-pointer
    new = re.sub(
        r'(class="flex items-center justify-between px-4 )py-3( rounded-xl cursor-pointer)',
        r'\1py-1.5\2',
        content
    )
    if new != content: changed = True; content = new

    # 6. Submenu child items: px-4 py-2 rounded-lg -> px-4 py-1 rounded-lg
    new = re.sub(
        r'(px-4 )py-2( rounded-lg[^"]*(?:transition|block|hover)[^"]*")',
        r'\1py-1\2',
        content
    )
    if new != content: changed = True; content = new

    # Also handle: text-sm ... px-4 py-2 rounded-lg
    new = re.sub(
        r'( px-4 )py-2( rounded-lg(?:\s+transition-colors\s+block)?)',
        r'\1py-1\2',
        content
    )
    if new != content: changed = True; content = new

    # 7. Section labels: mt-6 mb-2 -> mt-3 mb-1
    new = content.replace('class="px-4 mt-6 mb-2"', 'class="px-4 mt-3 mb-1"')
    if new != content: changed = True; content = new

    new = content.replace('"px-4 mt-6 mb-2"', '"px-4 mt-3 mb-1"')
    if new != content: changed = True; content = new

    # 8. pb-6 in nav -> pb-4
    new = re.sub(
        r'(overflow-y-auto[^"]*?)pb-6',
        r'\1pb-4',
        content
    )
    if new != content: changed = True; content = new

    return content, changed


fixed_files = []
skipped_files = []

for fname in TARGET_PAGES:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  [MISSING] {fname}")
        continue

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

# Final verification
print("\n--- VERIFICATION ---")
for fname in TARGET_PAGES:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    aside_match = re.search(r'<aside.*?</aside>', content, re.DOTALL)
    if not aside_match:
        print(f"{fname}: no aside")
        continue
    sidebar = aside_match.group(0)
    issues = []
    if 'py-3' in sidebar: issues.append('py-3')
    if 'gap-2' in sidebar: issues.append('gap-2')
    if 'py-6' in sidebar: issues.append('py-6')
    if 'mb-8' in sidebar: issues.append('mb-8')
    if ' py-2 rounded-lg' in sidebar: issues.append('py-2')
    if 'mt-6 mb-2' in sidebar: issues.append('mt-6')
    status = "ISSUES: " + str(issues) if issues else "CLEAN"
    print(f"  {fname}: {status}")
