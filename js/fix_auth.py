text = open('auth.js', encoding='utf-8').read()

old = "        if (mobileAccount) mobileAccount.style.display = 'flex';\n        }\n        \n        // Optional: redirect"
new = "        if (mobileAccount) mobileAccount.style.display = 'flex';\n        \n        // Optional: redirect"

if old in text:
    open('auth.js', 'w', encoding='utf-8').write(text.replace(old, new))
    print('Fixed stray brace')
else:
    idx = text.find('mobileAccount.style.display')
    print('Not found, nearby:', repr(text[idx:idx+200]))
