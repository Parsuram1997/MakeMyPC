import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    def remove_order_history_from_customers(match):
        block = match.group(0)
        # We need to remove the "Order History" link from this block
        # <a href="admin-order-history.html" ...>
        #     Order History
        # </a>
        # Keep in mind that we might have active state tags inside it too if it's the active page
        block_clean = re.sub(
            r'<a[^>]*href="admin-order-history\.html"[^>]*>\s*(?:<div[^>]*></div>\s*)?Order History\s*</a>\s*',
            '',
            block,
            flags=re.IGNORECASE | re.DOTALL
        )
        return block_clean

    new_content = re.sub(
        r'(<details[^>]*name="sidebar-menu"[^>]*>.*?<span[^>]*>Customers</span>.*?</details>)',
        remove_order_history_from_customers,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Removed Order History from Customers in {fname}")

print(f"Total files updated: {count}")
