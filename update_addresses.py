import os
import re

def update_addresses():
    with open('admin-addresses.html', 'r', encoding='utf-8') as f:
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
                        Addresses
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">View and manage customer addresses in one place.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Addresses
                    </button>
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">upload</span> Import Addresses
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">add</span> Add Address
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 4 KPI Cards -->
                <div class="grid grid-cols-4 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">contacts</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Addresses</p>
                            <p class="text-2xl font-bold text-white">3,256</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">All customer addresses</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 flex items-center justify-center shrink-0 border border-[#00D084]/20">
                            <span class="material-symbols-outlined text-[#00D084] text-xl">home</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Default Addresses</p>
                            <p class="text-2xl font-bold text-white">1,842</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Default shipping addresses</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-orange-500/10 flex items-center justify-center shrink-0 border border-orange-500/20">
                            <span class="material-symbols-outlined text-orange-500 text-xl">location_on</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Billing Addresses</p>
                            <p class="text-2xl font-bold text-white">2,514</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Billing addresses</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#007AFF]/10 flex items-center justify-center shrink-0 border border-[#007AFF]/20">
                            <span class="material-symbols-outlined text-[#007AFF] text-xl">map</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Unique Pin Codes</p>
                            <p class="text-2xl font-bold text-white">1,124</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Across all addresses</p>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search by name, email, phone, pincode..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Types <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Customers <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        All Status <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
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
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">ADDRESS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">CUSTOMER</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">TYPE</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-center">PIN CODE</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">STATUS</th>
                                        <th class="py-4 px-6 text-[10px] font-bold text-on-surface-variant uppercase tracking-widest text-right">ACTIONS</th>
                                    </tr>
                                </thead>
                                <tbody class="text-sm divide-y divide-white/5">
                                    
                                    <!-- Row 1 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer bg-white/[0.02]">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">221B Baker Street, Near Park Street</p>
                                                    <p class="text-[10px] text-on-surface-variant">Kolkata, West Bengal, 700016</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <img src="images/about-team-3.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover mt-0.5">
                                                <div>
                                                    <p class="text-xs text-white">Rahul Verma</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">rahul@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 98765 43210</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Home</span>
                                                <span class="text-[9px] font-medium text-[#00D084] bg-[#00D084]/10 px-2 py-0.5 rounded tracking-wide">Default Shipping</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">700016</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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

                                    <!-- Row 2 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">456 MG Road, Indiranagar</p>
                                                    <p class="text-[10px] text-on-surface-variant">Bangalore, Karnataka, 560038</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <img src="images/about-team-1.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover mt-0.5">
                                                <div>
                                                    <p class="text-xs text-white">Priya Sharma</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">priya@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 87654 32109</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-[#B14EEF] bg-[#B14EEF]/10 px-2 py-0.5 rounded tracking-wide">Work</span>
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Shipping</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">560038</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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

                                    <!-- Row 3 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">12 Green Park, Hauz Khas</p>
                                                    <p class="text-[10px] text-on-surface-variant">New Delhi, Delhi, 110016</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <img src="images/about-team-2.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover mt-0.5">
                                                <div>
                                                    <p class="text-xs text-white">Amit Singh</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">amit@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 76543 21098</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-orange-500 bg-orange-500/10 px-2 py-0.5 rounded tracking-wide">Other</span>
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Billing</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">110016</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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

                                    <!-- Row 4 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">Flat 3B, Ocean View, Marine Drive</p>
                                                    <p class="text-[10px] text-on-surface-variant">Mumbai, Maharashtra, 400020</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <img src="images/about-team-4.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover mt-0.5">
                                                <div>
                                                    <p class="text-xs text-white">Neha Gupta</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">neha@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 65432 10987</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Home</span>
                                                <span class="text-[9px] font-medium text-[#00D084] bg-[#00D084]/10 px-2 py-0.5 rounded tracking-wide">Default Shipping</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">400020</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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

                                    <!-- Row 5 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">Block A, Sector 62, Noida</p>
                                                    <p class="text-[10px] text-on-surface-variant">Noida, Uttar Pradesh, 201309</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <div class="w-6 h-6 rounded-full bg-blue-500/20 text-blue-500 flex items-center justify-center text-[10px] font-bold border border-blue-500/30 mt-0.5">
                                                    V
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Vikram Joshi</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">vikram@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 54321 09876</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-[#B14EEF] bg-[#B14EEF]/10 px-2 py-0.5 rounded tracking-wide">Work</span>
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Shipping</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">201309</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-red-500 tracking-wider">Inactive</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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
                                    
                                    <!-- Row 6 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">7/45 Anna Nagar, 3rd Avenue</p>
                                                    <p class="text-[10px] text-on-surface-variant">Chennai, Tamil Nadu, 600040</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <div class="w-6 h-6 rounded-full bg-[#B14EEF]/20 text-[#B14EEF] flex items-center justify-center text-[10px] font-bold border border-[#B14EEF]/30 mt-0.5">
                                                    A
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white">Arjun Saxena</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">arjun@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 43210 98765</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-orange-500 bg-orange-500/10 px-2 py-0.5 rounded tracking-wide">Other</span>
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Billing</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">600040</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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

                                    <!-- Row 7 -->
                                    <tr class="hover:bg-white/5 transition-colors group cursor-pointer">
                                        <td class="py-4 px-6">
                                            <div class="flex gap-4 items-start">
                                                <div class="w-8 h-8 mt-1 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant">
                                                    <span class="material-symbols-outlined text-[16px]">location_on</span>
                                                </div>
                                                <div>
                                                    <p class="text-xs text-white mb-0.5">Near City Center Mall, Salt Lake</p>
                                                    <p class="text-[10px] text-on-surface-variant">Kolkata, West Bengal, 700064</p>
                                                    <p class="text-[10px] text-on-surface-variant">India</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex items-start gap-2">
                                                <img src="images/about-team-3.jpg" alt="Avatar" class="w-6 h-6 rounded-full border border-white/10 object-cover mt-0.5">
                                                <div>
                                                    <p class="text-xs text-white">Deepak Yadav</p>
                                                    <p class="text-[9px] text-on-surface-variant mb-0.5">deepak@example.com</p>
                                                    <p class="text-[9px] text-on-surface-variant">+91 98760 12345</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <div class="flex flex-col items-start gap-2">
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Home</span>
                                                <span class="text-[9px] font-medium text-white bg-white/10 px-2 py-0.5 rounded tracking-wide">Shipping</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-6 align-top pt-5 text-sm text-white font-medium text-center">700064</td>
                                        <td class="py-4 px-6 align-top pt-5">
                                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                                        </td>
                                        <td class="py-4 px-6 text-right align-top pt-4">
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
                            <p class="text-[11px] text-on-surface-variant">Showing 1 to 7 of 3,256 addresses</p>
                            
                            <div class="flex items-center gap-4">
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 rounded-lg border border-white/5 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                                        <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg bg-primary text-white flex items-center justify-center text-xs font-bold shadow-[0_0_10px_rgba(0,122,255,0.3)]">1</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">2</button>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">3</button>
                                    <span class="w-8 h-8 flex items-center justify-center text-on-surface-variant text-xs">...</span>
                                    <button class="w-8 h-8 rounded-lg border border-transparent flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors text-xs">326</button>
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
                    
                    <!-- RIGHT COLUMN: Selected Address Panel -->
                    <div class="w-[340px] shrink-0 bg-surface-container border border-white/5 rounded-xl flex flex-col p-6 sticky top-6 self-start max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
                        
                        <!-- Top Header -->
                        <div class="flex items-center justify-between mb-6">
                            <h3 class="text-sm font-bold text-white tracking-widest">Address Details</h3>
                            <span class="text-[10px] font-bold text-[#00D084] tracking-wider">Active</span>
                        </div>
                        
                        <!-- Address Card -->
                        <div class="flex items-start gap-4 mb-6">
                            <div class="w-12 h-12 rounded-full bg-primary/20 text-primary flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-[20px]">location_on</span>
                            </div>
                            <div>
                                <span class="text-[9px] font-medium text-[#00D084] bg-transparent border border-[#00D084]/30 px-2 py-0.5 rounded tracking-wide mb-2 inline-block">Default Shipping</span>
                                <p class="text-xs text-white leading-relaxed">221B Baker Street, Near Park Street<br>Kolkata, West Bengal, 700016<br>India</p>
                            </div>
                        </div>
                        
                        <!-- Details Grid -->
                        <div class="space-y-4 mb-6 flex-1">
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Customer</p>
                                <p class="text-xs text-white font-medium text-right">Rahul Verma</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Email</p>
                                <p class="text-xs text-white font-medium text-right truncate">rahul@example.com</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Phone</p>
                                <p class="text-xs text-white font-medium text-right">+91 98765 43210</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Address Type</p>
                                <p class="text-xs text-white font-medium text-right">Home</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Address For</p>
                                <p class="text-xs text-white font-medium text-right">Shipping</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Pin Code</p>
                                <p class="text-xs text-white font-medium text-right">700016</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Added On</p>
                                <p class="text-[10px] text-white font-medium text-right">12 May 2024, 10:30 AM</p>
                            </div>
                            <div class="grid grid-cols-[100px_1fr] gap-2 items-center">
                                <p class="text-[10px] text-on-surface-variant">Last Updated</p>
                                <p class="text-[10px] text-white font-medium text-right">14 May 2024, 04:15 PM</p>
                            </div>
                        </div>
                        
                        <!-- Main Actions -->
                        <div class="flex gap-2 mb-3">
                            <button class="flex-1 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-xs font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)]">
                                Edit Address
                            </button>
                            <button class="flex-1 py-2.5 rounded-lg bg-transparent border border-red-500/30 text-red-500 hover:bg-red-500/10 transition-all text-xs font-medium flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">delete</span> Delete Address
                            </button>
                        </div>
                        
                        <!-- Secondary Actions -->
                        <div class="flex gap-2 mb-6">
                            <button class="flex-1 py-2 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-[10px] font-medium flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">star</span> Mark as Default
                            </button>
                            <button class="flex-1 py-2 rounded-lg bg-surface-deep border border-white/5 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-[10px] font-medium flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">map</span> View on Map
                            </button>
                        </div>
                        
                        <!-- Address Summary -->
                        <div class="bg-surface-deep rounded-xl p-4 border border-white/5">
                            <h4 class="text-[11px] font-bold text-white mb-3">Address Summary</h4>
                            
                            <div class="space-y-3">
                                <div class="flex justify-between items-center">
                                    <p class="text-[10px] text-on-surface-variant">Total Orders Shipped</p>
                                    <p class="text-[10px] text-white font-medium">12</p>
                                </div>
                                <div class="flex justify-between items-center">
                                    <p class="text-[10px] text-on-surface-variant">Total Spent</p>
                                    <p class="text-[10px] text-white font-medium">₹ 1,48,650</p>
                                </div>
                                <div class="flex justify-between items-center">
                                    <p class="text-[10px] text-on-surface-variant">Last Order Date</p>
                                    <p class="text-[10px] text-white font-medium">12 May 2024</p>
                                </div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-white/5">
                                    <p class="text-[10px] text-on-surface-variant">Order Status</p>
                                    <span class="text-[9px] font-bold text-[#00D084] tracking-wider">Delivered</span>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                </div>

            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('admin-addresses.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating admin-addresses.html!")

update_addresses()
