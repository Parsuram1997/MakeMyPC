import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

customers_nav_template = """        <details class="group" open>
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">group</span>
                    <span class="text-body-sm font-medium">Customers</span>
                </div>
                <span class="material-symbols-outlined text-[18px] transition-transform duration-300 group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    All Customers
                </a>
                <a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Customer Groups
                </a>
                <a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Saved Builds
                </a>
                <a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Addresses
                </a>
            </div>
        </details>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the existing Customers <a> tag
    pattern_a = r'<a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\s*<span class="material-symbols-outlined">group</span>\s*<span class="text-body-sm font-medium">Customers</span>\s*</a>'
    
    if re.search(pattern_a, content):
        content = re.sub(pattern_a, customers_nav_template, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated customers nav in {file}")
    else:
        # Check if already a details block
        pattern_details = r'<details[^>]*>\s*<summary[^>]*>\s*<div[^>]*>\s*<span[^>]*>group</span>\s*<span[^>]*>Customers</span>\s*</div>.*?</details>'
        if re.search(pattern_details, content, flags=re.DOTALL):
            print(f"Already details in {file}")
        else:
            print(f"Could not find customers nav in {file}")
