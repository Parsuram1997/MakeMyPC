import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"
fixed = 0

for fname in os.listdir(PAGES_DIR):
    if not fname.endswith(".html"):
        continue
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add style="margin:0" to sidebar <details> that don't already have it
    # Pattern: <details class="group" name="sidebar-menu" [open]>
    new = re.sub(
        r'(<details class="group" name="sidebar-menu")((?! style)[^>]*)(>)',
        r'\1\2 style="margin:0"\3',
        content
    )

    if new != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new)
        fixed += 1

print(f"Fixed {fixed} files with margin:0 on details elements.")
