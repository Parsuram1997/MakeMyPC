"""
Fix: Remove the duplicate unlinked Shipping button (href="#") from all admin sidebars.
The correct one (href="admin-shipping.html") is kept.
"""

import os

PAGES_DIR = r"c:\Projects\MakeMyPC"

# The broken/duplicate Shipping entry with href="#" — exact string to remove
DUPLICATE_SHIPPING = '''        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>\r\n'''

# Same but with \n line endings (just in case)
DUPLICATE_SHIPPING_LF = '''        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>\n'''

fixed_files = []
skipped_files = []

for fname in os.listdir(PAGES_DIR):
    if not (fname.startswith("admin-") and fname.endswith(".html")):
        continue

    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if both a duplicate (href="#") and the real (href="admin-shipping.html") exist
    has_duplicate = 'href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\r\n            <span class="material-symbols-outlined">local_shipping</span>' in content or \
                    'href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\n            <span class="material-symbols-outlined">local_shipping</span>' in content
    has_real = 'href="admin-shipping.html"' in content and 'local_shipping' in content

    if has_duplicate and has_real:
        # Remove the unlinked duplicate (CRLF version)
        new_content = content.replace(DUPLICATE_SHIPPING, "", 1)
        if new_content == content:
            # Try LF version
            new_content = content.replace(DUPLICATE_SHIPPING_LF, "", 1)
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            fixed_files.append(fname)
            print(f"  [FIXED] {fname}")
        else:
            print(f"  [WARN]  {fname} - could not match exact string, skipping")
            skipped_files.append(fname)
    elif has_duplicate and not has_real:
        # Only duplicate exists — fix its href to point to admin-shipping.html
        new_content = content.replace(
            'href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\r\n            <span class="material-symbols-outlined">local_shipping</span>\r\n            <span class="text-body-sm font-medium">Shipping</span>',
            'href="admin-shipping.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\r\n            <span class="material-symbols-outlined">local_shipping</span>\r\n            <span class="text-body-sm font-medium">Shipping</span>',
            1
        )
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            fixed_files.append(fname + " [href fixed]")
            print(f"  [HREF-FIXED] {fname}")
        else:
            skipped_files.append(fname)
    else:
        skipped_files.append(fname)

print(f"\nDone. Fixed {len(fixed_files)} file(s), skipped {len(skipped_files)}.")
if fixed_files:
    print("Fixed:")
    for f in fixed_files:
        print(f"  - {f}")
if skipped_files:
    print("Skipped (already correct or no match):")
    for f in skipped_files:
        print(f"  - {f}")
