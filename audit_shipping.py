import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"
pages = [
    "product-add.html","product-inventory.html","product-categories.html",
    "product-brands.html","product-compatibility.html","product-reviews.html",
    "compatibility-manager.html","account-settings.html","compare-products.html",
    "my-builds.html","submit-ticket.html","custom-pc-builder.html",
    "smart-builder.html","orders-management.html","order-tracking.html"
]

for fname in pages:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    aside = re.search(r"<aside.*?</aside>", content, re.DOTALL)
    if not aside:
        print(fname + ": NO ASIDE")
        continue
    sidebar = aside.group(0)
    ship_count = sidebar.count("Shipping")
    # find lines with Shipping
    lines = [l.strip()[:120] for l in sidebar.split("\n") if "Shipping" in l and "href" in l]
    print(fname + ": count=" + str(ship_count) + " => " + str(lines))
