import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin-' in f or 'product-' in f or 'orders-' in f or 'account-' in f or 'my-builds' in f or f == 'submit-ticket.html')]

products_files = [
    'product-management.html', 'product-add.html', 'product-brands.html', 
    'product-categories.html', 'product-compatibility.html', 'product-inventory.html', 
    'product-reviews.html'
]
orders_files = [
    'orders-management.html', 'admin-order-history.html', 'order-tracking.html'
]
customers_files = [
    'admin-customers.html', 'admin-customer-groups.html', 'admin-saved-builds.html', 
    'admin-addresses.html', 'admin-wishlist.html', 'admin-support-tickets.html', 
    'admin-loyalty-rewards.html', 'admin-activity-logs.html', 'admin-email-notifications.html', 
    'admin-blocked-customers.html'
]

count = 0
for fname in admin_files:
    if not os.path.exists(fname): continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<aside' not in content:
        continue

    # 1. Remove all 'open' attributes from the sidebar details tags
    # These could be <details class="group" name="sidebar-menu" open> or <details class="group" name="sidebar-menu" open style="margin:0">
    # We will just regex replace them.
    new_content = re.sub(
        r'<details class="group" name="sidebar-menu"[^>]*>',
        r'<details class="group" name="sidebar-menu" style="margin:0">',
        content
    )
    
    # 2. Add 'open' attribute to the correct details tag based on the file category
    if fname in products_files:
        # The first sidebar-menu details is Products
        new_content = re.sub(
            r'(<span class="text-body-sm font-medium">Products</span>\s*</div>\s*<span[^>]*>expand_more</span>\s*</summary>)',
            r'\1', # Not here. We need to match the <details> tag just above it.
            new_content
        )
        # Better approach: split by '<details class="group" name="sidebar-menu" style="margin:0">'
        # and re-join with 'open' in the correct occurrence.
        
    def add_open(text, menu_name):
        # We find the <details ...> that contains the menu_name in its summary
        pattern = r'(<details class="group" name="sidebar-menu" style="margin:0">)(\s*<summary[^>]*>\s*<div[^>]*>\s*<span[^>]*>[^<]*</span>\s*<span[^>]*>' + menu_name + r'</span>)'
        return re.sub(pattern, r'<details class="group" name="sidebar-menu" open style="margin:0">\2', text, flags=re.IGNORECASE)

    if fname in products_files:
        new_content = add_open(new_content, 'Products')
    elif fname in orders_files:
        new_content = add_open(new_content, 'Orders')
    elif fname in customers_files:
        new_content = add_open(new_content, 'Customers')

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Fixed accordion open states in {count} files.')
