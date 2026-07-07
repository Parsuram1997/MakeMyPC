import os
import re

# Read template structure
with open("product-management.html", "r", encoding="utf-8") as f:
    template = f.read()

# Extract everything before <main class="ml-64 relative">
# Actually, the sidebar is inside `<aside>`. <main class="ml-64 relative"> is the start of the content.
head_sidebar_match = re.search(r'^(.*?)<main class="ml-64 relative">', template, flags=re.DOTALL)
head_sidebar = head_sidebar_match.group(1) if head_sidebar_match else ""

# -----------------
# 1. Product Add
# -----------------
product_add_content = """<main class="ml-64 relative">
<!-- Content Area -->
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <!-- Header Section -->
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6">
        <div>
            <div class="flex items-center gap-2 mb-2">
                <a href="product-management.html" class="text-on-surface-variant hover:text-primary transition-colors flex items-center"><span class="material-symbols-outlined text-sm">arrow_back</span> Back to Products</a>
            </div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Add New Product</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Create a new product listing in the inventory.</p>
        </div>
        <div class="flex gap-3">
            <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface hover:bg-white/5 transition-all font-medium">Cancel</button>
            <button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all font-bold">Save Product</button>
        </div>
    </div>

    <!-- Form Area -->
    <div class="p-gutter max-w-4xl">
        <div class="glass-card rounded-2xl p-6">
            <div class="grid grid-cols-2 gap-6">
                <div class="col-span-2">
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Product Name</label>
                    <input type="text" placeholder="e.g. AMD Ryzen 9 7950X3D" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-3 px-4 text-on-surface focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all">
                </div>
                <div>
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Category</label>
                    <select class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-3 px-4 text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select">
                        <option>CPU</option>
                        <option>GPU</option>
                        <option>Motherboard</option>
                    </select>
                </div>
                <div>
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Brand</label>
                    <select class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-3 px-4 text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select">
                        <option>AMD</option>
                        <option>Intel</option>
                        <option>NVIDIA</option>
                    </select>
                </div>
                <div>
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Selling Price (₹)</label>
                    <input type="number" placeholder="0" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-3 px-4 text-on-surface focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all">
                </div>
                <div>
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Initial Stock</label>
                    <input type="number" placeholder="0" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-3 px-4 text-on-surface focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all">
                </div>
                <div class="col-span-2">
                    <label class="block text-body-sm text-on-surface-variant mb-1.5 font-medium">Product Images</label>
                    <div class="w-full h-32 border-2 border-dashed border-white/20 rounded-xl flex flex-col items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-white/5">
                        <span class="material-symbols-outlined text-3xl text-on-surface-variant mb-2">cloud_upload</span>
                        <p class="text-body-sm text-on-surface-variant">Click or drag images here to upload</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</main>
<script src="js/global.js"></script>
</body>
</html>
"""

# -----------------
# 2. Product Categories
# -----------------
product_categories_content = """<main class="ml-64 relative">
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6">
        <div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Categories</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Manage hardware categories and hierarchy.</p>
        </div>
        <button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold">
            <span class="material-symbols-outlined text-lg">add</span> Add Category
        </button>
    </div>

    <div class="p-gutter max-w-5xl">
        <div class="glass-card rounded-2xl overflow-hidden">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="border-b border-white/10 bg-white/5">
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase">Category Name</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase">Total Products</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase">Status</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase text-right">Actions</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-bold text-on-surface">CPU (Processors)</td>
                        <td class="p-4 text-on-surface-variant">142</td>
                        <td class="p-4"><span class="px-2.5 py-1 rounded-full bg-cyber-teal/20 text-cyber-teal text-xs font-bold border border-cyber-teal/30">Active</span></td>
                        <td class="p-4 text-right">
                            <button class="p-1.5 hover:text-primary transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 hover:text-error transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
                        </td>
                    </tr>
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-bold text-on-surface">GPU (Graphics Cards)</td>
                        <td class="p-4 text-on-surface-variant">84</td>
                        <td class="p-4"><span class="px-2.5 py-1 rounded-full bg-cyber-teal/20 text-cyber-teal text-xs font-bold border border-cyber-teal/30">Active</span></td>
                        <td class="p-4 text-right">
                            <button class="p-1.5 hover:text-primary transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 hover:text-error transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
                        </td>
                    </tr>
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-bold text-on-surface">Motherboard</td>
                        <td class="p-4 text-on-surface-variant">112</td>
                        <td class="p-4"><span class="px-2.5 py-1 rounded-full bg-cyber-teal/20 text-cyber-teal text-xs font-bold border border-cyber-teal/30">Active</span></td>
                        <td class="p-4 text-right">
                            <button class="p-1.5 hover:text-primary transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 hover:text-error transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
                        </td>
                    </tr>
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-bold text-on-surface">RAM</td>
                        <td class="p-4 text-on-surface-variant">216</td>
                        <td class="p-4"><span class="px-2.5 py-1 rounded-full bg-cyber-teal/20 text-cyber-teal text-xs font-bold border border-cyber-teal/30">Active</span></td>
                        <td class="p-4 text-right">
                            <button class="p-1.5 hover:text-primary transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 hover:text-error transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</main>
<script src="js/global.js"></script>
</body>
</html>
"""

