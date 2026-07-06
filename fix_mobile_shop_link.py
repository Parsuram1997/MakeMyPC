c = open('apply_consistent_nav_v2.py', encoding='utf-8').read()
old = "href=\"prebuilt-pcs.html\" style=\"font-size:18px;font-weight:700;color:#d7e2ff;text-decoration:none;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;\""
new = "href=\"shop.html\" style=\"font-size:18px;font-weight:700;color:#d7e2ff;text-decoration:none;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;\""
r = c.replace(old, new)
print('CHANGED' if r != c else 'NO MATCH')
open('apply_consistent_nav_v2.py', 'w', encoding='utf-8').write(r)
