import sys

with open('js/global.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = """            if (cart.length > 0) {
                badge.textContent = cart.length;
                badge.classList.remove('hidden');
            } else {
                badge.classList.add('hidden');
            }"""

new_block = """            if (cart.length > 0) {
                badge.textContent = cart.length;
                badge.style.display = 'flex';
            } else {
                badge.style.display = 'none';
            }"""

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('js/global.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("global.js cart badge logic updated.")
else:
    print("Could not find the target block in global.js.")
