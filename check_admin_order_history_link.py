import re
with open('admin-order-history.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'<a href="orders-management.html"[^>]*>.*?</a>', text, re.DOTALL)
if m1: print('All Orders:', m1.group(0))

m2 = re.search(r'<a href="admin-order-history.html"[^>]*>.*?</a>', text, re.DOTALL)
if m2: print('Order History (admin):', m2.group(0))

m3 = re.search(r'<a href="order-history.html"[^>]*>.*?</a>', text, re.DOTALL)
if m3: print('Order History (customer):', m3.group(0))
