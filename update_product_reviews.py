import os
import re

def update_product_reviews():
    with open('product-reviews.html', 'r', encoding='utf-8') as f:
        content = f.read()

    main_pattern = r'(<main[^>]*>).*?(</main>)'
    match = re.search(main_pattern, content, flags=re.DOTALL)
    
    new_main_content = """
        <!-- Content Area -->
        <div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar bg-surface-deep text-on-surface">
            
            <!-- Header -->
            <header class="flex items-center justify-between px-8 py-6 pb-4 shrink-0 mt-2">
                <div>
                    <h2 class="font-headline-lg text-headline-lg text-white font-bold tracking-tight flex items-center gap-2">
                        Product Reviews
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">Manage and moderate all customer reviews and ratings.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Reviews
                    </button>
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">publish</span> Import Reviews
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">add</span> Add Review
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 5 KPI Cards -->
                <div class="grid grid-cols-5 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">chat</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Reviews</p>
                            <p class="text-2xl font-bold text-white">2,483</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">All time reviews</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 flex items-center justify-center shrink-0 border border-[#00D084]/20">
                            <span class="material-symbols-outlined text-[#00D084] text-xl">verified</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Approved Reviews</p>
                            <p class="text-2xl font-bold text-white">2,152</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">86.7% of total</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-yellow-500/10 flex items-center justify-center shrink-0 border border-yellow-500/20">
                            <span class="material-symbols-outlined text-yellow-500 text-xl">schedule</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Pending Reviews</p>
                            <p class="text-2xl font-bold text-white">214</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">8.6% of total</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-red-500/10 flex items-center justify-center shrink-0 border border-red-500/20">
                            <span class="material-symbols-outlined text-red-500 text-xl">close</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Rejected Reviews</p>
                            <p class="text-2xl font-bold text-white">117</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">4.7% of total</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0 border border-blue-500/20">
                            <span class="material-symbols-outlined text-blue-500 text-xl">star</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Average Rating</p>
                            <p class="text-2xl font-bold text-white">4.6</p>
                            <div class="flex items-center gap-1 mt-1">
                                <span class="material-symbols-outlined text-[10px] text-yellow-500">star</span>
                                <p class="text-[10px] text-yellow-500">Excellent</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm group flex-1">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search reviews, product, customer..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Status <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Ratings <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Products <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Customers <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">calendar_today</span> Date Range <span class="material-symbols-outlined text-sm ml-2">calendar_month</span>
                    </button>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-4 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2 ml-auto">
                        <span class="material-symbols-outlined text-sm">filter_alt</span> Filters
                    </button>
                </div>

                <!-- Table Area -->
                <div class="mt-6 flex-1 bg-surface-container border border-white/5 rounded-xl flex flex-col overflow-hidden">
                    
                    <!-- Table Header & Tabs -->
                    <div class="px-6 border-b border-white/5 flex items-center justify-between shrink-0">
                        <div class="flex gap-6">
                            <button class="py-4 text-sm font-medium text-white border-b-2 border-primary flex items-center gap-2">
                                All Reviews <span class="bg-white/10 text-white text-[10px] px-1.5 py-0.5 rounded">2,483</span>
                            </button>
                            <button class="py-4 text-sm font-medium text-on-surface-variant hover:text-white border-b-2 border-transparent transition-colors flex items-center gap-2">
                                Pending <span class="bg-white/5 text-on-surface-variant text-[10px] px-1.5 py-0.5 rounded">214</span>
                            </button>
                            <button class="py-4 text-sm font-medium text-on-surface-variant hover:text-white border-b-2 border-transparent transition-colors flex items-center gap-2">
                                Approved <span class="bg-white/5 text-on-surface-variant text-[10px] px-1.5 py-0.5 rounded">2,152</span>
                            </button>
                            <button class="py-4 text-sm font-medium text-on-surface-variant hover:text-white border-b-2 border-transparent transition-colors flex items-center gap-2">
                                Rejected <span class="bg-[#B14EEF]/20 text-[#B14EEF] text-[10px] px-1.5 py-0.5 rounded">117</span>
                            </button>
                        </div>
                        
                        <div class="flex items-center gap-3">
                            <button class="bg-surface-deep border border-white/5 rounded-lg py-1.5 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                                Sort By: Latest <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                            </button>
                            
                            <div class="flex bg-surface-deep border border-white/5 rounded-lg p-0.5">
                                <button class="p-1 rounded bg-primary/20 text-primary"><span class="material-symbols-outlined text-[16px] block">format_list_bulleted</span></button>
                                <button class="p-1 rounded text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px] block">grid_view</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Table -->
                    <div class="flex-1 overflow-x-auto overflow-y-auto custom-scrollbar">
                        <table class="w-full text-left border-collapse min-w-[1200px]">
                            <thead class="sticky top-0 bg-surface-container z-10">
                                <tr class="border-b border-white/5">
                                    <th class="py-4 px-6 w-12"><div class="w-4 h-4 rounded border border-white/20"></div></th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[300px]">REVIEW</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[200px]">PRODUCT</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[200px]">CUSTOMER</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[120px]">RATING</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[100px]">STATUS</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest w-[120px]">DATE</th>
                                    <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="text-sm divide-y divide-white/5">
                                
                                <!-- Row 1 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                    <td class="py-4 px-6">
                                        <div class="flex gap-4 items-start">
                                            <div class="w-12 h-12 rounded bg-surface-deep border border-white/10 shrink-0 p-1 flex items-center justify-center relative overflow-hidden">
                                                <div class="absolute inset-0 bg-[#0068B5]/20"></div>
                                                <span class="text-white font-bold text-[8px] relative z-10 tracking-widest uppercase">INTEL<br/>CORE</span>
                                            </div>
                                            <div>
                                                <p class="text-xs text-white leading-relaxed line-clamp-2">Excellent performance for gaming and content creation. Runs cool and stable.</p>
                                                <div class="flex gap-2 mt-2">
                                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 overflow-hidden flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-on-surface-variant">image</span></div>
                                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 overflow-hidden flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-on-surface-variant">image</span></div>
                                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center text-[8px] text-primary font-bold">+2</div>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Intel Core i7-14700K</p>
                                        <p class="text-[10px] text-on-surface-variant">CPU • Intel</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Rahul Verma</p>
                                        <p class="text-[10px] text-on-surface-variant mb-1">rahul@example.com</p>
                                        <div class="flex items-center gap-1 text-[#00D084]">
                                            <span class="material-symbols-outlined text-[10px]">verified</span>
                                            <span class="text-[9px] font-medium tracking-wide">Verified Buyer</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <div class="flex items-center gap-0.5 mb-1">
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                        </div>
                                        <p class="text-[10px] text-white">5.0</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 bg-[#00D084]/10 text-[#00D084] text-[10px] font-bold tracking-wider">Approved</span>
                                    </td>
                                    <td class="py-4 px-6 text-xs text-white">2 hours ago</td>
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
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                    <td class="py-4 px-6">
                                        <div class="flex gap-4 items-start">
                                            <div class="w-12 h-12 rounded bg-surface-deep border border-white/10 shrink-0 p-1 flex items-center justify-center relative overflow-hidden">
                                                <div class="absolute inset-0 bg-red-500/10"></div>
                                                <span class="material-symbols-outlined text-white/50 text-2xl relative z-10">memory</span>
                                            </div>
                                            <div>
                                                <p class="text-xs text-white leading-relaxed line-clamp-2">Beast GPU! 4K gaming with ray tracing is buttery smooth.</p>
                                                <div class="flex gap-2 mt-2">
                                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 overflow-hidden flex items-center justify-center"><span class="material-symbols-outlined text-[12px] text-on-surface-variant">image</span></div>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">ASUS ROG Strix RTX 4090</p>
                                        <p class="text-[10px] text-on-surface-variant">GPU • NVIDIA</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Priya Sharma</p>
                                        <p class="text-[10px] text-on-surface-variant mb-1">priya@example.com</p>
                                        <div class="flex items-center gap-1 text-[#00D084]">
                                            <span class="material-symbols-outlined text-[10px]">verified</span>
                                            <span class="text-[9px] font-medium tracking-wide">Verified Buyer</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <div class="flex items-center gap-0.5 mb-1">
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-white/20">star</span>
                                        </div>
                                        <p class="text-[10px] text-white">4.0</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 bg-[#00D084]/10 text-[#00D084] text-[10px] font-bold tracking-wider">Approved</span>
                                    </td>
                                    <td class="py-4 px-6 text-xs text-white">5 hours ago</td>
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
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                    <td class="py-4 px-6">
                                        <div class="flex gap-4 items-start">
                                            <div class="w-12 h-12 rounded bg-surface-deep border border-white/10 shrink-0 p-1 flex items-center justify-center relative overflow-hidden">
                                                <div class="absolute inset-0 bg-yellow-500/10"></div>
                                                <span class="material-symbols-outlined text-white/50 text-2xl relative z-10">memory_alt</span>
                                            </div>
                                            <div>
                                                <p class="text-xs text-white leading-relaxed line-clamp-2">Great memory for high performance builds. XMP works perfectly.</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Corsair Vengeance 32GB DDR5</p>
                                        <p class="text-[10px] text-on-surface-variant">RAM • Corsair</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Amit Singh</p>
                                        <p class="text-[10px] text-on-surface-variant mb-1">amit@example.com</p>
                                        <div class="flex items-center gap-1 text-[#00D084]">
                                            <span class="material-symbols-outlined text-[10px]">verified</span>
                                            <span class="text-[9px] font-medium tracking-wide">Verified Buyer</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <div class="flex items-center gap-0.5 mb-1">
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                        </div>
                                        <p class="text-[10px] text-white">5.0</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-full border border-yellow-500/20 bg-yellow-500/10 text-yellow-500 text-[10px] font-bold tracking-wider">Pending</span>
                                    </td>
                                    <td class="py-4 px-6 text-xs text-white">1 day ago</td>
                                    <td class="py-4 px-6 text-right">
                                        <div class="flex items-center justify-end gap-2 opacity-100">
                                            <button class="w-8 h-8 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg bg-[#00D084]/10 border border-[#00D084]/30 flex items-center justify-center text-[#00D084] hover:bg-[#00D084]/20 transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">check</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg bg-red-500/10 border border-red-500/30 flex items-center justify-center text-red-500 hover:bg-red-500/20 transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">close</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>

                                <!-- Row 4 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                    <td class="py-4 px-6">
                                        <div class="flex gap-4 items-start">
                                            <div class="w-12 h-12 rounded bg-surface-deep border border-white/10 shrink-0 p-1 flex items-center justify-center relative overflow-hidden">
                                                <div class="absolute inset-0 bg-white/5"></div>
                                                <span class="material-symbols-outlined text-white/50 text-2xl relative z-10">developer_board</span>
                                            </div>
                                            <div>
                                                <p class="text-xs text-white leading-relaxed line-clamp-2">Good motherboard but the BIOS could be more user friendly.</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">MSI MAG B650 Tomahawk WiFi</p>
                                        <p class="text-[10px] text-on-surface-variant">Motherboard • MSI</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Neha Gupta</p>
                                        <p class="text-[10px] text-on-surface-variant mb-1">neha@example.com</p>
                                        <div class="flex items-center gap-1 text-[#00D084]">
                                            <span class="material-symbols-outlined text-[10px]">verified</span>
                                            <span class="text-[9px] font-medium tracking-wide">Verified Buyer</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <div class="flex items-center gap-0.5 mb-1">
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-white/20">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-white/20">star</span>
                                        </div>
                                        <p class="text-[10px] text-white">3.0</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-full border border-[#00D084]/20 bg-[#00D084]/10 text-[#00D084] text-[10px] font-bold tracking-wider">Approved</span>
                                    </td>
                                    <td class="py-4 px-6 text-xs text-white">2 days ago</td>
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
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="py-4 px-6"><div class="w-4 h-4 rounded border border-white/20"></div></td>
                                    <td class="py-4 px-6">
                                        <div class="flex gap-4 items-start">
                                            <div class="w-12 h-12 rounded bg-surface-deep border border-white/10 shrink-0 p-1 flex items-center justify-center relative overflow-hidden">
                                                <div class="absolute inset-0 bg-white/5"></div>
                                                <span class="material-symbols-outlined text-white/50 text-2xl relative z-10">sim_card</span>
                                            </div>
                                            <div>
                                                <p class="text-xs text-white leading-relaxed line-clamp-2">Super fast SSD. Boot times are incredible.</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Samsung 990 PRO 1TB</p>
                                        <p class="text-[10px] text-on-surface-variant">SSD • Samsung</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <p class="text-xs font-medium text-white mb-1">Vikram Joshi</p>
                                        <p class="text-[10px] text-on-surface-variant mb-1">vikram@example.com</p>
                                        <div class="flex items-center gap-1 text-[#00D084]">
                                            <span class="material-symbols-outlined text-[10px]">verified</span>
                                            <span class="text-[9px] font-medium tracking-wide">Verified Buyer</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        <div class="flex items-center gap-0.5 mb-1">
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                            <span class="material-symbols-outlined text-[14px] text-yellow-500">star</span>
                                        </div>
                                        <p class="text-[10px] text-white">5.0</p>
                                    </td>
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-full border border-red-500/20 bg-red-500/10 text-red-500 text-[10px] font-bold tracking-wider">Rejected</span>
                                    </td>
                                    <td class="py-4 px-6 text-xs text-white">2 days ago</td>
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
                            <p class="text-[11px] text-on-surface-variant">Showing 1 to 10 of 2,483 reviews</p>
                            
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
            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('product-reviews.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating product-reviews.html!")

update_product_reviews()
