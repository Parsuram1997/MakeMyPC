import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Order History link
    # Old link might be pointing to '#' or 'admin-order-history.html' if previously set
    order_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Order History\s*</a>'
    new_order = '<a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Order History\n                </a>'
    
    if re.search(order_pattern, content):
        content = re.sub(order_pattern, new_order, content)

    # Note: If the file being updated is admin-order-history.html itself, we will set it as active after generating it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_order_history():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    order_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Order History</h2>
                    <p class="text-on-surface-variant text-sm">View and manage all orders placed by customers.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export Orders
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">more_horiz</span>
                        More Actions
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-6 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">inventory_2</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TOTAL ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">1,256</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">All time orders</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">currency_rupee</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TOTAL SPENT</p>
                        <h3 class="text-lg font-bold text-white leading-tight">₹ 3,42,85,600</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">All time spent</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">local_shipping</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">DELIVERED ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">1,102</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">87.7% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">schedule</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">PROCESSING ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">98</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">7.8% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#7F1D1D]/30 text-[#FC8181] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">close</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">CANCELLED ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">56</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">4.5% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">assignment_return</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">RETURNED ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">32</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">2.5% of total</p>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-4 relative z-10">
                <div class="flex gap-3 flex-1 max-w-5xl">
                    <div class="relative flex-1 max-w-[260px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by Order ID, Customer, Email..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-9 pr-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Orders</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Status</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-44">
                        <option>All Payment Methods</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Time</option>
                    </select>
                    <button class="px-3 py-2 rounded-lg border border-white/5 hover:bg-white/5 transition-colors text-[13px] flex items-center gap-1.5 text-white bg-surface-container-highest/50">
                        <span class="material-symbols-outlined text-[16px]">filter_alt</span>
                        Filters
                    </button>
                    <button class="px-3 py-2 text-primary hover:text-primary-fixed transition-colors text-[13px] font-medium">
                        Reset
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
                                    <th class="px-4 py-3 font-medium tracking-wider">ORDER ID <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CUSTOMER</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">DATE <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">TOTAL AMOUNT <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">PAYMENT <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">STATUS <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">ITEMS <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 - Active -->
                                <tr class="bg-primary/5 hover:bg-primary/10 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-white font-medium">
                                            #ORD-2024-1256 <span class="material-symbols-outlined text-[14px] text-on-surface-variant cursor-pointer">content_copy</span>
                                        </div>
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
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 1,48,650</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">Online (UPI)</p>
                                        <p class="text-[9px] text-[#68D391] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Paid</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Delivered</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">8 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 2 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-on-surface-variant font-medium">
                                            #ORD-2024-1255 <span class="material-symbols-outlined text-[14px] text-on-surface-variant/50 cursor-pointer">content_copy</span>
                                        </div>
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
                                        <p class="text-white text-[11px]">11 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 79,999</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">Credit Card</p>
                                        <p class="text-[9px] text-[#68D391] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Paid</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Delivered</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">6 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 3 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-on-surface-variant font-medium">
                                            #ORD-2024-1254 <span class="material-symbols-outlined text-[14px] text-on-surface-variant/50 cursor-pointer">content_copy</span>
                                        </div>
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
                                        <p class="text-white text-[11px]">10 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 1,02,300</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">Net Banking</p>
                                        <p class="text-[9px] text-[#68D391] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Paid</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Delivered</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">7 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 4 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-on-surface-variant font-medium">
                                            #ORD-2024-1253 <span class="material-symbols-outlined text-[14px] text-on-surface-variant/50 cursor-pointer">content_copy</span>
                                        </div>
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
                                        <p class="text-white text-[11px]">09 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 45,600</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">COD</p>
                                        <p class="text-[9px] text-[#F6AD55] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#F6AD55]"></span> Pending</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[10px] font-medium border border-[#63B3ED]/20">Processing</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">5 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Additional placeholder rows can be generated dynamically in real app -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-on-surface-variant font-medium">
                                            #ORD-2024-1252 <span class="material-symbols-outlined text-[14px] text-on-surface-variant/50 cursor-pointer">content_copy</span>
                                        </div>
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
                                        <p class="text-white text-[11px]">08 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">03:30 PM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 2,35,800</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">Credit Card</p>
                                        <p class="text-[9px] text-[#68D391] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Paid</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[10px] font-medium border border-[#B794F6]/20">Shipped</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">10 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-on-surface-variant font-medium">
                                            #ORD-2024-1250 <span class="material-symbols-outlined text-[14px] text-on-surface-variant/50 cursor-pointer">content_copy</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=6" class="w-6 h-6 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[11px]">Sneha Reddy</p>
                                                <p class="text-[9px] text-on-surface-variant mt-0.5">sneha@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">06 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">01:05 PM</p>
                                    </td>
                                    <td class="px-4 py-3 font-medium text-white">₹ 11,999</td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">Net Banking</p>
                                        <p class="text-[9px] text-[#68D391] mt-0.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#68D391]"></span> Paid</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#FC8181] text-[10px] font-medium border border-[#FC8181]/20">Cancelled</span>
                                    </td>
                                    <td class="px-4 py-3 text-white">4 items</td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="p-3 border-t border-white/5 bg-surface-deep/50 backdrop-blur flex justify-between items-center text-xs">
                        <p class="text-on-surface-variant">Showing 1 to 10 of 1,256 orders</p>
                        <div class="flex gap-1 items-center">
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors disabled:opacity-50 text-white"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                            <button class="w-7 h-7 rounded bg-primary text-on-primary flex items-center justify-center font-medium">1</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">3</button>
                            <span class="w-7 h-7 flex items-center justify-center text-on-surface-variant">...</span>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">126</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                            <div class="flex items-center gap-2 ml-4">
                                <span class="text-on-surface-variant">10 / page</span>
                                <span class="material-symbols-outlined text-sm">expand_more</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar (Order Details) -->
                <div class="w-[320px] shrink-0 flex flex-col gap-4 overflow-y-auto custom-scrollbar pr-1">
                    
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="text-sm font-medium text-white">Order Details</h3>
                            <a href="#" class="text-[10px] text-primary hover:underline">View Full Order</a>
                        </div>
                        <div class="flex justify-between items-center mt-3">
                            <div>
                                <h4 class="text-base font-bold text-white leading-none">#ORD-2024-1256</h4>
                                <p class="text-[10px] text-on-surface-variant mt-1">Placed on 12 May 2024, 10:30 AM</p>
                            </div>
                            <span class="text-[#68D391] text-[10px] font-medium border border-[#68D391]/20 px-2 py-0.5 rounded">Delivered</span>
                        </div>
                        
                        <div class="grid grid-cols-4 gap-2 mt-4 pt-4 border-t border-white/5">
                            <button class="flex flex-col items-center justify-center gap-1.5 text-on-surface-variant hover:text-white transition-colors">
                                <span class="material-symbols-outlined text-[18px]">receipt_long</span>
                                <span class="text-[9px]">Invoice</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1.5 text-on-surface-variant hover:text-white transition-colors">
                                <span class="material-symbols-outlined text-[18px]">local_shipping</span>
                                <span class="text-[9px]">Tracking</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1.5 text-on-surface-variant hover:text-white transition-colors">
                                <span class="material-symbols-outlined text-[18px]">assignment_return</span>
                                <span class="text-[9px]">Return</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1.5 text-on-surface-variant hover:text-white transition-colors">
                                <span class="material-symbols-outlined text-[18px]">download</span>
                                <span class="text-[9px]">Download</span>
                            </button>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-[11px] uppercase tracking-wider text-on-surface-variant font-medium mb-3">Customer Information</h3>
                        <div class="flex items-center gap-3 mb-4">
                            <img src="https://i.pravatar.cc/150?u=1" class="w-10 h-10 rounded-full">
                            <div class="flex-1 min-w-0">
                                <p class="text-sm font-medium text-white truncate">Rahul Verma</p>
                                <p class="text-[10px] text-primary truncate">rahul@example.com</p>
                            </div>
                            <a href="#" class="text-[10px] text-primary hover:underline whitespace-nowrap">View Profile &gt;</a>
                        </div>
                        <div class="space-y-2.5">
                            <div class="flex items-start gap-2">
                                <span class="material-symbols-outlined text-[14px] text-on-surface-variant mt-0.5">call</span>
                                <p class="text-[11px] text-on-surface-variant">+91 98765 43210</p>
                            </div>
                            <div class="flex items-start gap-2">
                                <span class="material-symbols-outlined text-[14px] text-on-surface-variant mt-0.5">location_on</span>
                                <p class="text-[11px] text-on-surface-variant leading-snug">
                                    221B Baker Street, Near Park Street<br>
                                    Kolkata, West Bengal - 700016<br>
                                    India
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-[11px] uppercase tracking-wider text-on-surface-variant font-medium mb-3">Order Summary</h3>
                        <div class="space-y-2 text-[11px]">
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Items (8)</span>
                                <span class="text-white">₹ 1,28,350</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Shipping</span>
                                <span class="text-white">₹ 0</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Tax (18%)</span>
                                <span class="text-white">₹ 20,300</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Discount</span>
                                <span class="text-white">- ₹ 0</span>
                            </div>
                            <div class="pt-2 mt-2 border-t border-white/5 flex justify-between items-center">
                                <span class="text-white font-medium">Total Amount</span>
                                <span class="text-sm font-bold text-white">₹ 1,48,650</span>
                            </div>
                            <div class="flex justify-between items-center pt-2">
                                <span class="text-on-surface-variant">Payment Method</span>
                                <span class="text-white">Online (UPI)</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Payment Status</span>
                                <span class="text-[#68D391] font-medium">Paid</span>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-[11px] uppercase tracking-wider text-on-surface-variant font-medium mb-4">Order Timeline</h3>
                        <div class="relative pl-3 space-y-4 before:absolute before:inset-0 before:ml-4 before:-translate-x-px before:h-full before:w-0.5 before:bg-white/10">
                            
                            <div class="relative flex items-start gap-4">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#68D391] ring-4 ring-surface-deep z-10 shrink-0 mt-1 shadow-[0_0_8px_rgba(104,211,145,0.4)]"></div>
                                <div>
                                    <h4 class="text-[11px] font-medium text-white">Delivered</h4>
                                    <p class="text-[9px] text-on-surface-variant mt-0.5">Order delivered on 15 May 2024, 02:30 PM</p>
                                </div>
                            </div>
                            
                            <div class="relative flex items-start gap-4">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#B794F6] ring-4 ring-surface-deep z-10 shrink-0 mt-1 shadow-[0_0_8px_rgba(183,148,246,0.4)]"></div>
                                <div>
                                    <h4 class="text-[11px] font-medium text-white">Shipped</h4>
                                    <p class="text-[9px] text-on-surface-variant mt-0.5">Order shipped on 14 May 2024, 11:20 AM</p>
                                </div>
                            </div>
                            
                            <div class="relative flex items-start gap-4">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#63B3ED] ring-4 ring-surface-deep z-10 shrink-0 mt-1 shadow-[0_0_8px_rgba(99,179,237,0.4)]"></div>
                                <div>
                                    <h4 class="text-[11px] font-medium text-white">Processing</h4>
                                    <p class="text-[9px] text-on-surface-variant mt-0.5">Order is being processed on 12 May 2024, 10:45 AM</p>
                                </div>
                            </div>
                            
                            <div class="relative flex items-start gap-4">
                                <div class="w-2.5 h-2.5 rounded-full bg-white/20 ring-4 ring-surface-deep z-10 shrink-0 mt-1"></div>
                                <div>
                                    <h4 class="text-[11px] font-medium text-white">Order Placed</h4>
                                    <p class="text-[9px] text-on-surface-variant mt-0.5">Order placed on 12 May 2024, 10:30 AM</p>
                                </div>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep">{order_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Order History'
    # By this time, it should already be updated to admin-order-history.html by update_sidebar_in_file in the loop (except maybe base_html was read before. Wait, base_html is read before update_sidebar_in_file runs on it? No, base_html is read fresh).
    # Actually, we will just use regex to find Order History and make it active.
    order_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Order History\s*</a>'
    order_active = """<a href="admin-order-history.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Order History
                </a>"""
    new_html = re.sub(order_inactive, order_active, new_html)

    with open('admin-order-history.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-order-history.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-order-history.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_order_history()

if __name__ == '__main__':
    main()
