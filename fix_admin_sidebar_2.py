import re
with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_sidebar = """<!-- SideNavBar -->
<aside class="h-screen w-64 fixed left-0 top-0 border-r border-white/10 bg-surface-deep z-50 flex flex-col py-6">
<div class="px-6 mb-10">
<h1 class="font-headline-sm text-headline-sm font-bold text-electric-blue">MakeMyPC</h1>
<p class="text-[10px] uppercase tracking-widest text-on-surface-variant/50 mt-1">Enterprise Admin</p>
</div>
<nav class="flex flex-col gap-2 px-4 flex-1 mt-6">
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
</nav>
</aside>
"""

nav_match = re.search(r'<!-- SideNavBar -->\s*<nav[^>]*fixed top-0[^>]*>.*?</nav>', content, re.DOTALL | re.IGNORECASE)
if nav_match:
    new_content = content.replace(nav_match.group(0), correct_sidebar)
    with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Fixed admin-dashboard.html')
else:
    print('SideNavBar not found in admin-dashboard.html')
