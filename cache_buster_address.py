import sys

with open('js/address.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Add a cache buster and alert
if "addressForm.addEventListener('submit', async (e) => {" in text:
    text = text.replace(
        "addressForm.addEventListener('submit', async (e) => {\n        e.preventDefault();\n        if (!currentUser) {",
        "addressForm.addEventListener('submit', async (e) => {\n        e.preventDefault();\n        // Debug alert to confirm JS execution\n        // alert('Address JS is running! Current User: ' + (currentUser ? currentUser.uid : 'null'));\n        if (!currentUser) {"
    )

with open('js/address.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('account-settings.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

if 'src="js/address.js"' in html_text:
    html_text = html_text.replace('src="js/address.js"', 'src="js/address.js?v=' + str(sys.modules.get('time', __import__('time')).time()) + '"')
    with open('account-settings.html', 'w', encoding='utf-8') as f:
        f.write(html_text)

print("Added cache buster to account-settings.html")
