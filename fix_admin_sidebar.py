import glob, re

correct_nav = """<nav class="flex flex-col gap-2 px-4 flex-1 mt-6">
    <a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
        <span class="material-symbols-outlined">dashboard</span>
        <span class="text-body-sm font-medium">Dashboard</span>
    </a>
    <a href="product-management.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
        <span class="material-symbols-outlined">inventory_2</span>
        <span class="text-body-sm font-medium">Products</span>
    </a>
    <a href="orders-management.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
        <span class="material-symbols-outlined">receipt_long</span>
        <span class="text-body-sm font-medium">Orders</span>
    </a>
    <a href="index.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary mt-auto">
        <span class="material-symbols-outlined">storefront</span>
        <span class="text-body-sm font-medium">Main Site</span>
    </a>
</nav>"""

admin_files = ['admin-dashboard.html', 'admin-dashboard-overview.html', 'product-management.html', 'orders-management.html']

for f in admin_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find the <aside>
        aside_match = re.search(r'<aside[^>]*>.*?</aside>', content, re.DOTALL | re.IGNORECASE)
        if aside_match:
            aside_content = aside_match.group(0)
            
            # The top nav injected inside aside starts with <nav class="fixed top-0 w-full z-50
            # It ends with </nav>
            # But we must be careful to match the correct nav.
            # In some files, maybe it's slightly different.
            nav_match = re.search(r'<nav[^>]*fixed top-0[^>]*>.*?</nav>', aside_content, re.DOTALL | re.IGNORECASE)
            if nav_match:
                new_aside = aside_content.replace(nav_match.group(0), correct_nav)
                new_content = content.replace(aside_content, new_aside)
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Fixed {f}")
            else:
                print(f"Wrong nav not found in aside for {f}")
        else:
            print(f"Aside not found in {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
