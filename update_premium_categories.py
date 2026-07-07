import re

with open('product-categories.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_sidebar_match = re.search(r'^(.*?)<main class="ml-64 relative">', content, flags=re.DOTALL)
if not head_sidebar_match:
    print("Could not find <main> tag")
    exit(1)

head_sidebar = head_sidebar_match.group(1)

new_main = """<main class="ml-64 relative">
<!-- Content Area -->
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar bg-surface-deep">
    
    <!-- Top Header -->
    <div class="p-gutter border-b border-white/5 pb-6 shrink-0 mt-6 sticky top-0 bg-surface-deep z-20 backdrop-blur-md bg-opacity-90">
        <div class="flex items-end justify-between">
            <div>
                <h2 class="font-headline-lg text-headline-lg text-on-surface">Categories</h2>
                <p class="text-on-surface-variant text-body-sm mt-1">Manage product categories used across PC Builder, Shop and Inventory.</p>
            </div>
            <div class="flex gap-3">
                <button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold">
                    <span class="material-symbols-outlined text-lg">add</span> Add Category
                </button>
            </div>
        </div>

        <!-- Filters Row -->
        <div class="flex items-center gap-4 mt-6">
            <div class="relative w-full max-w-md group flex-1">
                <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant group-focus-within:text-primary transition-colors">search</span>
                <input class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 pl-10 pr-4 text-sm focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all text-on-surface" placeholder="Search Categories..." type="text">
            </div>
            
            <select class="bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select min-w-[150px]">
                <option>Status: All</option>
                <option>Active</option>
                <option>Hidden</option>
            </select>

            <select class="bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select min-w-[150px]">
                <option>Sort By: Order</option>
                <option>Name (A-Z)</option>
                <option>Products (High-Low)</option>
            </select>
        </div>
    </div>

    <div class="p-gutter flex-1 pb-20">
        <!-- Stats Cards -->
        <div class="grid grid-cols-4 gap-4 mb-8">
            <div class="glass-card rounded-xl p-4 flex items-center justify-between border-l-4 border-l-primary/50">
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-1">Total Categories</p>
                    <p class="text-2xl font-bold text-on-surface">18</p>
                </div>
                <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center"><span class="material-symbols-outlined text-primary">category</span></div>
            </div>
            <div class="glass-card rounded-xl p-4 flex items-center justify-between border-l-4 border-l-cyber-teal/50">
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-1">Active</p>
                    <p class="text-2xl font-bold text-on-surface">16</p>
                </div>
                <div class="w-10 h-10 rounded-full bg-cyber-teal/10 flex items-center justify-center"><span class="material-symbols-outlined text-cyber-teal">visibility</span></div>
            </div>
            <div class="glass-card rounded-xl p-4 flex items-center justify-between border-l-4 border-l-surface-variant">
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-1">Hidden</p>
                    <p class="text-2xl font-bold text-on-surface">2</p>
                </div>
                <div class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center"><span class="material-symbols-outlined text-on-surface-variant">visibility_off</span></div>
            </div>
            <div class="glass-card rounded-xl p-4 flex items-center justify-between border-l-4 border-l-tertiary-container/50">
                <div>
                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-1">Total Products</p>
                    <p class="text-2xl font-bold text-on-surface">2,483</p>
                </div>
                <div class="w-10 h-10 rounded-full bg-tertiary-container/10 flex items-center justify-center"><span class="material-symbols-outlined text-tertiary-container">inventory_2</span></div>
            </div>
        </div>

        <!-- Tab Grouping -->
        <div class="flex items-center gap-2 mb-6 border-b border-white/10 pb-2">
            <button class="px-6 py-2 rounded-t-lg border-b-2 border-primary text-primary font-bold text-sm bg-primary/5">🖥️ PC Components</button>
            <button class="px-6 py-2 rounded-t-lg border-b-2 border-transparent text-on-surface-variant hover:text-on-surface hover:bg-white/5 transition-all text-sm font-medium">💻 Devices</button>
            <button class="px-6 py-2 rounded-t-lg border-b-2 border-transparent text-on-surface-variant hover:text-on-surface hover:bg-white/5 transition-all text-sm font-medium">🎮 Accessories</button>
        </div>

        <!-- Data Table Area -->
        <div class="glass-card rounded-2xl overflow-hidden border border-white/5 shadow-2xl">
            <!-- Table Action Bar (Bulk Actions) -->
            <div class="bg-surface-container/50 px-4 py-3 flex items-center justify-between border-b border-white/10">
                <div class="flex items-center gap-4">
                    <input type="checkbox" class="w-4 h-4 rounded bg-surface-deep border-outline-variant text-primary focus:ring-offset-surface-deep cursor-pointer">
                    <div class="flex items-center gap-2 border-l border-white/10 pl-4">
                        <select class="bg-surface-deep border border-outline-variant/30 rounded py-1 px-3 text-xs text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select">
                            <option>Bulk Action</option>
                            <option>Delete</option>
                            <option>Hide</option>
                            <option>Show</option>
                            <option>Export</option>
                        </select>
                        <button class="px-3 py-1 rounded bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-medium text-on-surface transition-colors">Apply</button>
                    </div>
                </div>
                <p class="text-xs text-on-surface-variant">Showing 1–9 of 9 Categories</p>
            </div>

            <!-- The Table -->
            <table class="w-full text-left border-collapse whitespace-nowrap">
                <thead>
                    <tr class="bg-surface-container/30 border-b border-white/5">
                        <th class="w-8 p-3"></th> <!-- Drag -->
                        <th class="w-8 p-3"></th> <!-- Checkbox -->
                        <th class="p-3 text-[10px] text-on-surface-variant font-bold uppercase tracking-widest">Category</th>
                        <th class="p-3 text-[10px] text-on-surface-variant font-bold uppercase tracking-widest text-center">Products</th>
                        <th class="p-3 text-[10px] text-on-surface-variant font-bold uppercase tracking-widest text-center">Status</th>
                        <th class="p-3 text-[10px] text-on-surface-variant font-bold uppercase tracking-widest text-center">Updated</th>
                        <th class="p-3 text-[10px] text-on-surface-variant font-bold uppercase tracking-widest text-right pr-6">Actions</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-white/5 text-sm">
                    
                    <!-- Row 1: CPU -->
                    <tr class="hover:bg-white/5 transition-colors group">
                        <td class="p-3 text-center cursor-move text-on-surface-variant opacity-0 group-hover:opacity-100 transition-opacity"><span class="material-symbols-outlined text-sm">drag_indicator</span></td>
                        <td class="p-3"><input type="checkbox" class="w-4 h-4 rounded bg-surface-deep border-outline-variant text-primary cursor-pointer"></td>
                        <td class="p-3">
                            <div class="flex items-center gap-4">
                                <button class="w-6 h-6 rounded flex items-center justify-center hover:bg-white/10 transition-colors" onclick="toggleRow('row-cpu-sub')"><span class="material-symbols-outlined text-sm text-on-surface-variant transition-transform" id="icon-cpu-sub">chevron_right</span></button>
                                <div class="w-10 h-10 rounded-xl bg-surface-container border border-white/10 flex items-center justify-center text-xl shadow-inner">🧠</div>
                                <div>
                                    <p class="font-bold text-on-surface text-base group-hover:text-primary transition-colors">CPU</p>
                                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest">Desktop Processors</p>
                                </div>
                            </div>
                        </td>
                        <td class="p-3 text-center">
                            <a href="#" class="inline-flex flex-col items-center hover:bg-white/5 px-3 py-1 rounded transition-colors group/link">
                                <span class="font-bold text-on-surface">142</span>
                                <span class="text-[10px] text-primary group-hover/link:underline">View Products →</span>
                            </a>
                        </td>
                        <td class="p-3 text-center">
                            <div class="flex items-center justify-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-cyber-teal shadow-[0_0_8px_#00A4A6]"></span>
                                <button class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-inner transition-all">
                                    <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                                </button>
                            </div>
                        </td>
                        <td class="p-3 text-center text-on-surface-variant text-xs">Today, 10:42 AM</td>
                        <td class="p-3 text-right pr-6 relative">
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors" onclick="openDrawer()"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors ml-1"><span class="material-symbols-outlined text-sm">more_vert</span></button>
                        </td>
                    </tr>
                    
                    <!-- Hidden Sub Row: CPU -->
                    <tr id="row-cpu-sub" class="hidden bg-surface-container-low/30 border-l-2 border-l-primary">
                        <td colspan="7" class="p-0">
                            <div class="pl-24 pr-6 py-2 flex flex-col gap-1">
                                <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0 hover:bg-white/5 px-4 rounded transition-colors">
                                    <div class="flex items-center gap-3">
                                        <div class="w-1.5 h-1.5 rounded-full bg-primary"></div>
                                        <span class="text-sm font-medium text-on-surface">Intel Processors</span>
                                    </div>
                                    <a href="#" class="text-[10px] text-primary hover:underline">82 Products →</a>
                                </div>
                                <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0 hover:bg-white/5 px-4 rounded transition-colors">
                                    <div class="flex items-center gap-3">
                                        <div class="w-1.5 h-1.5 rounded-full bg-primary"></div>
                                        <span class="text-sm font-medium text-on-surface">AMD Processors</span>
                                    </div>
                                    <a href="#" class="text-[10px] text-primary hover:underline">60 Products →</a>
                                </div>
                            </div>
                        </td>
                    </tr>

                    <!-- Row 2: GPU -->
                    <tr class="hover:bg-white/5 transition-colors group">
                        <td class="p-3 text-center cursor-move text-on-surface-variant opacity-0 group-hover:opacity-100 transition-opacity"><span class="material-symbols-outlined text-sm">drag_indicator</span></td>
                        <td class="p-3"><input type="checkbox" class="w-4 h-4 rounded bg-surface-deep border-outline-variant text-primary cursor-pointer"></td>
                        <td class="p-3">
                            <div class="flex items-center gap-4">
                                <button class="w-6 h-6 rounded flex items-center justify-center hover:bg-white/10 transition-colors"><span class="material-symbols-outlined text-sm text-on-surface-variant transition-transform">chevron_right</span></button>
                                <div class="w-10 h-10 rounded-xl bg-surface-container border border-white/10 flex items-center justify-center text-xl shadow-inner">🎮</div>
                                <div>
                                    <p class="font-bold text-on-surface text-base group-hover:text-primary transition-colors">GPU</p>
                                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest">Graphics Cards</p>
                                </div>
                            </div>
                        </td>
                        <td class="p-3 text-center">
                            <a href="#" class="inline-flex flex-col items-center hover:bg-white/5 px-3 py-1 rounded transition-colors group/link">
                                <span class="font-bold text-on-surface">84</span>
                                <span class="text-[10px] text-primary group-hover/link:underline">View Products →</span>
                            </a>
                        </td>
                        <td class="p-3 text-center">
                            <div class="flex items-center justify-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-cyber-teal shadow-[0_0_8px_#00A4A6]"></span>
                                <button class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-inner transition-all">
                                    <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                                </button>
                            </div>
                        </td>
                        <td class="p-3 text-center text-on-surface-variant text-xs">Yesterday</td>
                        <td class="p-3 text-right pr-6 relative">
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors ml-1"><span class="material-symbols-outlined text-sm">more_vert</span></button>
                        </td>
                    </tr>

                    <!-- Row 3: Motherboard -->
                    <tr class="hover:bg-white/5 transition-colors group">
                        <td class="p-3 text-center cursor-move text-on-surface-variant opacity-0 group-hover:opacity-100 transition-opacity"><span class="material-symbols-outlined text-sm">drag_indicator</span></td>
                        <td class="p-3"><input type="checkbox" class="w-4 h-4 rounded bg-surface-deep border-outline-variant text-primary cursor-pointer"></td>
                        <td class="p-3">
                            <div class="flex items-center gap-4">
                                <button class="w-6 h-6 rounded flex items-center justify-center hover:bg-white/10 transition-colors"><span class="material-symbols-outlined text-sm text-on-surface-variant transition-transform">chevron_right</span></button>
                                <div class="w-10 h-10 rounded-xl bg-surface-container border border-white/10 flex items-center justify-center text-xl shadow-inner">🟩</div>
                                <div>
                                    <p class="font-bold text-on-surface text-base group-hover:text-primary transition-colors">Motherboard</p>
                                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest">Mainboards</p>
                                </div>
                            </div>
                        </td>
                        <td class="p-3 text-center">
                            <a href="#" class="inline-flex flex-col items-center hover:bg-white/5 px-3 py-1 rounded transition-colors group/link">
                                <span class="font-bold text-on-surface">112</span>
                                <span class="text-[10px] text-primary group-hover/link:underline">View Products →</span>
                            </a>
                        </td>
                        <td class="p-3 text-center">
                            <div class="flex items-center justify-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-cyber-teal shadow-[0_0_8px_#00A4A6]"></span>
                                <button class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-inner transition-all">
                                    <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                                </button>
                            </div>
                        </td>
                        <td class="p-3 text-center text-on-surface-variant text-xs">2 days ago</td>
                        <td class="p-3 text-right pr-6 relative">
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors ml-1"><span class="material-symbols-outlined text-sm">more_vert</span></button>
                        </td>
                    </tr>
                    
                    <!-- Row 4: SSD -->
                    <tr class="hover:bg-white/5 transition-colors group opacity-60">
                        <td class="p-3 text-center cursor-move text-on-surface-variant opacity-0 group-hover:opacity-100 transition-opacity"><span class="material-symbols-outlined text-sm">drag_indicator</span></td>
                        <td class="p-3"><input type="checkbox" class="w-4 h-4 rounded bg-surface-deep border-outline-variant text-primary cursor-pointer"></td>
                        <td class="p-3">
                            <div class="flex items-center gap-4">
                                <button class="w-6 h-6 rounded flex items-center justify-center hover:bg-white/10 transition-colors invisible"><span class="material-symbols-outlined text-sm text-on-surface-variant transition-transform">chevron_right</span></button>
                                <div class="w-10 h-10 rounded-xl bg-surface-container border border-white/10 flex items-center justify-center text-xl shadow-inner">⚡</div>
                                <div>
                                    <p class="font-bold text-on-surface text-base group-hover:text-primary transition-colors">SSD</p>
                                    <p class="text-[10px] text-on-surface-variant uppercase tracking-widest">NVMe & SATA</p>
                                </div>
                            </div>
                        </td>
                        <td class="p-3 text-center">
                            <a href="#" class="inline-flex flex-col items-center hover:bg-white/5 px-3 py-1 rounded transition-colors group/link">
                                <span class="font-bold text-on-surface">156</span>
                                <span class="text-[10px] text-primary group-hover/link:underline">View Products →</span>
                            </a>
                        </td>
                        <td class="p-3 text-center">
                            <div class="flex items-center justify-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-surface-variant"></span>
                                <button class="w-10 h-5 rounded-full bg-surface-container border border-white/20 flex items-center px-1 transition-all">
                                    <div class="w-3.5 h-3.5 rounded-full bg-white/50 shadow-sm"></div>
                                </button>
                            </div>
                        </td>
                        <td class="p-3 text-center text-on-surface-variant text-xs">Oct 14</td>
                        <td class="p-3 text-right pr-6 relative">
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 rounded hover:bg-white/10 text-on-surface-variant transition-colors ml-1"><span class="material-symbols-outlined text-sm">more_vert</span></button>
                        </td>
                    </tr>

                </tbody>
            </table>

            <!-- Pagination Footer -->
            <div class="bg-surface-container/30 px-6 py-4 flex items-center justify-between border-t border-white/5">
                <p class="text-xs text-on-surface-variant">Showing <strong>1–9</strong> of <strong>9</strong> PC Component Categories</p>
                <div class="flex items-center gap-2">
                    <button class="px-3 py-1 rounded border border-white/10 text-xs font-medium text-on-surface-variant hover:text-on-surface hover:bg-white/5 transition-colors opacity-50 cursor-not-allowed">Previous</button>
                    <button class="w-7 h-7 rounded bg-primary text-on-primary font-bold text-xs flex items-center justify-center">1</button>
                    <button class="px-3 py-1 rounded border border-white/10 text-xs font-medium text-on-surface hover:bg-white/5 transition-colors">Next</button>
                </div>
            </div>

        </div>
    </div>
</div>

<!-- Right Side Drawer (Edit Category) -->
<div id="drawer-overlay" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 opacity-0 pointer-events-none transition-opacity duration-300" onclick="closeDrawer()"></div>

<div id="edit-drawer" class="fixed top-0 right-0 h-screen w-[500px] bg-surface-container shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out border-l border-white/10 flex flex-col">
    
    <div class="px-6 py-5 border-b border-white/5 flex items-center justify-between shrink-0 bg-surface-deep/50 backdrop-blur-md">
        <div>
            <h3 class="font-bold text-lg text-on-surface">Edit Category</h3>
            <p class="text-xs text-on-surface-variant mt-0.5">Editing: CPU</p>
        </div>
        <button class="p-2 rounded-full hover:bg-white/10 transition-colors text-on-surface-variant" onclick="closeDrawer()">
            <span class="material-symbols-outlined">close</span>
        </button>
    </div>

    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-6">
        
        <div>
            <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Category Name</label>
            <input type="text" value="CPU" class="w-full bg-surface-deep border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
        </div>
        
        <div>
            <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Slug</label>
            <input type="text" value="cpu-processors" class="w-full bg-surface-deep border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
            <p class="text-[10px] text-on-surface-variant mt-1">makemypc.com/shop/<span class="text-primary">cpu-processors</span></p>
        </div>

        <div>
            <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Description</label>
            <textarea rows="3" class="w-full bg-surface-deep border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all resize-none">Desktop Processors</textarea>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Icon Emoji</label>
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-lg bg-surface-deep border border-white/10 flex items-center justify-center text-xl">🧠</div>
                    <button class="text-xs text-primary hover:underline">Change</button>
                </div>
            </div>
            <div>
                <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Display Order</label>
                <input type="number" value="1" class="w-full bg-surface-deep border border-outline-variant/30 rounded-lg py-2.5 px-4 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
            </div>
        </div>

        <div>
            <label class="block text-xs font-bold text-on-surface-variant mb-1.5 uppercase tracking-wider">Thumbnail Image</label>
            <div class="w-full h-24 border border-dashed border-white/20 rounded-xl flex flex-col items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-surface-deep">
                <span class="material-symbols-outlined text-xl text-on-surface-variant mb-1">add_photo_alternate</span>
                <p class="text-[10px] text-on-surface-variant">Upload thumbnail</p>
            </div>
        </div>

        <div class="pt-4 border-t border-white/5 space-y-4">
            <h4 class="text-sm font-bold text-on-surface">Visibility Settings</h4>
            
            <label class="flex items-center justify-between cursor-pointer">
                <div>
                    <p class="text-sm text-on-surface font-medium">Show in PC Builder</p>
                    <p class="text-[10px] text-on-surface-variant">Display as a step in the builder engine.</p>
                </div>
                <div class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-inner transition-all">
                    <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                </div>
            </label>

            <label class="flex items-center justify-between cursor-pointer">
                <div>
                    <p class="text-sm text-on-surface font-medium">Show in Shop</p>
                    <p class="text-[10px] text-on-surface-variant">Display in the e-commerce storefront.</p>
                </div>
                <div class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-inner transition-all">
                    <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                </div>
            </label>
        </div>

    </div>

    <div class="p-6 border-t border-white/5 bg-surface-deep shrink-0 flex gap-3">
        <button class="flex-1 py-2.5 rounded-lg border border-white/10 text-on-surface font-medium hover:bg-white/5 transition-all" onclick="closeDrawer()">Cancel</button>
        <button class="flex-1 py-2.5 rounded-lg bg-electric-blue text-white font-bold shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all" onclick="closeDrawer()">Save Changes</button>
    </div>
</div>

</main>
<script>
    function toggleRow(rowId) {
        const row = document.getElementById(rowId);
        const icon = document.getElementById('icon-cpu-sub');
        if(row.classList.contains('hidden')) {
            row.classList.remove('hidden');
            icon.style.transform = 'rotate(90deg)';
        } else {
            row.classList.add('hidden');
            icon.style.transform = 'rotate(0deg)';
        }
    }

    function openDrawer() {
        const drawer = document.getElementById('edit-drawer');
        const overlay = document.getElementById('drawer-overlay');
        drawer.classList.remove('translate-x-full');
        overlay.classList.remove('opacity-0', 'pointer-events-none');
    }

    function closeDrawer() {
        const drawer = document.getElementById('edit-drawer');
        const overlay = document.getElementById('drawer-overlay');
        drawer.classList.add('translate-x-full');
        overlay.classList.add('opacity-0', 'pointer-events-none');
    }
</script>
<script src="js/global.js"></script>
</body>
</html>
"""

with open('product-categories.html', 'w', encoding='utf-8') as f:
    f.write(head_sidebar + new_main)

print("Updated product-categories.html to Premium Admin layout.")
