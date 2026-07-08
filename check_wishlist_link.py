import re
with open('admin-wishlist.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'<a href="admin-customers.html"[^>]*>.*?</a>', text, re.DOTALL)
if m1: print('All Customers:', m1.group(0))

m2 = re.search(r'<a href="admin-wishlist.html"[^>]*>.*?</a>', text, re.DOTALL)
if m2: print('Wishlist:', m2.group(0))
