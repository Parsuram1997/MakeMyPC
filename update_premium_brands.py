import re

with open('product-brands.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_sidebar_match = re.search(r'^(.*?)<main class="ml-64 relative">', content, flags=re.DOTALL)
if not head_sidebar_match:
    print("Could not find <main> tag")
    exit(1)

head_sidebar = head_sidebar_match.group(1)

new_main = """<main class="ml-64 relative">
<!-- Content Area -->
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar bg-surface-deep">
    
    <!-- Header -->
    <div class="p-gutter border-b border-white/5 pb-6 shrink-0 mt-6 bg-surface-deep">
        <div class="flex items-end justify-between">
            <div>
                <h2 class="font-headline-lg text-headline-lg text-white font-bold tracking-tight">Brands</h2>
                <p class="text-on-surface-variant text-sm mt-1">Manage all partner brands and storefront pages.</p>
            </div>
            <div class="flex gap-3">
                <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface hover:bg-white/5 transition-all flex items-center gap-2 font-medium text-sm">
                    <span class="material-symbols-outlined text-lg">cloud_upload</span> Import Brands
                </button>
                <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface hover:bg-white/5 transition-all flex items-center gap-2 font-medium text-sm">
                    <span class="material-symbols-outlined text-lg">download</span> Export Brands
                </button>
                <button class="px-5 py-2.5 rounded-lg bg-primary text-white shadow-lg shadow-primary/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold text-sm">
                    <span class="material-symbols-outlined text-lg">add</span> Add Brand
                </button>
            </div>
        </div>

        <!-- 5 KPI Cards -->
        <div class="grid grid-cols-5 gap-4 mt-6">
            <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-blue-500 text-2xl">inventory_2</span>
                </div>
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Brands</p>
                    <p class="text-2xl font-bold text-white">24</p>
                    <p class="text-[10px] text-on-surface-variant mt-1">All registered brands</p>
                </div>
            </div>
            <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-green-500/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-green-500 text-2xl">check_circle</span>
                </div>
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Active Brands</p>
                    <p class="text-2xl font-bold text-white">20</p>
                    <p class="text-[10px] text-on-surface-variant mt-1">Listed on storefront</p>
                </div>
            </div>
            <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-yellow-500/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-yellow-500 text-2xl">visibility_off</span>
                </div>
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Hidden Brands</p>
                    <p class="text-2xl font-bold text-white">4</p>
                    <p class="text-[10px] text-on-surface-variant mt-1">Not visible on site</p>
                </div>
            </div>
            <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-purple-500/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-purple-500 text-2xl">sell</span>
                </div>
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Products</p>
                    <p class="text-2xl font-bold text-white">2,483</p>
                    <p class="text-[10px] text-on-surface-variant mt-1">Across all brands</p>
                </div>
            </div>
            <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-primary text-2xl">emoji_events</span>
                </div>
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Top Brand</p>
                    <p class="text-xl font-bold text-white leading-tight">ASUS</p>
                    <p class="text-[10px] text-on-surface-variant mt-1">412 Products</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content Area -->
    <div class="p-gutter flex-1 pb-20 flex flex-col gap-6">
        
        <!-- Filter Bar -->
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-4">
                <div class="relative">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-lg">search</span>
                    <input type="text" placeholder="Search brands..." class="bg-surface-container border border-white/10 rounded-lg pl-10 pr-4 py-2 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary w-64 transition-all">
                </div>
                
                <div class="relative group">
                    <button class="bg-surface-container border border-white/10 rounded-lg px-4 py-2 text-sm text-on-surface flex items-center gap-2 hover:border-white/20 transition-colors">
                        Status: All <span class="material-symbols-outlined text-sm">expand_more</span>
                    </button>
                </div>

                <div class="relative group">
                    <button class="bg-surface-container border border-white/10 rounded-lg px-4 py-2 text-sm text-on-surface flex items-center gap-2 hover:border-white/20 transition-colors">
                        Sort: A - Z <span class="material-symbols-outlined text-sm">expand_more</span>
                    </button>
                </div>

                <div class="relative group">
                    <button class="bg-surface-container border border-white/10 rounded-lg px-4 py-2 text-sm text-on-surface flex items-center gap-2 hover:border-white/20 transition-colors">
                        <span class="material-symbols-outlined text-sm text-yellow-500">star</span> Featured <span class="material-symbols-outlined text-sm">expand_more</span>
                    </button>
                </div>
            </div>

            <div class="flex bg-surface-container border border-white/10 rounded-lg p-1">
                <button class="p-1.5 rounded bg-primary text-white shadow"><span class="material-symbols-outlined text-sm block">grid_view</span></button>
                <button class="p-1.5 rounded text-on-surface-variant hover:text-white"><span class="material-symbols-outlined text-sm block">view_list</span></button>
            </div>
        </div>

        <!-- Data Table -->
        <div class="bg-surface-container border border-white/5 rounded-xl overflow-hidden flex-1">
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="border-b border-white/5 text-[10px] uppercase tracking-widest text-on-surface-variant bg-white/[0.02]">
                            <th class="p-4 w-12 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </th>
                            <th class="py-4 px-2 font-bold">Brand</th>
                            <th class="py-4 px-4 font-bold">Country</th>
                            <th class="py-4 px-4 font-bold">Products</th>
                            <th class="py-4 px-4 font-bold">Status</th>
                            <th class="py-4 px-4 font-bold">Featured</th>
                            <th class="py-4 px-4 font-bold">Last Updated</th>
                            <th class="py-4 px-4 font-bold text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-white/5 text-sm">
                        <!-- ASUS -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-black/40 border border-white/10 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-white text-lg italic tracking-tighter">ASUS</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">ASUS</div>
                                        <div class="text-xs text-on-surface-variant">In Search of Incredible</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇹🇼</span>
                                    <span class="text-xs font-medium text-on-surface">Taiwan</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">412</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-yellow-500/30 bg-yellow-500/10 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="text-[11px] text-yellow-500 font-medium">Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">Today, 10:42 AM</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- MSI -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-black/40 border border-white/10 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-white text-lg tracking-widest text-red-500">msi</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">MSI</div>
                                        <div class="text-xs text-on-surface-variant">Gaming Redefined</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇹🇼</span>
                                    <span class="text-xs font-medium text-on-surface">Taiwan</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">298</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-white/10 bg-white/5 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-on-surface-variant" style="font-variation-settings: 'FILL' 0;">star</span>
                                    <span class="text-[11px] text-on-surface-variant font-medium">Not Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">Yesterday, 04:21 PM</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- GIGABYTE -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-black/40 border border-white/10 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-white text-xs tracking-tighter">GIGABYTE</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">GIGABYTE</div>
                                        <div class="text-xs text-on-surface-variant">Upgrade Your Life</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇹🇼</span>
                                    <span class="text-xs font-medium text-on-surface">Taiwan</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">256</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-yellow-500/30 bg-yellow-500/10 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="text-[11px] text-yellow-500 font-medium">Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">2 days ago</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- Intel -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-blue-500/10 border border-blue-500/20 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-blue-400 text-lg">intel</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">Intel</div>
                                        <div class="text-xs text-on-surface-variant">Intel. Innovation Built-In</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇺🇸</span>
                                    <span class="text-xs font-medium text-on-surface">USA</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">186</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-yellow-500/30 bg-yellow-500/10 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="text-[11px] text-yellow-500 font-medium">Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">3 days ago</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- AMD -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-black/40 border border-white/10 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-white text-lg">AMD</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">AMD</div>
                                        <div class="text-xs text-on-surface-variant">together we advance_</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇺🇸</span>
                                    <span class="text-xs font-medium text-on-surface">USA</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">174</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-white/10 bg-white/5 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-on-surface-variant" style="font-variation-settings: 'FILL' 0;">star</span>
                                    <span class="text-[11px] text-on-surface-variant font-medium">Not Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">5 days ago</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- NVIDIA -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-[#76b900]/10 border border-[#76b900]/20 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-[#76b900] text-[10px] tracking-widest uppercase">NVIDIA</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">NVIDIA</div>
                                        <div class="text-xs text-on-surface-variant">The Way It's Meant To Be Played</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇺🇸</span>
                                    <span class="text-xs font-medium text-on-surface">USA</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">162</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-green-500 w-12">Active</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer" checked>
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-yellow-500/30 bg-yellow-500/10 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="text-[11px] text-yellow-500 font-medium">Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">1 week ago</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- Corsair -->
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="p-4 text-center">
                                <input type="checkbox" class="rounded bg-black/20 border-white/20 text-primary focus:ring-primary/50 focus:ring-offset-0">
                            </td>
                            <td class="py-3 px-2">
                                <div class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-lg bg-black/40 border border-white/10 flex items-center justify-center p-2 shrink-0">
                                        <span class="font-bold text-yellow-500 text-[10px] tracking-widest uppercase">CORSAIR</span>
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-base">CORSAIR</div>
                                        <div class="text-xs text-on-surface-variant">Precision for Winners</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-2 bg-white/5 px-2.5 py-1 rounded-full w-max border border-white/10">
                                    <span class="text-base">🇺🇸</span>
                                    <span class="text-xs font-medium text-on-surface">USA</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="font-bold text-white text-base">132</div>
                                <a href="#" class="text-[11px] text-primary hover:underline">View Products</a>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold text-red-500 w-12">Hidden</span>
                                    <label class="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" class="sr-only peer">
                                        <div class="w-9 h-5 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-green-500"></div>
                                    </label>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center gap-1.5 border border-white/10 bg-white/5 px-2 py-1 rounded w-max">
                                    <span class="material-symbols-outlined text-[14px] text-on-surface-variant" style="font-variation-settings: 'FILL' 0;">star</span>
                                    <span class="text-[11px] text-on-surface-variant font-medium">Not Featured</span>
                                </div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="text-sm text-on-surface">1 week ago</div>
                                <div class="text-[11px] text-on-surface-variant">by Admin</div>
                            </td>
                            <td class="py-3 px-4">
                                <div class="flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="View">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="Edit">
                                        <span class="material-symbols-outlined text-[18px]">edit</span>
                                    </button>
                                    <button class="w-8 h-8 rounded-lg hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors" title="More">
                                        <span class="material-symbols-outlined text-[18px]">more_vert</span>
                                    </button>
                                </div>
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
            
            <!-- Bottom Pagination -->
            <div class="border-t border-white/5 px-6 pt-4 pb-10 flex items-center justify-between mt-auto">
                <div class="text-sm text-on-surface-variant">Showing 1 to 10 of 24 brands</div>
                <div class="flex items-center gap-2">
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors disabled:opacity-50"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
                    <button class="w-8 h-8 rounded bg-primary text-white font-medium text-sm">1</button>
                    <button class="w-8 h-8 rounded hover:bg-white/5 text-on-surface font-medium text-sm transition-colors">2</button>
                    <button class="w-8 h-8 rounded hover:bg-white/5 text-on-surface font-medium text-sm transition-colors">3</button>
                    <span class="text-on-surface-variant">...</span>
                    <button class="w-8 h-8 rounded hover:bg-white/5 text-on-surface font-medium text-sm transition-colors">10</button>
                    <button class="w-8 h-8 rounded border border-white/10 flex items-center justify-center text-on-surface hover:bg-white/5 transition-colors"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
                    
                    <div class="ml-4 flex items-center gap-2 border border-white/10 rounded px-2">
                        <select class="bg-transparent border-none text-sm text-on-surface focus:ring-0 py-1.5 pl-2 pr-6 cursor-pointer">
                            <option value="10">10 / page</option>
                            <option value="20">20 / page</option>
                            <option value="50">50 / page</option>
                        </select>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
</main>"""

new_content = head_sidebar + new_main

with open('product-brands.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated product-brands.html to Premium layout.")
