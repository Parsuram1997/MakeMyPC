"""
Fix duplicate Shipping button in product pages and other non-admin pages.
Removes the unlinked href="#" Shipping and keeps only href="admin-shipping.html" one.
Also checks for any other sidebar issues across all these pages.
"""

import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"

# All pages with sidebars (non-admin) to check
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
    "custom-pc-builder.html",
]

# Exact duplicate Shipping block to remove (href="#" + local_shipping icon)
DUPLICATE_SHIPPING_CRLF = (
    '        <a href="#" class="flex items-center gap-3 px-4 py-1.5 rounded-xl'
    ' transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\r\n'
    '            <span class="material-symbols-outlined">local_shipping</span>\r\n'
    '            <span class="text-body-sm font-medium">Shipping</span>\r\n'
    '        </a>\r\n'
)

DUPLICATE_SHIPPING_LF = (
    '        <a href="#" class="flex items-center gap-3 px-4 py-1.5 rounded-xl'
    ' transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\n'
    '            <span class="material-symbols-outlined">local_shipping</span>\n'
    '            <span class="text-body-sm font-medium">Shipping</span>\n'
    '        </a>\n'
)

fixed = []
clean = []

for fname in TARGET_PAGES:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Count Shipping occurrences in sidebar
    aside = re.search(r"<aside.*?</aside>", content, re.DOTALL)
    if not aside:
        print(f"  [NO ASIDE] {fname}")
        continue

    sidebar = aside.group(0)
    ship_count = sidebar.count("Shipping")
    has_real = 'href="admin-shipping.html"' in sidebar and "local_shipping" in sidebar

    if ship_count >= 2 and has_real:
        # Remove the unlinked duplicate
        new_content = content.replace(DUPLICATE_SHIPPING_CRLF, "", 1)
        if new_content == content:
            new_content = content.replace(DUPLICATE_SHIPPING_LF, "", 1)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            fixed.append(fname)
            print(f"  [FIXED] {fname} - removed duplicate Shipping (was x{ship_count})")
        else:
            # Try regex approach for slight whitespace variation
            new_content = re.sub(
                r'        <a href="#" class="flex items-center gap-3 px-4 py-1\.5 rounded-xl'
                r' transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\s*'
                r'<span class="material-symbols-outlined">local_shipping</span>\s*'
                r'<span class="text-body-sm font-medium">Shipping</span>\s*'
                r'</a>\r?\n',
                "",
                content,
                count=1
            )
            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed.append(fname)
                print(f"  [FIXED-REGEX] {fname}")
            else:
                print(f"  [WARN] {fname} - ship_count={ship_count} but pattern not matched")
    elif ship_count == 1:
        clean.append(fname)
        print(f"  [CLEAN] {fname} - Shipping x1 (OK)")
    elif ship_count == 0:
        clean.append(fname)
        print(f"  [CLEAN] {fname} - no Shipping (OK)")
    else:
        print(f"  [SKIP] {fname} - ship_count={ship_count}, has_real={has_real}")

print(f"\nDone. Fixed {len(fixed)}, clean {len(clean)}.")

# Final verification
print("\n--- FINAL CHECK ---")
for fname in TARGET_PAGES:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    aside = re.search(r"<aside.*?</aside>", content, re.DOTALL)
    if not aside:
        continue
    sidebar = aside.group(0)
    count = sidebar.count("Shipping")
    status = "OK" if count <= 1 else f"STILL DUPLICATE x{count}"
    print(f"  {fname}: Shipping x{count} => {status}")
