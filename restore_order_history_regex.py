import os
import re

count = 0
for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'href="admin-order-history.html"' in content: continue
    
    # We want to insert Order History link right after the All Orders link
    pattern = r'(<a href="orders-management\.html"[^>]*>\s*All Orders\s*</a>)'
    replace = r'\1\n                <a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">\n                    Order History\n                </a>'
    
    new_content = re.sub(pattern, replace, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
print(f'Fixed remaining {count} files.')
