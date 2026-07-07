import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    if file == 'product-management.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'\s*<li[^>]*>.*?href=["\']product-management\.html["\'].*?</li>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')

if os.path.exists('product-management.html'):
    os.remove('product-management.html')
    print('Deleted product-management.html')
