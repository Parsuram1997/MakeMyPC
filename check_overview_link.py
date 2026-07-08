import re
with open('admin-dashboard-overview.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'<a href="admin-dashboard.html"[^>]*>.*?</a>', text, re.DOTALL)
if m1: print('Dashboard link:', m1.group(0))

m2 = re.search(r'<a href="admin-dashboard-overview.html"[^>]*>.*?</a>', text, re.DOTALL)
if m2: print('Analytics link:', m2.group(0))
