import os
import re

ADMIN_FILES = [
    "admin-dashboard.html",
    "admin-dashboard-overview.html",
    "product-management.html",
    "orders-management.html"
]

PRODUCTS_NAV = """
        <details class="group" open>
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">inventory_2</span>
                    <span class="text-body-sm font-medium">Products</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="product-management.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">All Products</a>
                <a href="product-add.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Add Product</a>
                <a href="product-categories.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Categories</a>
                <a href="product-brands.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Brands</a>
                <a href="product-inventory.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Inventory</a>
                <a href="product-compatibility.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Compatibility</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Reviews</a>
            </div>
        </details>
"""

# 1. Update Navigation across existing files
for file in ADMIN_FILES:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to replace the <details> block for Products
        pattern = r'<details class="group">(?:\s*<summary.*?>.*?Products.*?</summary>\s*<div.*?>.*?</div>\s*)</details>'
        new_content = re.sub(pattern, PRODUCTS_NAV.strip(), content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

# 2. Modify product-management.html
if os.path.exists("product-management.html"):
    with open("product-management.html", 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove header
    header_pattern = r'<!-- Top Navigation Bar -->\s*<header.*?</header>'
    content = re.sub(header_pattern, '', content, flags=re.DOTALL)
    
    # Remove footer
    footer_pattern = r'<!-- Footer -->\s*<footer.*?</footer>'
    content = re.sub(footer_pattern, '', content, flags=re.DOTALL)

    # Link "Add Product" button
    content = content.replace('<button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold">\n<span class="material-symbols-outlined text-lg">add</span>\n                        Add Product\n                    </button>',
                              '<a href="product-add.html" class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold">\n<span class="material-symbols-outlined text-lg">add</span>\n                        Add Product\n                    </a>')

    # Add Delete button to Quick Edit section
    # Find all instances of: <button class="p-1.5 rounded-lg bg-surface-container hover:bg-primary/20 hover:text-primary transition-all active:scale-90 flex items-center justify-center"...
    # Replace to add a delete button next to it.
    btn_pattern = r'(<button class="p-1\.5 rounded-lg bg-surface-container hover:bg-primary/20 hover:text-primary transition-all active:scale-90 flex items-center justify-center".*?>\s*<span class="material-symbols-outlined text-sm">edit</span>\s*</button>)'
    replacement = r'\1\n<button class="p-1.5 rounded-lg bg-surface-container hover:bg-error/20 hover:text-error transition-all active:scale-90 flex items-center justify-center mt-1" title="Delete">\n<span class="material-symbols-outlined text-sm">delete</span>\n</button>'
    content = re.sub(btn_pattern, replacement, content)
    
    with open("product-management.html", 'w', encoding='utf-8') as f:
        f.write(content)


print("Nav updated and product-management.html modified.")
