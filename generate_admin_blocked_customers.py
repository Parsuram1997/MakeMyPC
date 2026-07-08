import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Blocked Customers link
    blocked_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Blocked Customers\s*</a>'
    new_blocked = '<a href="admin-blocked-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Blocked Customers\n                </a>'
    
    if re.search(blocked_pattern, content):
        content = re.sub(blocked_pattern, new_blocked, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_blocked_customers():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    blocked_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Blocked Customers</h2>
                    <p class="text-on-surface-variant text-sm">Manage customers who are blocked from placing orders or accessing services.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export List
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">more_horiz</span>
                        More Actions
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">block</span>
                        Block Customer
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-5 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#FC8181]/10 text-[#FC8181] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">group_off</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">TOTAL BLOCKED</p>
                        <h3 class="text-lg font-bold text-white leading-tight">156</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">All time blocked customers</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#FC8181]/20 text-[#FC8181] border border-[#FC8181]/20 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">gpp_bad</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">ACTIVE BLOCKED</p>
                        <h3 class="text-lg font-bold text-white leading-tight">132</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">Currently blocked</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">history</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">UNBLOCKED (THIS MONTH)</p>
                        <h3 class="text-lg font-bold text-white leading-tight">24</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">Customers unblocked</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#FC8181]/10 text-[#FC8181] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">warning</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">BLOCKED ORDERS</p>
                        <h3 class="text-lg font-bold text-white leading-tight">218</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">Orders from blocked users</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-10 h-10 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[20px]">currency_rupee</span>
                    </div>
                    <div>
                        <p class="text-[9px] text-on-surface-variant uppercase tracking-wider mb-0.5 font-semibold">REFUNDS PROCESSED</p>
                        <h3 class="text-lg font-bold text-white leading-tight">₹ 2,45,300</h3>
                        <p class="text-[10px] text-on-surface-variant mt-0.5">From blocked customers</p>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-4 relative z-10">
                <div class="flex gap-3 flex-1 max-w-4xl">
                    <div class="relative flex-1 max-w-[280px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by name, email, phone, or customer ID..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-9 pr-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-36">
                        <option>All Reasons</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Status</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Time</option>
                    </select>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-[16px]">filter_list</span>
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
                                    <th class="px-4 py-3 font-medium tracking-wider w-10">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CUSTOMER</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CONTACT</th>
                                    <th class="px-4 py-3 font-medium tracking-wider w-[220px]">REASON</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">BLOCKED ON</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">BLOCKED BY</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">STATUS</th>
                                    <th class="px-4 py-3 font-medium tracking-wider text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group bg-white/[0.02]">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=1" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Rohit Kumar</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1256</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">rohit.kumar@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 98765 43210</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#FC8181] mt-0.5">warning</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Fake Order</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Multiple fake orders</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 2 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=2" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Neha Verma</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1255</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">neha.verma@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 91234 56789</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#F6AD55] mt-0.5">credit_card_off</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Payment Fraud</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Payment issues</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">11 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 3 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=3" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Amit Singh</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1254</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">amit.singh@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 99887 66554</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#B794F6] mt-0.5">block</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Abuse / Harassment</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Abusive behavior</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">10 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 4 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=4" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Pooja Sharma</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1253</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">pooja.sharma@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 88776 54321</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#F6AD55] mt-0.5">currency_exchange</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Refund Abuse</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Misused refund policy</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">09 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 5 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=5" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Vikram Joshi</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1252</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">vikram.joshi@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 77665 44332</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#FC8181] mt-0.5">gavel</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Chargeback</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Excessive chargebacks</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">08 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">03:30 PM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 6 - Active -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-xs font-medium border border-[#B794F6]/20">AS</div>
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Arjun Saxena</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1251</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">arjun.saxena@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 66554 33221</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-slate-400 mt-0.5">policy</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Policy Violation</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Terms of service violation</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">07 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">02:10 PM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                            <span class="material-symbols-outlined text-[12px]">gpp_bad</span>
                                            Active
                                        </div>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 7 - Unblocked -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <img src="https://i.pravatar.cc/150?u=6" class="w-8 h-8 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Sneha Reddy</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1250</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">sneha.reddy@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 55443 22110</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#F6AD55] mt-0.5">local_shipping</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">COD Abuse</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Repeated COD refusal</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">06 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">01:05 PM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] text-[10px] font-medium">Unblocked</span>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 8 - Unblocked -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-3">
                                        <input type="checkbox" class="rounded border-white/20 bg-surface-deep/50 text-primary focus:ring-primary/50">
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded-full bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center text-xs font-medium border border-[#63B3ED]/20">DK</div>
                                            <div>
                                                <p class="font-medium text-white text-[12px]">Deepak Yadav</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">CUS-2024-1249</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">deepak.yadav@example.com</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">+91 44332 11099</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-start gap-2">
                                            <span class="material-symbols-outlined text-[14px] text-[#FC8181] mt-0.5">group_add</span>
                                            <div>
                                                <p class="text-white text-[11px] font-medium">Account Sharing</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">Suspicious account activity</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <p class="text-white text-[11px]">05 May 2024</p>
                                        <p class="text-[9px] text-on-surface-variant mt-0.5">12:40 PM</p>
                                    </td>
                                    <td class="px-4 py-3">
                                        <div class="flex items-center gap-2">
                                            <div class="w-5 h-5 rounded-full bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center text-[8px] font-medium border border-[#B794F6]/20">AD</div>
                                            <span class="text-white text-[11px]">Admin User</span>
                                        </div>
                                    </td>
                                    <td class="px-4 py-3">
                                        <span class="text-[#68D391] text-[10px] font-medium">Unblocked</span>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-7 h-7 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="p-3 border-t border-white/5 bg-surface-deep/50 backdrop-blur flex justify-between items-center text-xs">
                        <p class="text-on-surface-variant">Showing 1 to 8 of 156 blocked customers</p>
                        <div class="flex gap-1 items-center">
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors disabled:opacity-50 text-white"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                            <button class="w-7 h-7 rounded bg-primary text-on-primary flex items-center justify-center font-medium">1</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">3</button>
                            <span class="w-7 h-7 flex items-center justify-center text-on-surface-variant">...</span>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">16</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                            <div class="flex items-center gap-2 ml-4">
                                <span class="text-on-surface-variant">10 / page</span>
                                <span class="material-symbols-outlined text-sm">expand_more</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar (Customer Details) -->
                <div class="w-[340px] shrink-0 flex flex-col overflow-y-auto custom-scrollbar pr-1">
                    <div class="glass-card rounded-xl border border-white/5 p-6 flex flex-col min-h-0 relative">
                        
                        <!-- Header -->
                        <div class="flex justify-between items-center mb-6">
                            <h3 class="text-sm font-medium text-white">Customer Details</h3>
                            <div class="flex items-center gap-1 text-[#FC8181] text-[10px] font-medium">
                                <span class="material-symbols-outlined text-[14px]">gpp_bad</span>
                                Active
                            </div>
                        </div>

                        <!-- Profile Info -->
                        <div class="flex gap-4 mb-6">
                            <img src="https://i.pravatar.cc/150?u=1" class="w-12 h-12 rounded-full border border-white/10">
                            <div>
                                <h4 class="text-sm font-medium text-white leading-tight">Rohit Kumar</h4>
                                <p class="text-[11px] text-on-surface-variant mt-0.5">CUS-2024-1256</p>
                                <p class="text-[11px] text-on-surface-variant mt-1">rohit.kumar@example.com</p>
                                <p class="text-[11px] text-on-surface-variant mt-0.5">+91 98765 43210</p>
                            </div>
                        </div>

                        <!-- Stats -->
                        <div class="grid grid-cols-3 gap-2 mb-6 text-center">
                            <div class="p-2 rounded-lg bg-surface-container-highest/30 border border-white/5">
                                <div class="flex items-center justify-center gap-1 text-on-surface-variant mb-1">
                                    <span class="material-symbols-outlined text-[12px]">shopping_bag</span>
                                    <span class="text-[10px]">Total Orders</span>
                                </div>
                                <p class="text-[12px] font-medium text-white">12</p>
                            </div>
                            <div class="p-2 rounded-lg bg-surface-container-highest/30 border border-white/5">
                                <div class="flex items-center justify-center gap-1 text-on-surface-variant mb-1">
                                    <span class="material-symbols-outlined text-[12px]">currency_rupee</span>
                                    <span class="text-[10px]">Total Spent</span>
                                </div>
                                <p class="text-[12px] font-medium text-white">₹ 45,600</p>
                            </div>
                            <div class="p-2 rounded-lg bg-surface-container-highest/30 border border-white/5">
                                <div class="flex items-center justify-center gap-1 text-on-surface-variant mb-1">
                                    <span class="material-symbols-outlined text-[12px]">currency_exchange</span>
                                    <span class="text-[10px]">Refunds</span>
                                </div>
                                <p class="text-[12px] font-medium text-white">₹ 5,200</p>
                            </div>
                        </div>

                        <!-- Info List -->
                        <div class="space-y-4 mb-6 flex-1">
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">Reason</div>
                                <div class="col-span-8 text-white font-medium">Fake Order</div>
                            </div>
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">Details</div>
                                <div class="col-span-8 text-on-surface-variant">Customer placed multiple fake orders using different accounts and addresses.</div>
                            </div>
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">Blocked On</div>
                                <div class="col-span-8 text-white">12 May 2024, 10:30 AM</div>
                            </div>
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">Blocked By</div>
                                <div class="col-span-8 text-white">Admin User</div>
                            </div>
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">IP Address</div>
                                <div class="col-span-8 text-white">103.21.244.12</div>
                            </div>
                            <div class="grid grid-cols-12 gap-2 text-[11px]">
                                <div class="col-span-4 text-on-surface-variant">Last Order ID</div>
                                <div class="col-span-8 text-white">ORD-2024-1256</div>
                            </div>
                        </div>

                        <!-- Recent Orders -->
                        <div class="mb-6 pt-4 border-t border-white/5">
                            <div class="flex justify-between items-center mb-4">
                                <h4 class="text-[12px] font-medium text-white">Recent Orders (Before Blocked)</h4>
                                <a href="#" class="text-[10px] text-primary hover:underline">View All</a>
                            </div>
                            <div class="space-y-3">
                                <div class="flex justify-between items-center text-[11px]">
                                    <span class="text-white w-[90px]">ORD-2024-1258</span>
                                    <span class="text-white w-[50px]">₹ 15,990</span>
                                    <span class="text-on-surface-variant w-[65px]">12 May 2024</span>
                                    <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[9px] font-medium border border-[#F6AD55]/20 bg-[#7C4A15]/20">Cancelled</span>
                                </div>
                                <div class="flex justify-between items-center text-[11px]">
                                    <span class="text-white w-[90px]">ORD-2024-1257</span>
                                    <span class="text-white w-[50px]">₹ 24,500</span>
                                    <span class="text-on-surface-variant w-[65px]">11 May 2024</span>
                                    <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[9px] font-medium border border-[#F6AD55]/20 bg-[#7C4A15]/20">Cancelled</span>
                                </div>
                                <div class="flex justify-between items-center text-[11px]">
                                    <span class="text-white w-[90px]">ORD-2024-1256</span>
                                    <span class="text-white w-[50px]">₹ 18,450</span>
                                    <span class="text-on-surface-variant w-[65px]">10 May 2024</span>
                                    <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[9px] font-medium border border-[#F6AD55]/20 bg-[#7C4A15]/20">Cancelled</span>
                                </div>
                            </div>
                        </div>

                        <!-- Action Buttons -->
                        <div class="flex flex-col gap-2 mt-auto">
                            <button class="w-full py-2 rounded-lg border border-primary/50 text-primary hover:bg-primary/5 transition-colors text-[12px] font-medium flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[16px]">lock_open</span>
                                Unblock Customer
                            </button>
                            <button class="w-full py-2 rounded-lg border border-[#FC8181]/30 text-[#FC8181] hover:bg-[#FC8181]/5 transition-colors text-[12px] font-medium flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[16px]">delete</span>
                                Delete Customer
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep flex flex-col">{blocked_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Blocked Customers'
    blocked_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Blocked Customers\s*</a>'
    blocked_active = """<a href="admin-blocked-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Blocked Customers
                </a>"""
    if not re.search(blocked_inactive, new_html):
        print("Could not find inactive Blocked Customers link to replace.")
    new_html = re.sub(blocked_inactive, blocked_active, new_html)

    with open('admin-blocked-customers.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-blocked-customers.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-blocked-customers.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_blocked_customers()

if __name__ == '__main__':
    main()
