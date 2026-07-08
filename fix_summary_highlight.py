import re

with open('admin-order-history.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove highlight from Customers summary
text = re.sub(
    r'(<details[^>]*name="sidebar-menu"[^>]*>\s*<summary class="[^"]*)text-primary bg-primary/10([^"]*")(\s*>\s*<div[^>]*>\s*<span[^>]*>group</span>\s*<span[^>]*>Customers</span>)',
    r'\1text-on-surface-variant\2\3',
    text,
    flags=re.DOTALL
)

# 2. Add highlight to Orders summary (if it doesn't already have it)
# We look for the Orders summary with text-on-surface-variant
text = re.sub(
    r'(<details[^>]*name="sidebar-menu"[^>]*open[^>]*>\s*<summary class="[^"]*)text-on-surface-variant([^"]*")(\s*>\s*<div[^>]*>\s*<span[^>]*>shopping_cart</span>\s*<span[^>]*>Orders</span>)',
    r'\1text-primary bg-primary/10\2\3',
    text,
    flags=re.DOTALL
)

with open('admin-order-history.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed summary highlights in admin-order-history.html")
