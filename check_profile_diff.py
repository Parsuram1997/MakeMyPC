with open(r'c:\Projects\MakeMyPC\admin-dashboard-overview.html', 'r', encoding='utf-8') as f:
    text1 = f.read()
with open(r'c:\Projects\MakeMyPC\admin-coupons.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

import re
m1 = re.search(r'<details class="group" name="sidebar-profile-menu">.*?</details>', text1, re.DOTALL | re.IGNORECASE)
m2 = re.search(r'<details class="group" name="sidebar-profile-menu">.*?</details>', text2, re.DOTALL | re.IGNORECASE)

if m1 and m2:
    if m1.group(0) == m2.group(0):
        print('Profile blocks are EXACTLY identical in both files.')
    else:
        print('Profile blocks are DIFFERENT!')
