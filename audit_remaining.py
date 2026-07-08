import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"
pages = ["compatibility-manager.html", "account-settings.html", "compare-products.html", "my-builds.html", "submit-ticket.html"]

for fname in pages:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    aside_match = re.search(r"<aside.*?</aside>", content, re.DOTALL)
    if not aside_match:
        print(f"{fname}: NO ASIDE")
        continue
    sidebar = aside_match.group(0)
    print(f"=== {fname} ===")
    for line in sidebar.split("\n"):
        s = line.strip()
        for kw in ["py-3", "gap-2", "py-6", "mb-8", "py-2 rounded", "mt-6", "<aside", "<nav ", "px-6 mb", "px-4 mb"]:
            if kw in s:
                print(f"  [{kw}] {s[:150]}")
                break
    print()
