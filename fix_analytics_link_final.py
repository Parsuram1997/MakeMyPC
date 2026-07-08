import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html') and f != 'admin-analytics.html']

# 1. Update the Analytics link in all HTML files to point to admin-dashboard-overview.html
count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    def fix_analytics_link(match):
        block = match.group(0)
        # We replace href="#" or href="admin-analytics.html" with href="admin-dashboard-overview.html"
        block = re.sub(r'href="[^"]*"', 'href="admin-dashboard-overview.html"', block)
        return block

    new_content = re.sub(
        r'<a[^>]*>\s*<span[^>]*>analytics</span>\s*<span[^>]*>Analytics</span>\s*</a>',
        fix_analytics_link,
        content,
        flags=re.IGNORECASE
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Fixed Analytics link target in {fname}")

print(f"Total files updated: {count}")

# 2. Delete the temporary admin-analytics.html since admin-dashboard-overview.html is the real one
analytics_path = os.path.join(PAGES_DIR, "admin-analytics.html")
if os.path.exists(analytics_path):
    os.remove(analytics_path)
    print("Deleted placeholder admin-analytics.html")
