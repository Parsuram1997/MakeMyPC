import re

with open('admin-order-tracking.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix "All Orders" to be inactive
text = re.sub(
    r'<a href="orders-management\.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Orders\s*</a>',
    '<a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">\\n                    All Orders\\n                </a>',
    text,
    flags=re.DOTALL
)

# Fix "Order Tracking" to use the correct active style
text = re.sub(
    r'<a href="admin-order-tracking\.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block bg-white/10 text-white font-semibold">\s*Order Tracking\s*</a>',
    '<a href="admin-order-tracking.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">\\n                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>\\n                    Order Tracking\\n                </a>',
    text,
    flags=re.DOTALL
)

with open('admin-order-tracking.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed active states.")
