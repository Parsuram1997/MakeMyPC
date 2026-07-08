import os
import re

def generate_admin_shipping():
    # Read the base template from an existing admin file (like admin-dashboard.html)
    with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
        base_html = f.read()

    # Find the main content area
    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    shipping_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined text-[32px] text-white">local_shipping</span>
                    <div>
                        <h1 class="text-3xl font-bold text-white mb-2 tracking-tight">Shipping</h1>
                        <p class="text-on-surface-variant text-sm">Manage shipments, carriers, delivery and tracking.</p>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <button class="px-5 py-2.5 rounded-xl bg-primary hover:bg-primary/90 text-on-primary font-medium transition-all duration-300 flex items-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">add</span>
                        Create Shipment
                        <span class="material-symbols-outlined text-[18px] ml-1">expand_more</span>
                    </button>
                </div>
            </div>

            <!-- Stats Grid (5 Cards) -->
            <div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-8 relative z-10">
                <!-- Total Shipments -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-10 h-10 rounded-xl bg-[#3b82f6]/10 border border-[#3b82f6]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#3b82f6] text-[20px]">inventory_2</span>
                        </div>
                        <div>
                            <p class="text-xs font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Total Shipments</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">1,452</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-3">
                        <span class="material-symbols-outlined text-[14px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">12.8%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Pending Shipments -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-10 h-10 rounded-xl bg-[#ef4444]/10 border border-[#ef4444]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#ef4444] text-[20px]">schedule</span>
                        </div>
                        <div>
                            <p class="text-xs font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Pending Shipments</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">128</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-3">
                        <span class="material-symbols-outlined text-[14px] text-red-400">arrow_downward</span>
                        <span class="text-xs font-medium text-red-400">5.3%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- In Transit -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-10 h-10 rounded-xl bg-[#3b82f6]/10 border border-[#3b82f6]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#3b82f6] text-[20px]">local_shipping</span>
                        </div>
                        <div>
                            <p class="text-xs font-medium text-on-surface-variant mb-1 uppercase tracking-wider">In Transit</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">842</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-3">
                        <span class="material-symbols-outlined text-[14px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">18.6%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Delivered -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-10 h-10 rounded-xl bg-[#10b981]/10 border border-[#10b981]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#10b981] text-[20px]">check_circle</span>
                        </div>
                        <div>
                            <p class="text-xs font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Delivered</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">1,213</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-3">
                        <span class="material-symbols-outlined text-[14px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">14.2%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Returned / RTO -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-10 h-10 rounded-xl bg-[#ef4444]/10 border border-[#ef4444]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#ef4444] text-[20px]">assignment_return</span>
                        </div>
                        <div>
                            <p class="text-xs font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Returned / RTO</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">47</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-3">
                        <span class="material-symbols-outlined text-[14px] text-red-400">arrow_downward</span>
                        <span class="text-xs font-medium text-red-400">8.7%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>
            </div>

            <!-- Filters Bar -->
            <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-4 mb-6 relative z-10 flex items-center gap-4">
                <!-- Search -->
                <div class="relative flex-1 max-w-[320px]">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px] pointer-events-none">search</span>
                    <input type="text" placeholder="Search by Order ID, AWB, Customer, Destination..." class="w-full h-10 bg-black/20 border border-white/10 rounded-lg pl-10 pr-4 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:border-primary/50 transition-colors" />
                </div>

                <!-- Dropdown Filters -->
                <div class="relative flex-1 max-w-[150px]">
                    <select class="w-full h-10 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Status</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[18px]">expand_more</span>
                </div>
                
                <div class="relative flex-1 max-w-[150px]">
                    <select class="w-full h-10 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Carriers</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[18px]">expand_more</span>
                </div>

                <div class="relative flex-1 max-w-[150px]">
                    <select class="w-full h-10 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Warehouses</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[18px]">expand_more</span>
                </div>

                <div class="flex items-center gap-4">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:border-white/20 bg-surface-container/50 text-white font-medium transition-all duration-300 flex items-center gap-2 text-sm">
                        <span class="material-symbols-outlined text-[18px]">filter_list</span>
                        Filters
                    </button>
                    <a href="#" class="text-primary hover:text-primary/80 text-sm font-medium transition-colors">Reset</a>
                </div>
                
                <div class="relative max-w-[240px] ml-auto">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px] pointer-events-none">calendar_month</span>
                    <input type="text" value="12 May 2024 - 18 May 2024" readonly class="w-full h-10 bg-black/20 border border-white/10 rounded-lg pl-10 pr-10 text-sm text-white focus:outline-none focus:border-primary/50 transition-colors cursor-pointer" />
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px] pointer-events-none">expand_more</span>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="flex gap-6 relative z-10">
                
                <!-- Left Column (approx 2/3) -->
                <div class="w-2/3 flex flex-col gap-6">
                    
                    <!-- Shipments Table Card -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        
                        <!-- Tabs -->
                        <div class="flex items-center px-2 pt-2 border-b border-white/5 overflow-x-auto custom-scrollbar">
                            <button class="px-4 py-3 text-sm font-medium text-primary border-b-2 border-primary whitespace-nowrap">All Shipments (1,452)</button>
                            <button class="px-4 py-3 text-sm font-medium text-on-surface-variant hover:text-white hover:bg-white/5 rounded-t-lg transition-colors whitespace-nowrap border-b-2 border-transparent">Pending (128)</button>
                            <button class="px-4 py-3 text-sm font-medium text-on-surface-variant hover:text-white hover:bg-white/5 rounded-t-lg transition-colors whitespace-nowrap border-b-2 border-transparent">In Transit (842)</button>
                            <button class="px-4 py-3 text-sm font-medium text-on-surface-variant hover:text-white hover:bg-white/5 rounded-t-lg transition-colors whitespace-nowrap border-b-2 border-transparent">Delivered (1,213)</button>
                            <button class="px-4 py-3 text-sm font-medium text-on-surface-variant hover:text-white hover:bg-white/5 rounded-t-lg transition-colors whitespace-nowrap border-b-2 border-transparent">Returned (47)</button>
                        </div>
                        
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="border-b border-white/5 bg-black/20">
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Order ID</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Customer</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">AWB / Tracking ID</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Carrier</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Status</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Est. Delivery</th>
                                        <th class="py-3 px-6 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider text-center">Actions</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-white/5">
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1254</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">18 May 2024, 10:30 AM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Rohit Kumar</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Bhubaneswar, Odisha</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">1498563214785</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Delhivery</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-white">
                                                DELHIVERY
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#3b82f6]/20 text-[#3b82f6]">In Transit</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Bhubaneswar Hub</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">20 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">by 8:00 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1253</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">18 May 2024, 09:15 AM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Pooja Sharma</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Delhi, Delhi</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">3126549874123</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">BlueDart</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-blue-500">
                                                BLUE <span class="text-[#10b981]">DART</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#f59e0b]/20 text-[#f59e0b]">Pending</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Ready to Ship</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">21 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">by 8:00 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1252</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">17 May 2024, 08:45 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Amit Singh</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Mumbai, Maharashtra</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">X1234567890IN</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">XpressBees</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-[#f59e0b]">
                                                XPRESS<span class="text-white">BEES</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/20 text-[#10b981]">Delivered</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Delivered on 18 May</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">18 May 2024</p>
                                            <p class="text-[10px] text-[#10b981] flex items-center gap-0.5 mt-0.5"><span class="material-symbols-outlined text-[12px]">check</span> Delivered</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1251</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">17 May 2024, 07:20 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Neha Verma</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Lucknow, Uttar Pradesh</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">1498523698741</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Delhivery</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-white">
                                                DELHIVERY
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#3b82f6]/20 text-[#3b82f6]">In Transit</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Lucknow Hub</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">19 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">by 8:00 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1250</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">17 May 2024, 06:10 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Manoj Jha</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Patna, Bihar</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">3126598741236</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">BlueDart</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-blue-500">
                                                BLUE <span class="text-[#10b981]">DART</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#3b82f6]/20 text-[#3b82f6]">In Transit</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Patna Hub</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">20 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">by 8:00 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1249</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">16 May 2024, 11:30 AM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Sanjay Kumar</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Jaipur, Rajasthan</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">X1234567892IN</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">XpressBees</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-[#f59e0b]">
                                                XPRESS<span class="text-white">BEES</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#ef4444]/20 text-[#ef4444]">Returned</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">RTO Initiated</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-on-surface-variant font-medium">-</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1248</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">16 May 2024, 10:00 AM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Vikash Yadav</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Indore, Madhya Pradesh</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">1498523698745</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Delhivery</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-white">
                                                DELHIVERY
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/20 text-[#10b981]">Delivered</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Delivered on 17 May</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">17 May 2024</p>
                                            <p class="text-[10px] text-[#10b981] flex items-center gap-0.5 mt-0.5"><span class="material-symbols-outlined text-[12px]">check</span> Delivered</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-6">
                                            <a href="#" class="text-sm font-medium text-primary hover:underline">ORD-2024-1247</a>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">16 May 2024, 09:20 AM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">Anjali Patel</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">Ahmedabad, Gujarat</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm text-white font-medium">3126549874127</span>
                                                <span class="material-symbols-outlined text-[14px] text-primary cursor-pointer hover:text-primary/80">content_copy</span>
                                            </div>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">BlueDart</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-1 font-black italic tracking-tighter text-blue-500">
                                                BLUE <span class="text-[#10b981]">DART</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6">
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold bg-[#f59e0b]/20 text-[#f59e0b]">Pending</span>
                                            <p class="text-[10px] text-on-surface-variant mt-1">Label Created</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <p class="text-sm text-white font-medium">21 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">by 8:00 PM</p>
                                        </td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                                                </button>
                                                <button class="w-8 h-8 rounded-lg bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[18px]">more_horiz</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                </tbody>
                            </table>
                        </div>
                        
                        <!-- Pagination -->
                        <div class="p-4 border-t border-white/5 flex items-center justify-between">
                            <p class="text-sm text-on-surface-variant">Showing 1 to 8 of 1,452 shipments</p>
                            <div class="flex items-center gap-2">
                                <button class="w-8 h-8 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors disabled:opacity-50">
                                    <span class="material-symbols-outlined text-[18px]">chevron_left</span>
                                </button>
                                <button class="w-8 h-8 rounded bg-primary text-on-primary flex items-center justify-center text-sm font-medium">1</button>
                                <button class="w-8 h-8 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-sm font-medium">2</button>
                                <button class="w-8 h-8 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-sm font-medium">3</button>
                                <span class="text-on-surface-variant text-sm">...</span>
                                <button class="w-8 h-8 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-sm font-medium">182</button>
                                
                                <div class="relative ml-2">
                                    <select class="h-8 bg-transparent border border-white/10 rounded px-2 pr-6 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                                        <option value="10">10 / page</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-1.5 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[16px]">expand_more</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column (approx 1/3) -->
                <div class="w-1/3 flex flex-col gap-6">
                    
                    <!-- Quick Actions -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-5 border-b border-white/5">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Quick Actions</h3>
                        </div>
                        <div class="flex flex-col">
                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">add_circle</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Create Shipment</p>
                                    <p class="text-[11px] text-on-surface-variant">Create a new shipment</p>
                                </div>
                            </a>
                            
                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">upload_file</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Bulk Upload Shipments</p>
                                    <p class="text-[11px] text-on-surface-variant">Upload shipments in bulk</p>
                                </div>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">print</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Print Shipping Labels</p>
                                    <p class="text-[11px] text-on-surface-variant">Print labels for shipments</p>
                                </div>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">local_shipping</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Manage Carriers</p>
                                    <p class="text-[11px] text-on-surface-variant">Add or manage shipping carriers</p>
                                </div>
                            </a>
                        </div>
                    </div>

                    <!-- Shipping Analytics -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-5 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Shipping Analytics</h3>
                            <div class="relative">
                                <select class="text-xs text-on-surface-variant bg-transparent border-none appearance-none cursor-pointer pr-4 focus:outline-none hover:text-white transition-colors">
                                    <option>This Month</option>
                                    <option>Last Month</option>
                                </select>
                                <span class="material-symbols-outlined absolute right-0 top-1/2 -translate-y-1/2 text-[14px] pointer-events-none text-on-surface-variant">expand_more</span>
                            </div>
                        </div>
                        <div class="p-5 flex items-center gap-6">
                            <!-- Donut Chart -->
                            <div class="relative w-[120px] h-[120px] shrink-0">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                                    <!-- Base Circle -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="12"></circle>
                                    <!-- Delivered (Green) ~83% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#10b981" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="42.7"></circle>
                                    <!-- In Transit (Blue) ~58% of remaining -> Overlapping visual trick or proper offset -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#3b82f6" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="180" stroke-dashoffset="160" transform="rotate(300 50 50)"></circle>
                                    <!-- Pending (Yellow) ~8% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#f59e0b" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="230" transform="rotate(240 50 50)"></circle>
                                    <!-- Returned (Red) ~3% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#ef4444" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="242" transform="rotate(225 50 50)"></circle>
                                </svg>
                                <div class="absolute inset-0 flex flex-col items-center justify-center">
                                    <span class="text-xl font-bold text-white">1,452</span>
                                    <span class="text-[10px] text-on-surface-variant">Total</span>
                                </div>
                            </div>
                            
                            <!-- Legend -->
                            <div class="flex-1 flex flex-col gap-3">
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-2">
                                        <div class="w-2 h-2 rounded-full bg-[#10b981]"></div>
                                        <span class="text-xs text-on-surface-variant">Delivered</span>
                                    </div>
                                    <span class="text-xs font-medium text-white">1,213 <span class="text-on-surface-variant font-normal">(83.6%)</span></span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-2">
                                        <div class="w-2 h-2 rounded-full bg-[#3b82f6]"></div>
                                        <span class="text-xs text-on-surface-variant">In Transit</span>
                                    </div>
                                    <span class="text-xs font-medium text-white">842 <span class="text-on-surface-variant font-normal">(58.0%)</span></span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-2">
                                        <div class="w-2 h-2 rounded-full bg-[#f59e0b]"></div>
                                        <span class="text-xs text-on-surface-variant">Pending</span>
                                    </div>
                                    <span class="text-xs font-medium text-white">128 <span class="text-on-surface-variant font-normal">(8.8%)</span></span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center gap-2">
                                        <div class="w-2 h-2 rounded-full bg-[#ef4444]"></div>
                                        <span class="text-xs text-on-surface-variant">Returned</span>
                                    </div>
                                    <span class="text-xs font-medium text-white">47 <span class="text-on-surface-variant font-normal">(3.2%)</span></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Top Carriers Performance -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-5 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Top Carriers Performance</h3>
                            <div class="relative">
                                <select class="text-xs text-on-surface-variant bg-transparent border-none appearance-none cursor-pointer pr-4 focus:outline-none hover:text-white transition-colors">
                                    <option>This Month</option>
                                    <option>Last Month</option>
                                </select>
                                <span class="material-symbols-outlined absolute right-0 top-1/2 -translate-y-1/2 text-[14px] pointer-events-none text-on-surface-variant">expand_more</span>
                            </div>
                        </div>
                        <div class="p-5 flex flex-col gap-4">
                            <div class="flex flex-col gap-1.5">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-white font-medium">Delhivery</span>
                                    <span class="text-white">685 <span class="text-on-surface-variant">(47.1%)</span></span>
                                </div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 47.1%"></div>
                                </div>
                            </div>
                            
                            <div class="flex flex-col gap-1.5">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-white font-medium">BlueDart</span>
                                    <span class="text-white">512 <span class="text-on-surface-variant">(35.2%)</span></span>
                                </div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 35.2%"></div>
                                </div>
                            </div>

                            <div class="flex flex-col gap-1.5">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-white font-medium">XpressBees</span>
                                    <span class="text-white">205 <span class="text-on-surface-variant">(14.1%)</span></span>
                                </div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 14.1%"></div>
                                </div>
                            </div>

                            <div class="flex flex-col gap-1.5">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-white font-medium">India Post</span>
                                    <span class="text-white">50 <span class="text-on-surface-variant">(3.4%)</span></span>
                                </div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-[#10b981] rounded-full" style="width: 3.4%"></div>
                                </div>
                            </div>

                            <div class="flex flex-col gap-1.5">
                                <div class="flex items-center justify-between text-xs">
                                    <span class="text-white font-medium">Others</span>
                                    <span class="text-on-surface-variant font-medium">—</span>
                                </div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 0%"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Delivery Performance -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-5 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Delivery Performance</h3>
                            <div class="relative">
                                <select class="text-xs text-on-surface-variant bg-transparent border-none appearance-none cursor-pointer pr-4 focus:outline-none hover:text-white transition-colors">
                                    <option>This Month</option>
                                    <option>Last Month</option>
                                </select>
                                <span class="material-symbols-outlined absolute right-0 top-1/2 -translate-y-1/2 text-[14px] pointer-events-none text-on-surface-variant">expand_more</span>
                            </div>
                        </div>
                        <div class="p-5 grid grid-cols-3 gap-4">
                            <div class="flex flex-col items-center justify-center text-center">
                                <h4 class="text-xl font-bold text-white mb-1">98.2%</h4>
                                <p class="text-[10px] text-on-surface-variant mb-1">On-time Delivery</p>
                                <div class="flex items-center gap-0.5">
                                    <span class="material-symbols-outlined text-[12px] text-[#10b981]">arrow_upward</span>
                                    <span class="text-[10px] font-medium text-[#10b981]">2.8%</span>
                                </div>
                            </div>
                            <div class="flex flex-col items-center justify-center text-center">
                                <h4 class="text-xl font-bold text-white mb-1">1.8%</h4>
                                <p class="text-[10px] text-on-surface-variant mb-1">Delays</p>
                                <div class="flex items-center gap-0.5">
                                    <span class="material-symbols-outlined text-[12px] text-[#ef4444]">arrow_downward</span>
                                    <span class="text-[10px] font-medium text-[#ef4444]">0.6%</span>
                                </div>
                            </div>
                            <div class="flex flex-col items-center justify-center text-center">
                                <h4 class="text-xl font-bold text-white mb-1">0.3%</h4>
                                <p class="text-[10px] text-on-surface-variant mb-1">RTO Rate</p>
                                <div class="flex items-center gap-0.5">
                                    <span class="material-symbols-outlined text-[12px] text-[#ef4444]">arrow_downward</span>
                                    <span class="text-[10px] font-medium text-[#ef4444]">0.2%</span>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{shipping_content}</main>', base_html)
    
    # Update active state in sidebar
    new_html = new_html.replace('href="admin-shipping.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary"', 
                                'href="admin-shipping.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 bg-primary/10 text-primary"')
    

    with open('admin-shipping.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Successfully generated admin-shipping.html")

if __name__ == '__main__':
    generate_admin_shipping()
