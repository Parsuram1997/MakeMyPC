import os
import glob
import re

def fix_marketing_link():
    html_files = glob.glob('*.html')
    
    # Matches the Marketing link where href is "#"
    marketing_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">campaign</span>\s*<span class="text-body-sm font-medium">Marketing</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if marketing_pattern.search(content):
            # Replace href="#" with href="admin-marketing.html"
            new_content = marketing_pattern.sub(r'<a href="admin-marketing.html"\1>\n            <span class="material-symbols-outlined">campaign</span>\n            <span class="text-body-sm font-medium">Marketing</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Marketing link in {filepath}")
            count += 1
            
    print(f"Fixed Marketing link in {count} files.")

if __name__ == '__main__':
    fix_marketing_link()
