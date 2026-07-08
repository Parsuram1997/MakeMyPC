import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Loyalty & Rewards link
    loyalty_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Loyalty &amp; Rewards\s*</a>'
    new_loyalty = '<a href="admin-loyalty-rewards.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Loyalty &amp; Rewards\n                </a>'
    
    if re.search(loyalty_pattern, content):
        content = re.sub(loyalty_pattern, new_loyalty, content)
    else:
        # It could be & not &amp; depending on how it's written
        loyalty_pattern2 = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Loyalty & Rewards\s*</a>'
        new_loyalty2 = '<a href="admin-loyalty-rewards.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Loyalty & Rewards\n                </a>'
        content = re.sub(loyalty_pattern2, new_loyalty2, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_loyalty_rewards():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    loyalty_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Loyalty & Rewards</h2>
                    <p class="text-on-surface-variant text-sm">Manage customer loyalty points, rewards, tiers and offers.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export Report
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">settings</span>
                        Reward Settings
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">add</span>
                        Add Reward
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-5 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">group</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL MEMBERS</p>
                        <h3 class="text-xl font-bold text-white leading-tight">2,847</h3>
                        <p class="text-[11px] text-[#68D391] mt-1 font-medium">+18% <span class="text-on-surface-variant font-normal">from last month</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">stars</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL POINTS ISSUED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">12,45,600</h3>
                        <p class="text-[11px] text-[#68D391] mt-1 font-medium">+22% <span class="text-on-surface-variant font-normal">from last month</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">shopping_bag</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL POINTS REDEEMED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">8,76,450</h3>
                        <p class="text-[11px] text-[#68D391] mt-1 font-medium">+16% <span class="text-on-surface-variant font-normal">from last month</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">redeem</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL REWARDS REDEEMED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">1,256</h3>
                        <p class="text-[11px] text-[#68D391] mt-1 font-medium">+10% <span class="text-on-surface-variant font-normal">from last month</span></p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">currency_rupee</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL REWARD VALUE</p>
                        <h3 class="text-xl font-bold text-white leading-tight">₹ 18,75,230</h3>
                        <p class="text-[11px] text-[#68D391] mt-1 font-medium">+20% <span class="text-on-surface-variant font-normal">from last month</span></p>
                    </div>
                </div>
            </div>

            <!-- Tabs -->
            <div class="flex gap-6 border-b border-white/10 mb-6 relative z-10 text-sm">
                <a href="#" class="text-primary font-medium border-b-2 border-primary pb-3 px-1">Overview</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Members</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Point Transactions</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Rewards</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Tiers</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Promotions</a>
            </div>

            <!-- Main Content Grid -->
            <div class="grid grid-cols-12 gap-6 relative z-10 flex-1 min-h-0 overflow-y-auto custom-scrollbar pb-6 pr-2">
                
                <!-- Left/Middle Section (spans 8 cols) -->
                <div class="col-span-8 flex flex-col gap-6">
                    
                    <!-- Top Row: Points Summary & How Points Are Earned -->
                    <div class="grid grid-cols-2 gap-6">
                        <!-- Points Summary -->
                        <div class="glass-card rounded-xl border border-white/5 p-5">
                            <h3 class="text-sm font-medium text-white mb-6">Points Summary</h3>
                            <div class="flex gap-6 items-center">
                                <!-- Donut Chart using conic-gradient -->
                                <div class="relative w-44 h-44 rounded-full flex items-center justify-center" style="background: conic-gradient(#1B5038 0% 60%, #1A4B8C 60% 92%, #7F1D1D 92% 100%); padding: 16px;">
                                    <div class="bg-surface-deep w-full h-full rounded-full flex flex-col items-center justify-center border border-white/5 shadow-inner">
                                        <span class="text-xl font-bold text-white leading-none">12,45,600</span>
                                        <span class="text-[10px] text-on-surface-variant mt-1">Total Points</span>
                                    </div>
                                </div>
                                <div class="flex flex-col gap-4 flex-1">
                                    <div>
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#68D391]"></span>
                                            <span class="text-xs text-on-surface-variant">Earned</span>
                                        </div>
                                        <div class="flex justify-between items-center pl-4.5">
                                            <span class="text-sm font-medium text-white">12,45,600</span>
                                            <span class="text-[10px] text-on-surface-variant">(60%)</span>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#63B3ED]"></span>
                                            <span class="text-xs text-on-surface-variant">Redeemed</span>
                                        </div>
                                        <div class="flex justify-between items-center pl-4.5">
                                            <span class="text-sm font-medium text-white">8,76,450</span>
                                            <span class="text-[10px] text-on-surface-variant">(32%)</span>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#FC8181]"></span>
                                            <span class="text-xs text-on-surface-variant">Expired</span>
                                        </div>
                                        <div class="flex justify-between items-center pl-4.5">
                                            <span class="text-sm font-medium text-white">1,23,750</span>
                                            <span class="text-[10px] text-on-surface-variant">(8%)</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- How Points Are Earned -->
                        <div class="glass-card rounded-xl border border-white/5 p-5">
                            <h3 class="text-sm font-medium text-white mb-4">How Points Are Earned</h3>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between p-2 hover:bg-white/5 rounded-lg transition-colors group cursor-default">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center group-hover:bg-[#1B5038]/50 transition-colors">
                                            <span class="material-symbols-outlined text-[18px]">shopping_cart_checkout</span>
                                        </div>
                                        <div>
                                            <p class="text-[13px] font-medium text-white">Place an Order</p>
                                            <p class="text-[10px] text-on-surface-variant">10 Points per ₹100</p>
                                        </div>
                                    </div>
                                    <span class="text-xs font-medium text-[#68D391]">10 Pts</span>
                                </div>
                                <div class="flex items-center justify-between p-2 hover:bg-white/5 rounded-lg transition-colors group cursor-default">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center group-hover:bg-[#7C4A15]/50 transition-colors">
                                            <span class="material-symbols-outlined text-[18px]">star_rate</span>
                                        </div>
                                        <div>
                                            <p class="text-[13px] font-medium text-white">Write a Product Review</p>
                                            <p class="text-[10px] text-on-surface-variant">50 Points</p>
                                        </div>
                                    </div>
                                    <span class="text-xs font-medium text-[#68D391]">50 Pts</span>
                                </div>
                                <div class="flex items-center justify-between p-2 hover:bg-white/5 rounded-lg transition-colors group cursor-default">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center group-hover:bg-[#7C4A15]/50 transition-colors">
                                            <span class="material-symbols-outlined text-[18px]">group_add</span>
                                        </div>
                                        <div>
                                            <p class="text-[13px] font-medium text-white">Refer a Friend</p>
                                            <p class="text-[10px] text-on-surface-variant">200 Points</p>
                                        </div>
                                    </div>
                                    <span class="text-xs font-medium text-[#68D391]">200 Pts</span>
                                </div>
                                <div class="flex items-center justify-between p-2 hover:bg-white/5 rounded-lg transition-colors group cursor-default">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center group-hover:bg-[#52358C]/50 transition-colors">
                                            <span class="material-symbols-outlined text-[18px]">person</span>
                                        </div>
                                        <div>
                                            <p class="text-[13px] font-medium text-white">Complete Profile</p>
                                            <p class="text-[10px] text-on-surface-variant">100 Points</p>
                                        </div>
                                    </div>
                                    <span class="text-xs font-medium text-[#68D391]">100 Pts</span>
                                </div>
                                <div class="flex items-center justify-between p-2 hover:bg-white/5 rounded-lg transition-colors group cursor-default">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center group-hover:bg-[#1A4B8C]/50 transition-colors">
                                            <span class="material-symbols-outlined text-[18px]">cake</span>
                                        </div>
                                        <div>
                                            <p class="text-[13px] font-medium text-white">First Order Bonus</p>
                                            <p class="text-[10px] text-on-surface-variant">300 Points</p>
                                        </div>
                                    </div>
                                    <span class="text-xs font-medium text-[#68D391]">300 Pts</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom: Recent Points Transactions -->
                    <div class="glass-card rounded-xl border border-white/5 flex flex-col flex-1">
                        <div class="p-5 border-b border-white/5 pb-4">
                            <h3 class="text-sm font-medium text-white">Recent Points Transactions</h3>
                        </div>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left text-sm border-collapse">
                                <thead class="bg-surface-deep/50 text-[10px] uppercase text-on-surface-variant/70">
                                    <tr>
                                        <th class="px-5 py-3 font-medium tracking-wider">MEMBER</th>
                                        <th class="px-5 py-3 font-medium tracking-wider">TYPE</th>
                                        <th class="px-5 py-3 font-medium tracking-wider">DESCRIPTION</th>
                                        <th class="px-5 py-3 font-medium tracking-wider">POINTS</th>
                                        <th class="px-5 py-3 font-medium tracking-wider">DATE &uarr;</th>
                                        <th class="px-5 py-3 font-medium tracking-wider">EXPIRY DATE</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-white/5 text-xs">
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="px-5 py-3">
                                            <div class="flex items-center gap-2">
                                                <img src="https://i.pravatar.cc/150?u=1" class="w-7 h-7 rounded-full">
                                                <div>
                                                    <p class="font-medium text-white text-[12px]">Rahul Verma</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">rahul@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-5 py-3">
                                            <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Earned</span>
                                        </td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px] font-medium">Order #ORD-2024-1256</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Placed an order</p>
                                        </td>
                                        <td class="px-5 py-3 text-[#68D391] font-medium">+1,256</td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px]">12 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                        </td>
                                        <td class="px-5 py-3 text-on-surface-variant text-[11px]">12 May 2025</td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="px-5 py-3">
                                            <div class="flex items-center gap-2">
                                                <img src="https://i.pravatar.cc/150?u=2" class="w-7 h-7 rounded-full">
                                                <div>
                                                    <p class="font-medium text-white text-[12px]">Priya Sharma</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">priya@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-5 py-3">
                                            <span class="px-2 py-0.5 rounded text-[#63B3ED] text-[10px] font-medium border border-[#63B3ED]/20">Redeemed</span>
                                        </td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px] font-medium">Redeemed for ₹500 Discount</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Order #ORD-2024-1250</p>
                                        </td>
                                        <td class="px-5 py-3 text-[#FC8181] font-medium">-500</td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px]">11 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                        </td>
                                        <td class="px-5 py-3 text-on-surface-variant text-[11px]">-</td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="px-5 py-3">
                                            <div class="flex items-center gap-2">
                                                <img src="https://i.pravatar.cc/150?u=3" class="w-7 h-7 rounded-full">
                                                <div>
                                                    <p class="font-medium text-white text-[12px]">Amit Singh</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">amit@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-5 py-3">
                                            <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Earned</span>
                                        </td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px] font-medium">Product Review</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Reviewed ASUS TUF B650</p>
                                        </td>
                                        <td class="px-5 py-3 text-[#68D391] font-medium">+50</td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px]">10 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                        </td>
                                        <td class="px-5 py-3 text-on-surface-variant text-[11px]">10 May 2025</td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="px-5 py-3">
                                            <div class="flex items-center gap-2">
                                                <img src="https://i.pravatar.cc/150?u=4" class="w-7 h-7 rounded-full">
                                                <div>
                                                    <p class="font-medium text-white text-[12px]">Neha Gupta</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">neha@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-5 py-3">
                                            <span class="px-2 py-0.5 rounded text-[#68D391] text-[10px] font-medium border border-[#68D391]/20">Earned</span>
                                        </td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px] font-medium">Refer a Friend</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Referred by Amit Singh</p>
                                        </td>
                                        <td class="px-5 py-3 text-[#68D391] font-medium">+200</td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px]">09 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                        </td>
                                        <td class="px-5 py-3 text-on-surface-variant text-[11px]">09 May 2025</td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="px-5 py-3">
                                            <div class="flex items-center gap-2">
                                                <img src="https://i.pravatar.cc/150?u=5" class="w-7 h-7 rounded-full">
                                                <div>
                                                    <p class="font-medium text-white text-[12px]">Vikram Joshi</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">vikram@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-5 py-3">
                                            <span class="px-2 py-0.5 rounded text-[#FC8181] text-[10px] font-medium border border-[#FC8181]/20">Expired</span>
                                        </td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px] font-medium">Points Expired</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Order #ORD-2023-998</p>
                                        </td>
                                        <td class="px-5 py-3 text-[#FC8181] font-medium">-150</td>
                                        <td class="px-5 py-3">
                                            <p class="text-white text-[11px]">08 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">12:30 PM</p>
                                        </td>
                                        <td class="px-5 py-3 text-on-surface-variant text-[11px]">08 May 2024</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="p-4 border-t border-white/5 mt-auto">
                            <a href="#" class="text-primary hover:underline text-[13px] font-medium">View All Transactions</a>
                        </div>
                    </div>

                </div>

                <!-- Right Section (spans 4 cols) -->
                <div class="col-span-4 flex flex-col gap-6">
                    
                    <!-- Loyalty Tiers -->
                    <div class="glass-card rounded-xl border border-white/5 p-5">
                        <div class="flex justify-between items-start mb-4">
                            <div>
                                <h3 class="text-sm font-medium text-white mb-0.5">Loyalty Tiers</h3>
                                <p class="text-[11px] text-on-surface-variant">Manage customer loyalty tiers and benefits</p>
                            </div>
                            <a href="#" class="text-[12px] text-primary hover:underline font-medium mt-1">Manage Tiers</a>
                        </div>
                        <div class="space-y-2 mt-4">
                            <div class="flex items-center justify-between p-3 rounded-lg bg-surface-deep/40 border border-white/5 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-[#7C4A15]/20 flex items-center justify-center border border-[#7C4A15]/40">
                                        <span class="material-symbols-outlined text-[16px] text-[#D69E2E]">military_tech</span>
                                    </div>
                                    <div>
                                        <p class="text-[13px] font-medium text-white">Bronze</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">0 - 999 Points</p>
                                    </div>
                                </div>
                                <span class="text-[11px] font-medium text-[#68D391]">5% Off on Accessories</span>
                            </div>
                            
                            <div class="flex items-center justify-between p-3 rounded-lg bg-surface-deep/40 border border-white/5 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-slate-400/20 flex items-center justify-center border border-slate-400/40">
                                        <span class="material-symbols-outlined text-[16px] text-slate-300">military_tech</span>
                                    </div>
                                    <div>
                                        <p class="text-[13px] font-medium text-white">Silver</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">1,000 - 4,999 Points</p>
                                    </div>
                                </div>
                                <span class="text-[11px] font-medium text-on-surface-variant">7% Off + Free Shipping</span>
                            </div>

                            <div class="flex items-center justify-between p-3 rounded-lg bg-surface-deep/40 border border-white/5 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-[#7C4A15]/30 flex items-center justify-center border border-[#F6AD55]/40">
                                        <span class="material-symbols-outlined text-[16px] text-[#F6AD55]">military_tech</span>
                                    </div>
                                    <div>
                                        <p class="text-[13px] font-medium text-white">Gold</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">5,000 - 14,999 Points</p>
                                    </div>
                                </div>
                                <span class="text-[11px] font-medium text-[#F6AD55]">10% Off + Priority Support</span>
                            </div>

                            <div class="flex items-center justify-between p-3 rounded-lg bg-surface-deep/40 border border-white/5 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-[#52358C]/30 flex items-center justify-center border border-[#B794F6]/40">
                                        <span class="material-symbols-outlined text-[16px] text-[#B794F6]">military_tech</span>
                                    </div>
                                    <div>
                                        <p class="text-[13px] font-medium text-white">Platinum</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">15,000+ Points</p>
                                    </div>
                                </div>
                                <span class="text-[11px] font-medium text-[#B794F6]">15% Off + Exclusive Offers</span>
                            </div>
                        </div>
                    </div>

                    <!-- Top Members -->
                    <div class="glass-card rounded-xl border border-white/5 p-5">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-sm font-medium text-white">Top Members</h3>
                            <a href="#" class="text-[12px] text-primary hover:underline font-medium">View All</a>
                        </div>
                        
                        <div class="grid grid-cols-12 text-[10px] uppercase text-on-surface-variant/70 mb-3 px-1">
                            <div class="col-span-7">MEMBER</div>
                            <div class="col-span-3">TIER</div>
                            <div class="col-span-2 text-right">POINTS</div>
                        </div>
                        
                        <div class="space-y-4 px-1">
                            <div class="grid grid-cols-12 items-center">
                                <div class="col-span-7 flex items-center gap-2">
                                    <img src="https://i.pravatar.cc/150?u=1" class="w-6 h-6 rounded-full">
                                    <span class="text-[12px] text-white">Rahul Verma</span>
                                </div>
                                <div class="col-span-3">
                                    <span class="px-2 py-0.5 rounded text-[#B794F6] text-[10px] font-medium border border-[#B794F6]/20 bg-[#52358C]/20">Platinum</span>
                                </div>
                                <div class="col-span-2 text-right text-[12px] text-white font-medium">18,450</div>
                            </div>
                            
                            <div class="grid grid-cols-12 items-center">
                                <div class="col-span-7 flex items-center gap-2">
                                    <img src="https://i.pravatar.cc/150?u=2" class="w-6 h-6 rounded-full">
                                    <span class="text-[12px] text-white">Priya Sharma</span>
                                </div>
                                <div class="col-span-3">
                                    <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[10px] font-medium border border-[#F6AD55]/20 bg-[#7C4A15]/20">Gold</span>
                                </div>
                                <div class="col-span-2 text-right text-[12px] text-white font-medium">12,760</div>
                            </div>
                            
                            <div class="grid grid-cols-12 items-center">
                                <div class="col-span-7 flex items-center gap-2">
                                    <img src="https://i.pravatar.cc/150?u=3" class="w-6 h-6 rounded-full">
                                    <span class="text-[12px] text-white">Amit Singh</span>
                                </div>
                                <div class="col-span-3">
                                    <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[10px] font-medium border border-[#F6AD55]/20 bg-[#7C4A15]/20">Gold</span>
                                </div>
                                <div class="col-span-2 text-right text-[12px] text-white font-medium">11,230</div>
                            </div>
                            
                            <div class="grid grid-cols-12 items-center">
                                <div class="col-span-7 flex items-center gap-2">
                                    <img src="https://i.pravatar.cc/150?u=4" class="w-6 h-6 rounded-full">
                                    <span class="text-[12px] text-white">Neha Gupta</span>
                                </div>
                                <div class="col-span-3">
                                    <span class="px-2 py-0.5 rounded text-slate-300 text-[10px] font-medium border border-slate-400/20 bg-slate-400/20">Silver</span>
                                </div>
                                <div class="col-span-2 text-right text-[12px] text-white font-medium">4,890</div>
                            </div>
                            
                            <div class="grid grid-cols-12 items-center">
                                <div class="col-span-7 flex items-center gap-2">
                                    <img src="https://i.pravatar.cc/150?u=5" class="w-6 h-6 rounded-full">
                                    <span class="text-[12px] text-white">Vikram Joshi</span>
                                </div>
                                <div class="col-span-3">
                                    <span class="px-2 py-0.5 rounded text-slate-300 text-[10px] font-medium border border-slate-400/20 bg-slate-400/20">Silver</span>
                                </div>
                                <div class="col-span-2 text-right text-[12px] text-white font-medium">4,320</div>
                            </div>
                        </div>
                    </div>

                    <!-- Create Special Promotion -->
                    <div class="rounded-xl overflow-hidden relative p-6 bg-gradient-to-br from-[#2E1A4D] to-[#1A0B2E] border border-[#B794F6]/20 flex flex-col justify-center">
                        <!-- Background glow effect -->
                        <div class="absolute -right-8 -bottom-8 w-32 h-32 bg-[#B794F6]/20 rounded-full blur-2xl"></div>
                        <div class="relative z-10 w-2/3">
                            <h3 class="text-sm font-bold text-white mb-2">Create Special Promotion</h3>
                            <p class="text-[11px] text-[#B794F6] mb-4 leading-relaxed">Run exclusive offers and bonus points</p>
                            <button class="px-4 py-2 rounded-lg bg-[#52358C] hover:bg-[#6B46C1] text-white font-medium transition-colors text-xs inline-block">
                                Create Promotion
                            </button>
                        </div>
                        <!-- Large Icon on the right -->
                        <div class="absolute right-4 bottom-0 opacity-50 translate-y-2">
                            <span class="material-symbols-outlined text-[90px] text-[#B794F6]">redeem</span>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep flex flex-col">{loyalty_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Loyalty & Rewards'
    loyalty_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Loyalty &amp; Rewards\s*</a>'
    loyalty_active = """<a href="admin-loyalty-rewards.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Loyalty &amp; Rewards
                </a>"""
    if not re.search(loyalty_inactive, new_html):
        # fallback for normal &
        loyalty_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Loyalty & Rewards\s*</a>'
    new_html = re.sub(loyalty_inactive, loyalty_active, new_html)

    with open('admin-loyalty-rewards.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-loyalty-rewards.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-loyalty-rewards.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_loyalty_rewards()

if __name__ == '__main__':
    main()
