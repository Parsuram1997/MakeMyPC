import os, re

# Pages where pt-0 needs to become pt-8 on main content tag
PAGES_TO_FIX = [
    'calculators-tools.html',
    'custom-pc-builder.html',
    'prebuilt-pcs.html',
    'smart-builder.html',
    'support-faq.html',
]

# order-tracking has mt-28, that's fine
# compare/compatibility have their own layout

fixed = []
for fname in PAGES_TO_FIX:
    try:
        text = open(fname, encoding='utf-8').read()
    except Exception:
        print('Could not open', fname)
        continue
    
    # Replace pt-0 in <main> tag with pt-8
    new_text = re.sub(
        r'(<main\s+class="[^"]*)\bpt-0\b',
        lambda m: m.group(1) + 'pt-8',
        text
    )
    
    if new_text != text:
        open(fname, 'w', encoding='utf-8').write(new_text)
        fixed.append(fname)
    else:
        print(fname, ': pt-0 not found in <main> class')

print('Fixed top padding:', fixed)
