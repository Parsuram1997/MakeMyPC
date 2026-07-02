import json
import urllib.request
import os
import re

json_path = r"C:\Users\PARSURAM NAIK\.gemini\antigravity-ide\brain\cefde63a-aecd-485f-b590-dae5ce411290\.system_generated\steps\85\output.txt"
dest_dir = r"c:\Projects\MakeMyPC"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def to_filename(title):
    # Map specific titles
    mapping = {
        "MakeMyPC - Home": "index.html",
        "Custom PC Builder": "custom-pc-builder.html",
        "Prebuilt PCs": "prebuilt-pcs.html",
        "Product Details - Intel Core i9-14900K": "product-details.html",
        "Compare Products - CPUs": "compare-products.html",
        "Shopping Cart - MakeMyPC": "shopping-cart.html",
        "Account Settings - MakeMyPC": "account-settings.html",
        "My Builds - MakeMyPC": "my-builds.html",
        "Order Tracking - MakeMyPC": "order-tracking.html",
        "Support & FAQ - MakeMyPC": "support-faq.html",
        "Submit a Ticket - MakeMyPC": "submit-ticket.html",
        "Ticket Submitted Successfully - MakeMyPC": "ticket-submitted.html",
        "Calculators & Tools": "calculators-tools.html",
        "Admin Dashboard - MakeMyPC": "admin-dashboard.html"
    }
    if title in mapping:
        return mapping[title]
    
    # Fallback
    name = title.lower()
    name = re.sub(r' - makemypc', '', name)
    name = re.sub(r'[^a-z0-9]+', '-', name)
    return name.strip('-') + '.html'

os.makedirs(dest_dir, exist_ok=True)

for screen in data.get("screens", []):
    title = screen.get("title", "")
    url = screen.get("htmlCode", {}).get("downloadUrl", "")
    
    if url:
        filename = to_filename(title)
        filepath = os.path.join(dest_dir, filename)
        print(f"Downloading {title} to {filename}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print(f"  -> Saved {filename}")
        except Exception as e:
            print(f"  -> Error downloading {title}: {e}")
