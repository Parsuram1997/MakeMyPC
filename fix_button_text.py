import sys

with open('js/auth.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix innerText -> innerHTML in handleLogin
old_login = "const originalText = submitBtn.innerText;"
new_login = "const originalText = submitBtn.innerHTML;"

if old_login in text:
    text = text.replace(old_login, new_login)
    with open('js/auth.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed innerText to innerHTML in auth.js")
else:
    print("Could not find the target line in auth.js.")
