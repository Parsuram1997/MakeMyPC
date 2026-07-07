import re

with open('product-add.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_sidebar_match = re.search(r'^(.*?)<main class="ml-64 relative">', content, flags=re.DOTALL)
if not head_sidebar_match:
    print("Could not find <main> tag")
    exit(1)

head_sidebar = head_sidebar_match.group(1)

new_main = """<main class="ml-64 relative">
<!-- Content Area -->
<div class="flex-1 overflow-y-auto h-screen flex flex-col custom-scrollbar">
    <!-- Header Section -->
    <div class="p-gutter flex items-end justify-between border-b border-white/5 pb-6 shrink-0 mt-6 bg-surface-deep z-10 sticky top-0">
        <div>
            <div class="flex items-center gap-2 mb-2">
                <a href="product-management.html" class="text-on-surface-variant hover:text-primary transition-colors flex items-center"><span class="material-symbols-outlined text-sm">arrow_back</span> Back to Products</a>
            </div>
            <h2 class="font-headline-lg text-headline-lg text-on-surface">Add New Product</h2>
            <p class="text-on-surface-variant text-body-sm mt-1">Create a new product listing with detailed specifications.</p>
        </div>
        <div class="flex gap-3">
            <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface hover:bg-white/5 transition-all font-medium">Cancel</button>
            <button class="px-5 py-2.5 rounded-lg bg-electric-blue text-white shadow-lg shadow-electric-blue/20 hover:scale-[1.02] active:scale-95 transition-all font-bold">Save Product</button>
        </div>
    </div>

    <!-- Form Area -->
    <div class="p-gutter max-w-5xl mx-auto w-full grid grid-cols-3 gap-6 pb-20">
        
        <!-- Left Column: Basic Info & Specs -->
        <div class="col-span-2 flex flex-col gap-6">
            
            <!-- Basic Information -->
            <div class="glass-card rounded-2xl p-6">
                <h3 class="text-label-mono text-primary uppercase tracking-widest mb-6">Basic Information</h3>
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
                </div>
            </div>

            <!-- Specifications -->
            <div class="glass-card rounded-2xl p-6 border-secondary/20 relative overflow-hidden">
                <div class="absolute top-0 right-0 p-6 flex items-center gap-3">
                    <span class="text-[10px] uppercase tracking-widest text-on-surface-variant">Automatically manage</span>
                    <button class="w-10 h-5 rounded-full bg-cyber-teal flex items-center px-1 shadow-[0_0_10px_rgba(0,164,166,0.3)] transition-all">
                        <div class="w-3.5 h-3.5 rounded-full bg-white ml-auto shadow-sm"></div>
                    </button>
                </div>

                <h3 class="text-label-mono text-secondary uppercase tracking-widest mb-2">Specifications</h3>
                <p class="text-xs text-on-surface-variant mb-6 w-2/3">Turn on "Automatically manage" to let our system fetch standard specs based on the model name.</p>
                
                <div class="grid grid-cols-2 gap-x-6 gap-y-4">
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Socket</label>
                        <input type="text" placeholder="e.g. AM5, LGA 1700" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">TDP</label>
                        <input type="text" placeholder="e.g. 120W" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Clock Speed</label>
                        <input type="text" placeholder="e.g. 4.2 GHz Base / 5.7 GHz Boost" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Memory Type</label>
                        <input type="text" placeholder="e.g. DDR5" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">PCIe Version</label>
                        <input type="text" placeholder="e.g. PCIe 5.0" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Generation</label>
                        <input type="text" placeholder="e.g. 14th Gen, Zen 4" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all">
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Column: Media, Pricing & Inventory -->
        <div class="col-span-1 flex flex-col gap-6">
            
            <!-- Pricing & Inventory -->
            <div class="glass-card rounded-2xl p-6 border-white/5">
                <h3 class="text-label-mono text-tertiary-container uppercase tracking-widest mb-4">Pricing & Inventory</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Selling Price (₹)</label>
                        <div class="relative">
                            <span class="absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant font-bold">₹</span>
                            <input type="number" placeholder="0" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 pl-8 pr-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all font-mono font-bold">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs text-on-surface-variant mb-1 font-medium">Initial Stock</label>
                        <input type="number" placeholder="0" class="w-full bg-surface-container border border-outline-variant/30 rounded-lg py-2.5 px-4 text-body-sm text-on-surface focus:ring-1 focus:ring-primary outline-none transition-all font-mono">
                    </div>
                </div>
            </div>

            <!-- Product Images -->
            <div class="glass-card rounded-2xl p-6 border-white/5">
                <h3 class="text-label-mono text-electric-blue uppercase tracking-widest mb-4">Product Images</h3>
                
                <div class="space-y-4">
                    <!-- Thumbnail -->
                    <div>
                        <p class="text-xs text-on-surface font-bold mb-2 flex justify-between">Thumbnail <span class="text-on-surface-variant font-normal">1:1 Aspect</span></p>
                        <div class="w-full h-24 border border-dashed border-white/20 rounded-xl flex items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-white/5">
                            <span class="material-symbols-outlined text-xl text-on-surface-variant">add_photo_alternate</span>
                        </div>
                    </div>

                    <!-- Gallery -->
                    <div>
                        <p class="text-xs text-on-surface font-bold mb-2">Gallery</p>
                        <div class="w-full h-24 border border-dashed border-white/20 rounded-xl flex flex-col items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-white/5">
                            <span class="material-symbols-outlined text-xl text-on-surface-variant mb-1">collections</span>
                            <p class="text-[10px] text-on-surface-variant">Upload multiple images</p>
                        </div>
                    </div>

                    <!-- 360 & Video -->
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <p class="text-[10px] text-on-surface font-bold mb-1">360 Images</p>
                            <div class="w-full h-16 border border-dashed border-white/20 rounded-lg flex items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-white/5">
                                <span class="material-symbols-outlined text-lg text-on-surface-variant">360</span>
                            </div>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface font-bold mb-1">Videos</p>
                            <div class="w-full h-16 border border-dashed border-white/20 rounded-lg flex items-center justify-center hover:border-primary/50 transition-colors cursor-pointer bg-white/5">
                                <span class="material-symbols-outlined text-lg text-on-surface-variant">smart_display</span>
                            </div>
                        </div>
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

with open('product-add.html', 'w', encoding='utf-8') as f:
    f.write(head_sidebar + new_main)

print("Updated product-add.html with specifications and detailed media sections.")
