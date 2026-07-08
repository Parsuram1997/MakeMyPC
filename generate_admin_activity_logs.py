import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Activity Logs link
    activity_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Activity Logs\s*</a>'
    new_activity = '<a href="admin-activity-logs.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Activity Logs\n                </a>'
    
    if re.search(activity_pattern, content):
        content = re.sub(activity_pattern, new_activity, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_activity_logs():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    activity_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Activity Logs</h2>
                    <p class="text-on-surface-variant text-sm">Track all important activities performed by customers and admin users.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export Logs
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">assignment</span>
                        Audit Report
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">filter_alt</span>
                        Filters
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-5 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">show_chart</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TOTAL ACTIVITIES</p>
                        <h3 class="text-lg font-bold text-white leading-tight">24,856</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">All time activities</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">event</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TODAY'S ACTIVITIES</p>
                        <h3 class="text-lg font-bold text-white leading-tight">1,256</h3>
                        <p class="text-[10px] text-[#68D391] mt-0.5 font-medium">+12.5% <span class="text-on-surface-variant font-normal">vs yesterday</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">group</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">UNIQUE USERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">2,847</h3>
                        <p class="text-[10px] text-[#68D391] mt-0.5 font-medium">+8.3% <span class="text-on-surface-variant font-normal">vs last 7 days</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">admin_panel_settings</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">ADMIN ACTIONS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">856</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">3.4% of total activities</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">person</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">CUSTOMER ACTIONS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">24,000</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">96.6% of total activities</p>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-4 relative z-10">
                <div class="flex gap-3 flex-1 max-w-5xl">
                    <div class="relative flex-1 max-w-[240px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by user, action, module..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-9 pr-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-28">
                        <option>All Users</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Modules</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Actions</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-28">
                        <option>All Status</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-28">
                        <option>All Time</option>
                    </select>
                    <button class="px-3 py-2 text-primary hover:text-primary-fixed transition-colors text-[13px] font-medium">
                        Reset
                    </button>
                </div>
                <div class="flex items-center gap-2">
                    <button class="w-9 h-9 rounded-lg bg-primary/20 text-primary flex items-center justify-center border border-primary/30">
                        <span class="material-symbols-outlined text-[18px]">view_list</span>
                    </button>
                    <button class="w-9 h-9 rounded-lg bg-surface-container-highest/50 text-on-surface-variant hover:text-white flex items-center justify-center border border-white/5 transition-colors">
                        <span class="material-symbols-outlined text-[18px]">grid_view</span>
                    </button>
                </div>
            </div>

            <!-- Content Area (Table + Sidebar) -->
            <div class="flex gap-4 flex-1 min-h-0 relative z-10">
                
                <!-- Table -->
                <div class="glass-card rounded-xl flex-1 flex flex-col overflow-hidden border border-white/5">
                    <div class="overflow-y-auto custom-scrollbar flex-1">
                        <table class="w-full text-left text-sm border-collapse">
                            <thead class="sticky top-0 bg-surface-deep text-[10px] uppercase text-on-surface-variant/70 border-b border-white/5 z-10">
                                <tr>
                                    <th class="px-4 py-3 font-medium tracking-wider w-[120px]">TIME <span class="material-symbols-outlined text-[12px] align-middle">unfold_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">USER</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">USER TYPE</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">ACTION</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">MODULE</th>
                                    <th class="px-4 py-3 font-medium tracking-wider w-[240px]">DESCRIPTION</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">IP ADDRESS</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">STATUS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=1" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Rahul Verma</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">rahul@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[9px] font-medium border border-[#63B3ED]/20 bg-[#1A4B8C]/20">Customer</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#68D391]">shopping_cart_checkout</span>
                                            <span class="text-[11px]">Placed Order</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Orders</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Order #ORD-2024-1256
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">103.21.244.12</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Row 2 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:25 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=2" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Priya Sharma</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">priya@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[9px] font-medium border border-[#63B3ED]/20 bg-[#1A4B8C]/20">Customer</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#B794F6]">person</span>
                                            <span class="text-[11px]">Updated Profile</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Profile</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Updated mobile number
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">103.21.244.15</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Row 3 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:20 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=3" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Amit Singh</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">amit@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[9px] font-medium border border-[#63B3ED]/20 bg-[#1A4B8C]/20">Customer</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#FC8181]">favorite</span>
                                            <span class="text-[11px]">Added to Wishlist</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Wishlist</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Added MSI RTX 4070 Ti
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">117.199.65.32</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Row 4 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:15 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=4" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Neha Gupta</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">neha@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[9px] font-medium border border-[#63B3ED]/20 bg-[#1A4B8C]/20">Customer</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#63B3ED]">note_add</span>
                                            <span class="text-[11px]">Created Ticket</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Support Tickets</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Issue with order delivery
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">152.58.126.11</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Row 5 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:10 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=5" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Vikram Joshi</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">vikram@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[9px] font-medium border border-[#63B3ED]/20 bg-[#1A4B8C]/20">Customer</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#68D391]">check_circle</span>
                                            <span class="text-[11px]">Payment Successful</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Payments</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Order #ORD-2024-1255
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">117.199.65.32</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Admin Row 1 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:05 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-6 h-6 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[10px] font-medium border border-[#B794F6]/20">AD</div>
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Admin User</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">admin@makemypc.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[9px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Admin</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#F6AD55]">inventory_2</span>
                                            <span class="text-[11px]">Updated Product</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Products</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Updated price of i5-13400F
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">103.21.244.12</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Admin Row 2 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:00 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-6 h-6 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[10px] font-medium border border-[#B794F6]/20">AD</div>
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Admin User</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">admin@makemypc.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[9px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Admin</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#FC8181]">person_remove</span>
                                            <span class="text-[11px]">Deleted Customer</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Customers</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Customer ID: CUS-2541
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">152.58.126.11</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Admin Row 3 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:55 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-6 h-6 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[10px] font-medium border border-[#B794F6]/20">AD</div>
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Admin User</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">admin@makemypc.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[9px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Admin</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#63B3ED]">mail</span>
                                            <span class="text-[11px]">Bulk Email Sent</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Email & Notifications</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Sent newsletter to 1,256 users
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">103.21.244.12</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Admin Row 4 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:50 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-6 h-6 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[10px] font-medium border border-[#B794F6]/20">AD</div>
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Admin User</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">admin@makemypc.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[9px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Admin</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#F6AD55]">local_shipping</span>
                                            <span class="text-[11px]">Updated Order Status</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Orders</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Order #ORD-2024-1254
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">117.199.65.32</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium text-[11px]">Success</span>
                                    </td>
                                </tr>
                                <!-- Admin Row 5 - Failed -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-6 h-6 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[10px] font-medium border border-[#B794F6]/20">AD</div>
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Admin User</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">admin@makemypc.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[9px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Admin</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2 text-white">
                                            <span class="material-symbols-outlined text-[14px] text-[#63B3ED]">login</span>
                                            <span class="text-[11px]">Login</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">Authentication</td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px] truncate max-w-[240px]">
                                        Invalid password attempt
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant text-[11px]">103.21.244.15</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#FC8181] font-medium text-[11px]">Failed</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="p-3 border-t border-white/5 bg-surface-deep/50 backdrop-blur flex justify-between items-center text-xs">
                        <p class="text-on-surface-variant">Showing 1 to 10 of 24,856 activities</p>
                        <div class="flex gap-1 items-center">
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors disabled:opacity-50 text-white"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                            <button class="w-7 h-7 rounded bg-primary text-on-primary flex items-center justify-center font-medium">1</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">3</button>
                            <span class="w-7 h-7 flex items-center justify-center text-on-surface-variant">...</span>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2486</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                            <div class="flex items-center gap-2 ml-4">
                                <span class="text-on-surface-variant">10 / page</span>
                                <span class="material-symbols-outlined text-sm">expand_more</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar -->
                <div class="w-[300px] shrink-0 flex flex-col gap-4 overflow-y-auto custom-scrollbar pr-1">
                    
                    <!-- Activity Overview Donut Chart -->
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-[12px] font-medium text-white mb-4">Activity Overview</h3>
                        <div class="flex items-center gap-4">
                            <!-- Conic gradient for 34%, 22.7%, 19.5%, 11.4%, 12.4% -->
                            <!-- Colors matching screenshot: Green, Purple, Red, Blue, Orange -->
                            <div class="relative w-28 h-28 rounded-full shrink-0" style="background: conic-gradient(#68D391 0% 34%, #B794F6 34% 56.7%, #F6AD55 56.7% 76.2%, #63B3ED 76.2% 87.6%, #E2E8F0 87.6% 100%); padding: 12px;">
                                <div class="bg-surface-deep w-full h-full rounded-full flex flex-col items-center justify-center border border-white/5 shadow-inner">
                                    <span class="text-sm font-bold text-white leading-none">24,856</span>
                                    <span class="text-[8px] text-on-surface-variant mt-1 text-center leading-tight">Total<br>Activities</span>
                                </div>
                            </div>
                            <div class="flex-1 space-y-2 text-[10px]">
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-1.5 text-on-surface-variant">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Orders
                                    </div>
                                    <span class="text-white">8,456 (34%)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-1.5 text-on-surface-variant">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#B794F6]"></span> Products
                                    </div>
                                    <span class="text-white">5,632 (22.7%)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-1.5 text-on-surface-variant">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#F6AD55]"></span> Customers
                                    </div>
                                    <span class="text-white">4,856 (19.5%)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-1.5 text-on-surface-variant">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#63B3ED]"></span> Support
                                    </div>
                                    <span class="text-white">2,845 (11.4%)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-1.5 text-on-surface-variant">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#E2E8F0]"></span> Others
                                    </div>
                                    <span class="text-white">3,067 (12.4%)</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Top Actions -->
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-center mb-3">
                            <h3 class="text-[12px] font-medium text-white">Top Actions</h3>
                            <a href="#" class="text-[10px] text-primary hover:underline">View All</a>
                        </div>
                        <div class="space-y-3">
                            <div class="flex justify-between items-center text-[11px]">
                                <div class="flex items-center gap-2 text-white">
                                    <span class="material-symbols-outlined text-[14px] text-[#68D391]">shopping_cart_checkout</span>
                                    Placed Order
                                </div>
                                <span class="text-on-surface-variant font-medium">8,456</span>
                            </div>
                            <div class="flex justify-between items-center text-[11px]">
                                <div class="flex items-center gap-2 text-white">
                                    <span class="material-symbols-outlined text-[14px] text-[#B794F6]">person</span>
                                    Updated Profile
                                </div>
                                <span class="text-on-surface-variant font-medium">3,245</span>
                            </div>
                            <div class="flex justify-between items-center text-[11px]">
                                <div class="flex items-center gap-2 text-white">
                                    <span class="material-symbols-outlined text-[14px] text-[#FC8181]">favorite</span>
                                    Added to Wishlist
                                </div>
                                <span class="text-on-surface-variant font-medium">2,845</span>
                            </div>
                            <div class="flex justify-between items-center text-[11px]">
                                <div class="flex items-center gap-2 text-white">
                                    <span class="material-symbols-outlined text-[14px] text-[#68D391]">check_circle</span>
                                    Payment Successful
                                </div>
                                <span class="text-on-surface-variant font-medium">2,120</span>
                            </div>
                            <div class="flex justify-between items-center text-[11px]">
                                <div class="flex items-center gap-2 text-white">
                                    <span class="material-symbols-outlined text-[14px] text-[#63B3ED]">note_add</span>
                                    Created Ticket
                                </div>
                                <span class="text-on-surface-variant font-medium">1,952</span>
                            </div>
                        </div>
                    </div>

                    <!-- Top Active Users -->
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-[12px] font-medium text-white">Top Active Users</h3>
                            <a href="#" class="text-[10px] text-primary hover:underline">View All</a>
                        </div>
                        <div class="space-y-3">
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-white">
                                    <img src="https://i.pravatar.cc/150?u=1" class="w-5 h-5 rounded-full">
                                    <span class="text-[11px]">Rahul Verma</span>
                                </div>
                                <span class="text-[10px] text-on-surface-variant">156 Activities</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-white">
                                    <img src="https://i.pravatar.cc/150?u=2" class="w-5 h-5 rounded-full">
                                    <span class="text-[11px]">Priya Sharma</span>
                                </div>
                                <span class="text-[10px] text-on-surface-variant">128 Activities</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-white">
                                    <img src="https://i.pravatar.cc/150?u=3" class="w-5 h-5 rounded-full">
                                    <span class="text-[11px]">Amit Singh</span>
                                </div>
                                <span class="text-[10px] text-on-surface-variant">112 Activities</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-white">
                                    <img src="https://i.pravatar.cc/150?u=4" class="w-5 h-5 rounded-full">
                                    <span class="text-[11px]">Neha Gupta</span>
                                </div>
                                <span class="text-[10px] text-on-surface-variant">98 Activities</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-white">
                                    <img src="https://i.pravatar.cc/150?u=5" class="w-5 h-5 rounded-full">
                                    <span class="text-[11px]">Vikram Joshi</span>
                                </div>
                                <span class="text-[10px] text-on-surface-variant">88 Activities</span>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Filters -->
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-[12px] font-medium text-white mb-3">Quick Filters</h3>
                        <div class="grid grid-cols-2 gap-2">
                            <button class="p-2 rounded-lg border border-white/5 bg-surface-deep/50 hover:bg-white/5 transition-colors text-[10px] text-on-surface-variant flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">admin_panel_settings</span>
                                Admin Actions
                            </button>
                            <button class="p-2 rounded-lg border border-white/5 bg-surface-deep/50 hover:bg-white/5 transition-colors text-[10px] text-on-surface-variant flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">person</span>
                                Customer Actions
                            </button>
                            <button class="p-2 rounded-lg border border-white/5 bg-surface-deep/50 hover:bg-white/5 transition-colors text-[10px] text-on-surface-variant flex items-center justify-center gap-1.5 text-[#FC8181]">
                                <span class="material-symbols-outlined text-[14px]">warning</span>
                                Failed Actions
                            </button>
                            <button class="p-2 rounded-lg border border-white/5 bg-surface-deep/50 hover:bg-white/5 transition-colors text-[10px] text-on-surface-variant flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">login</span>
                                Login Activities
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep">{activity_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Activity Logs'
    activity_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Activity Logs\s*</a>'
    activity_active = """<a href="admin-activity-logs.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Activity Logs
                </a>"""
    if not re.search(activity_inactive, new_html):
        print("Could not find inactive Activity Logs link to replace.")
    new_html = re.sub(activity_inactive, activity_active, new_html)

    with open('admin-activity-logs.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-activity-logs.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-activity-logs.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_activity_logs()

if __name__ == '__main__':
    main()
