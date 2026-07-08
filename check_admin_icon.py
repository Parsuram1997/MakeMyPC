import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

icons = {}
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We are looking for something like:
    # <span class="material-symbols-outlined">...</span>
    # <span class="text-body-sm font-medium">Admin Users</span>
    # or similar
    
    m = re.search(r'<span class="material-symbols-outlined[^"]*">([^<]+)</span>\s*<span class="text-body-sm font-medium">Admin Users</span>', text)
    if m:
        icon = m.group(1).strip()
        if icon not in icons:
            icons[icon] = []
        icons[icon].append(fname)

for icon, files in icons.items():
    print(f'Icon: {icon} (in {len(files)} files)')
    print(files[:3], '...')
