import sys

with open('js/auth.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """// Also attach to any existing #logout-btn for backward compatibility
const logoutBtn = document.getElementById('logout-btn');
if (logoutBtn) {"""
new_code = """// Also attach to any existing #logout-btn for backward compatibility
if (logoutBtn) {"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('js/auth.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed syntax error in auth.js")
else:
    print("Could not find the duplicate declaration block.")

