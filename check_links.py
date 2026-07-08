import re
with open('admin-order-tracking.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'<a href="orders-management.html"[^>]*>.*?</a>', text, re.DOTALL)
if m1: print('All Orders:', m1.group(0))

m2 = re.search(r'<a href="admin-order-tracking.html"[^>]*>.*?</a>', text, re.DOTALL)
if m2: print('Order Tracking:', m2.group(0))
