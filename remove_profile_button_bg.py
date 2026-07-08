import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the trigger button
    # Original (before any changes today, but modified by earlier scripts)
    # class="flex items-center justify-between p-3 rounded-xl group-open:bg-white/[0.02] bg-surface-container border border-white/5 group-open:border-b-transparent hover:bg-white/5 transition-colors cursor-pointer group-open:rounded-b-none"
    
    # We want to replace it with a clean class list matching other buttons:
    # "flex items-center justify-between px-4 py-1.5 rounded-xl hover:bg-white/5 transition-colors cursor-pointer"
    
    # We'll use regex to target the div exactly:
    def replace_trigger(match):
        return '<div class="flex items-center justify-between px-3 py-1.5 rounded-xl hover:bg-white/5 transition-colors cursor-pointer">'

    new_content = re.sub(
        r'<div class="flex items-center justify-between p-3 rounded-xl[^>]*group-open:rounded-b-none">',
        replace_trigger,
        content
    )

    # 2. Update the dropdown container
    # Since the trigger no longer has a border or background, the dropdown container should be a complete rounded box with a slight margin top.
    # Replace: 'bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl'
    # With: 'bg-surface-container/50 border border-white/5 rounded-xl mt-1'
    
    new_content = new_content.replace(
        'bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl',
        'bg-surface-container/50 border border-white/5 rounded-xl mt-1'
    )
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Updated profile button bg in {count} files.')
