import re

with open('admin-order-history.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix "Order History" to be active
text = re.sub(
    r'<a href="admin-order-history\.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">\s*Order History\s*</a>',
    '<a href="admin-order-history.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">\\n                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>\\n                    Order History\\n                </a>',
    text,
    flags=re.DOTALL
)

with open('admin-order-history.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed Order History active state.")
