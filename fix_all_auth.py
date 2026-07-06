import os

SCRIPTS = '\n<script src="js/global.js" type="module"></script>\n<script type="module" src="js/auth.js"></script>\n'
SKIP = {'admin-dashboard.html', 'admin-dashboard-overview.html', 'product-management.html', 'orders-management.html', 'login.html', 'signup.html'}

fixed = []
already = []
for fname in os.listdir('.'):
    if not fname.endswith('.html') or fname in SKIP:
        continue
    try:
        text = open(fname, encoding='utf-8').read()
    except Exception:
        continue
    
    if 'auth.js' in text:
        already.append(fname)
    elif '</body>' in text:
        text = text.replace('</body>', SCRIPTS + '</body>', 1)
        open(fname, 'w', encoding='utf-8').write(text)
        fixed.append(fname)

print('Already had auth.js:', len(already))
for f in sorted(already): print(' ', f)
print()
print('Fixed (auth.js added):', len(fixed))
for f in sorted(fixed): print(' ', f)
