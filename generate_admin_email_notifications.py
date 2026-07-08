import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Email & Notifications link
    email_pattern = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Email &amp; Notifications\s*</a>'
    new_email = '<a href="admin-email-notifications.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Email &amp; Notifications\n                </a>'
    
    if re.search(email_pattern, content):
        content = re.sub(email_pattern, new_email, content)
    else:
        # fallback for & instead of &amp;
        email_pattern2 = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Email & Notifications\s*</a>'
        new_email2 = '<a href="admin-email-notifications.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Email & Notifications\n                </a>'
        content = re.sub(email_pattern2, new_email2, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_email_notifications():
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    email_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-blue-500/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-6 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-1">Email & Notifications</h2>
                    <p class="text-on-surface-variant text-sm">Manage all email communications and notification settings.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">send</span>
                        Send Email
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">add_box</span>
                        Create Template
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-on-primary font-medium transition-colors text-sm flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">settings</span>
                        Settings
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-5 gap-4 mb-6 relative z-10">
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">mail</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL SENT</p>
                        <h3 class="text-xl font-bold text-white leading-tight">1,25,680</h3>
                        <p class="text-[11px] text-on-surface-variant mt-1">All time emails</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">send</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">DELIVERED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">1,18,560</h3>
                        <p class="text-[11px] text-on-surface-variant mt-1">94.3% delivered</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">drafts</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">OPENED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">68,450</h3>
                        <p class="text-[11px] text-on-surface-variant mt-1">54.6% open rate</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">ads_click</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">CLICKED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">21,340</h3>
                        <p class="text-[11px] text-on-surface-variant mt-1">17.1% click rate</p>
                    </div>
                </div>
                <div class="glass-card p-4 rounded-xl border border-white/5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">reply</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">BOUNCED</p>
                        <h3 class="text-xl font-bold text-white leading-tight">7,120</h3>
                        <p class="text-[11px] text-on-surface-variant mt-1">5.7% bounce rate</p>
                    </div>
                </div>
            </div>

            <!-- Tabs -->
            <div class="flex gap-6 border-b border-white/10 mb-5 relative z-10 text-sm">
                <a href="#" class="text-primary font-medium border-b-2 border-primary pb-3 px-1">Email Campaigns</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Templates</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Notification Settings</a>
                <a href="#" class="text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Subscribers</a>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-4 relative z-10">
                <div class="flex gap-3 flex-1 max-w-4xl">
                    <div class="relative flex-1 max-w-[280px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by campaign name, subject..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-9 pr-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-36">
                        <option>All Campaigns</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Status</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-32">
                        <option>All Channels</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-3 py-2 text-[13px] focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-28">
                        <option>All Time</option>
                    </select>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-[16px]">filter_list</span>
                        Filters
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
                                    <th class="px-5 py-4 font-medium tracking-wider">CAMPAIGN NAME</th>
                                    <th class="px-5 py-4 font-medium tracking-wider w-[260px]">SUBJECT</th>
                                    <th class="px-5 py-4 font-medium tracking-wider">RECIPIENTS</th>
                                    <th class="px-5 py-4 font-medium tracking-wider">SENT ON</th>
                                    <th class="px-5 py-4 font-medium tracking-wider">STATUS</th>
                                    <th class="px-5 py-4 font-medium tracking-wider">PERFORMANCE</th>
                                    <th class="px-5 py-4 font-medium tracking-wider text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">campaign</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">New Year Special Offer</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px]">🎉 New Year Special Offer - Up to 20% OFF!</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">18,560</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">12 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">52.6%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">16.2%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 2 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">shopping_cart</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Abandoned Build Reminder</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">Complete your saved build today!</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">8,450</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">11 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">47.8%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">12.4%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 3 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">inventory_2</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Order Confirmation</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">Your Order #ORD-2024-1256 is confirmed</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">2,345</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">10 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">75.3%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">28.6%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 4 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">local_shipping</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Order Shipped</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">Good news! Your order is on the way</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">2,210</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">09 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">03:30 PM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">71.1%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">22.1%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 5 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">star</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Product Review Request</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">How was your experience with your purchase?</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">1,980</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">08 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">09:45 AM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">34.6%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">9.2%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 6 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#FC8181]/20 text-[#FC8181] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">favorite</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Wishlist Price Drop Alert</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">Good news! Items in your wishlist are on sale</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">6,782</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">07 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">05:10 PM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">49.2%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">13.7%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 7 - Bounced -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-cyan-500/20 text-cyan-400 flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">mail</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Newsletter - May 2024</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">May Updates: New Products, Offers & More</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">22,650</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">06 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">10:00 AM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#FC8181] text-[10px] font-medium bg-[#FC8181]/20">Bounced</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">40.5%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">11.3%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 8 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-5 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-8 h-8 rounded bg-[#F6AD55]/20 text-[#F6AD55] flex items-center justify-center shrink-0">
                                                <span class="material-symbols-outlined text-[18px]">notifications_active</span>
                                            </div>
                                            <span class="font-medium text-white text-[12px]">Account Verification</span>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[12px] truncate w-[260px] opacity-80">Verify your email address</p>
                                    </td>
                                    <td class="px-5 py-4 text-white font-medium text-[12px]">3,245</td>
                                    <td class="px-5 py-4">
                                        <p class="text-white text-[11px]">05 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">02:20 PM</p>
                                    </td>
                                    <td class="px-5 py-4">
                                        <span class="px-2 py-1 rounded text-[#68D391] text-[10px] font-medium bg-[#1B5038]/30">Delivered</span>
                                    </td>
                                    <td class="px-5 py-4">
                                        <div class="flex gap-4">
                                            <div>
                                                <p class="text-white font-medium text-[11px]">68.3%</p>
                                                <p class="text-[9px] text-on-surface-variant">Open Rate</p>
                                            </div>
                                            <div>
                                                <p class="text-white font-medium text-[11px]">18.9%</p>
                                                <p class="text-[9px] text-on-surface-variant">Click Rate</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-5 py-4 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded bg-surface-container-highest/50 hover:bg-white/10 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                                <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="p-4 border-t border-white/5 bg-surface-deep/50 backdrop-blur flex justify-between items-center text-xs">
                        <p class="text-on-surface-variant">Showing 1 to 8 of 125 campaigns</p>
                        <div class="flex gap-1 items-center">
                            <button class="w-8 h-8 rounded flex items-center justify-center hover:bg-white/5 transition-colors disabled:opacity-50 text-white"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                            <button class="w-8 h-8 rounded bg-primary text-on-primary flex items-center justify-center font-medium">1</button>
                            <button class="w-8 h-8 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2</button>
                            <button class="w-8 h-8 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">3</button>
                            <span class="w-8 h-8 flex items-center justify-center text-on-surface-variant">...</span>
                            <button class="w-8 h-8 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">16</button>
                            <button class="w-8 h-8 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                            <div class="flex items-center gap-2 ml-4">
                                <span class="text-on-surface-variant">10 / page</span>
                                <span class="material-symbols-outlined text-sm">expand_more</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar -->
                <div class="w-[340px] shrink-0 flex flex-col gap-6 overflow-y-auto custom-scrollbar pr-1">
                    
                    <!-- Email Performance Overview -->
                    <div class="glass-card p-6 rounded-xl border border-white/5">
                        <h3 class="text-[13px] font-medium text-white mb-6">Email Performance Overview</h3>
                        <div class="flex items-center gap-6">
                            <!-- Conic gradient for chart -->
                            <div class="relative w-32 h-32 rounded-full shrink-0" style="background: conic-gradient(#68D391 0% 94.3%, #FC8181 94.3% 100%); padding: 14px;">
                                <div class="bg-surface-deep w-full h-full rounded-full flex flex-col items-center justify-center border border-white/5 shadow-inner">
                                    <span class="text-lg font-bold text-white leading-none">1,25,680</span>
                                    <span class="text-[9px] text-on-surface-variant mt-1 text-center">Total Sent</span>
                                </div>
                            </div>
                            <div class="flex-1 space-y-3 text-[11px]">
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-2 text-on-surface-variant">
                                        <span class="w-2 h-2 rounded-full bg-[#68D391]"></span> Delivered
                                    </div>
                                    <span class="text-white">94.3% (1,18,560)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-2 text-on-surface-variant">
                                        <span class="w-2 h-2 rounded-full bg-[#FC8181]"></span> Bounced
                                    </div>
                                    <span class="text-white">5.7% (7,120)</span>
                                </div>
                                <div class="flex justify-between items-center pt-2 border-t border-white/5">
                                    <div class="flex items-center gap-2 text-on-surface-variant">
                                        <span class="w-2 h-2 rounded-full bg-[#3182CE]"></span> Opened
                                    </div>
                                    <span class="text-white">54.6% (68,450)</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center gap-2 text-on-surface-variant">
                                        <span class="w-2 h-2 rounded-full bg-[#F6AD55]"></span> Clicked
                                    </div>
                                    <span class="text-white">17.1% (21,340)</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Actions -->
                    <div class="glass-card p-6 rounded-xl border border-white/5">
                        <h3 class="text-[13px] font-medium text-white mb-4">Quick Actions</h3>
                        <div class="space-y-2">
                            <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white transition-colors">campaign</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Send Email Campaign</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Send email to selected audience</p>
                                    </div>
                                </div>
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                            </a>
                            <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white transition-colors">post_add</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Create Template</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Design new email template</p>
                                    </div>
                                </div>
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                            </a>
                            <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white transition-colors">group</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Manage Subscribers</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">View and manage subscribers</p>
                                    </div>
                                </div>
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                            </a>
                            <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white transition-colors">settings</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Notification Settings</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Configure email & notifications</p>
                                    </div>
                                </div>
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                            </a>
                        </div>
                    </div>

                    <!-- Recently Used Templates -->
                    <div class="glass-card p-6 rounded-xl border border-white/5">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-[13px] font-medium text-white">Recently Used Templates</h3>
                            <a href="#" class="text-[11px] text-primary hover:underline font-medium">View All</a>
                        </div>
                        <div class="space-y-3">
                            <div class="flex justify-between items-center p-3 rounded-lg bg-surface-deep/50 border border-white/5">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded bg-cyan-900/40 text-cyan-400 flex items-center justify-center">
                                        <span class="material-symbols-outlined text-[16px]">inventory_2</span>
                                    </div>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Order Confirmation</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Used 245 times</p>
                                    </div>
                                </div>
                                <button class="w-7 h-7 rounded hover:bg-white/5 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                </button>
                            </div>
                            
                            <div class="flex justify-between items-center p-3 rounded-lg bg-surface-deep/50 border border-white/5">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded bg-teal-900/40 text-teal-400 flex items-center justify-center">
                                        <span class="material-symbols-outlined text-[16px]">password</span>
                                    </div>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Password Reset</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Used 189 times</p>
                                    </div>
                                </div>
                                <button class="w-7 h-7 rounded hover:bg-white/5 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                </button>
                            </div>

                            <div class="flex justify-between items-center p-3 rounded-lg bg-surface-deep/50 border border-white/5">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded bg-sky-900/40 text-sky-400 flex items-center justify-center">
                                        <span class="material-symbols-outlined text-[16px]">mail</span>
                                    </div>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Newsletter Template</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Used 156 times</p>
                                    </div>
                                </div>
                                <button class="w-7 h-7 rounded hover:bg-white/5 text-on-surface-variant hover:text-white flex items-center justify-center transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                </button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-hidden bg-surface-deep flex flex-col">{email_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Email & Notifications'
    email_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Email &amp; Notifications\s*</a>'
    email_active = """<a href="admin-email-notifications.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Email &amp; Notifications
                </a>"""
    if not re.search(email_inactive, new_html):
        # fallback
        email_inactive = r'<a href="[^"]*" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Email & Notifications\s*</a>'
    
    new_html = re.sub(email_inactive, email_active, new_html)

    with open('admin-email-notifications.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-email-notifications.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-email-notifications.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_email_notifications()

if __name__ == '__main__':
    main()
