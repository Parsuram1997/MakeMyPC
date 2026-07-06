import sys

with open('generate_shop.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = '''  <div class="max-w-container-max mx-auto px-6 md:px-16">
    <div class="flex gap-3 overflow-x-auto hide-scroll pb-2">'''

new_str = '''  <div class="max-w-container-max mx-auto">
    <!-- Moved px to the scroll container and added pseudo element spacer for edge padding on scroll -->
    <div class="flex gap-3 overflow-x-auto hide-scroll pb-2 px-6 md:px-16 after:content-[''] after:w-4 after:flex-shrink-0">'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('generate_shop.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("generate_shop.py updated successfully.")
else:
    print("Pattern not found in generate_shop.py. Attempting flexible replace...")
    # Just replace the specific lines
    content = content.replace('class="max-w-container-max mx-auto px-6 md:px-16"', 'class="max-w-container-max mx-auto"')
    content = content.replace('class="flex gap-3 overflow-x-auto hide-scroll pb-2"', 'class="flex gap-3 overflow-x-auto hide-scroll pb-2 px-6 md:px-16 after:content-[\'\'] after:w-4 after:md:w-16 after:flex-shrink-0"')
    with open('generate_shop.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("generate_shop.py updated via flexible replace.")

