import os
import re

def update_saved_builds():
    with open('admin-saved-builds.html', 'r', encoding='utf-8') as f:
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
                        Saved Builds
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">View and manage all PC builds saved by customers.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Builds
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">bolt</span> Send Offer / Reminder
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 5 KPI Cards -->
                <div class="grid grid-cols-5 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">favorite</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Saved Builds</p>
                            <p class="text-2xl font-bold text-white">1,256</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">All time saved builds</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 flex items-center justify-center shrink-0 border border-[#00D084]/20">
                            <span class="material-symbols-outlined text-[#00D084] text-xl">bookmark</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Active Builds</p>
                            <p class="text-2xl font-bold text-white">842</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Not converted yet</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-orange-500/10 flex items-center justify-center shrink-0 border border-orange-500/20">
                            <span class="material-symbols-outlined text-orange-500 text-xl">shopping_cart_checkout</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Converted Builds</p>
                            <p class="text-2xl font-bold text-white">414</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Converted to orders</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#E91E63]/10 flex items-center justify-center shrink-0 border border-[#E91E63]/20">
                            <span class="material-symbols-outlined text-[#E91E63] text-xl">currency_rupee</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Value</p>
                            <p class="text-2xl font-bold text-white">₹ 3,42,85,600</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Total value of saved builds</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0 border border-blue-500/20">
                            <span class="material-symbols-outlined text-blue-500 text-xl">payments</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Avg Build Value</p>
                            <p class="text-2xl font-bold text-white">₹ 27,300</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Average build value</p>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search by build name, customer..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Status: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Converted: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Category: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Price Range <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-2.5 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all">
                        <span class="material-symbols-outlined text-[16px] block">calendar_today</span>
                    </button>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2 ml-auto">
                        <span class="material-symbols-outlined text-[16px]">filter_alt</span> Filters
                    </button>
                    
                    <div class="flex bg-surface-deep border border-white/5 rounded-lg p-0.5 ml-2">
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
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">BUILD NAME</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">CUSTOMER</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">CATEGORY</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">TOTAL PRICE</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">STATUS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">LAST SAVED</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-right">ACTIONS</th>
                                    </tr>
                                </thead>
                                <tbody class="text-sm divide-y divide-white/5">
                                    
                                    <!-- Row 1 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer bg-white/[0.02]">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/cpu-1.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-bold text-white mb-0.5">Rahul's Gaming Beast</p>
                                                    <p class="text-[10px] text-on-surface-variant">Ryzen 7 7800X3D, RTX 4070 Ti...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <img src="images/about-team-3.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover">
                                                <div>
                                                    <p class="text-xs text-white">Rahul Verma</p>
                                                    <p class="text-[9px] text-on-surface-variant">rahul@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-[#B14EEF] tracking-wide">Gaming</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹1,48,650</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">2 hours ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 2 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/gpu-1.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Streaming & Editing PC</p>
                                                    <p class="text-[10px] text-on-surface-variant">Intel i7-14700K, RTX 4060 Ti...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <img src="images/about-team-1.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover">
                                                <div>
                                                    <p class="text-xs text-white">Priya Sharma</p>
                                                    <p class="text-[9px] text-on-surface-variant">priya@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-[#007AFF] tracking-wide">Streaming</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹1,02,300</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">1 day ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 3 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/gpu-2.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Video Editing Powerhouse</p>
                                                    <p class="text-[10px] text-on-surface-variant">Ryzen 9 7950X, RTX 4080...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <img src="images/about-team-2.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover">
                                                <div>
                                                    <p class="text-xs text-white">Amit Singh</p>
                                                    <p class="text-[9px] text-on-surface-variant">amit@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-[#00D084] tracking-wide">Editing</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹2,35,800</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-blue-500 tracking-wider">Converted</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">2 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 4 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/cpu-2.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Office Workstation</p>
                                                    <p class="text-[10px] text-on-surface-variant">Intel i5-13400, 16GB RAM...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-6 rounded-full bg-orange-500/20 text-orange-500 flex items-center justify-center text-[10px] font-bold border border-orange-500/30">
                                                    N
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Neha Gupta</p>
                                                    <p class="text-[9px] text-on-surface-variant">neha@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-[#00D084] tracking-wide">Productivity</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹45,600</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">3 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 5 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/motherboard-1.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Compact Budget Build</p>
                                                    <p class="text-[10px] text-on-surface-variant">Ryzen 5 5600G, 16GB RAM...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-6 rounded-full bg-blue-500/20 text-blue-500 flex items-center justify-center text-[10px] font-bold border border-blue-500/30">
                                                    V
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Vikram Joshi</p>
                                                    <p class="text-[9px] text-on-surface-variant">vikram@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-orange-500 tracking-wide">Budget</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹38,750</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-orange-500 tracking-wider">Expired</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">7 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 6 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/motherboard-2.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Future Proof Gaming PC</p>
                                                    <p class="text-[10px] text-on-surface-variant">Intel i9-14900K, RTX 4090...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-6 rounded-full bg-[#B14EEF]/20 text-[#B14EEF] flex items-center justify-center text-[10px] font-bold border border-[#B14EEF]/30">
                                                    A
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Arjun Saxena</p>
                                                    <p class="text-[9px] text-on-surface-variant">arjun@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-[#B14EEF] tracking-wide">Gaming</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹3,45,500</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">8 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 7 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/ram-1.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">3D Rendering Beast</p>
                                                    <p class="text-[10px] text-on-surface-variant">Ryzen 9 7950X3D, RTX 4080...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-6 rounded-full bg-pink-500/20 text-pink-500 flex items-center justify-center text-[10px] font-bold border border-pink-500/30">
                                                    D
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Deepak Yadav</p>
                                                    <p class="text-[9px] text-on-surface-variant">deepak@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-blue-500 tracking-wide">Workstation</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹2,18,900</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-blue-500 tracking-wider">Converted</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">10 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                    <!-- Row 8 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-center">
                                                <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                                    <img src="images/ram-2.jpg" alt="Case" class="w-full h-full object-contain">
                                                </div>
                                                <div>
                                                    <p class="text-sm font-medium text-white mb-0.5">Student Budget Build</p>
                                                    <p class="text-[10px] text-on-surface-variant">Intel i3-12100F, 8GB RAM...</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <img src="images/about-team-4.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover">
                                                <div>
                                                    <p class="text-xs text-white">Sneha Reddy</p>
                                                    <p class="text-[9px] text-on-surface-variant">sneha@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-medium text-orange-500 tracking-wide">Budget</span>
                                        </td>
                                        <td class="py-4 px-6 text-sm text-white font-medium">₹26,800</td>
                                        <td class="py-4 px-6">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-xs text-on-surface-variant">12 days ago</td>
                                        <td class="py-4 px-6 text-right">
                                            <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">mail</span>
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
                            <p class="text-[11px] text-on-surface-variant">Showing 1 to 8 of 1,256 builds</p>
                            
                            <div class="flex items-center gap-4">
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                                        <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center text-xs font-bold shadow-[0_0_10px_rgba(0,122,255,0.3)]">1</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">2</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">3</button>
                                    <span class="w-8 h-8 flex items-center justify-center text-on-surface-variant text-xs">...</span>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">157</button>
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
                    
                    <!-- RIGHT COLUMN: Selected Build Panel -->
                    <div class="w-80 shrink-0 bg-surface-container border border-white/5 rounded-xl flex flex-col p-6 sticky top-6 self-start max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
                        
                        <!-- Build Header -->
                        <div class="flex items-start gap-4 mb-4">
                            <div class="w-14 h-14 rounded-xl bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 overflow-hidden p-1">
                                <img src="images/cpu-1.jpg" alt="Case" class="w-full h-full object-contain">
                            </div>
                            <div class="flex-1">
                                <div class="flex items-center gap-2 mb-1">
                                    <h3 class="text-sm font-bold text-white">Rahul's Gaming Beast</h3>
                                    <span class="text-[8px] font-bold text-[#00D084] bg-[#00D084]/20 px-1.5 py-0.5 rounded tracking-widest uppercase">Active</span>
                                </div>
                                <p class="text-[9px] text-on-surface-variant">Saved on 12 May 2024 · 2 hours ago</p>
                            </div>
                        </div>
                        
                        <!-- Price -->
                        <div class="mb-4">
                            <p class="text-2xl font-bold text-white tracking-tight">₹1,48,650</p>
                            <p class="text-[10px] text-on-surface-variant">(Approx.)</p>
                        </div>
                        
                        <!-- Main Actions -->
                        <div class="flex flex-col gap-2 mb-6">
                            <button class="w-full py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-xs font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center justify-center gap-2">
                                View Full Build <span class="material-symbols-outlined text-[14px]">open_in_new</span>
                            </button>
                            <div class="flex gap-2">
                                <button class="flex-1 py-2 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-xs font-medium flex items-center justify-center gap-1.5">
                                    <span class="material-symbols-outlined text-[14px]">share</span> Share Build
                                </button>
                                <button class="flex-1 py-2 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-xs font-medium flex items-center justify-center gap-1.5">
                                    <span class="material-symbols-outlined text-[14px]">mail</span> Send Offer
                                </button>
                            </div>
                        </div>
                        
                        <hr class="border-white/5 mb-5">
                        
                        <!-- Build Summary -->
                        <div class="mb-5 flex-1">
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-4">Build Summary</h4>
                            
                            <div class="space-y-3">
                                <!-- CPU -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">memory</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">CPU</p>
                                        <p class="text-[10px] text-white truncate font-medium">AMD Ryzen 7 7800X3D</p>
                                    </div>
                                </div>
                                
                                <!-- GPU -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">developer_board</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">GPU</p>
                                        <p class="text-[10px] text-white truncate font-medium">NVIDIA RTX 4070 Ti SUPER</p>
                                    </div>
                                </div>
                                
                                <!-- Motherboard -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">dns</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">Motherboard</p>
                                        <p class="text-[10px] text-white truncate font-medium">ASUS TUF B650-PLUS WIFI</p>
                                    </div>
                                </div>
                                
                                <!-- RAM -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">sd_card</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">RAM</p>
                                        <p class="text-[10px] text-white truncate font-medium">32GB Corsair DDR5 6000MHz</p>
                                    </div>
                                </div>
                                
                                <!-- Storage -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">hard_drive</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">Storage</p>
                                        <p class="text-[10px] text-white truncate font-medium">1TB Samsung 980 PRO NVMe</p>
                                    </div>
                                </div>
                                
                                <!-- PSU -->
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded bg-surface-deep flex items-center justify-center border border-white/5">
                                        <span class="material-symbols-outlined text-[14px] text-[#00D084]">power</span>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <p class="text-[9px] text-on-surface-variant mb-0.5">PSU</p>
                                        <p class="text-[10px] text-white truncate font-medium">Corsair RM850e 850W</p>
                                    </div>
                                </div>
                            </div>
                            
                            <button class="text-[10px] text-primary hover:underline mt-4 font-medium">
                                + 6 more components
                            </button>
                        </div>
                        
                        <hr class="border-white/5 mb-5">
                        
                        <!-- Customer Info -->
                        <div>
                            <h4 class="text-[10px] font-bold text-white tracking-widest uppercase mb-3">Customer Info</h4>
                            
                            <div class="flex items-center gap-3 mb-4">
                                <img src="images/about-team-3.jpg" alt="Rahul" class="w-10 h-10 rounded-full border border-white/10 object-cover">
                                <div>
                                    <div class="flex items-center gap-2 mb-0.5">
                                        <p class="text-xs font-bold text-white">Rahul Verma</p>
                                        <span class="text-[7px] font-bold text-[#B14EEF] bg-[#B14EEF]/20 px-1 py-0.5 rounded tracking-widest uppercase">VIP</span>
                                    </div>
                                    <div class="flex items-center gap-1.5 text-[9px] text-on-surface-variant mb-0.5">
                                        <span class="material-symbols-outlined text-[10px]">mail</span> rahul@example.com
                                    </div>
                                    <div class="flex items-center gap-1.5 text-[9px] text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[10px]">call</span> +91 98765 43210
                                    </div>
                                </div>
                            </div>
                            
                            <button class="w-full py-2 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-xs font-medium">
                                View Customer Profile
                            </button>
                        </div>
                        
                    </div>
                </div>

            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('admin-saved-builds.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating admin-saved-builds.html!")

update_saved_builds()
