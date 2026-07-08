import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin-' in f or 'product-' in f or 'orders-' in f or 'account-' in f or 'my-builds' in f or f == 'submit-ticket.html')]

# The HTML block to find
find_block = """                <a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    All Orders
                </a>"""

# The replacement block (adding Order History after it)
replace_block = """                <a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    All Orders
                </a>
                <a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    Order History
                </a>"""

count = 0
for fname in admin_files:
    if not os.path.exists(fname): continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if find_block in content and 'href="admin-order-history.html"' not in content:
        new_content = content.replace(find_block, replace_block)
        if new_content != content:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f'Added Order History button back to {count} files.')
