import sys

with open('generate_shop.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the specific flex container line
old_line = '<div class="flex flex-col lg:flex-row gap-10 items-start">'
new_line = '<div class="flex flex-col lg:flex-row gap-10 items-center">'

if old_line in text:
    text = text.replace(old_line, new_line, 1)
    with open('generate_shop.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated items-start to items-center.")
else:
    print("Could not find the target line.")