# -----------------
# 3. Product Brands
# -----------------
product_brands_content = """<main class="ml-64 relative">
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6">
        <div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Brands</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Manage partner brands and storefront pages.</p>
        </div>
        <button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2 font-bold">
            <span class="material-symbols-outlined text-lg">add</span> Add Brand
        </button>
    </div>

    <div class="p-gutter grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        <div class="glass-card rounded-2xl p-6 flex items-center justify-between hover:border-primary/50 transition-colors">
            <div class="flex items-center gap-4">
                <div class="w-16 h-16 rounded-lg bg-white flex items-center justify-center p-2"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Intel_logo_%282020%2C_light_blue%29.svg/1024px-Intel_logo_%282020%2C_light_blue%29.svg.png" class="w-full h-auto"></div>
                <div>
                    <h4 class="font-bold text-on-surface text-lg">Intel</h4>
                    <a href="#" class="text-[10px] uppercase text-primary tracking-widest mt-1 inline-block hover:underline">Edit Brand Page</a>
                </div>
            </div>
            <div class="flex flex-col gap-2">
                <button class="p-1.5 rounded bg-surface-container hover:bg-white/10 text-on-surface-variant transition-colors" title="Upload new logo"><span class="material-symbols-outlined text-sm">upload</span></button>
                <button class="p-1.5 rounded bg-surface-container hover:bg-error/20 hover:text-error text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
            </div>
        </div>

        <div class="glass-card rounded-2xl p-6 flex items-center justify-between hover:border-primary/50 transition-colors">
            <div class="flex items-center gap-4">
                <div class="w-16 h-16 rounded-lg bg-black flex items-center justify-center p-2 border border-white/20"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/AMD_Logo.svg/1024px-AMD_Logo.svg.png" class="w-full h-auto"></div>
                <div>
                    <h4 class="font-bold text-on-surface text-lg">AMD</h4>
                    <a href="#" class="text-[10px] uppercase text-primary tracking-widest mt-1 inline-block hover:underline">Edit Brand Page</a>
                </div>
            </div>
            <div class="flex flex-col gap-2">
                <button class="p-1.5 rounded bg-surface-container hover:bg-white/10 text-on-surface-variant transition-colors" title="Upload new logo"><span class="material-symbols-outlined text-sm">upload</span></button>
                <button class="p-1.5 rounded bg-surface-container hover:bg-error/20 hover:text-error text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
            </div>
        </div>

        <div class="glass-card rounded-2xl p-6 flex items-center justify-between hover:border-primary/50 transition-colors">
            <div class="flex items-center gap-4">
                <div class="w-16 h-16 rounded-lg bg-white flex items-center justify-center p-2"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Nvidia_logo.svg/1024px-Nvidia_logo.svg.png" class="w-full h-auto"></div>
                <div>
                    <h4 class="font-bold text-on-surface text-lg">NVIDIA</h4>
                    <a href="#" class="text-[10px] uppercase text-primary tracking-widest mt-1 inline-block hover:underline">Edit Brand Page</a>
                </div>
            </div>
            <div class="flex flex-col gap-2">
                <button class="p-1.5 rounded bg-surface-container hover:bg-white/10 text-on-surface-variant transition-colors" title="Upload new logo"><span class="material-symbols-outlined text-sm">upload</span></button>
                <button class="p-1.5 rounded bg-surface-container hover:bg-error/20 hover:text-error text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
            </div>
        </div>
    </div>
</div>
</main>
<script src="js/global.js"></script>
</body>
</html>
"""

