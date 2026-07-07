import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the products <details> block
    pattern = r'(<details[^>]*>\s*<summary[^>]*>\s*<div[^>]*>\s*<span[^>]*>inventory_2</span>.*?<span[^>]*>Products</span>.*?</div>.*?</summary>).*?(</details>)'
    match = re.search(pattern, content, flags=re.DOTALL)
    
    if not match:
        continue
        
    summary_part = match.group(1)
    
    items = [
        ('product-add.html', 'Add Product'),
        ('product-inventory.html', 'Inventory'),
        ('product-categories.html', 'Categories'),
        ('product-brands.html', 'Brands'),
        ('product-compatibility.html', 'Compatibility'),
        ('#', 'Reviews')
    ]
    
    new_div = '            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">\n'
    
    for href, text in items:
        if file == href or (file == 'admin-dashboard.html' and href == 'product-inventory.html' and False): # Just match file
            is_active = True
        else:
            is_active = False
            
        if is_active:
            new_div += f'''                <a href="{href}" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    {text}
                </a>\n'''
        else:
            new_div += f'''                <a href="{href}" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    {text}
                </a>\n'''
                
    new_div += '            </div>\n        '
    
    new_content = content[:match.start()] + summary_part + '\n' + new_div + '</details>' + content[match.end():]
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated sidebar in {file}')

print('Sidebar update complete.')
