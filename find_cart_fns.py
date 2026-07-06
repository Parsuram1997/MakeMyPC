import re
text = open('shop.html', encoding='utf-8').read()
# Find all JS functions in the page
fns = re.findall(r'function\s+(\w+)', text)
print('Functions defined in shop.html:')
for f in fns:
    print(' ', f)

# Find onclick handlers
clicks = re.findall(r"onclick=\"([^\"]{1,80})\"", text)
print('\nOnclick handlers (first 20):')
for c in clicks[:20]:
    print(' ', c)
