import os

admin_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin-' in f or 'product-' in f or 'orders-' in f or 'account-' in f or 'my-builds' in f or f == 'submit-ticket.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('href="order-tracking.html"', 'href="admin-order-tracking.html"')

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Updated Order Tracking link in {count} files.')
