import os, re

# Pages to check for missing/zero top padding on main content wrapper
SKIP = {'admin-dashboard.html', 'admin-dashboard-overview.html', 'product-management.html', 'orders-management.html'}

issues = []
for fname in os.listdir('.'):
    if not fname.endswith('.html') or fname in SKIP:
        continue
    try:
        text = open(fname, encoding='utf-8').read()
    except Exception:
        continue
    
    # Find main tag with pt-0
    if re.search(r'<main[^>]+\bpt-0\b', text):
        issues.append((fname, 'has pt-0'))
    # Find main tag with no pt- class at all (potential cut-off)
    m = re.search(r'<main\s+class="([^"]+)"', text)
    if m and 'pt-' not in m.group(1):
        issues.append((fname, 'no pt- at all: ' + m.group(1)[:60]))

print('Pages with padding issues:')
for fname, issue in issues:
    print(f'  {fname}: {issue}')
