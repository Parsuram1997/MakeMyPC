import os
import glob
import re

def fix_payments_link():
    html_files = glob.glob('*.html')
    
    # Matches the Payments link where href is "#"
    payments_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">payments</span>\s*<span class="text-body-sm font-medium">Payments</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if payments_pattern.search(content):
            # Replace href="#" with href="admin-payments.html"
            new_content = payments_pattern.sub(r'<a href="admin-payments.html"\1>\n            <span class="material-symbols-outlined">payments</span>\n            <span class="text-body-sm font-medium">Payments</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Payments link in {filepath}")
            count += 1
            
    print(f"Fixed Payments link in {count} files.")

if __name__ == '__main__':
    fix_payments_link()
