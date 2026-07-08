import os
import glob
import re

def fix_reports_link():
    html_files = glob.glob('*.html')
    
    # Matches the Reports link where href is "#"
    reports_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">summarize</span>\s*<span class="text-body-sm font-medium">Reports</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if reports_pattern.search(content):
            # Replace href="#" with href="admin-reports.html"
            new_content = reports_pattern.sub(r'<a href="admin-reports.html"\1>\n            <span class="material-symbols-outlined">summarize</span>\n            <span class="text-body-sm font-medium">Reports</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Reports link in {filepath}")
            count += 1
            
    print(f"Fixed Reports link in {count} files.")

if __name__ == '__main__':
    fix_reports_link()
