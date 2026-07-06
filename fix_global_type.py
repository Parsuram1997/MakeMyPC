import re, os

# Fix all HTML pages where global.js has type="module" incorrectly
fixed = []
for fname in os.listdir('.'):
    if not fname.endswith('.html'):
        continue
    try:
        text = open(fname, encoding='utf-8').read()
    except Exception:
        continue
    
    old = '<script src="js/global.js" type="module">'
    new = '<script src="js/global.js">'
    if old in text:
        open(fname, 'w', encoding='utf-8').write(text.replace(old, new))
        fixed.append(fname)

print('Fixed global.js type=module in:', fixed if fixed else 'none')

# Verify shop.html final state
text = open('shop.html', encoding='utf-8').read()
idx = text.find('global.js')
print('shop.html global.js context:', repr(text[max(0,idx-5):idx+50]))
