import os

admin_files = [f for f in os.listdir('.') if f.endswith('.html')]

count = 0
for fname in admin_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # The dropdown container currently has 'bg-surface-container/50 border border-white/5'
    # We will remove those classes to make it fully transparent like the rest of the submenus.
    new_content = content.replace(
        'bg-surface-container/50 border border-white/5 rounded-xl mt-1 p-1 flex flex-col gap-0',
        'p-1 flex flex-col gap-0 mt-1'
    )
    
    # Just in case it has different classes:
    new_content = new_content.replace('bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl', '')
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Removed dropdown background in {count} files.')
