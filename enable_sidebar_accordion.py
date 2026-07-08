import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # The sidebar <nav> section contains the <details> tags for Products, Orders, Customers.
    # We want to ensure all <details> inside <nav> have name="sidebar-menu"
    
    # We can just look for <details class="group"> (which doesn't have a name) and replace it
    # with <details class="group" name="sidebar-menu">
    new_content = content.replace('<details class="group">', '<details class="group" name="sidebar-menu">')
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Added name attribute for accordion behavior in {count} files.')
