text = open('account-settings.html', encoding='utf-8').read()

# Find the main tag with pt-0
old = '<main class="pt-0 pb-20 max-w-container-max mx-auto px-gutter">'
new = '<main class="pt-8 pb-20 max-w-container-max mx-auto px-gutter">'

if old in text:
    open('account-settings.html', 'w', encoding='utf-8').write(text.replace(old, new, 1))
    print('Fixed: pt-0 -> pt-8')
else:
    # Find main tag
    idx = text.find('<main')
    if idx >= 0:
        print('Main tag:', repr(text[idx:idx+100]))
    else:
        print('No main tag found')
        # Check px-gutter context
        idx2 = text.find('px-gutter')
        if idx2 >= 0:
            print('px-gutter context:', repr(text[max(0,idx2-80):idx2+30]))
