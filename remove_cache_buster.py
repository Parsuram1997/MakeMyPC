import sys
import re

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove any query string from js/address.js
new_text = re.sub(r'src="js/address\.js\?v=[^"]+"', 'src="js/address.js"', text)

with open('account-settings.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Removed cache buster from account-settings.html")
