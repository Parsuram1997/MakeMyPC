import os, re

DIR = '.'

files_changed = []
for fname in os.listdir(DIR):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(DIR, fname)
    try:
        text = open(path, encoding='utf-8').read()
    except Exception:
        continue
    original = text

    # 1. Desktop nav: href="prebuilt-pcs.html" ... >Shop<
    text = re.sub(
        r'href="prebuilt-pcs\.html"([^>]*)>Shop<',
        lambda m: 'href="shop.html"' + m.group(1) + '>Shop<',
        text, flags=re.IGNORECASE
    )

    # 2. Mobile menu: href="prebuilt-pcs.html" ...> Shop <span
    text = re.sub(
        r'href="prebuilt-pcs\.html"([^>]*)>\s*\n?\s*Shop\s*<span',
        lambda m: 'href="shop.html"' + m.group(1) + '>\n        Shop <span',
        text, flags=re.IGNORECASE
    )

    # 3. Hero button onclick
    text = text.replace(
        "window.location.href='prebuilt-pcs.html'",
        "window.location.href='shop.html'"
    )

    # 4. Bottom mobile tab bar in index.html
    text = text.replace(
        'href="prebuilt-pcs.html" class="flex flex-col items-center gap-1 p-2 text-on-surface-variant hover:text-white transition-colors"',
        'href="shop.html" class="flex flex-col items-center gap-1 p-2 text-on-surface-variant hover:text-white transition-colors"'
    )

    if text != original:
        open(path, 'w', encoding='utf-8').write(text)
        n = original.count('prebuilt-pcs.html') - text.count('prebuilt-pcs.html')
        files_changed.append((fname, n))

print('DONE: Fixed', len(files_changed), 'files:')
for fname, n in sorted(files_changed):
    print(' ', fname, ':', n, 'link(s) updated')