# -----------------
# 4. Product Inventory
# -----------------
product_inventory_content = """<main class="ml-64 relative">
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6">
        <div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Inventory Matrix</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Detailed view of stock levels, reserved units, and pricing.</p>
        </div>
        <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface hover:bg-white/5 transition-all flex items-center gap-2 font-medium">
            <span class="material-symbols-outlined text-lg">download</span> Export CSV
        </button>
    </div>

    <div class="p-gutter">
        <div class="glass-card rounded-2xl overflow-hidden overflow-x-auto custom-scrollbar">
            <table class="w-full text-left border-collapse whitespace-nowrap">
                <thead>
                    <tr class="border-b border-white/10 bg-white/5">
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase">Product</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase text-right">Total Stock</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase text-right">Reserved</th>
                        <th class="p-4 text-label-mono text-cyber-teal font-bold uppercase text-right">Available</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase">Warehouse</th>
                        <th class="p-4 text-label-mono text-on-surface-variant font-medium uppercase text-right">Purchase (₹)</th>
                        <th class="p-4 text-label-mono text-primary font-bold uppercase text-right">Selling (₹)</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-white/5 text-sm">
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-medium text-on-surface">Intel Core i9-14900K</td>
                        <td class="p-4 text-right">15</td>
                        <td class="p-4 text-right text-tertiary-container">2</td>
                        <td class="p-4 text-right font-bold text-cyber-teal">13</td>
                        <td class="p-4 text-on-surface-variant">WH-DEL-01</td>
                        <td class="p-4 text-right opacity-60">45,000</td>
                        <td class="p-4 text-right font-bold text-primary">52,000</td>
                    </tr>
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-medium text-on-surface">ASUS ROG Strix RTX 4090</td>
                        <td class="p-4 text-right">3</td>
                        <td class="p-4 text-right text-tertiary-container">1</td>
                        <td class="p-4 text-right font-bold text-cyber-teal">2</td>
                        <td class="p-4 text-on-surface-variant">WH-MUM-02</td>
                        <td class="p-4 text-right opacity-60">1,60,000</td>
                        <td class="p-4 text-right font-bold text-primary">1,85,990</td>
                    </tr>
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-medium text-on-surface">AMD Ryzen 7 7800X3D</td>
                        <td class="p-4 text-right">45</td>
                        <td class="p-4 text-right text-tertiary-container">12</td>
                        <td class="p-4 text-right font-bold text-cyber-teal">33</td>
                        <td class="p-4 text-on-surface-variant">WH-DEL-01</td>
                        <td class="p-4 text-right opacity-60">32,500</td>
                        <td class="p-4 text-right font-bold text-primary">36,800</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</main>
<script src="js/global.js"></script>
</body>
</html>
"""

