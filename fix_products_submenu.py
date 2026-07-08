"""
Fix: Replace old-style broken Products submenu (with product-management.html and href="#")
with the correct Products submenu using real existing pages.
Affects: admin-dashboard.html, admin-assembly.html, admin-coupons.html,
         admin-dashboard-overview.html, admin-marketing.html, admin-payments.html, admin-shipping.html
"""

import os

PAGES_DIR = r"c:\Projects\MakeMyPC"

OLD_PRODUCTS_DIV = '''            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="product-management.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">All Products</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Categories</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Brands</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Inventory</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Compatibility</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Reviews</a>
            </div>'''

NEW_PRODUCTS_DIV = '''            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="product-add.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Add Product
                </a>
                <a href="product-inventory.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Inventory
                </a>
                <a href="product-categories.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Categories
                </a>
                <a href="product-brands.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Brands
                </a>
                <a href="product-compatibility.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Compatibility
                </a>
                <a href="product-reviews.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Reviews
                </a>
            </div>'''

fixed = []

for fname in os.listdir(PAGES_DIR):
    if not (fname.startswith("admin-") and fname.endswith(".html")):
        continue
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if OLD_PRODUCTS_DIV in content:
        content = content.replace(OLD_PRODUCTS_DIV, NEW_PRODUCTS_DIV, 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        fixed.append(fname)
        print(f"  [FIXED] {fname}")
    else:
        print(f"  [SKIP]  {fname}")

print(f"\nDone. Fixed {len(fixed)} file(s).")
