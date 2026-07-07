import os
import re

def update_customers():
    with open('admin-customers.html', 'r', encoding='utf-8') as f:
        content = f.read()

    main_pattern = r'(<main[^>]*>).*?(</main>)'
    match = re.search(main_pattern, content, flags=re.DOTALL)
    
    new_main_content = """
        <!-- Content Area -->
        <div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar bg-surface-deep text-on-surface">
            
            <!-- Header -->
            <header class="flex items-center justify-between px-8 py-6 pb-4 shrink-0 mt-2">
                <div>
                    <h2 class="font-headline-lg text-headline-lg text-white font-bold tracking-tight">
                        Customers
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">Manage all customers, their activity, orders and support.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Customers
                    </button>
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">publish</span> Import Customers
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">add</span> Add Customer
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 5 KPI Cards -->
                <div class="grid grid-cols-5 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0 border border-blue-500/20">
                            <span class="material-symbols-outlined text-blue-500 text-xl">group</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Customers</p>
                            <p class="text-2xl font-bold text-white">2,483</p>
                            <p class="text-[10px] text-[#00D084] mt-1 font-medium">▲ 12.5% this month</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 flex items-center justify-center shrink-0 border border-[#00D084]/20">
                            <span class="material-symbols-outlined text-[#00D084] text-xl">how_to_reg</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Active Customers</p>
                            <p class="text-2xl font-bold text-white">2,156</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">86.8% of total</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">shopping_cart</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Orders</p>
                            <p class="text-2xl font-bold text-white">5,874</p>
                            <p class="text-[10px] text-[#00D084] mt-1 font-medium">▲ 8.3% this month</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-orange-500/10 flex items-center justify-center shrink-0 border border-orange-500/20">
                            <span class="material-symbols-outlined text-orange-500 text-xl">account_balance_wallet</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Spent</p>
                            <p class="text-2xl font-bold text-white">₹ 2,48,56,890</p>
                            <p class="text-[10px] text-[#00D084] mt-1 font-medium">▲ 15.2% this month</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#E91E63]/10 flex items-center justify-center shrink-0 border border-[#E91E63]/20">
                            <span class="material-symbols-outlined text-[#E91E63] text-xl">star</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Avg. Order Value</p>
                            <p class="text-2xl font-bold text-white">₹ 42,350</p>
                            <p class="text-[10px] text-[#00D084] mt-1 font-medium">▲ 6.1% this month</p>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm group flex-1">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search by name, email, phone..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Status <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Groups <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Locations <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">calendar_today</span> Date Range <span class="material-symbols-outlined text-sm ml-2">calendar_month</span>
                    </button>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-4 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2 ml-auto">
                        <span class="material-symbols-outlined text-sm">filter_alt</span> Filters
                    </button>
                    
                    <div class="flex bg-surface-deep border border-white/5 rounded-lg p-0.5 ml-2">
                        <button class="p-1 rounded bg-primary/20 text-primary"><span class="material-symbols-outlined text-[16px] block">format_list_bulleted</span></button>
                        <button class="p-1 rounded text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px] block">grid_view</span></button>
                    </div>
                </div>

                <!-- Dual Column Area -->
                <div class="mt-6 flex gap-4 flex-1 items-stretch min-h-[600px]">
                    
                    <!-- LEFT COLUMN: Data Table -->
                    <div class="flex-1 bg-surface-container border border-white/5 rounded-xl flex flex-col overflow-hidden min-w-[800px]">
                        <!-- Table -->
                        <div class="flex-1 overflow-x-auto overflow-y-auto custom-scrollbar">
                            <table class="w-full text-left border-collapse min-w-[900px]">
                                <thead class="sticky top-0 bg-surface-container z-10">
                                    <tr class="border-b border-white/5">
                                        <th class="py-4 px-6 w-12"><div class="w-4 h-4 rounded border border-white/20"></div></th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">CUSTOMER</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">CONTACT</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">ORDERS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">TOTAL SPENT</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">STATUS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">JOINED ON</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-right">ACTIONS</th>
                                    </tr>
                                </thead>
                                <tbody class="text-sm divide-y divide-white/5">
                                    
                                    <!-- Row 1 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer bg-white/[0.02]">
                                        <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <div class="w-10 h-10 rounded-full bg-surface-deep border border-white/10 overflow-hidden shrink-0">
                                                    <img src="images/about-team-3.jpg" alt="Avatar" class="w-full h-full object-cover">
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-bold text-white">Rahul Verma</p>
                                                        <span class="text-[8px] font-bold text-primary bg-primary/20 px-1.5 py-0.5 rounded tracking-widest">VIP</span>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">rahul@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-xs text-on-surface-variant">+91 98765 43210</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">12</p>
                                            <a href="#" class="text-[10px] text-primary hover:underline">View Orders</a>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">₹1,28,450</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">12 May 2024</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 2 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <div class="w-10 h-10 rounded-full bg-surface-deep border border-white/10 overflow-hidden shrink-0">
                                                    <img src="images/about-team-1.jpg" alt="Avatar" class="w-full h-full object-cover">
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-medium text-white">Priya Sharma</p>
                                                        <span class="text-[8px] font-bold text-[#B14EEF] bg-[#B14EEF]/20 px-1.5 py-0.5 rounded tracking-widest">Premium</span>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">priya@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-xs text-on-surface-variant">+91 87654 32109</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">9</p>
                                            <a href="#" class="text-[10px] text-primary hover:underline">View Orders</a>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">₹98,750</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">10 May 2024</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 3 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <div class="w-10 h-10 rounded-full bg-surface-deep border border-white/10 overflow-hidden shrink-0">
                                                    <img src="images/about-team-2.jpg" alt="Avatar" class="w-full h-full object-cover">
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-medium text-white">Amit Singh</p>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">amit@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-xs text-on-surface-variant">+91 76543 21098</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">7</p>
                                            <a href="#" class="text-[10px] text-primary hover:underline">View Orders</a>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">₹76,900</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">08 May 2024</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 4 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <div class="w-10 h-10 rounded-full bg-surface-deep border border-white/10 overflow-hidden shrink-0">
                                                    <img src="images/about-team-4.jpg" alt="Avatar" class="w-full h-full object-cover">
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-medium text-white">Neha Gupta</p>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">neha@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-xs text-on-surface-variant">+91 65432 10987</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">15</p>
                                            <a href="#" class="text-[10px] text-primary hover:underline">View Orders</a>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">₹2,45,600</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-orange-500/20 text-orange-500 text-[10px] font-bold tracking-wider">Inactive</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">05 May 2024</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 5 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <div class="w-10 h-10 rounded-full bg-surface-deep border border-white/10 overflow-hidden shrink-0 flex items-center justify-center text-white font-bold text-sm bg-gradient-to-br from-indigo-500 to-purple-500">
                                                    AS
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-medium text-white">Arjun Saxena</p>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">arjun@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-xs text-on-surface-variant">+91 43210 98765</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">4</p>
                                            <a href="#" class="text-[10px] text-primary hover:underline">View Orders</a>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">₹45,800</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-red-500/20 text-red-500 text-[10px] font-bold tracking-wider">Blocked</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">01 May 2024</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                </tbody>
                            </table>
                        </div>
                        
                        <!-- Pagination Bar -->
                        <div class="px-6 py-4 border-t border-white/5 flex items-center justify-between shrink-0 bg-surface-container">
                            <div class="flex items-center gap-3">
                                <div class="w-4 h-4 rounded border border-white/20"></div>
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-1.5 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                                    Bulk Actions <span class="material-symbols-outlined text-sm ml-1">expand_more</span>
                                </button>
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-1.5 px-4 text-xs font-medium text-white hover:bg-white/5 transition-all">
                                    Apply
                                </button>
                            </div>
                            
                            <div class="flex items-center gap-6">
                                <p class="text-[11px] text-on-surface-variant">Showing 1 to 10 of 2,483 customers</p>
                                
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                                        <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center text-xs font-bold shadow-[0_0_10px_rgba(0,122,255,0.3)]">1</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">2</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">3</button>
                                    <span class="w-8 h-8 flex items-center justify-center text-on-surface-variant text-xs">...</span>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">249</button>
                                    <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                                        <span class="material-symbols-outlined text-[16px]">chevron_right</span>
                                    </button>
                                </div>
                                
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-1.5 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                                    10 / page <span class="material-symbols-outlined text-sm ml-1">expand_more</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    
                    <!-- RIGHT COLUMN: Customer Profile Panel -->
                    <div class="w-80 shrink-0 bg-surface-container border border-white/5 rounded-xl flex flex-col p-6 sticky top-6 self-start max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
                        
                        <!-- Top Action -->
                        <div class="flex justify-end mb-2">
                            <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                <span class="material-symbols-outlined text-[16px]">edit</span>
                            </button>
                        </div>
                        
                        <!-- Profile Header -->
                        <div class="flex flex-col items-center text-center">
                            <div class="w-20 h-20 rounded-full border-2 border-white/10 p-1 mb-3">
                                <div class="w-full h-full rounded-full overflow-hidden bg-surface-deep">
                                    <img src="images/about-team-3.jpg" alt="Rahul Verma" class="w-full h-full object-cover">
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-center gap-2 mb-1">
                                <h3 class="text-base font-bold text-white">Rahul Verma</h3>
                                <span class="text-[8px] font-bold text-primary bg-primary/20 px-1.5 py-0.5 rounded tracking-widest uppercase">VIP</span>
                            </div>
                            
                            <p class="text-xs text-on-surface-variant mb-1">rahul@example.com</p>
                            <p class="text-xs text-on-surface-variant mb-3 flex items-center justify-center gap-1">
                                <span class="material-symbols-outlined text-[14px]">call</span> +91 98765 43210
                            </p>
                            
                            <p class="text-[11px] text-on-surface-variant/70 flex items-center justify-center gap-1 mb-4">
                                <span class="material-symbols-outlined text-[12px]">location_on</span> Mumbai, Maharashtra, India
                            </p>
                            
                            <div class="flex items-center gap-1 text-[#00D084] text-[10px] font-medium tracking-wide mb-6">
                                <span class="material-symbols-outlined text-[14px]">check_circle</span> Active Customer
                            </div>
                        </div>
                        
                        <hr class="border-white/5 mb-6">
                        
                        <!-- Customer Overview -->
                        <div class="mb-6">
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-4">Customer Overview</h4>
                            
                            <div class="space-y-3">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-on-surface-variant">Total Orders</span>
                                    <span class="font-medium text-white">12</span>
                                </div>
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-on-surface-variant">Total Spent</span>
                                    <span class="font-medium text-white">₹1,28,450</span>
                                </div>
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-on-surface-variant">Average Order Value</span>
                                    <span class="font-medium text-white">₹10,704</span>
                                </div>
                                <div class="flex items-center justify-between text-xs mt-4 pt-4 border-t border-white/5">
                                    <span class="text-on-surface-variant">First Order</span>
                                    <span class="text-on-surface-variant">12 May 2024</span>
                                </div>
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-on-surface-variant">Last Order</span>
                                    <span class="text-on-surface-variant">18 Jun 2024</span>
                                </div>
                            </div>
                        </div>
                        
                        <hr class="border-white/5 mb-6">
                        
                        <!-- Quick Actions -->
                        <div class="mb-6">
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-4">Quick Actions</h4>
                            
                            <div class="grid grid-cols-2 gap-2">
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-2.5 px-3 flex flex-col items-center justify-center gap-1.5 hover:bg-white/5 transition-colors group">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-hover:text-white transition-colors">shopping_cart</span>
                                    <span class="text-[10px] text-on-surface-variant group-hover:text-white font-medium transition-colors">View Orders</span>
                                </button>
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-2.5 px-3 flex flex-col items-center justify-center gap-1.5 hover:bg-white/5 transition-colors group">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-hover:text-white transition-colors">bookmark</span>
                                    <span class="text-[10px] text-on-surface-variant group-hover:text-white font-medium transition-colors">View Saved Builds</span>
                                </button>
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-2.5 px-3 flex flex-col items-center justify-center gap-1.5 hover:bg-white/5 transition-colors group">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-hover:text-white transition-colors">home_pin</span>
                                    <span class="text-[10px] text-on-surface-variant group-hover:text-white font-medium transition-colors">View Addresses</span>
                                </button>
                                <button class="bg-surface-deep border border-white/5 rounded-lg py-2.5 px-3 flex flex-col items-center justify-center gap-1.5 hover:bg-white/5 transition-colors group">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-hover:text-white transition-colors">mail</span>
                                    <span class="text-[10px] text-on-surface-variant group-hover:text-white font-medium transition-colors">Send Message</span>
                                </button>
                            </div>
                        </div>
                        
                        <!-- Notes -->
                        <div>
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-3">Notes</h4>
                            <textarea class="w-full bg-surface-deep border border-white/5 rounded-lg p-3 text-xs text-white placeholder-on-surface-variant/50 focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all resize-none h-24" placeholder="Add a note about this customer..."></textarea>
                        </div>
                        
                    </div>
                </div>

            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('admin-customers.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating admin-customers.html!")

update_customers()
