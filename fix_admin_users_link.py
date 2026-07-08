import os
import glob
import re

def fix_admin_users_link():
    html_files = glob.glob('*.html')
    
    # Matches the Admin Users link where href is "#"
    admin_users_pattern = re.compile(r'<a href="#"( class="[^"]*")>\s*<span class="material-symbols-outlined">admin_panel_settings</span>\s*<span class="text-body-sm font-medium">Admin Users</span>\s*</a>')
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if admin_users_pattern.search(content):
            # Replace href="#" with href="admin-users.html"
            new_content = admin_users_pattern.sub(r'<a href="admin-users.html"\1>\n            <span class="material-symbols-outlined">admin_panel_settings</span>\n            <span class="text-body-sm font-medium">Admin Users</span>\n        </a>', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Admin Users link in {filepath}")
            count += 1
            
    print(f"Fixed Admin Users link in {count} files.")

if __name__ == '__main__':
    fix_admin_users_link()
