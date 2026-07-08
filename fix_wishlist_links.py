import glob
import re

def fix_wishlist_link(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Wishlist link regardless of its current href and whether it has the emoji
    # It might be in the sidebar. We look for the <a> tag that contains "Wishlist" inside the Customers dropdown.
    # The class is "text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block"
    # or if active, it has "text-primary bg-primary/10"
    
    # Let's use a regex that matches the <a> tag surrounding "Wishlist" in the sidebar
    pattern_inactive_old = r'<a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Wishlist( ❤️)?\s*</a>'
    new_inactive = '<a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Wishlist ❤️\n                </a>'
    
    pattern_inactive_new = r'<a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Wishlist\s*</a>'
    
    # Active state pattern
    pattern_active = r'<a href="admin-wishlist.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*Wishlist( ❤️)?\s*</a>'
    new_active = """<a href="admin-wishlist.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Wishlist ❤️
                </a>"""

    changed = False
    
    if re.search(pattern_inactive_old, content):
        content = re.sub(pattern_inactive_old, new_inactive, content)
        changed = True
        
    if re.search(pattern_inactive_new, content):
        content = re.sub(pattern_inactive_new, new_inactive, content)
        changed = True
        
    if re.search(pattern_active, content):
        content = re.sub(pattern_active, new_active, content)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        fix_wishlist_link(filepath)

if __name__ == '__main__':
    main()
