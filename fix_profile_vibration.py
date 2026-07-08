import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is group-open:border-b-0 causing a 1px layout shift (vibration).
    # We replace it with group-open:border-b-transparent
    new_content = content.replace('group-open:border-b-0', 'group-open:border-b-transparent')
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Fixed vibration issue in {count} files.')
