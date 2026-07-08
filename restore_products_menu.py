import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

PRODUCT_LINKS = [
    ("product-add.html",           "Add Product"),
    ("product-inventory.html",     "Inventory"),
    ("product-categories.html",    "Categories"),
    ("product-brands.html",        "Brands"),
    ("product-compatibility.html", "Compatibility"),
    ("product-reviews.html",       "Reviews"),
]

def sidebar_link(href, label, is_active):
    if is_active:
        return (
            f'                <a href="{href}" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">\n'
            f'                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>\n'
            f'                    {label}\n'
            f'                </a>'
        )
    return (
        f'                <a href="{href}" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">\n'
        f'                    {label}\n'
        f'                </a>'
    )

def build_products_block(fname):
    product_links_html = "\n".join(
        sidebar_link(href, label, href == fname)
        for href, label in PRODUCT_LINKS
    )
    
    # Is this a product page? If so, the Products submenu should be open.
    is_product_page = fname in [link[0] for link in PRODUCT_LINKS]
    open_attr = " open" if is_product_page else ""
    
    return f'''        <details class="group" name="sidebar-menu"{open_attr} style="margin:0">
            <summary class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">inventory_2</span>
                    <span class="text-body-sm font-medium">Products</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-0.5 mt-0.5 mb-1">
{product_links_html}
            </div>
        </details>
'''

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to insert the Products block right after the Dashboard link.
    # Pattern to match Dashboard link block:
    # <a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-[^"]+ bg-[^"]* hover:bg-white/5 hover:text-primary">
    #     <span class="material-symbols-outlined">dashboard</span>
    #     <span class="text-body-sm font-medium">Dashboard</span>
    # </a>
    
    # A robust way is to find the closing </a> of the Dashboard link inside the <nav>
    
    def insert_products(match):
        return match.group(0) + "\n" + build_products_block(fname)
        
    # Before inserting, check if Products is already there (some frontend pages might not have had PC builder and thus didn't get deleted, or might not have Dashboard)
    if 'class="text-body-sm font-medium">Products</span>' not in content:
        # Find the Dashboard link inside nav
        new_content = re.sub(
            r'(<a href="admin-dashboard\.html"[^>]*>.*?<span class="text-body-sm font-medium">Dashboard</span>\s*</a>)',
            insert_products,
            content,
            flags=re.DOTALL
        )
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Restored Products menu to {fname}")

print(f"Total files updated: {count}")
