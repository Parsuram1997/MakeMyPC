import os
import re

# 1. Read template
with open('admin_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 2. Fix title and sidebar active states for orders-management.html
# Title
template = re.sub(r'<title>.*?</title>', '<title>Orders Management | MakeMyPC Admin</title>', template)

# Remove active state from Dashboard
template = re.sub(
    r'<a href="admin-dashboard\.html" class="flex items-center gap-3 px-4 py-1\.5 rounded-xl transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary">',
    '<a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">',
    template
)

# Add active state to Orders dropdown
template = re.sub(
    r'<details class="group" name="sidebar-menu" style="margin:0">\s*<summary class="flex items-center justify-between px-4 py-1\.5 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none \[&::-webkit-details-marker\]:hidden">\s*<div class="flex items-center gap-3">\s*<span class="material-symbols-outlined">shopping_cart</span>\s*<span class="text-body-sm font-medium">Orders</span>',
    '<details class="group" name="sidebar-menu" open style="margin:0">\n            <summary class="flex items-center justify-between px-4 py-1.5 rounded-xl cursor-pointer transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">\n                <div class="flex items-center gap-3">\n                    <span class="material-symbols-outlined">shopping_cart</span>\n                    <span class="text-body-sm font-medium">Orders</span>',
    template
)

# Add active state to "All Orders" inner link
template = re.sub(
    r'<a href="orders-management\.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">\s*All Orders\s*</a>',
    '<a href="orders-management.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-1 rounded-lg relative block">\n                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>\n                    All Orders\n                </a>',
    template
)

# 3. Create main content HTML
main_content = """
    <div class="w-full max-w-7xl mx-auto space-y-6">
        
        <!-- Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mt-2">
            <div>
                <h1 class="text-2xl font-bold text-white mb-1">All Orders</h1>
                <p class="text-sm text-on-surface-variant">View and manage all customer orders in one place.</p>
            </div>
            <div class="flex items-center gap-3">
                <button class="bg-surface border border-white/10 hover:bg-white/5 text-sm font-medium text-white px-4 py-2 rounded-lg transition-colors flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">download</span> Export Orders
                </button>
                <button class="bg-electric-blue hover:bg-blue-600 text-sm font-medium text-white px-4 py-2 rounded-lg transition-colors flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">add</span> Create Order
                </button>
            </div>
        </div>

        <!-- KPI Grid -->
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            <!-- Total Orders -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-electric-blue/10 flex items-center justify-center text-electric-blue">
                        <span class="material-symbols-outlined">shopping_cart</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Total Orders</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">1,254</div>
                <div class="text-xs text-[#00D084] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_upward</span> 12.6% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
            <!-- Pending -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-[#FFB020]/10 flex items-center justify-center text-[#FFB020]">
                        <span class="material-symbols-outlined">schedule</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Pending</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">182</div>
                <div class="text-xs text-[#00D084] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_upward</span> 8.3% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
            <!-- Processing -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-[#B388FF]/10 flex items-center justify-center text-[#B388FF]">
                        <span class="material-symbols-outlined">inventory_2</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Processing</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">268</div>
                <div class="text-xs text-[#00D084] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_upward</span> 11.4% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
            <!-- Shipped -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-electric-blue/10 flex items-center justify-center text-electric-blue">
                        <span class="material-symbols-outlined">local_shipping</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Shipped</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">642</div>
                <div class="text-xs text-[#00D084] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_upward</span> 14.2% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
            <!-- Delivered -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-[#00D084]/10 flex items-center justify-center text-[#00D084]">
                        <span class="material-symbols-outlined">check_circle</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Delivered</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">1,024</div>
                <div class="text-xs text-[#00D084] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_upward</span> 16.8% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
            <!-- Cancelled -->
            <div class="bg-surface-deep border border-white/5 rounded-xl p-4 flex flex-col relative overflow-hidden group">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-full bg-[#F87171]/10 flex items-center justify-center text-[#F87171]">
                        <span class="material-symbols-outlined">cancel</span>
                    </div>
                    <div class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wider">Cancelled / Returned</div>
                </div>
                <div class="text-2xl font-bold text-white mb-1">87</div>
                <div class="text-xs text-[#F87171] flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">arrow_downward</span> 5.2% <span class="text-on-surface-variant">vs last month</span>
                </div>
            </div>
        </div>

        <!-- Filter Bar -->
        <div class="flex flex-wrap items-center gap-3">
            <div class="relative flex-1 min-w-[250px]">
                <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                <input type="text" placeholder="Search by Order ID, Customer, Email, Phone..." class="w-full bg-surface-deep border border-white/10 rounded-lg pl-9 pr-4 py-2 text-sm text-white focus:outline-none focus:border-primary transition-colors placeholder:text-on-surface-variant/70">
            </div>
            
            <select class="bg-surface-deep border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-primary appearance-none cursor-pointer pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E')] bg-[length:16px] bg-no-repeat bg-[position:right_8px_center]">
                <option>All Status</option>
            </select>
            
            <select class="bg-surface-deep border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-primary appearance-none cursor-pointer pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E')] bg-[length:16px] bg-no-repeat bg-[position:right_8px_center]">
                <option>All Payment Status</option>
            </select>

            <select class="bg-surface-deep border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-primary appearance-none cursor-pointer pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E')] bg-[length:16px] bg-no-repeat bg-[position:right_8px_center]">
                <option>All Shipping Status</option>
            </select>
            
            <select class="bg-surface-deep border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-primary appearance-none cursor-pointer pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E')] bg-[length:16px] bg-no-repeat bg-[position:right_8px_center]">
                <option>All Channels</option>
            </select>

            <button class="bg-surface-deep border border-white/10 hover:bg-white/5 text-sm font-medium text-white px-3 py-2 rounded-lg transition-colors flex items-center gap-2">
                <span class="material-symbols-outlined text-[16px]">filter_list</span> Filters
            </button>
            <button class="text-sm font-medium text-electric-blue hover:underline px-2 transition-colors">
                Reset
            </button>
            
            <div class="ml-auto flex items-center gap-2 bg-surface-deep border border-white/10 rounded-lg px-3 py-2 text-sm text-white">
                <span class="material-symbols-outlined text-[16px] text-on-surface-variant">calendar_today</span>
                12 May 2024 - 18 May 2024
            </div>
        </div>

        <!-- Table -->
        <div class="bg-surface-deep border border-white/5 rounded-xl overflow-hidden shadow-lg">
            <div class="overflow-x-auto custom-scrollbar">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="border-b border-white/5 bg-white/[0.02]">
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">ORDER ID</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">CUSTOMER</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">DATE</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">TOTAL</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">PAYMENT</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">FULFILLMENT</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">STATUS</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap">CHANNEL</th>
                            <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider whitespace-nowrap text-right">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-white/5 text-sm text-white">
                        <!-- Row 1 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1254</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">18 May 2024, 10:30 AM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#007AFF]/20 text-[#007AFF] flex items-center justify-center text-[10px] font-bold shrink-0">RK</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Rohit Kumar</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">rohit.kumar@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 98765 43210</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">18 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">10:30 AM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹45,320</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">1 Item</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">Online</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#B388FF]/10 text-[#B388FF] border border-[#B388FF]/20 mb-1">Processing</span>
                                <div class="text-[11px] text-on-surface-variant">Assembling</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#FFB020]/10 text-[#FFB020] border border-[#FFB020]/20">Processing</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 2 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1253</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">18 May 2024, 09:15 AM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#FFB020]/20 text-[#FFB020] flex items-center justify-center text-[10px] font-bold shrink-0">PS</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Pooja Sharma</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">pooja.sharma@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 98711 22334</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">18 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">09:15 AM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹28,750</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">1 Item</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">UPI</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#007AFF]/10 text-[#007AFF] border border-[#007AFF]/20 mb-1">Shipped</span>
                                <div class="text-[11px] text-on-surface-variant">Shipped on 18 May</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#007AFF]/10 text-[#007AFF] border border-[#007AFF]/20">Shipped</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>
                        
                        <!-- Row 3 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1252</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">17 May 2024, 08:45 PM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#B388FF]/20 text-[#B388FF] flex items-center justify-center text-[10px] font-bold shrink-0">AS</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Amit Singh</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">amit.singh@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 91234 56789</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">17 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">08:45 PM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹62,999</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">2 Items</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">Card</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#007AFF]/10 text-[#007AFF] border border-[#007AFF]/20 mb-1">Shipped</span>
                                <div class="text-[11px] text-on-surface-variant">Shipped on 17 May</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#007AFF]/10 text-[#007AFF] border border-[#007AFF]/20">Shipped</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">smartphone</span> Mobile App</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 4 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1251</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">17 May 2024, 07:20 PM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#00D084]/20 text-[#00D084] flex items-center justify-center text-[10px] font-bold shrink-0">NV</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Neha Verma</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">neha.verma@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 99876 54321</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">17 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">07:20 PM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹19,999</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">1 Item</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#FFB020]/10 text-[#FFB020] border border-[#FFB020]/20 mb-1">Pending</span>
                                <div class="text-[11px] text-on-surface-variant">COD</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-white/10 text-on-surface-variant border border-white/20 mb-1">Pending</span>
                                <div class="text-[11px] text-on-surface-variant">Waiting for pickup</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#FFB020]/10 text-[#FFB020] border border-[#FFB020]/20">Pending</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 5 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1250</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">17 May 2024, 06:10 PM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#00A4A6]/20 text-[#00A4A6] flex items-center justify-center text-[10px] font-bold shrink-0">MJ</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Manoj Jha</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">manoj.jha@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 90011 22334</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">17 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">06:10 PM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹1,15,500</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">3 Items</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">Net Banking</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#B388FF]/10 text-[#B388FF] border border-[#B388FF]/20 mb-1">Processing</span>
                                <div class="text-[11px] text-on-surface-variant">Assembling</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#FFB020]/10 text-[#FFB020] border border-[#FFB020]/20">Processing</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 6 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1249</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">16 May 2024, 11:30 AM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#FFB020]/20 text-[#FFB020] flex items-center justify-center text-[10px] font-bold shrink-0">SK</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Sanjay Kumar</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">sanjay.kumar@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 87654 32109</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">16 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">11:30 AM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹33,200</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">1 Item</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#F87171]/10 text-[#F87171] border border-[#F87171]/20 mb-1">Failed</span>
                                <div class="text-[11px] text-on-surface-variant">Card</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-white/10 text-on-surface-variant border border-white/20 mb-1">Pending</span>
                                <div class="text-[11px] text-on-surface-variant">Payment Failed</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#F87171]/10 text-[#F87171] border border-[#F87171]/20">Payment Failed</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 7 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1248</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">16 May 2024, 10:00 AM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#B388FF]/20 text-[#B388FF] flex items-center justify-center text-[10px] font-bold shrink-0">VY</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Vikash Yadav</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">vikash.yadav@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 93456 78901</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">16 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">10:00 AM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹26,999</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">1 Item</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">UPI</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Delivered</span>
                                <div class="text-[11px] text-on-surface-variant">Delivered on 16 May</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20">Delivered</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">language</span> Website</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                        <!-- Row 8 -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="px-4 py-3">
                                <a href="#" class="text-electric-blue font-medium hover:underline">ORD-2024-1247</a>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">15 May 2024, 09:20 PM</div>
                            </td>
                            <td class="px-4 py-3">
                                <div class="flex items-center gap-3">
                                    <div class="w-7 h-7 rounded-full bg-[#B388FF]/20 text-[#B388FF] flex items-center justify-center text-[10px] font-bold shrink-0">AP</div>
                                    <div class="min-w-0">
                                        <p class="font-medium text-white truncate">Anjali Patel</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">anjali.patel@email.com</p>
                                        <p class="text-[11px] text-on-surface-variant truncate">+91 98765 00123</p>
                                    </div>
                                </div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-medium">15 May 2024</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">09:20 PM</div>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <div class="font-bold">₹58,770</div>
                                <div class="text-[11px] text-on-surface-variant mt-0.5">2 Items</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Paid</span>
                                <div class="text-[11px] text-on-surface-variant">Card</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20 mb-1">Delivered</span>
                                <div class="text-[11px] text-on-surface-variant">Delivered on 17 May</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#00D084]/10 text-[#00D084] border border-[#00D084]/20">Delivered</span>
                            </td>
                            <td class="px-4 py-3 text-[11px] text-on-surface-variant">
                                <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[14px]">smartphone</span> Mobile App</div>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Print"><span class="material-symbols-outlined text-[16px]">print</span></button>
                                    <button class="w-7 h-7 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                </div>
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>

            <!-- Pagination -->
            <div class="border-t border-white/5 bg-white/[0.01] px-4 py-3 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="text-xs text-on-surface-variant">
                    Showing 1 to 8 of 1,254 orders
                </div>
                <div class="flex items-center gap-2">
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors disabled:opacity-50">
                        <span class="material-symbols-outlined text-[18px]">chevron_left</span>
                    </button>
                    
                    <button class="w-8 h-8 rounded bg-electric-blue text-white text-xs font-medium flex items-center justify-center">1</button>
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-xs font-medium transition-colors">2</button>
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-xs font-medium transition-colors">3</button>
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-xs font-medium transition-colors">4</button>
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-xs font-medium transition-colors">5</button>
                    
                    <span class="text-on-surface-variant text-xs">...</span>
                    
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-xs font-medium transition-colors">157</button>
                    
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                        <span class="material-symbols-outlined text-[18px]">chevron_right</span>
                    </button>
                    
                    <div class="ml-2 flex items-center gap-2">
                        <select class="bg-surface-deep border border-white/10 rounded px-2 py-1 text-xs text-white focus:outline-none focus:border-primary appearance-none cursor-pointer pr-6 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%236b7280%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E')] bg-[length:12px] bg-no-repeat bg-[position:right_4px_center]">
                            <option>10 / page</option>
                            <option>25 / page</option>
                            <option>50 / page</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

    </div>
"""

final_html = template.replace('<!-- INSERT CONTENT HERE -->', main_content)

with open(r'c:\Projects\MakeMyPC\orders-management.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print('Generated orders-management.html')
