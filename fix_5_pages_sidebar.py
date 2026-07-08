"""
Replace the non-standard sidebars in 5 pages with the same standard admin sidebar.
Each page gets the sidebar with the correct active state for its section.
"""

import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"

# ── Standard admin sidebar template
# {ACTIVE_SECTION} will be replaced per-page
# Sections: "none", "pcbuilder", "orders", "customers"

def build_sidebar(active_section="none", active_page=None):
    """Build the standard admin sidebar HTML."""

    # Products section - always inactive for these 5 pages
    products_summary = 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"'
    products_open = ' open' if active_section == 'products' else ''

    # PC Builder section
    pcbuilder_open = ' open' if active_section == 'pcbuilder' else ''
    pcbuilder_summary = 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"' if active_section == 'pcbuilder' else 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"'

    # Orders section
    orders_open = ' open' if active_section == 'orders' else ''
    orders_summary = 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"' if active_section == 'orders' else 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"'

    # Customers section
    customers_open = ' open' if active_section == 'customers' else ''
    customers_summary = 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"' if active_section == 'customers' else 'class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden"'

    def pcb_link(href, label):
        if active_page == href:
            return f'''                <a href="{href}" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    {label}
                </a>'''
        return f'''                <a href="{href}" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">
                    {label}
                </a>'''

    sidebar = f'''<!-- Sidebar Navigation -->
<aside class="h-screen w-64 fixed left-0 top-0 border-r border-white/10 bg-surface-deep z-50 flex flex-col py-4">
    <div class="px-6 mb-4 shrink-0">
        <h1 class="font-headline-sm text-headline-sm font-bold text-electric-blue dark:text-primary">MakeMyPC</h1>
        <p class="text-[10px] uppercase tracking-widest text-on-surface-variant/50 mt-1">Enterprise Admin</p>
    </div>

    <nav class="flex flex-col gap-0.5 px-4 flex-1 overflow-y-auto custom-scrollbar pb-4">
        <a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">dashboard</span>
            <span class="text-body-sm font-medium">Dashboard</span>
        </a>

        <details class="group" name="sidebar-menu"{products_open}>
            <summary {products_summary}>
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">inventory_2</span>
                    <span class="text-body-sm font-medium">Products</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
{pcb_link("product-add.html", "Add Product")}
{pcb_link("product-inventory.html", "Inventory")}
{pcb_link("product-categories.html", "Categories")}
{pcb_link("product-brands.html", "Brands")}
{pcb_link("product-compatibility.html", "Compatibility")}
{pcb_link("product-reviews.html", "Reviews")}
            </div>
        </details>

        <details class="group" name="sidebar-menu"{pcbuilder_open}>
            <summary {pcbuilder_summary}>
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">computer</span>
                    <span class="text-body-sm font-medium">PC Builder</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
{pcb_link("custom-pc-builder.html", "Custom Builder")}
{pcb_link("admin-saved-builds.html", "Saved Builds")}
{pcb_link("compatibility-manager.html", "Compatibility Engine")}
{pcb_link("smart-builder.html", "Smart Builder")}
            </div>
        </details>

        <details class="group" name="sidebar-menu"{orders_open}>
            <summary {orders_summary}>
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">shopping_cart</span>
                    <span class="text-body-sm font-medium">Orders</span>
                </div>
                <span class="material-symbols-outlined text-sm transition-transform group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
{pcb_link("orders-management.html", "All Orders")}
{pcb_link("admin-order-history.html", "Order History")}
{pcb_link("order-tracking.html", "Order Tracking")}
            </div>
        </details>

        <details class="group" name="sidebar-menu"{customers_open}>
            <summary {customers_summary}>
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">group</span>
                    <span class="text-body-sm font-medium">Customers</span>
                </div>
                <span class="material-symbols-outlined text-[18px] transition-transform duration-300 group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">All Customers</a>
                <a href="admin-customer-groups.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Customer Groups</a>
                <a href="admin-saved-builds.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Saved Builds</a>
                <a href="admin-addresses.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Addresses</a>
                <a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Wishlist</a>
                <a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Order History</a>
                <a href="admin-support-tickets.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Support Tickets</a>
                <a href="admin-loyalty-rewards.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Loyalty &amp; Rewards</a>
                <a href="admin-activity-logs.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Activity Logs</a>
                <a href="admin-email-notifications.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Email &amp; Notifications</a>
                <a href="admin-blocked-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">Blocked Customers</a>
            </div>
        </details>

        <a href="admin-assembly.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">build</span>
            <span class="text-body-sm font-medium">Assembly</span>
        </a>
        <a href="admin-payments.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">payments</span>
            <span class="text-body-sm font-medium">Payments</span>
        </a>
        <a href="admin-coupons.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_offer</span>
            <span class="text-body-sm font-medium">Coupons</span>
        </a>
        <a href="admin-dashboard-overview.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">analytics</span>
            <span class="text-body-sm font-medium">Analytics</span>
        </a>
        <a href="admin-marketing.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">campaign</span>
            <span class="text-body-sm font-medium">Marketing</span>
        </a>
        <a href="index.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">language</span>
            <span class="text-body-sm font-medium">Website</span>
        </a>
        <a href="admin-reports.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">summarize</span>
            <span class="text-body-sm font-medium">Reports</span>
        </a>
        <a href="admin-shipping.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">local_shipping</span>
            <span class="text-body-sm font-medium">Shipping</span>
        </a>

        <div class="px-4 mt-3 mb-1">
            <p class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">User Management</p>
        </div>
        <a href="admin-users.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">manage_accounts</span>
            <span class="text-body-sm font-medium">Admin Users</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">shield_person</span>
            <span class="text-body-sm font-medium">Roles &amp; Permissions</span>
        </a>

        <a href="#" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary mt-auto mb-2">
            <span class="material-symbols-outlined">settings</span>
            <span class="text-body-sm font-medium">Settings</span>
        </a>
    </nav>

    <div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4 pb-4">
        <details class="group" name="sidebar-profile-menu">
            <summary class="list-none outline-none">
                <div class="flex items-center justify-between p-3 rounded-t-xl group-open:bg-white/[0.02] bg-surface-container border border-white/5 group-open:border-b-0 hover:bg-white/5 transition-colors cursor-pointer group-open:rounded-b-none rounded-b-xl">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-[#B3D4FF] text-[#0A1929] flex items-center justify-center font-bold text-sm">AD</div>
                        <div class="overflow-hidden">
                            <p class="text-xs font-bold text-white truncate mb-0.5">Admin Profile</p>
                            <p class="text-[10px] text-on-surface-variant truncate mb-1">Super Admin</p>
                            <div class="flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                <span class="text-[9px] text-[#00D084]/70">Online</span>
                            </div>
                        </div>
                    </div>
                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-open:rotate-180 transition-transform">expand_more</span>
                </div>
            </summary>
            <div class="bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl p-2 flex flex-col gap-0.5">
                <a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">person</span>
                    Profile Settings
                </a>
                <a href="admin-security.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">lock</span>
                    Security
                </a>
                <a href="admin-preferences.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">settings</span>
                    Preferences
                </a>
                <div class="h-[1px] bg-white/5 my-1 mx-2"></div>
                <a href="#" onclick="if(typeof signOutUser==='function')signOutUser()" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-[#F87171] hover:bg-[#F87171]/10 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">logout</span>
                    Sign Out
                </a>
            </div>
        </details>
    </div>
</aside>'''
    return sidebar


# ── Pages to fix with their active section and active page
PAGES_TO_FIX = {
    "compatibility-manager.html": ("pcbuilder", "compatibility-manager.html"),
    "account-settings.html":      ("none",      None),
    "compare-products.html":      ("none",      None),
    "my-builds.html":             ("none",      None),
    "submit-ticket.html":         ("none",      None),
}

for fname, (section, active_page) in PAGES_TO_FIX.items():
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  [MISSING] {fname}")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and replace the entire <aside>...</aside> block
    new_sidebar = build_sidebar(active_section=section, active_page=active_page)
    new_content = re.sub(
        r'<!-- Sidebar.*?-->\s*<aside.*?</aside>',
        new_sidebar,
        content,
        flags=re.DOTALL,
        count=1
    )

    # If comment not found, try without comment
    if new_content == content:
        new_content = re.sub(
            r'<aside\b.*?</aside>',
            new_sidebar,
            content,
            flags=re.DOTALL,
            count=1
        )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [FIXED] {fname}")
    else:
        print(f"  [NO CHANGE] {fname}")

print("\nDone.")
