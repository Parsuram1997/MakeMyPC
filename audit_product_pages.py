import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"
pages = [
    "product-add.html","product-inventory.html","product-categories.html",
    "product-brands.html","product-compatibility.html","product-reviews.html",
]

checks = {
    "Shipping x1 only": lambda s: s.count("Shipping") == 1,
    "has admin-shipping link": lambda s: 'href="admin-shipping.html"' in s,
    "has Dashboard": lambda s: "Dashboard" in s,
    "has PC Builder": lambda s: "PC Builder" in s,
    "has Customers": lambda s: "Customers" in s,
    "has Orders": lambda s: "Orders" in s,
    "no py-3 nav": lambda s: 'px-4 py-3 rounded-xl' not in s,
    "no gap-2 nav": lambda s: 'gap-2 px-4 flex-1' not in s,
    "no py-6 aside": lambda s: 'py-6' not in s,
    "no mb-8": lambda s: 'mb-8' not in s,
}

print("FILE".ljust(35), "PASS/FAIL")
print("-" * 90)
for fname in pages:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    aside = re.search(r"<aside.*?</aside>", content, re.DOTALL)
    if not aside:
        print(fname + ": NO ASIDE")
        continue
    sidebar = aside.group(0)
    fails = [name for name, fn in checks.items() if not fn(sidebar)]
    passes = [name for name, fn in checks.items() if fn(sidebar)]
    if fails:
        print(fname.ljust(35) + " FAIL: " + str(fails))
    else:
        print(fname.ljust(35) + " ALL OK (" + str(len(passes)) + "/" + str(len(checks)) + " checks)")
