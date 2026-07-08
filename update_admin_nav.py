import os
import re

files = ['admin-dashboard.html', 'admin-dashboard-overview.html', 'product-management.html', 'orders-management.html']

aside_content = """<aside class="h-screen w-64 fixed left-0 top-0 border-r border-white/10 bg-surface-deep z-50 flex flex-col py-6">
    <div class="px-6 mb-8 shrink-0">
        <h1 class="font-headline-sm text-headline-sm font-bold text-electric-blue dark:text-primary">MakeMyPC</h1>
        <p class="text-[10px] uppercase tracking-widest text-on-surface-variant/50 mt-1">Enterprise Admin</p>
    </div>

    <nav class="flex flex-col gap-2 px-4 flex-1 overflow-y-auto custom-scrollbar pb-6">
        <a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">dashboard</span>
            <span class="text-body-sm font-medium">Dashboard</span>
        </a>

        <details class="group">
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">inventory_2</span>
                    <span class="text-body-sm font-medium">Products</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="product-management.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">All Products</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Categories</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Brands</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Inventory</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Compatibility</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Reviews</a>
            </div>
        </details>

        <details class="group">
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">computer</span>
                    <span class="text-body-sm font-medium">PC Builder</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Custom Builds</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Saved Builds</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Compatibility Engine</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Featured Builds</a>
            </div>
        </details>

        <details class="group">
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">shopping_cart</span>
                    <span class="text-body-sm font-medium">Orders</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="flex flex-col gap-1 pl-12 pr-4 pt-1 pb-2">
                <a href="orders-management.html" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">All Orders</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Custom PC</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Components</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Ready PCs</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Laptops</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Returns</a>
                <a href="#" class="text-body-sm text-on-surface-variant hover:text-primary py-1.5 transition-colors">Refunds</a>
            </div>
        </details>

        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">group</span>
            <span class="text-body-sm font-medium">Customers</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">build</span>
            <span class="text-body-sm font-medium">Assembly</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">payments</span>
            <span class="text-body-sm font-medium">Payments</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_offer</span>
            <span class="text-body-sm font-medium">Coupons</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">analytics</span>
            <span class="text-body-sm font-medium">Analytics</span>
        </a>

        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">campaign</span>
            <span class="text-body-sm font-medium">Marketing</span>
        </a>
        <a href="index.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">language</span>
            <span class="text-body-sm font-medium">Website</span>
        </a>
        <a href="admin-reports.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">summarize</span>
            <span class="text-body-sm font-medium">Reports</span>
        </a>
        <a href="admin-shipping.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">notifications</span>
            <span class="text-body-sm font-medium">Notifications</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">admin_panel_settings</span>
            <span class="text-body-sm font-medium">Admin Users</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary mt-auto mb-4">
            <span class="material-symbols-outlined">settings</span>
            <span class="text-body-sm font-medium">Settings</span>
        </a>
    </nav>

    <div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4">
        <div class="flex items-center gap-3 p-3 rounded-lg bg-surface-glass border border-white/5 hover:bg-white/5 transition-colors cursor-pointer">
            <div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold text-xs">AD</div>
            <div class="overflow-hidden">
                <p class="text-xs font-bold text-on-surface truncate">Admin Profile</p>
                <p class="text-[10px] text-on-surface-variant truncate">Sign out</p>
            </div>
        </div>
    </div>
</aside>"""

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match the entire aside block
        # Some sidebars might have different classes, so we use <aside[^>]*>.*?</aside>
        pattern = re.compile(r'<aside[^>]*>.*?</aside>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(aside_content, content, count=1)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Could not find aside in {file}")
