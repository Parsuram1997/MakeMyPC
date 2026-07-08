import os
import glob
import re

def update_sidebar_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Wishlist link
    wishlist_pattern = r'<a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Wishlist ❤️\s*</a>'
    new_wishlist = '<a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Wishlist\n                </a>'
    
    if re.search(wishlist_pattern, content):
        content = re.sub(wishlist_pattern, new_wishlist, content)
    else:
        # Fallback if without emoji
        wishlist_pattern_2 = r'<a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Wishlist\s*</a>'
        new_wishlist_2 = '<a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    Wishlist\n                </a>'
        content = re.sub(wishlist_pattern_2, new_wishlist_2, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_wishlist():
    # Base layout from admin-customers.html
    base_file = 'admin-customers.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    # We need to replace the content of <main> with the new Wishlist UI.
    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    wishlist_content = """
        <div class="flex flex-col h-full relative">
            <div class="absolute inset-0 bg-electric-blue/5 blur-[120px] rounded-full pointer-events-none"></div>
            
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div>
                    <h2 class="text-headline-lg font-bold text-white mb-2">Wishlist</h2>
                    <p class="text-on-surface-variant">View and manage all wishlist items saved by customers.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">download</span>
                        Export Wishlist
                    </button>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-sm">local_offer</span>
                        Send Offer / Discount
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-primary text-on-primary hover:bg-primary/90 transition-colors text-sm flex items-center gap-2 font-medium">
                        <span class="material-symbols-outlined text-sm">filter_list</span>
                        Filter
                    </button>
                </div>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-4 gap-6 mb-8 relative z-10">
                <div class="glass-card p-6 rounded-2xl flex items-center gap-4 border border-white/5">
                    <div class="w-12 h-12 rounded-xl bg-[#52358C]/30 text-[#B794F6] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined">favorite</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">TOTAL WISHLIST ITEMS</p>
                        <h3 class="text-2xl font-bold text-white mb-1">2,847</h3>
                        <p class="text-xs text-on-surface-variant">All time items</p>
                    </div>
                </div>
                <div class="glass-card p-6 rounded-2xl flex items-center gap-4 border border-white/5">
                    <div class="w-12 h-12 rounded-xl bg-[#1B5038]/30 text-[#68D391] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined">group</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">CUSTOMERS</p>
                        <h3 class="text-2xl font-bold text-white mb-1">1,256</h3>
                        <p class="text-xs text-on-surface-variant">Unique customers</p>
                    </div>
                </div>
                <div class="glass-card p-6 rounded-2xl flex items-center gap-4 border border-white/5">
                    <div class="w-12 h-12 rounded-xl bg-[#7C4A15]/30 text-[#F6AD55] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined">shopping_cart</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">AVG ITEMS PER CUSTOMER</p>
                        <h3 class="text-2xl font-bold text-white mb-1">2.27</h3>
                        <p class="text-xs text-on-surface-variant">Average items</p>
                    </div>
                </div>
                <div class="glass-card p-6 rounded-2xl flex items-center gap-4 border border-white/5">
                    <div class="w-12 h-12 rounded-xl bg-[#1A4B8C]/30 text-[#63B3ED] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined">currency_rupee</span>
                    </div>
                    <div>
                        <p class="text-[10px] text-on-surface-variant uppercase tracking-wider mb-1 font-semibold">POTENTIAL VALUE</p>
                        <h3 class="text-2xl font-bold text-white mb-1">₹ 3,85,42,600</h3>
                        <p class="text-xs text-on-surface-variant">Total value of all wishlists</p>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex justify-between items-center mb-6 relative z-10">
                <div class="flex gap-4 flex-1 max-w-4xl">
                    <div class="relative flex-1 max-w-[300px]">
                        <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]">search</span>
                        <input type="text" placeholder="Search by product name, customer..." class="w-full bg-surface-container-highest/50 border border-white/5 rounded-lg pl-11 pr-4 py-2 text-sm focus:outline-none focus:border-primary/50 transition-colors text-white placeholder-on-surface-variant/50">
                    </div>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-40">
                        <option>All Categories</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-40">
                        <option>All Customers</option>
                    </select>
                    <select class="bg-surface-container-highest/50 border border-white/5 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-primary/50 transition-colors text-white appearance-none w-40">
                        <option>All Status</option>
                    </select>
                    <button class="px-4 py-2 rounded-lg border border-white/5 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white bg-surface-container-highest/50">
                        <span class="material-symbols-outlined text-[18px]">filter_alt</span>
                        More Filters
                    </button>
                </div>
                <div class="flex gap-2 bg-surface-container-highest/50 rounded-lg p-1 border border-white/5">
                    <button class="p-1 rounded bg-primary text-on-primary transition-colors flex"><span class="material-symbols-outlined text-[18px] block">view_list</span></button>
                    <button class="p-1 rounded hover:bg-white/5 text-on-surface-variant transition-colors flex"><span class="material-symbols-outlined text-[18px] block">grid_view</span></button>
                </div>
            </div>

            <!-- Content Area (Table + Sidebar) -->
            <div class="flex gap-6 flex-1 min-h-0 relative z-10">
                
                <!-- Table -->
                <div class="glass-card rounded-xl flex-1 flex flex-col overflow-hidden border border-white/5">
                    <div class="overflow-y-auto custom-scrollbar flex-1">
                        <table class="w-full text-left text-sm border-collapse">
                            <thead class="sticky top-0 bg-surface-deep text-[10px] uppercase text-on-surface-variant/70 border-b border-white/5 z-10">
                                <tr>
                                    <th class="px-4 py-3 font-medium w-12 text-center"></th>
                                    <th class="px-4 py-3 font-medium tracking-wider">PRODUCT</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">CUSTOMER</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">ADDED ON</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">PRICE</th>
                                    <th class="px-4 py-3 font-medium tracking-wider">STATUS</th>
                                    <th class="px-4 py-3 font-medium tracking-wider text-right">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5 text-xs">
                                <!-- Row 1 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-4 text-on-surface-variant/50 text-center"><span class="material-symbols-outlined text-[16px]">favorite_border</span></td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-10 h-10 rounded-lg bg-white p-1 shrink-0">
                                                <img src="https://m.media-amazon.com/images/I/51r26P2wSCL._SL1000_.jpg" alt="CPU" class="w-full h-full object-contain mix-blend-multiply">
                                            </div>
                                            <div>
                                                <p class="font-medium text-white line-clamp-1 text-sm">AMD Ryzen 7 7800X3D</p>
                                                <p class="text-[11px] text-on-surface-variant mt-0.5">Processor</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=1" class="w-7 h-7 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-xs">Rahul Verma</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">rahul@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <p class="text-white text-xs">12 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">10:30 AM</p>
                                    </td>
                                    <td class="px-4 py-4 font-medium text-white text-sm">₹ 33,990</td>
                                    <td class="px-4 py-4">
                                        <span class="px-2 py-0.5 rounded text-[#68D391] text-[11px] font-medium border border-[#68D391]/20">In Stock</span>
                                    </td>
                                    <td class="px-4 py-4 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="View Details">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="Send Email">
                                                <span class="material-symbols-outlined text-[16px]">mail</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 2 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-4 text-on-surface-variant/50 text-center"><span class="material-symbols-outlined text-[16px]">favorite_border</span></td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-10 h-10 rounded-lg bg-white p-1 shrink-0">
                                                <img src="https://m.media-amazon.com/images/I/71R21K29BvL._SL1500_.jpg" alt="GPU" class="w-full h-full object-contain mix-blend-multiply">
                                            </div>
                                            <div>
                                                <p class="font-medium text-white line-clamp-1 text-sm">MSI GeForce RTX 4070 Ti Super</p>
                                                <p class="text-[11px] text-on-surface-variant mt-0.5">Graphics Card</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=2" class="w-7 h-7 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-xs">Priya Sharma</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">priya@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <p class="text-white text-xs">11 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">04:15 PM</p>
                                    </td>
                                    <td class="px-4 py-4 font-medium text-white text-sm">₹ 79,999</td>
                                    <td class="px-4 py-4">
                                        <span class="px-2 py-0.5 rounded text-[#68D391] text-[11px] font-medium border border-[#68D391]/20">In Stock</span>
                                    </td>
                                    <td class="px-4 py-4 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="View Details">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="Send Email">
                                                <span class="material-symbols-outlined text-[16px]">mail</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                <!-- Row 3 -->
                                <tr class="hover:bg-white/5 transition-colors group">
                                    <td class="px-4 py-4 text-on-surface-variant/50 text-center"><span class="material-symbols-outlined text-[16px]">favorite_border</span></td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-10 h-10 rounded-lg bg-white p-1 shrink-0">
                                                <img src="https://m.media-amazon.com/images/I/61kM5FhJ71L._SL1000_.jpg" alt="Mobo" class="w-full h-full object-contain mix-blend-multiply">
                                            </div>
                                            <div>
                                                <p class="font-medium text-white line-clamp-1 text-sm">ASUS TUF B650-PLUS WIFI</p>
                                                <p class="text-[11px] text-on-surface-variant mt-0.5">Motherboard</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <div class="flex items-center gap-2">
                                            <img src="https://i.pravatar.cc/150?u=3" class="w-7 h-7 rounded-full">
                                            <div>
                                                <p class="font-medium text-white text-xs">Amit Singh</p>
                                                <p class="text-[10px] text-on-surface-variant mt-0.5">amit@example.com</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-4 py-4">
                                        <p class="text-white text-xs">10 May 2024</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">11:20 AM</p>
                                    </td>
                                    <td class="px-4 py-4 font-medium text-white text-sm">₹ 18,499</td>
                                    <td class="px-4 py-4">
                                        <span class="px-2 py-0.5 rounded text-[#F6AD55] text-[11px] font-medium border border-[#F6AD55]/20">Low Stock</span>
                                    </td>
                                    <td class="px-4 py-4 text-right">
                                        <div class="flex items-center justify-end gap-1 opacity-50 group-hover:opacity-100 transition-opacity">
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="View Details">
                                                <span class="material-symbols-outlined text-[16px]">visibility</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors" title="Send Email">
                                                <span class="material-symbols-outlined text-[16px]">mail</span>
                                            </button>
                                            <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant transition-colors">
                                                <span class="material-symbols-outlined text-[16px]">more_horiz</span>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="p-3 border-t border-white/5 bg-surface-deep/50 backdrop-blur flex justify-between items-center text-xs">
                        <p class="text-on-surface-variant">Showing 1 to 8 of 2,847 items</p>
                        <div class="flex gap-1 items-center">
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors disabled:opacity-50 text-white"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                            <button class="w-7 h-7 rounded bg-primary text-on-primary flex items-center justify-center font-medium">1</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">2</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">3</button>
                            <span class="w-7 h-7 flex items-center justify-center text-on-surface-variant">...</span>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white">356</button>
                            <button class="w-7 h-7 rounded flex items-center justify-center hover:bg-white/5 transition-colors text-white"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                            <div class="flex items-center gap-2 ml-4">
                                <span class="text-on-surface-variant">10 / page</span>
                                <span class="material-symbols-outlined text-sm">expand_more</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar -->
                <div class="w-[320px] shrink-0 flex flex-col gap-6 overflow-y-auto custom-scrollbar pr-1">
                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-sm font-medium text-white mb-6">Wishlist Summary</h3>
                        <div class="flex items-center gap-6">
                            <div class="relative w-[110px] h-[110px] shrink-0 rounded-full border-[8px] border-surface-container flex items-center justify-center" style="border-right-color: #68D391; border-top-color: #68D391; border-bottom-color: #F6AD55; border-left-color: #EF4444; transform: rotate(45deg)">
                                <div class="absolute inset-0 flex flex-col items-center justify-center bg-surface-deep rounded-full m-1" style="transform: rotate(-45deg)">
                                    <span class="text-xl font-bold text-white">2,847</span>
                                    <span class="text-[10px] text-on-surface-variant">Total Items</span>
                                </div>
                            </div>
                            <div class="flex-1 space-y-3 text-xs w-full">
                                <div class="flex items-center justify-between w-full">
                                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="w-2 h-2 rounded-full bg-[#68D391]"></span>In Stock</div>
                                    <div class="flex gap-2 text-right"><span class="text-white">2,156</span><span class="text-on-surface-variant/50 w-[40px] text-right inline-block">(75.8%)</span></div>
                                </div>
                                <div class="flex items-center justify-between w-full">
                                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="w-2 h-2 rounded-full bg-[#F6AD55]"></span>Low Stock</div>
                                    <div class="flex gap-2 text-right"><span class="text-white">356</span><span class="text-on-surface-variant/50 w-[40px] text-right inline-block">(12.5%)</span></div>
                                </div>
                                <div class="flex items-center justify-between w-full">
                                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="w-2 h-2 rounded-full bg-[#EF4444]"></span>Out of Stock</div>
                                    <div class="flex gap-2 text-right"><span class="text-white">335</span><span class="text-on-surface-variant/50 w-[40px] text-right inline-block">(11.7%)</span></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-sm font-medium text-white">Top Categories</h3>
                            <a href="#" class="text-xs text-primary hover:underline">View All</a>
                        </div>
                        <div class="space-y-4 text-xs">
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Processors</span>
                                <span class="text-white">612 items</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Graphics Cards</span>
                                <span class="text-white">589 items</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Motherboards</span>
                                <span class="text-white">478 items</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">RAM</span>
                                <span class="text-white">356 items</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-on-surface-variant">Storage</span>
                                <span class="text-white">342 items</span>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-sm font-medium text-white">Top Customers</h3>
                            <a href="#" class="text-xs text-primary hover:underline">View All</a>
                        </div>
                        <div class="space-y-4">
                            <div class="flex items-center gap-3">
                                <img src="https://i.pravatar.cc/150?u=1" class="w-8 h-8 rounded-full">
                                <div class="flex-1 min-w-0">
                                    <p class="text-xs font-medium text-white truncate">Rahul Verma</p>
                                </div>
                                <div class="text-right whitespace-nowrap">
                                    <p class="text-[11px] text-on-surface-variant">32 items</p>
                                </div>
                                <div class="text-right w-16 shrink-0">
                                    <p class="text-[11px] text-white">₹ 2,45,600</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-3">
                                <img src="https://i.pravatar.cc/150?u=2" class="w-8 h-8 rounded-full">
                                <div class="flex-1 min-w-0">
                                    <p class="text-xs font-medium text-white truncate">Priya Sharma</p>
                                </div>
                                <div class="text-right whitespace-nowrap">
                                    <p class="text-[11px] text-on-surface-variant">28 items</p>
                                </div>
                                <div class="text-right w-16 shrink-0">
                                    <p class="text-[11px] text-white">₹ 1,89,750</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-3">
                                <img src="https://i.pravatar.cc/150?u=3" class="w-8 h-8 rounded-full">
                                <div class="flex-1 min-w-0">
                                    <p class="text-xs font-medium text-white truncate">Amit Singh</p>
                                </div>
                                <div class="text-right whitespace-nowrap">
                                    <p class="text-[11px] text-on-surface-variant">24 items</p>
                                </div>
                                <div class="text-right w-16 shrink-0">
                                    <p class="text-[11px] text-white">₹ 1,56,300</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-5 rounded-xl border border-white/5">
                        <h3 class="text-sm font-medium text-white mb-4">Quick Actions</h3>
                        <div class="grid grid-cols-2 gap-2 mb-2">
                            <button class="py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-xs text-on-surface-variant flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">local_offer</span> Send Discount
                            </button>
                            <button class="py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-xs text-on-surface-variant flex items-center justify-center gap-1.5">
                                <span class="material-symbols-outlined text-[14px]">notifications_active</span> Price Drop Alert
                            </button>
                        </div>
                        <button class="w-full py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-xs text-on-surface-variant flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-[14px]">download</span> Export Wishlist
                        </button>
                    </div>
                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-8 h-screen overflow-hidden bg-surface-deep">{wishlist_content}</main>', base_html)
    
    # Remove active state from 'All Customers'
    all_customers_active = r'<a href="admin-customers.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">\s*<div class="absolute -left-\[17px\] top-0 bottom-0 w-\[2px\] bg-primary"></div>\s*All Customers\s*</a>'
    all_customers_inactive = '<a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\n                    All Customers\n                </a>'
    new_html = re.sub(all_customers_active, all_customers_inactive, new_html)
    
    # Add active state to 'Wishlist'
    wishlist_active = """<a href="admin-wishlist.html" class="text-sm text-primary font-medium bg-primary/10 px-4 py-2 rounded-lg relative block">
                    <div class="absolute -left-[17px] top-0 bottom-0 w-[2px] bg-primary"></div>
                    Wishlist
                </a>"""
    wishlist_old = r'<a href="#" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">\s*Wishlist( ❤️)?\s*</a>'
    new_html = re.sub(wishlist_old, wishlist_active, new_html)

    with open('admin-wishlist.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-wishlist.html")

def main():
    html_files = glob.glob('admin-*.html')
    for filepath in html_files:
        if filepath != 'admin-wishlist.html':
            update_sidebar_in_file(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_wishlist()

if __name__ == '__main__':
    main()
