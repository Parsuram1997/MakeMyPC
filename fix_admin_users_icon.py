import os
import re

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We want to replace <span class="material-symbols-outlined">manage_accounts</span>
    # with <span class="material-symbols-outlined">admin_panel_settings</span>
    # ONLY when it is followed by <span class="text-body-sm font-medium">Admin Users</span>
    
    new_text = re.sub(
        r'(<span class="material-symbols-outlined[^"]*">)manage_accounts(</span>\s*<span class="text-body-sm font-medium">Admin Users</span>)',
        r'\1admin_panel_settings\2',
        text
    )
    
    if new_text != text:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1

print(f"Updated Admin Users icon in {count} files.")
