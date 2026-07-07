import os
import re

files = ['admin-dashboard.html', 'admin-dashboard-overview.html', 'product-management.html', 'orders-management.html']

global_scrollbar_css = '''
        /* Custom Scrollbar for Glassmorphism */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.2);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            border: 2px solid transparent;
            background-clip: padding-box;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.3);
            border: 2px solid transparent;
            background-clip: padding-box;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
        }
'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We replace any occurrences of existing scrollbar-hide or custom-scrollbar scrollbar classes.
        content = re.sub(r'\s*\.custom-scrollbar::-webkit-scrollbar.*?}', '', content, flags=re.DOTALL)
        content = re.sub(r'\s*::-webkit-scrollbar.*?}', '', content, flags=re.DOTALL)
        content = re.sub(r'\s*\.scrollbar-hide::-webkit-scrollbar.*?}', '', content, flags=re.DOTALL)
        
        # Insert the global scrollbar CSS right after <style>
        content = re.sub(r'(<style>)', r'\1' + global_scrollbar_css, content, count=1)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
