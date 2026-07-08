import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # The notifications link:
    # <a href="#" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
    #     <span class="material-symbols-outlined">notifications</span>
    #     <span class="text-body-sm font-medium">Notifications</span>
    # </a>

    new_content = re.sub(
        r'<a[^>]*href="#"[^>]*>\s*<span[^>]*>notifications</span>\s*<span[^>]*>Notifications</span>\s*</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed Notifications link from {fname}")

print(f"Total files updated: {count}")