# -----------------
# 5. Product Compatibility
# -----------------
product_compatibility_content = """<main class="ml-64 relative">
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6">
        <div>
            <div class="flex items-center gap-3 mb-2">
                <span class="px-2 py-1 rounded bg-electric-blue text-white text-[10px] font-bold tracking-widest uppercase shadow-[0_0_10px_#007AFF]">Core Engine</span>
            </div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Compatibility Matrix</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Define hardware relationships for the PC Builder engine.</p>
        </div>
    </div>

    <div class="p-gutter grid grid-cols-12 gap-6 h-[calc(100vh-180px)]">
        <!-- Left Panel: Source Component -->
        <div class="col-span-4 flex flex-col gap-4">
            <div class="glass-card rounded-2xl p-4 flex flex-col h-full border-primary/20">
                <h3 class="text-label-mono text-primary uppercase tracking-widest mb-4">Select Component</h3>
                
                <div class="relative w-full mb-4">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
                    <input type="text" placeholder="Search CPU, Motherboard..." class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2 pl-10 pr-4 text-sm focus:ring-1 focus:ring-primary outline-none transition-all">
                </div>

                <div class="flex-1 overflow-y-auto custom-scrollbar flex flex-col gap-2">
                    <!-- Selected Item -->
                    <div class="p-3 rounded-xl bg-primary/10 border border-primary text-on-surface flex items-center justify-between cursor-pointer">
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-primary">memory</span>
                            <div>
                                <p class="font-bold text-sm">Ryzen 7 9700X</p>
                                <p class="text-[10px] text-primary">CPU • AMD</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Unselected Items -->
                    <div class="p-3 rounded-xl hover:bg-white/5 border border-transparent text-on-surface-variant flex items-center justify-between cursor-pointer transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined">memory</span>
                            <div>
                                <p class="font-bold text-sm">Core i9-14900K</p>
                                <p class="text-[10px] opacity-60">CPU • Intel</p>
                            </div>
                        </div>
                    </div>
                    <div class="p-3 rounded-xl hover:bg-white/5 border border-transparent text-on-surface-variant flex items-center justify-between cursor-pointer transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined">sd_card</span>
                            <div>
                                <p class="font-bold text-sm">Vengeance DDR5 32GB</p>
                                <p class="text-[10px] opacity-60">RAM • Corsair</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Right Panel: Targets -->
        <div class="col-span-8 flex flex-col gap-4">
            <div class="glass-card rounded-2xl p-6 flex flex-col h-full border-white/5">
                <div class="flex items-center justify-between mb-6">
                    <div>
                        <h3 class="text-label-mono text-on-surface-variant uppercase tracking-widest mb-1">Compatible With</h3>
                        <p class="text-xl font-bold text-on-surface flex items-center gap-2">Ryzen 7 9700X <span class="px-2 py-0.5 rounded-full bg-white/10 text-xs font-normal">AM5 Socket</span></p>
                    </div>
                    
                    <select class="bg-surface-container border border-outline-variant/30 rounded-lg py-2 px-3 text-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all appearance-none custom-select">
                        <option>Target: Motherboards</option>
                        <option>Target: RAM</option>
                        <option>Target: Coolers</option>
                    </select>
                </div>

                <div class="grid grid-cols-2 gap-3 flex-1 overflow-y-auto custom-scrollbar content-start">
                    
                    <!-- Compatible Toggle -->
                    <div class="p-4 rounded-xl border border-white/5 bg-white/5 flex items-center justify-between">
                        <div>
                            <p class="font-bold text-on-surface text-sm">B650 Chipset Motherboards</p>
                            <p class="text-xs text-on-surface-variant mt-1">Native Support</p>
                        </div>
                        <button class="w-12 h-6 rounded-full bg-cyber-teal flex items-center px-1 shadow-[0_0_10px_rgba(0,164,166,0.3)] transition-all">
                            <div class="w-4 h-4 rounded-full bg-white ml-auto shadow-sm"></div>
                        </button>
                    </div>

                    <div class="p-4 rounded-xl border border-white/5 bg-white/5 flex items-center justify-between">
                        <div>
                            <p class="font-bold text-on-surface text-sm">X670 Chipset Motherboards</p>
                            <p class="text-xs text-on-surface-variant mt-1">Native Support</p>
                        </div>
                        <button class="w-12 h-6 rounded-full bg-cyber-teal flex items-center px-1 shadow-[0_0_10px_rgba(0,164,166,0.3)] transition-all">
                            <div class="w-4 h-4 rounded-full bg-white ml-auto shadow-sm"></div>
                        </button>
                    </div>

                    <!-- Incompatible Toggle -->
                    <div class="p-4 rounded-xl border border-white/5 bg-surface-deep flex items-center justify-between opacity-60">
                        <div>
                            <p class="font-bold text-on-surface text-sm">H610 Chipset Motherboards</p>
                            <p class="text-xs text-error mt-1">Incompatible Socket</p>
                        </div>
                        <button class="w-12 h-6 rounded-full bg-surface-container border border-white/20 flex items-center px-1 transition-all">
                            <div class="w-4 h-4 rounded-full bg-white/50 shadow-sm"></div>
                        </button>
                    </div>

                    <div class="p-4 rounded-xl border border-white/5 bg-surface-deep flex items-center justify-between opacity-60">
                        <div>
                            <p class="font-bold text-on-surface text-sm">Z790 Chipset Motherboards</p>
                            <p class="text-xs text-error mt-1">Incompatible Socket</p>
                        </div>
                        <button class="w-12 h-6 rounded-full bg-surface-container border border-white/20 flex items-center px-1 transition-all">
                            <div class="w-4 h-4 rounded-full bg-white/50 shadow-sm"></div>
                        </button>
                    </div>

                </div>

            </div>
        </div>
    </div>
</div>
</main>
<script src="js/global.js"></script>
</body>
</html>
"""

# Write to files
files_to_create = {
    "product-add.html": product_add_content,
    "product-categories.html": product_categories_content,
    "product-brands.html": product_brands_content,
    "product-inventory.html": product_inventory_content,
    "product-compatibility.html": product_compatibility_content
}

for filename, content in files_to_create.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(head_sidebar + content)

print("Created all 5 new product management pages.")
