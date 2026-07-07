import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove the entire <li> containing "All Products" 
    # as well as the <a> tag itself so there's no empty bullet point.
    # From grep output: <a href="product-management.html" ...>All Products</a>
    
    # regex to match: <li> followed by anything non-greedy followed by All Products</a> followed by </li>
    new_content = re.sub(r'\s*<li[^>]*>.*?<a href="product-management\.html"[^>]*>All Products</a>.*?</li>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Removed All Products from {file}')

print('Script finished.')
