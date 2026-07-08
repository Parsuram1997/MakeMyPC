import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Support Tickets link
    support_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Support Tickets\s*</a>'
    new_support = '<a href="admin-support-tickets.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Support Tickets\n                </a>'
    
    if re.search(support_pattern, content):
        content = re.sub(support_pattern, new_support, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_support_tickets():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    support_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Support Tickets</h2>
                    <p class="text-on-surface-variant text-sm">Manage and resolve customer support requests efficiently.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export Tickets
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">description</span>
                        Reports
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">add</span>
                        New Ticket
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-6 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">inbox</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TOTAL TICKETS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">1,256</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">All time tickets</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">mark_email_unread</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">OPEN TICKETS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">156</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">12.4% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">schedule</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">IN PROGRESS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">82</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">6.5% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">check_circle</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">RESOLVED</p>
                        <h3 class="text-lg font-bold text-white leading-tight">896</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">71.3% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-surface-container-highest text-on-surface-variant flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">cancel</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">CLOSED</p>
                        <h3 class="text-lg font-bold text-white leading-tight">122</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">9.7% of total</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl flex items-center gap-4 border border-white/5">
                    <div class="w-10 h-10 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">timer</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">AVG. RESPONSE TIME</p>
                        <h3 class="text-lg font-bold text-white leading-tight">2h 35m</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">This month</p>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-4 relative z-10">
                <div class="flex gap-3 flex-1 max-w-5xl">
                    <div class="relative flex-1 max-w-[260px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by ticket ID, customer name, email..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-9 pr-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Status</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-36">
                        <option>All Categories</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Priority</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-36">
                        <option>All Channels</option>
                    </select>
                    <button class="px-3 py-2 rounded-lg border border-white/5 hover:bg-white/5 transition-colors text-[13px] flex items-center gap-1.5 text-white bg-surface-container-highest/50">
                        <span class="material-symbols-outlined text-[16px]">filter_alt</span>
                        More Filters
                    </button>
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
                                    <th class="px-4 py-3 font-medium tracking-wider">TICKET ID <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CUSTOMER</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">SUBJECT <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CATEGORY <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">PRIORITY <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">STATUS <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CHANNEL <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CREATED ON <span class="material-symbols-outlined text-[12px] align-middle">expand_more</span></th>
                                    <th class="px-4 py-3 font-medium tracking-wider text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 - Active -->
                                <tr class="bg-primary/5 hover:bg-primary/10 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="text-white font-medium">#TKT-2024-1256</div>
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
                                        <p class="text-white text-[11px] font-medium">Order not delivered</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Tracking ID: TRK123456</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Order & Delivery</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#FC8181] font-medium">High</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[10px] font-medium border border-[#63B3ED]/20">Open</span>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[16px]">mail</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
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
                                        <div class="text-on-surface-variant font-medium">#TKT-2024-1255</div>
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
                                        <p class="text-white text-[11px] font-medium">Wrong item received</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Order ID: ORD-1254</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Returns & Refunds</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#F6AD55] font-medium">Medium</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[10px] font-medium border border-[#F6AD55]/20">In Progress</span>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[16px]">call</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">11 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                    </td>
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
                                        <div class="text-on-surface-variant font-medium">#TKT-2024-1254</div>
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
                                        <p class="text-white text-[11px] font-medium">PC not powering on</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Build ID: BLD-4567</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Technical Support</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#FC8181] font-medium">High</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[10px] font-medium border border-[#F6AD55]/20">In Progress</span>
                                    </td>
                                    <td class="px-4 py-3 text-[#68D391]">
                                        <span class="material-symbols-outlined text-[16px]">chat</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">10 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                    </td>
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
                                        <div class="text-on-surface-variant font-medium">#TKT-2024-1253</div>
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
                                        <p class="text-white text-[11px] font-medium">Refund not processed</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Order ID: ORD-1248</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Returns & Refunds</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#F6AD55] font-medium">Medium</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[10px] font-medium border border-[#63B3ED]/20">Open</span>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[16px]">mail</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">09 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                    </td>
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
                                <!-- Row 5 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="text-on-surface-variant font-medium">#TKT-2024-1252</div>
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
                                        <p class="text-white text-[11px] font-medium">Need help with build</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Build ID: BLD-4590</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Pre Sales Support</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] font-medium">Low</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[10px] font-medium border border-[#B794F6]/20">Resolved</span>
                                    </td>
                                    <td class="px-4 py-3 text-[#68D391]">
                                        <span class="material-symbols-outlined text-[16px]">chat</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">08 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">03:30 PM</p>
                                    </td>
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
                                <!-- More placeholder rows representing the screenshot design -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <div class="text-on-surface-variant font-medium">#TKT-2024-1250</div>
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
                                        <p class="text-white text-[11px] font-medium">Missing parts in delivery</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">Order ID: ORD-1242</p>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">Order & Delivery</td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#F6AD55] font-medium">Medium</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="px-2 py-0.5 rounded text-[#B794F6] text-[10px] font-medium border border-[#B794F6]/20">Resolved</span>
                                    </td>
                                    <td class="px-4 py-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[16px]">mail</span>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">06 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">01:05 PM</p>
                                    </td>
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
                        <p class="text-on-surface-variant">Showing 1 to 10 of 1,256 tickets</p>
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

                <!-- Right Sidebar (Ticket Details) -->
                <div class="w-[320px] shrink-0 flex flex-col gap-4 overflow-y-auto custom-scrollbar pr-1">
                    
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-start mb-4">
                            <h3 class="text-sm font-medium text-white">Ticket Details</h3>
                            <div class="flex flex-col items-end gap-1.5">
                                <span class="text-[#63B3ED] text-[10px] font-medium border border-[#63B3ED]/20 px-2 py-0.5 rounded">Open</span>
                                <span class="text-[#FC8181] text-[10px] font-medium border border-[#FC8181]/20 px-2 py-0.5 rounded">High</span>
                            </div>
                        </div>
                        <div class="mb-4">
                            <h4 class="text-base font-bold text-white leading-tight">#TKT-2024-1256</h4>
                            <p class="text-[12px] text-white mt-1">Order not delivered</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Created on 12 May 2024, 10:30 AM</p>
                        </div>
                        
                        <div class="flex items-center gap-3 mb-5 border-y border-white/5 py-4">
                            <img src="https://i.pravatar.cc/150?u=1" class="w-10 h-10 rounded-full">
                            <div class="flex-1 min-w-0">
                                <p class="text-sm font-medium text-white truncate">Rahul Verma</p>
                                <p class="text-[10px] text-primary truncate">rahul@example.com</p>
                                <p class="text-[10px] text-on-surface-variant mt-0.5">+91 98765 43210</p>
                            </div>
                            <a href="#" class="text-[10px] text-primary hover:underline whitespace-nowrap self-start mt-1">View Profile &gt;</a>
                        </div>
                        
                        <div class="space-y-3 text-[11px] mb-5">
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Category</span>
                                <span class="text-white">Order & Delivery</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Order ID</span>
                                <span class="text-white">ORD-1234</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Channel</span>
                                <span class="text-white flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">mail</span> Email</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Assigned To</span>
                                <span class="text-white">Sumit Kumar</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Last Updated</span>
                                <span class="text-white">12 May 2024, 11:15 AM</span>
                            </div>
                        </div>

                        <div>
                            <h3 class="text-[11px] font-medium text-white mb-2">Ticket Description</h3>
                            <div class="text-[11px] text-on-surface-variant leading-relaxed space-y-2 bg-surface-deep/30 p-3 rounded-lg border border-white/5">
                                <p>Hi,</p>
                                <p>My order was supposed to be delivered on 10 May 2024 but I haven't received it yet. Tracking shows it's in transit for last 3 days.</p>
                                <p>Please look into this and help me.</p>
                                <p>Thanks,<br>Rahul</p>
                            </div>
                        </div>

                        <div class="mt-5 space-y-2">
                            <button class="w-full py-2.5 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[16px]">reply</span>
                                Reply to Customer
                            </button>
                            <div class="flex gap-2">
                                <button class="flex-1 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-xs flex items-center justify-center gap-1.5 text-white">
                                    <span class="material-symbols-outlined text-[16px]">edit_note</span>
                                    Add Note
                                </button>
                                <button class="flex-1 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-xs flex items-center justify-center gap-1.5 text-white">
                                    <span class="material-symbols-outlined text-[16px]">person_add</span>
                                    Assign Ticket
                                </button>
                            </div>
                            <button class="w-full py-2 rounded-lg border border-[#68D391]/30 hover:bg-[#68D391]/10 text-[#68D391] transition-colors text-xs flex items-center justify-center gap-1.5 mt-2">
                                <span class="material-symbols-outlined text-[16px]">check_circle</span>
                                Close Ticket
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep">{support_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Support Tickets'
    support_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Support Tickets\s*</a>'
    support_active = """<a href="admin-support-tickets.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Support Tickets
                </a>"""
    new_html = re.sub(support_inactive, support_active, new_html)

    with open('admin-support-tickets.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-support-tickets.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-support-tickets.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_support_tickets()

if __name__ == '__main__':
    main()
