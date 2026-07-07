import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dashboard
    if file in ['admin-dashboard.html', 'admin-dashboard-overview.html']:
        # Make dashboard active
        content = re.sub(
            r'(<a href="admin-dashboard\.html"\s+class=".*?)text-on-surface-variant(.*?hover:bg-white/5.*?")',
            r'\1text-primary bg-primary/10\2',
            content
        )
    else:
        # Make dashboard inactive (just in case)
        pass # It's already inactive by default

    # Products
    if file.startswith('product-'):
        # Make Products summary active
        # We need to find the summary inside details that has inventory_2
        pattern = r'(<summary\s+class="[^"]*)text-on-surface-variant(.*?hover:bg-white/5.*?")(\s*>\s*<div[^>]*>\s*<span[^>]*>inventory_2)'
        content = re.sub(
            pattern,
            r'\1text-primary bg-primary/10\2\3',
            content
        )

    # Orders
    if file.startswith('orders-'):
        # Make Orders summary active
        pattern = r'(<summary\s+class="[^"]*)text-on-surface-variant(.*?hover:bg-white/5.*?")(\s*>\s*<div[^>]*>\s*<span[^>]*>receipt_long)'
        content = re.sub(
            pattern,
            r'\1text-primary bg-primary/10\2\3',
            content
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated active states in {file}')

print('Finished updating parent active states.')
