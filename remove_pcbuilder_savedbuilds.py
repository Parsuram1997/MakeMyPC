import os, re
PAGES_DIR = r'c:\Projects\MakeMyPC'
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_saved_builds(match):
        block = match.group(0)
        # Remove Saved Builds link
        block_clean = re.sub(r'\n\s*<a href="admin-saved-builds\.html"[^>]*>\s*Saved Builds\s*</a>', '', block)
        block_clean = re.sub(r'<a href="admin-saved-builds\.html"[^>]*>\s*Saved Builds\s*</a>\s*', '', block_clean)
        return block_clean

    new_content = re.sub(
        r'(<details[^>]*name="sidebar-menu"[^>]*>.*?<span[^>]*>PC Builder</span>.*?</details>)',
        replace_saved_builds,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Fixed {fname}')

print(f'Fixed {count} files.')
