import os
import glob
import re

def add_shipping_link():
    html_files = glob.glob('*.html')
    
    # Matches the Reports link exactly as it is in the HTML files
    # We will insert Shipping right after it
    reports_pattern = re.compile(r'(<a href="admin-reports.html"[^>]*>\s*<span class="material-symbols-outlined">summarize</span>\s*<span class="text-body-sm font-medium">Reports</span>\s*</a>)')
    
    shipping_link = """
        <a href="admin-shipping.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>"""
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if reports_pattern.search(content):
            # Check if shipping is already there
            if 'admin-shipping.html' not in content:
                new_content = reports_pattern.sub(f'\\1{shipping_link}', content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added Shipping link to {filepath}")
                count += 1
            
    print(f"Added Shipping link to {count} files.")

if __name__ == '__main__':
    add_shipping_link()
