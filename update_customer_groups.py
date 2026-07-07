import os
import re

def update_customer_groups():
    with open('admin-customer-groups.html', 'r', encoding='utf-8') as f:
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
                        Customer Groups
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">Organize customers into groups to manage and target them better.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Groups
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">add</span> Create Group
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 5 KPI Cards -->
                <div class="grid grid-cols-5 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">workspace_premium</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Groups</p>
                            <p class="text-2xl font-bold text-white">12</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">All customer groups</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 flex items-center justify-center shrink-0 border border-[#00D084]/20">
                            <span class="material-symbols-outlined text-[#00D084] text-xl">group</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Customers</p>
                            <p class="text-2xl font-bold text-white">2,483</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Across all groups</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0 border border-blue-500/20">
                            <span class="material-symbols-outlined text-blue-500 text-xl">school</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Active Groups</p>
                            <p class="text-2xl font-bold text-white">9</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Groups with customers</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-orange-500/10 flex items-center justify-center shrink-0 border border-orange-500/20">
                            <span class="material-symbols-outlined text-orange-500 text-xl">business_center</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Avg. Group Spend</p>
                            <p class="text-2xl font-bold text-white">₹ 42,350</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Average order value</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#E91E63]/10 flex items-center justify-center shrink-0 border border-[#E91E63]/20">
                            <span class="material-symbols-outlined text-[#E91E63] text-xl">school</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Top Group</p>
                            <p class="text-lg font-bold text-white mt-1">VIP Customers</p>
                            <p class="text-[10px] text-on-surface-variant mt-0.5">Highest total spent</p>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search groups..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Status: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Sort By: Members <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    
                    <div class="flex bg-surface-deep border border-white/5 rounded-lg p-0.5 ml-auto">
                        <button class="p-1 rounded bg-primary/20 text-primary"><span class="material-symbols-outlined text-[16px] block">format_list_bulleted</span></button>
                        <button class="p-1 rounded text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px] block">grid_view</span></button>
                    </div>
                </div>

                <!-- Dual Column Area -->
                <div class="mt-6 flex gap-4 flex-1 items-stretch min-h-[600px]">
                    
                    <!-- LEFT COLUMN: Data Table -->
                    <div class="flex-1 bg-surface-container border border-white/5 rounded-xl flex flex-col overflow-hidden min-w-[700px]">
                        <!-- Table -->
                        <div class="flex-1 overflow-x-auto overflow-y-auto custom-scrollbar">
                            <table class="w-full text-left border-collapse min-w-[800px]">
                                <thead class="sticky top-0 bg-surface-container z-10">
                                    <tr class="border-b border-white/5">
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">GROUP NAME</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">MEMBERS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">TOTAL ORDERS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">TOTAL SPENT</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">AVG. ORDER VALUE</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">STATUS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-right">ACTIONS</th>
                                    </tr>
                                </thead>
                                <tbody class="text-sm divide-y divide-white/5">
                                    
                                    <!-- Row 1: VIP Customers -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer bg-white/[0.02]">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-[#B14EEF]/10 border border-[#B14EEF]/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-[#B14EEF] text-[20px]">workspace_premium</span>
                                                </div>
                                                <div>
                                                    <div class="flex items-center gap-2 mb-0.5">
                                                        <p class="text-sm font-bold text-white">VIP Customers</p>
                                                        <span class="text-[8px] font-bold text-[#B14EEF] bg-[#B14EEF]/20 px-1.5 py-0.5 rounded tracking-widest uppercase">VIP</span>
                                                    </div>
                                                    <p class="text-[10px] text-on-surface-variant">High value & loyal customers</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">156</p>
                                            <p class="text-[10px] text-on-surface-variant">6.3% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">852</td>
                                        <td class="py-4 px-6 text-sm text-white">₹48,56,890</td>
                                        <td class="py-4 px-6 text-sm text-white">₹56,915</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 2: Premium Customers -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-[#007AFF]/10 border border-[#007AFF]/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-[#007AFF] text-[20px]">star</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Premium Customers</p>
                                                    <p class="text-[10px] text-on-surface-variant">Frequent buyers with good spend</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">362</p>
                                            <p class="text-[10px] text-on-surface-variant">14.6% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">1,985</td>
                                        <td class="py-4 px-6 text-sm text-white">₹72,85,640</td>
                                        <td class="py-4 px-6 text-sm text-white">₹36,695</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 3: Gamers -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-[#00D084]/10 border border-[#00D084]/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-[#00D084] text-[20px]">sports_esports</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Gamers</p>
                                                    <p class="text-[10px] text-on-surface-variant">Customers interested in gaming PCs</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">845</p>
                                            <p class="text-[10px] text-on-surface-variant">34.0% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">3,642</td>
                                        <td class="py-4 px-6 text-sm text-white">₹1,85,45,320</td>
                                        <td class="py-4 px-6 text-sm text-white">₹50,915</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 4: Business -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-orange-500/10 border border-orange-500/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-orange-500 text-[20px]">business_center</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Business Customers</p>
                                                    <p class="text-[10px] text-on-surface-variant">Corporate & business buyers</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">218</p>
                                            <p class="text-[10px] text-on-surface-variant">8.8% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">1,156</td>
                                        <td class="py-4 px-6 text-sm text-white">₹68,45,210</td>
                                        <td class="py-4 px-6 text-sm text-white">₹59,210</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 5: Students -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-[#E91E63]/10 border border-[#E91E63]/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-[#E91E63] text-[20px]">school</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Students</p>
                                                    <p class="text-[10px] text-on-surface-variant">Students and educational buyers</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">487</p>
                                            <p class="text-[10px] text-on-surface-variant">19.6% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">1,842</td>
                                        <td class="py-4 px-6 text-sm text-white">₹42,65,780</td>
                                        <td class="py-4 px-6 text-sm text-white">₹23,156</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 6: Deal Hunters -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-[#B14EEF]/10 border border-[#B14EEF]/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-[#B14EEF] text-[20px]">sell</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Deal Hunters</p>
                                                    <p class="text-[10px] text-on-surface-variant">Customers looking for best deals</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">265</p>
                                            <p class="text-[10px] text-on-surface-variant">10.7% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">892</td>
                                        <td class="py-4 px-6 text-sm text-white">₹21,48,500</td>
                                        <td class="py-4 px-6 text-sm text-white">₹24,038</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 text-[#00D084] text-[10px] font-bold tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 7: Inactive -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-slate-500/10 border border-slate-500/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-slate-400 text-[20px]">schedule</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Inactive Customers</p>
                                                    <p class="text-[10px] text-on-surface-variant">No activity in last 90 days</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">112</p>
                                            <p class="text-[10px] text-on-surface-variant">4.5% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">98</td>
                                        <td class="py-4 px-6 text-sm text-white">₹2,15,600</td>
                                        <td class="py-4 px-6 text-sm text-white">₹21,980</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-orange-500/20 text-orange-500 text-[10px] font-bold tracking-wider">Inactive</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 8: Blocked -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-full bg-red-500/10 border border-red-500/20 flex items-center justify-center shrink-0">
                                                    <span class="material-symbols-outlined text-red-500 text-[20px]">block</span>
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Blocked Customers</p>
                                                    <p class="text-[10px] text-on-surface-variant">Blocked or restricted customers</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm font-medium text-white mb-0.5">38</p>
                                            <p class="text-[10px] text-on-surface-variant">1.5% of total</p>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white">12</td>
                                        <td class="py-4 px-6 text-sm text-white">₹8,450</td>
                                        <td class="py-4 px-6 text-sm text-white">₹704</td>
                                        <td class="py-4 px-6">
                                            <span class="px-2.5 py-1 rounded-full border border-red-500/20 text-red-500 text-[10px] font-bold tracking-wider">Inactive</span>
                                        </td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">edit</span>
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
                            <p class="text-[11px] text-on-surface-variant">Showing 1 to 8 of 12 groups</p>
                            
                            <div class="flex items-center gap-4">
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                                        <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center text-xs font-bold shadow-[0_0_10px_rgba(0,122,255,0.3)]">1</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">2</button>
                                    <span class="w-8 h-8 flex items-center justify-center text-on-surface-variant text-xs">...</span>
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
                    
                    <!-- RIGHT COLUMN: Customer Group Profile Panel -->
                    <div class="w-80 shrink-0 bg-surface-container border border-white/5 rounded-xl flex flex-col p-6 sticky top-6 self-start max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
                        
                        <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-4">SELECTED GROUP</h4>
                        
                        <!-- Profile Header -->
                        <div class="flex flex-col mb-6">
                            <div class="flex items-center justify-between mb-3">
                                <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 border border-[#B14EEF]/20 flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-[#B14EEF] text-2xl">workspace_premium</span>
                                </div>
                                <div class="flex items-center gap-1 text-[#00D084] text-[10px] font-medium tracking-wide">
                                    Active
                                </div>
                            </div>
                            
                            <h3 class="text-base font-bold text-white mb-1">VIP Customers</h3>
                            <p class="text-xs text-on-surface-variant">High value & loyal customers</p>
                        </div>
                        
                        <hr class="border-white/5 mb-6">
                        
                        <!-- Stats Grid -->
                        <div class="grid grid-cols-2 gap-y-6 gap-x-4 mb-6">
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">group</span>
                                    <span class="text-sm font-medium text-white">156</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Members</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">shopping_cart</span>
                                    <span class="text-sm font-medium text-white">852</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Total Orders</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="text-sm font-medium text-white">₹48,56,890</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Total Spent</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="text-sm font-medium text-white">₹56,915</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Avg. Order Value</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">schedule</span>
                                    <span class="text-xs text-white">12 May 2024</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Created On</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">person</span>
                                    <span class="text-xs text-white">Admin User</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Created By</p>
                            </div>
                        </div>
                        
                        <hr class="border-white/5 mb-6">
                        
                        <!-- Description -->
                        <div class="mb-6">
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-3">Group Description</h4>
                            <p class="text-[11px] text-on-surface-variant leading-relaxed">
                                This group contains our most valuable customers who have high lifetime value and engage frequently with our store.
                            </p>
                        </div>
                        
                        <hr class="border-white/5 mb-6">
                        
                        <!-- Top Members -->
                        <div class="mb-6">
                            <div class="flex items-center justify-between mb-4">
                                <h4 class="text-[10px] font-bold text-white tracking-widest uppercase">Top Members</h4>
                                <a href="#" class="text-[10px] text-primary hover:underline">View All</a>
                            </div>
                            
                            <div class="space-y-4">
                                <!-- Member 1 -->
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-3">
                                        <img src="images/about-team-3.jpg" alt="Rahul" class="w-8 h-8 rounded-full border border-white/10 object-cover">
                                        <div>
                                            <p class="text-xs font-medium text-white">Rahul Verma</p>
                                            <p class="text-[9px] text-on-surface-variant">rahul@example.com</p>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <p class="text-xs text-white">₹2,45,600</p>
                                        <p class="text-[9px] text-on-surface-variant">18 Orders</p>
                                    </div>
                                </div>
                                
                                <!-- Member 2 -->
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-3">
                                        <img src="images/about-team-1.jpg" alt="Priya" class="w-8 h-8 rounded-full border border-white/10 object-cover">
                                        <div>
                                            <p class="text-xs font-medium text-white">Priya Sharma</p>
                                            <p class="text-[9px] text-on-surface-variant">priya@example.com</p>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <p class="text-xs text-white">₹2,15,300</p>
                                        <p class="text-[9px] text-on-surface-variant">15 Orders</p>
                                    </div>
                                </div>
                                
                                <!-- Member 3 -->
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-3">
                                        <img src="images/about-team-2.jpg" alt="Amit" class="w-8 h-8 rounded-full border border-white/10 object-cover">
                                        <div>
                                            <p class="text-xs font-medium text-white">Amit Singh</p>
                                            <p class="text-[9px] text-on-surface-variant">amit@example.com</p>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <p class="text-xs text-white">₹1,89,750</p>
                                        <p class="text-[9px] text-on-surface-variant">14 Orders</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Action Button -->
                        <button class="w-full py-2.5 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-xs font-medium mt-auto">
                            Edit Group
                        </button>
                        
                    </div>
                </div>

            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('admin-customer-groups.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating admin-customer-groups.html!")

update_customer_groups()
