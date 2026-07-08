"""
Add cache-busting meta tags to all admin pages to force fresh load in browser.
Also restart the server on a different port to bypass any OS-level cache.
"""
import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"

META_LINE1 = '    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">'
META_LINE2 = '    <meta http-equiv="Pragma" content="no-cache">'
META_LINE3 = '    <meta http-equiv="Expires" content="0">'
CACHE_BLOCK = META_LINE1 + "\n" + META_LINE2 + "\n" + META_LINE3

fixed = 0
for fname in sorted(os.listdir(PAGES_DIR)):
    if not fname.endswith(".html"):
        continue
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "no-store, must-revalidate" not in content:
        # Insert after <meta charset=...>
        new = re.sub(
            r'(<meta\s+charset[^>]+>)',
            r'\1\n' + CACHE_BLOCK,
            content,
            count=1
        )
        if new != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new)
            fixed += 1

print(f"Cache-busting meta added to {fixed} files.")
