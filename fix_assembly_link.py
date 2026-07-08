import os
import glob
import re

def fix_assembly_link():
    html_files = glob.glob('*.html')
    
    # Matches the Assembly link where href is "#"
    assembly_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">build</span>\s*<span class="text-body-sm font-medium">Assembly</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if assembly_pattern.search(content):
            # Replace href="#" with href="admin-assembly.html"
            new_content = assembly_pattern.sub(r'<a href="admin-assembly.html"\1>\n            <span class="material-symbols-outlined">build</span>\n            <span class="text-body-sm font-medium">Assembly</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Assembly link in {filepath}")
            count += 1
            
    print(f"Fixed Assembly link in {count} files.")

if __name__ == '__main__':
    fix_assembly_link()
