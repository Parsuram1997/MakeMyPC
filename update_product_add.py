import os
import re

def update_product_add():
    with open('product-add.html', 'r', encoding='utf-8') as f:
        content = f.read()

    main_pattern = r'(<main[^>]*>).*?(</main>)'
    match = re.search(main_pattern, content, flags=re.DOTALL)
    new_main_content = """
        <!-- Top Header -->
        <header class="flex items-center justify-between px-8 py-6 border-b border-white/10 bg-surface-deep z-10 sticky top-0">
            <div>
                <h2 class="font-headline-sm text-headline-sm font-bold text-white mb-1">Add New Product</h2>
                <p class="text-body-sm text-on-surface-variant">Create a new product listing with detailed specifications.</p>
            </div>
            <div class="flex items-center gap-3">
                <button class="px-5 py-2.5 rounded-lg border border-white/10 text-on-surface-variant hover:text-white hover:bg-white/5 transition-all text-sm font-medium">Cancel</button>
                <button class="px-5 py-2.5 rounded-lg border border-white/10 text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">save</span>
                    Save as Draft
                </button>
                <button class="px-6 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">check</span>
                    Save & Publish
                </button>
            </div>
        </header>

        <div class="p-8 max-w-[1600px] mx-auto">
            
            <!-- 5-Step Stepper -->
            <div class="mb-8 w-full max-w-4xl mx-auto">
                <div class="flex items-center justify-between relative">
                    <div class="absolute left-0 top-4 w-full h-[1px] bg-white/10 -z-10"></div>
                    
                    <!-- Step 1 (Active) -->
                    <div class="flex flex-col items-center gap-3 z-10">
                        <div class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-medium shadow-[0_0_10px_rgba(0,122,255,0.4)]">1</div>
                        <span class="text-xs font-medium text-white">Basic Info</span>
                    </div>
                    
                    <!-- Step 2 -->
                    <div class="flex flex-col items-center gap-3 z-10">
                        <div class="w-8 h-8 rounded-full bg-surface-container border border-white/10 text-on-surface-variant flex items-center justify-center text-sm font-medium">2</div>
                        <span class="text-xs font-medium text-on-surface-variant">Specifications</span>
                    </div>
                    
                    <!-- Step 3 -->
                    <div class="flex flex-col items-center gap-3 z-10">
                        <div class="w-8 h-8 rounded-full bg-surface-container border border-white/10 text-on-surface-variant flex items-center justify-center text-sm font-medium">3</div>
                        <span class="text-xs font-medium text-on-surface-variant">Images & Media</span>
                    </div>
                    
                    <!-- Step 4 -->
                    <div class="flex flex-col items-center gap-3 z-10">
                        <div class="w-8 h-8 rounded-full bg-surface-container border border-white/10 text-on-surface-variant flex items-center justify-center text-sm font-medium">4</div>
                        <span class="text-xs font-medium text-on-surface-variant">Pricing & Inventory</span>
                    </div>
                    
                    <!-- Step 5 -->
                    <div class="flex flex-col items-center gap-3 z-10">
                        <div class="w-8 h-8 rounded-full bg-surface-container border border-white/10 text-on-surface-variant flex items-center justify-center text-sm font-medium">5</div>
                        <span class="text-xs font-medium text-on-surface-variant">Review & Publish</span>
                    </div>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                
                <!-- LEFT COLUMN (Main Form) -->
                <div class="lg:col-span-2 space-y-6">
                    
                    <!-- Form Container -->
                    <div class="bg-surface-container rounded-xl border border-white/5 overflow-hidden">
                        
                        <!-- Inner Tabs -->
                        <div class="flex items-center gap-6 px-6 pt-4 border-b border-white/5">
                            <button class="text-sm font-medium text-primary border-b-2 border-primary pb-3 px-1">Basic Information</button>
                            <button class="text-sm font-medium text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Description</button>
                            <button class="text-sm font-medium text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">SEO</button>
                            <button class="text-sm font-medium text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Shipping</button>
                            <button class="text-sm font-medium text-on-surface-variant hover:text-white pb-3 px-1 transition-colors">Other</button>
                        </div>
                        
                        <div class="p-6 space-y-6">
                            
                            <!-- Name & SKU -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant flex items-center justify-between">
                                        <span>Product Name <span class="text-red-500">*</span></span>
                                        <span class="text-[10px]">0/120</span>
                                    </label>
                                    <input type="text" placeholder="e.g. AMD Ryzen 9 7950X3D" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                </div>
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant flex items-center justify-between">
                                        <span>SKU (Stock Keeping Unit) <span class="text-red-500">*</span></span>
                                        <span class="text-[10px]">0/40</span>
                                    </label>
                                    <input type="text" placeholder="e.g. AMD-R9-7950X3D" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                </div>
                            </div>

                            <!-- Cat, Subcat, Brand -->
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant">Category <span class="text-red-500">*</span></label>
                                    <div class="relative">
                                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-lg">memory</span>
                                        <select class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg pl-10 pr-10 py-2.5 text-sm text-white appearance-none focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all cursor-pointer">
                                            <option>CPU</option>
                                            <option>GPU</option>
                                            <option>Motherboard</option>
                                        </select>
                                        <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-sm">expand_more</span>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant">Sub Category</label>
                                    <div class="relative">
                                        <select class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 pr-10 py-2.5 text-sm text-white/50 appearance-none focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all cursor-pointer">
                                            <option>Select Sub Category</option>
                                        </select>
                                        <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-sm">expand_more</span>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant">Brand <span class="text-red-500">*</span></label>
                                    <div class="relative">
                                        <div class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 rounded-full bg-[#000] border border-[#76B900] flex items-center justify-center overflow-hidden">
                                            <span class="text-[8px] font-bold text-[#76B900] whitespace-nowrap">AMD</span>
                                        </div>
                                        <select class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg pl-10 pr-10 py-2.5 text-sm text-white appearance-none focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all cursor-pointer">
                                            <option>AMD</option>
                                            <option>Intel</option>
                                            <option>NVIDIA</option>
                                        </select>
                                        <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-sm">expand_more</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Short Title & Tags -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant flex items-center justify-between">
                                        <span>Short Title</span>
                                        <span class="text-[10px]">0/160</span>
                                    </label>
                                    <input type="text" placeholder="e.g. 16-Core 32-Thread Desktop Processor" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                </div>
                                <div class="space-y-2">
                                    <label class="text-xs font-medium text-on-surface-variant flex items-center justify-between">
                                        <span>Tags</span>
                                        <span class="text-[10px]">0/200</span>
                                    </label>
                                    <input type="text" placeholder="Enter tags and press Enter" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                </div>
                            </div>

                            <!-- Highlights -->
                            <div class="space-y-2">
                                <label class="text-xs font-medium text-on-surface-variant flex items-center justify-between">
                                    <span>Product Highlights</span>
                                    <span class="text-[10px]">0/300</span>
                                </label>
                                <textarea rows="2" placeholder="e.g. Best for Gaming, Content Creation, High Performance" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-3 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all resize-none"></textarea>
                            </div>

                            <!-- Key Features -->
                            <div class="space-y-3">
                                <label class="text-xs font-medium text-on-surface-variant block">Key Features</label>
                                <div class="space-y-2">
                                    <!-- Feature Row -->
                                    <div class="flex items-center gap-3">
                                        <span class="material-symbols-outlined text-white/20 cursor-grab text-lg">drag_indicator</span>
                                        <input type="text" placeholder="Enter key feature" class="flex-1 bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                    </div>
                                    <!-- Feature Row -->
                                    <div class="flex items-center gap-3">
                                        <span class="material-symbols-outlined text-white/20 cursor-grab text-lg">drag_indicator</span>
                                        <input type="text" placeholder="Enter key feature" class="flex-1 bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                    </div>
                                    <!-- Feature Row -->
                                    <div class="flex items-center gap-3">
                                        <span class="material-symbols-outlined text-white/20 cursor-grab text-lg">drag_indicator</span>
                                        <input type="text" placeholder="Enter key feature" class="flex-1 bg-[#0a0f1c] border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                                    </div>
                                </div>
                                <button class="flex items-center gap-1.5 text-sm font-medium text-primary hover:text-primary-hover transition-colors mt-2">
                                    <span class="material-symbols-outlined text-[18px]">add</span>
                                    Add Feature
                                </button>
                            </div>

                        </div>
                    </div>
                    
                    <!-- Auto Specifications -->
                    <div class="bg-surface-container rounded-xl border border-white/5 p-6">
                        <div class="flex items-start justify-between mb-4">
                            <div>
                                <h3 class="text-sm font-medium text-white flex items-center gap-2">
                                    <span class="material-symbols-outlined text-[#B14EEF] text-[18px]">auto_awesome</span>
                                    Auto Specifications <span class="text-on-surface-variant font-normal">(Optional)</span>
                                </h3>
                                <p class="text-xs text-on-surface-variant mt-1">Turn on to automatically fetch specifications based on the product name.</p>
                            </div>
                            <!-- Toggle -->
                            <div class="w-10 h-5 bg-[#00D084] rounded-full relative cursor-pointer shadow-[0_0_8px_rgba(0,208,132,0.4)]">
                                <div class="w-4 h-4 bg-white rounded-full absolute top-0.5 right-0.5"></div>
                            </div>
                        </div>
                        
                        <div class="flex flex-wrap gap-2 mt-4">
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Socket</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Cores</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Threads</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Base Clock</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Boost Clock</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Cache</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">TDP</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Memory Type</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">PCIe Version</span>
                            <span class="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs text-on-surface-variant">Generation</span>
                        </div>
                    </div>
                    
                    <!-- Bottom Action Buttons -->
                    <div class="flex items-center justify-between pt-2">
                        <button class="px-6 py-2.5 rounded-lg border border-white/10 text-white hover:bg-white/5 transition-all text-sm font-medium">Cancel</button>
                        <button class="px-8 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2">
                            Next
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </button>
                    </div>
                    
                </div>
                
                <!-- RIGHT COLUMN (Side Panels) -->
                <div class="space-y-6">
                    
                    <!-- Pricing Card -->
                    <div class="bg-surface-container rounded-xl border border-white/5 p-5">
                        <h3 class="text-sm font-medium text-white flex items-center gap-2 mb-5">
                            <div class="w-6 h-6 rounded bg-blue-500/10 flex items-center justify-center">
                                <span class="material-symbols-outlined text-blue-500 text-sm">payments</span>
                            </div>
                            Pricing
                        </h3>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">Selling Price (₹) <span class="text-red-500">*</span></label>
                                <input type="text" placeholder="e.g. 52999" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                            </div>
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">MRP (₹)</label>
                                <input type="text" placeholder="e.g. 59999" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                            </div>
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">Cost Price (₹)</label>
                                <input type="text" placeholder="e.g. 45000" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                            </div>
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">Tax Class</label>
                                <div class="relative">
                                    <select class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg pl-3 pr-8 py-2 text-sm text-white appearance-none focus:outline-none focus:border-primary transition-all cursor-pointer">
                                        <option>GST 18%</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-sm">expand_more</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Inventory Card -->
                    <div class="bg-surface-container rounded-xl border border-white/5 p-5">
                        <h3 class="text-sm font-medium text-white flex items-center gap-2 mb-5">
                            <div class="w-6 h-6 rounded bg-green-500/10 flex items-center justify-center">
                                <span class="material-symbols-outlined text-green-500 text-sm">inventory_2</span>
                            </div>
                            Inventory
                        </h3>
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">Initial Stock <span class="text-red-500">*</span></label>
                                <input type="text" placeholder="e.g. 25" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                            </div>
                            <div class="space-y-1.5">
                                <label class="text-xs text-on-surface-variant">Low Stock Alert</label>
                                <input type="text" placeholder="e.g. 5" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg px-3 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                            </div>
                        </div>
                        <div class="space-y-1.5 mb-4">
                            <label class="text-xs text-on-surface-variant">SKU Barcode</label>
                            <div class="relative">
                                <input type="text" placeholder="Scan or enter barcode" class="w-full bg-[#0a0f1c] border border-white/10 rounded-lg pl-3 pr-10 py-2 text-sm text-white placeholder-white/20 focus:outline-none focus:border-primary transition-all">
                                <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm cursor-pointer hover:text-white">qr_code_scanner</span>
                            </div>
                        </div>
                        <label class="flex items-center gap-2 cursor-pointer group">
                            <div class="w-4 h-4 rounded border border-primary bg-primary/20 flex items-center justify-center">
                                <span class="material-symbols-outlined text-[12px] text-primary">check</span>
                            </div>
                            <span class="text-xs text-white group-hover:text-primary transition-colors font-medium">Track Inventory</span>
                        </label>
                    </div>
                    
                    <!-- Product Images Card -->
                    <div class="bg-surface-container rounded-xl border border-white/5 p-5">
                        <div class="flex items-center justify-between mb-5">
                            <h3 class="text-sm font-medium text-white flex items-center gap-2">
                                <div class="w-6 h-6 rounded bg-[#B14EEF]/10 flex items-center justify-center">
                                    <span class="material-symbols-outlined text-[#B14EEF] text-sm">image</span>
                                </div>
                                Product Images
                            </h3>
                            <span class="text-[10px] text-on-surface-variant">0/11 <a href="#" class="text-primary hover:underline">View Guidelines</a></span>
                        </div>
                        
                        <div class="border-2 border-dashed border-white/10 hover:border-primary/50 transition-colors rounded-xl bg-[#0a0f1c] p-6 flex flex-col items-center justify-center text-center gap-3 cursor-pointer">
                            <span class="material-symbols-outlined text-white/20 text-3xl">cloud_upload</span>
                            <div>
                                <p class="text-xs text-white mb-0.5">Drag & drop images here</p>
                                <p class="text-[10px] text-on-surface-variant">or</p>
                            </div>
                            <button class="px-4 py-1.5 rounded-lg border border-primary/30 text-primary text-xs font-medium hover:bg-primary/10 transition-colors">Upload Images</button>
                        </div>
                        
                        <div class="grid grid-cols-4 gap-2 mt-4">
                            <button class="flex flex-col items-center justify-center gap-1 p-2 rounded-lg border border-white/10 bg-white/5 hover:bg-white/10 transition-all group">
                                <span class="material-symbols-outlined text-[16px] text-white group-hover:text-primary transition-colors">image</span>
                                <span class="text-[9px] text-on-surface-variant group-hover:text-white transition-colors text-center leading-tight">Thumbnail<br/>Main image</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1 p-2 rounded-lg border border-white/5 hover:bg-white/5 transition-all group">
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">collections</span>
                                <span class="text-[9px] text-on-surface-variant group-hover:text-white transition-colors text-center leading-tight">Gallery<br/>Add multiple images</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1 p-2 rounded-lg border border-white/5 hover:bg-white/5 transition-all group">
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">360</span>
                                <span class="text-[9px] text-on-surface-variant group-hover:text-white transition-colors text-center leading-tight">360° View<br/>Add 360° images</span>
                            </button>
                            <button class="flex flex-col items-center justify-center gap-1 p-2 rounded-lg border border-white/5 hover:bg-white/5 transition-all group">
                                <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">videocam</span>
                                <span class="text-[9px] text-on-surface-variant group-hover:text-white transition-colors text-center leading-tight">Video<br/>Add product video</span>
                            </button>
                        </div>
                    </div>
                    
                    <!-- Publish Status Card -->
                    <div class="bg-surface-container rounded-xl border border-white/5 p-5">
                        <h3 class="text-sm font-medium text-white flex items-center gap-2 mb-5">
                            <div class="w-6 h-6 rounded bg-[#FFB020]/10 flex items-center justify-center">
                                <span class="material-symbols-outlined text-[#FFB020] text-sm">public</span>
                            </div>
                            Publish Status
                        </h3>
                        
                        <div class="grid grid-cols-2 gap-4">
                            <label class="flex items-start gap-3 cursor-pointer group">
                                <div class="w-4 h-4 rounded-full border-4 border-primary mt-0.5 shadow-[0_0_8px_rgba(0,122,255,0.4)]"></div>
                                <div>
                                    <p class="text-xs font-medium text-white">Draft</p>
                                    <p class="text-[10px] text-on-surface-variant mt-0.5">Save as draft</p>
                                </div>
                            </label>
                            <label class="flex items-start gap-3 cursor-pointer group">
                                <div class="w-4 h-4 rounded-full border border-white/20 mt-0.5 group-hover:border-white/50 transition-colors"></div>
                                <div>
                                    <p class="text-xs font-medium text-on-surface-variant group-hover:text-white transition-colors">Publish</p>
                                    <p class="text-[10px] text-on-surface-variant/70 mt-0.5">Make it live on site</p>
                                </div>
                            </label>
                        </div>
                        
                        <div class="h-[1px] bg-white/5 my-4"></div>
                        
                        <h4 class="text-xs font-medium text-on-surface-variant mb-4">Visibility</h4>
                        <div class="grid grid-cols-2 gap-4">
                            <label class="flex items-start gap-3 cursor-pointer group">
                                <div class="w-4 h-4 rounded-full border-4 border-primary mt-0.5 shadow-[0_0_8px_rgba(0,122,255,0.4)]"></div>
                                <div>
                                    <p class="text-xs font-medium text-white">Visible</p>
                                    <p class="text-[10px] text-on-surface-variant mt-0.5">Show on website</p>
                                </div>
                            </label>
                            <label class="flex items-start gap-3 cursor-pointer group">
                                <div class="w-4 h-4 rounded-full border border-white/20 mt-0.5 group-hover:border-white/50 transition-colors"></div>
                                <div>
                                    <p class="text-xs font-medium text-on-surface-variant group-hover:text-white transition-colors">Hidden</p>
                                    <p class="text-[10px] text-on-surface-variant/70 mt-0.5">Hide from website</p>
                                </div>
                            </label>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('product-add.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating product-add.html!")

update_product_add()
