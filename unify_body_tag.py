import os
import re

admin_files = [
    'account-settings.html', 'admin-activity-logs.html', 'admin-addresses.html', 'admin-assembly.html',
    'admin-blocked-customers.html', 'admin-coupons.html', 'admin-customer-groups.html', 'admin-customers.html',
    'admin-dashboard-overview.html', 'admin-dashboard.html', 'admin-email-notifications.html', 'admin-loyalty-rewards.html',
    'admin-marketing.html', 'admin-order-history.html', 'admin-payments.html', 'admin-preferences.html',
    'admin-profile.html', 'admin-reports.html', 'admin-saved-builds.html', 'admin-security.html',
    'admin-shipping.html', 'admin-support-tickets.html', 'admin-users.html', 'admin-wishlist.html',
    'admin_template.html', 'compare-products.html', 'compatibility-manager.html', 'my-builds.html',
    'orders-management.html', 'product-add.html', 'product-brands.html', 'product-categories.html',
    'product-compatibility.html', 'product-inventory.html', 'product-reviews.html', 'submit-ticket.html'
]

unified_body = '<body class="bg-surface-deep text-on-surface font-body-md text-body-md overflow-x-hidden">'

count = 0
for fname in admin_files:
    fpath = os.path.join(r'c:\Projects\MakeMyPC', fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<body[^>]*>', unified_body, content, count=1)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        
print(f'Unified body tags in {count} files.')
