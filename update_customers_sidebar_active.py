import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the customers <details> block
    pattern = r'(<details class="group".*?>\s*<summary[^>]*>\s*<div[^>]*>\s*<span[^>]*>group</span>.*?<span[^>]*>Customers</span>.*?</div>.*?</summary>).*?(</details>)'
    match = re.search(pattern, content, flags=re.DOTALL)
    
    if not match:
        continue
        
    summary_part = match.group(1)
    
    items = [
        ('admin-customers.html', 'All Customers'),
        ('admin-customer-groups.html', 'Customer Groups'),
        ('admin-saved-builds.html', 'Saved Builds'),
        ('admin-addresses.html', 'Addresses')
    ]
    
    new_div = '            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">\n'
    
    is_customers_active = False
    
    for href, text in items:
        if file == href:
            is_active = True
            is_customers_active = True
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
    
    # Adjust <details> and <summary> depending on if it's active
    if is_customers_active:
        summary_part = re.sub(r'<details class="group"([^>]*)>', r'<details class="group" open>', summary_part)
        summary_part = re.sub(r'(<summary[^>]*?)text-on-surface-variant', r'\1text-primary bg-primary/10', summary_part)
    else:
        summary_part = re.sub(r'<details class="group"\s*open>', r'<details class="group">', summary_part)
        summary_part = re.sub(r'(<summary[^>]*?)text-primary bg-primary/10', r'\1text-on-surface-variant', summary_part)
    
    new_content = content[:match.start()] + summary_part + '\n' + new_div + '</details>' + content[match.end():]
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated customers sidebar in {file}')

print('Customers sidebar active state update complete.')
