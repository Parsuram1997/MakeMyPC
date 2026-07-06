import os, re

remaining = []
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    text = open(f, encoding='utf-8').read()
    # Nav links pointing to prebuilt-pcs.html
    for m in re.finditer(r'href="prebuilt-pcs\.html"[^>]*>\s*\n?\s*Shop[\s<]', text, re.I):
        remaining.append((f, m.group(0).strip()[:100]))

print('Remaining Shop->prebuilt links:', len(remaining))
for r in remaining[:30]:
    print(' ', r[0], ':', r[1])

# Also check mobile tab bar
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    text = open(f, encoding='utf-8').read()
    if "href=\"prebuilt-pcs.html\"" in text and 'Shop' in text:
        # Count how many occurrences
        ct = text.count('href="prebuilt-pcs.html"')
        if ct > 0:
            print(f'  [{f}] still has {ct} prebuilt-pcs links')
