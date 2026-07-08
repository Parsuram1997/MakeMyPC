import os
import glob
import re

def fix_coupons_link():
    html_files = glob.glob('*.html')
    
    # Matches the Coupons link where href is "#"
    coupons_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">local_offer</span>\s*<span class="text-body-sm font-medium">Coupons</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if coupons_pattern.search(content):
            # Replace href="#" with href="admin-coupons.html"
            new_content = coupons_pattern.sub(r'<a href="admin-coupons.html"\1>\n            <span class="material-symbols-outlined">local_offer</span>\n            <span class="text-body-sm font-medium">Coupons</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Coupons link in {filepath}")
            count += 1
            
    print(f"Fixed Coupons link in {count} files.")

if __name__ == '__main__':
    fix_coupons_link()
