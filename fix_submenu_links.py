"""
Fix: Update all submenu hrefs in admin sidebar across ALL admin HTML pages.
Maps broken href="#" links to their correct existing pages,
and removes submenu items that have no corresponding page.
"""

import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"

# ─────────────────────────────────────────────────────────────────────────────
# FULL CORRECT SIDEBAR SUBMENUS
# These are the canonical versions to replace the broken ones.
# ─────────────────────────────────────────────────────────────────────────────

# ── PRODUCTS submenu (all already correct, just normalize style)
OLD_PRODUCTS_DIV = '''            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
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

# ── PC BUILDER submenu — old broken version (all href="#")
OLD_PCBUILDER_DIV = '''            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Custom Builds</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Saved Builds</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Compatibility Engine</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Featured Builds</a>
            </div>'''

# ── PC BUILDER submenu — correct version with real links
NEW_PCBUILDER_DIV = '''            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="custom-pc-builder.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Custom Builder
                </a>
                <a href="admin-saved-builds.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Saved Builds
                </a>
                <a href="compatibility-manager.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Compatibility Engine
                </a>
                <a href="smart-builder.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Smart Builder
                </a>
            </div>'''

# ── ORDERS submenu — old broken version (most href="#")
OLD_ORDERS_DIV = '''            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="orders-management.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">All Orders</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Custom PC</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Components</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Ready PCs</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Laptops</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Returns</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Refunds</a>
            </div>'''

# ── ORDERS submenu — correct version (only link to pages that exist)
NEW_ORDERS_DIV = '''            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    All Orders
                </a>
                <a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Order History
                </a>
                <a href="order-tracking.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Order Tracking
                </a>
            </div>'''

# ─────────────────────────────────────────────────────────────────────────────
# Process all admin pages
# ─────────────────────────────────────────────────────────────────────────────
fixed_files = []

for fname in os.listdir(PAGES_DIR):
    if not (fname.startswith("admin-") and fname.endswith(".html")):
        continue

    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # Fix PC Builder submenu
    if OLD_PCBUILDER_DIV in content:
        content = content.replace(OLD_PCBUILDER_DIV, NEW_PCBUILDER_DIV, 1)
        changes.append("PC Builder submenu")

    # Fix Orders submenu
    if OLD_ORDERS_DIV in content:
        content = content.replace(OLD_ORDERS_DIV, NEW_ORDERS_DIV, 1)
        changes.append("Orders submenu")

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        fixed_files.append((fname, changes))
        print(f"  [FIXED] {fname} => {', '.join(changes)}")
    else:
        print(f"  [SKIP]  {fname}")

print(f"\nDone. Fixed {len(fixed_files)} file(s).")
