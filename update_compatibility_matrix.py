import os
import re

def update_compatibility_matrix():
    with open('product-compatibility.html', 'r', encoding='utf-8') as f:
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
                        Compatibility Matrix
                        <span class="material-symbols-outlined text-sm text-primary cursor-pointer hover:text-white transition-colors">info</span>
                    </h2>
                    <p class="text-on-surface-variant text-sm mt-1">Manage hardware compatibility rules and relationships for PC Builder.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">publish</span> Import Rules
                    </button>
                    <button class="px-4 py-2.5 rounded-lg border border-white/10 text-on-surface hover:text-white hover:bg-white/5 transition-all text-sm font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">download</span> Export Rules
                    </button>
                    <button class="px-5 py-2.5 rounded-lg bg-primary text-white hover:bg-primary-hover transition-all text-sm font-medium shadow-[0_0_15px_rgba(0,122,255,0.3)] flex items-center gap-2 ml-2">
                        <span class="material-symbols-outlined text-[18px]">add</span> Create Rule
                    </button>
                </div>
            </header>

            <div class="px-8 pb-10 flex-1 flex flex-col max-w-[1920px] mx-auto w-full">
                
                <!-- 5 KPI Cards -->
                <div class="grid grid-cols-5 gap-4 mt-2">
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center shrink-0 border border-blue-500/20">
                            <span class="material-symbols-outlined text-blue-500 text-xl">view_in_ar</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Total Components</p>
                            <p class="text-2xl font-bold text-white">2,483</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Across all categories</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-green-500/10 flex items-center justify-center shrink-0 border border-green-500/20">
                            <span class="material-symbols-outlined text-green-500 text-xl">verified_user</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Compatibility Rules</p>
                            <p class="text-2xl font-bold text-white">18,620</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Active rules defined</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-yellow-500/10 flex items-center justify-center shrink-0 border border-yellow-500/20">
                            <span class="material-symbols-outlined text-yellow-500 text-xl">account_tree</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Compatible Pairs</p>
                            <p class="text-2xl font-bold text-white">45,231</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">Component combinations</p>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-red-500/20 bg-gradient-to-r from-red-500/5 to-transparent flex items-center gap-4 relative overflow-hidden">
                        <div class="w-12 h-12 rounded-lg bg-red-500/20 flex items-center justify-center shrink-0 border border-red-500/30">
                            <span class="material-symbols-outlined text-red-500 text-xl">gpp_bad</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-red-400/80 uppercase tracking-widest font-bold mb-0.5">Conflicts Found</p>
                            <p class="text-2xl font-bold text-white">12</p>
                            <div class="flex items-center gap-2 mt-1">
                                <p class="text-[10px] text-red-400">Require attention</p>
                                <a href="#" class="text-[10px] text-primary hover:underline flex items-center">View Conflicts <span class="material-symbols-outlined text-[10px]">arrow_forward</span></a>
                            </div>
                        </div>
                    </div>
                    <div class="bg-surface-container rounded-xl p-4 border border-white/5 flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg bg-[#B14EEF]/10 flex items-center justify-center shrink-0 border border-[#B14EEF]/20">
                            <span class="material-symbols-outlined text-[#B14EEF] text-xl">smart_toy</span>
                        </div>
                        <div>
                            <p class="text-[10px] text-on-surface-variant uppercase tracking-widest font-bold mb-0.5">Auto Detect Coverage</p>
                            <p class="text-2xl font-bold text-white">98%</p>
                            <p class="text-[10px] text-on-surface-variant mt-1">AI detection accuracy</p>
                        </div>
                    </div>
                </div>

                <!-- Filter Bar -->
                <div class="flex items-center gap-3 mt-6 bg-surface-container border border-white/5 p-3 rounded-xl">
                    <div class="relative w-full max-w-sm group">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm group-focus-within:text-primary transition-colors">search</span>
                        <input class="w-full bg-surface-deep border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white focus:ring-1 focus:ring-primary focus:border-primary outline-none transition-all placeholder-white/20" placeholder="Search component, brand, socket..." type="text">
                    </div>
                    
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Category: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Component Type: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Brand: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    <button class="bg-surface-deep border border-white/5 rounded-lg py-2 px-3 text-xs text-on-surface-variant hover:text-white hover:bg-white/5 transition-all flex items-center gap-2">
                        Rule Type: All <span class="material-symbols-outlined text-sm ml-2">expand_more</span>
                    </button>
                    
                    <div class="flex items-center gap-2 ml-auto">
                        <span class="text-xs text-on-surface-variant font-medium">Auto Detect</span>
                        <!-- Toggle -->
                        <div class="w-10 h-5 bg-primary rounded-full relative cursor-pointer shadow-[0_0_8px_rgba(0,122,255,0.4)]">
                            <div class="w-4 h-4 bg-white rounded-full absolute top-0.5 right-0.5"></div>
                        </div>
                        <span class="material-symbols-outlined text-sm text-on-surface-variant cursor-pointer hover:text-white ml-1">info</span>
                    </div>
                    
                    <div class="flex items-center ml-4 bg-surface-deep border border-white/5 rounded-lg p-0.5">
                        <button class="p-1.5 rounded-md bg-primary/20 text-primary"><span class="material-symbols-outlined text-sm block">grid_view</span></button>
                        <button class="p-1.5 rounded-md text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-sm block">format_list_bulleted</span></button>
                    </div>
                </div>

                <!-- Three Column Dashboard Area -->
                <div class="flex gap-4 mt-6 flex-1 min-h-[600px] items-stretch">
                    
                    <!-- COLUMN 1: Select Component (Left) -->
                    <div class="w-72 shrink-0 flex flex-col gap-4">
                        <h3 class="text-xs font-bold text-white tracking-wider flex items-center">1. SELECT COMPONENT</h3>
                        
                        <div class="bg-surface-container border border-white/5 rounded-xl flex-1 flex flex-col overflow-hidden p-4">
                            <!-- Tabs -->
                            <div class="flex border-b border-white/5 mb-4">
                                <button class="flex-1 text-xs font-medium text-white border-b-2 border-primary pb-2 text-center">By Category</button>
                                <button class="flex-1 text-xs font-medium text-on-surface-variant hover:text-white transition-colors border-b-2 border-transparent pb-2 text-center">By Name/Model</button>
                            </div>
                            
                            <!-- Dropdown -->
                            <div class="relative mb-4">
                                <select class="w-full bg-surface-deep border border-white/10 rounded-lg pl-3 pr-8 py-2 text-xs text-white appearance-none focus:outline-none focus:border-primary transition-all cursor-pointer">
                                    <option>All Categories</option>
                                    <option>CPU</option>
                                    <option>Motherboard</option>
                                </select>
                                <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-sm">expand_more</span>
                            </div>
                            
                            <!-- List -->
                            <div class="flex-1 overflow-y-auto custom-scrollbar -mx-2 px-2 space-y-2">
                                <!-- Active Item -->
                                <div class="bg-primary/10 border border-primary/30 rounded-lg p-3 cursor-pointer group flex items-center justify-between relative overflow-hidden">
                                    <div class="absolute left-0 top-0 bottom-0 w-1 bg-primary"></div>
                                    <div class="flex items-center gap-3 pl-2">
                                        <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-white">
                                            <span class="material-symbols-outlined text-[16px]">memory</span>
                                        </div>
                                        <div>
                                            <p class="text-sm font-bold text-white mb-0.5">Ryzen 7 9700X</p>
                                            <p class="text-[10px] text-on-surface-variant">CPU • AMD • AM5</p>
                                        </div>
                                    </div>
                                    <span class="text-[10px] font-bold text-primary bg-primary/20 px-2 py-0.5 rounded">Active</span>
                                </div>
                                
                                <!-- Inactive Items -->
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">memory</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">Core i9-14900K</p>
                                        <p class="text-[10px] text-on-surface-variant/70">CPU • Intel • LGA1700</p>
                                    </div>
                                </div>
                                
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">visibility</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">RTX 4090</p>
                                        <p class="text-[10px] text-on-surface-variant/70">GPU • NVIDIA</p>
                                    </div>
                                </div>
                                
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">memory_alt</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">Vengeance DDR5 32GB</p>
                                        <p class="text-[10px] text-on-surface-variant/70">RAM • Corsair</p>
                                    </div>
                                </div>
                                
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">developer_board</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">B650 Tomahawk WiFi</p>
                                        <p class="text-[10px] text-on-surface-variant/70">Motherboard • MSI</p>
                                    </div>
                                </div>
                                
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">sim_card</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">Samsung 990 PRO 1TB</p>
                                        <p class="text-[10px] text-on-surface-variant/70">SSD • NVMe</p>
                                    </div>
                                </div>
                                
                                <div class="border border-transparent hover:bg-white/5 rounded-lg p-3 cursor-pointer group flex items-center gap-3 transition-colors">
                                    <div class="w-8 h-8 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">power</span>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-on-surface-variant group-hover:text-white mb-0.5 transition-colors">RM850x 850W</p>
                                        <p class="text-[10px] text-on-surface-variant/70">PSU • Corsair</p>
                                    </div>
                                </div>
                                
                            </div>
                            
                            <button class="w-full py-2.5 rounded-lg border border-white/10 text-primary text-xs font-medium hover:bg-white/5 transition-colors mt-4 flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[16px]">add</span> Add New Component
                            </button>
                        </div>
                    </div>
                    
                    <!-- COLUMN 2: Rules & Matrix (Middle) -->
                    <div class="flex-1 flex flex-col gap-4 min-w-[500px]">
                        
                        <!-- Top Half: Compatibility Rules -->
                        <div class="flex flex-col gap-4">
                            <div class="flex items-center justify-between">
                                <h3 class="text-xs font-bold text-white tracking-wider">2. COMPATIBILITY RULES</h3>
                                <a href="#" class="text-xs font-medium text-primary hover:underline">Edit Rules</a>
                            </div>
                            
                            <div class="bg-surface-container border border-white/5 rounded-xl p-5">
                                
                                <!-- Compatible With -->
                                <h4 class="text-[10px] font-bold text-[#00D084] tracking-widest uppercase mb-3">Compatible With</h4>
                                
                                <div class="space-y-4 mb-6">
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-[#00D084] shadow-[0_0_5px_#00D084]"></div>
                                            <span class="text-xs font-medium text-white">Motherboards (Chipset)</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">B650 <span class="material-symbols-outlined text-[10px]">check</span></span>
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">X670 <span class="material-symbols-outlined text-[10px]">check</span></span>
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">X870 <span class="material-symbols-outlined text-[10px]">check</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">3 Compatible</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-[#00D084] shadow-[0_0_5px_#00D084]"></div>
                                            <span class="text-xs font-medium text-white">Memory (RAM)</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">DDR5 <span class="material-symbols-outlined text-[10px]">check</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">1 Compatible</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-[#00D084] shadow-[0_0_5px_#00D084]"></div>
                                            <span class="text-xs font-medium text-white">Coolers</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">AM5 Air Coolers <span class="material-symbols-outlined text-[10px]">check</span></span>
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">AM5 Liquid Coolers <span class="material-symbols-outlined text-[10px]">check</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">2 Compatible</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-[#00D084] shadow-[0_0_5px_#00D084]"></div>
                                            <span class="text-xs font-medium text-white">Power Supply (Minimum)</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">650W and above <span class="material-symbols-outlined text-[10px]">check</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">1 Compatible</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-[#00D084] shadow-[0_0_5px_#00D084]"></div>
                                            <span class="text-xs font-medium text-white">Cabinet Support</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">ATX <span class="material-symbols-outlined text-[10px]">check</span></span>
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">mATX <span class="material-symbols-outlined text-[10px]">check</span></span>
                                            <span class="px-2 py-1 rounded bg-[#00D084]/10 border border-[#00D084]/20 text-[#00D084] text-[10px] font-medium flex items-center gap-1">Mini ITX <span class="material-symbols-outlined text-[10px]">check</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">3 Compatible</span>
                                    </div>
                                </div>
                                
                                <!-- Not Compatible -->
                                <h4 class="text-[10px] font-bold text-red-500 tracking-widest uppercase mb-3">Not Compatible</h4>
                                
                                <div class="space-y-4 mb-4">
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-red-500 shadow-[0_0_5px_rgba(239,68,68,0.8)]"></div>
                                            <span class="text-xs font-medium text-white">Motherboards (Chipset)</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-red-500/10 border border-red-500/20 text-red-400 text-[10px] font-medium flex items-center gap-1">H610 <span class="material-symbols-outlined text-[10px]">close</span></span>
                                            <span class="px-2 py-1 rounded bg-red-500/10 border border-red-500/20 text-red-400 text-[10px] font-medium flex items-center gap-1">B460 <span class="material-symbols-outlined text-[10px]">close</span></span>
                                            <span class="px-2 py-1 rounded bg-red-500/10 border border-red-500/20 text-red-400 text-[10px] font-medium flex items-center gap-1">X299 <span class="material-symbols-outlined text-[10px]">close</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">3 Incompatible</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 border-b border-white/5 pb-4">
                                        <div class="w-40 shrink-0 flex items-center gap-2">
                                            <div class="w-1.5 h-1.5 rounded-full bg-red-500 shadow-[0_0_5px_rgba(239,68,68,0.8)]"></div>
                                            <span class="text-xs font-medium text-white">Memory (RAM)</span>
                                        </div>
                                        <div class="flex-1 flex flex-wrap gap-2">
                                            <span class="px-2 py-1 rounded bg-red-500/10 border border-red-500/20 text-red-400 text-[10px] font-medium flex items-center gap-1">DDR4 <span class="material-symbols-outlined text-[10px]">close</span></span>
                                        </div>
                                        <span class="text-xs text-on-surface-variant shrink-0">1 Incompatible</span>
                                    </div>
                                </div>
                                
                                <button class="text-[11px] font-medium text-primary hover:underline flex items-center gap-1 mt-2">
                                    <span class="material-symbols-outlined text-[14px]">add</span> Add Custom Rule
                                </button>
                                
                            </div>
                        </div>
                        
                        <!-- Bottom Half: Compatibility Matrix Table -->
                        <div class="bg-surface-container border border-white/5 rounded-xl p-5 flex-1 flex flex-col">
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-xs font-bold text-white tracking-wider uppercase flex items-center gap-2">
                                    Compatibility Matrix (CPU vs Motherboard Chipset)
                                    <span class="material-symbols-outlined text-[14px] text-on-surface-variant cursor-pointer">info</span>
                                </h3>
                                <a href="#" class="text-[11px] font-medium text-primary hover:underline flex items-center gap-1">
                                    View Full Matrix <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                                </a>
                            </div>
                            
                            <div class="overflow-x-auto flex-1">
                                <table class="w-full text-left border-collapse">
                                    <thead>
                                        <tr class="border-b border-white/10">
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider">CPU / Chipset</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">B650</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">X670</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">X870</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">H610</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">B460</th>
                                            <th class="py-3 px-4 text-[10px] font-medium text-on-surface-variant uppercase tracking-wider text-center">X299</th>
                                        </tr>
                                    </thead>
                                    <tbody class="text-xs text-white">
                                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                            <td class="py-3 px-4 font-medium">Ryzen 7 9700X</td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                        </tr>
                                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                            <td class="py-3 px-4 font-medium">Ryzen 5 7600X</td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                        </tr>
                                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                            <td class="py-3 px-4 font-medium">Core i9-14900K</td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                        </tr>
                                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                            <td class="py-3 px-4 font-medium">Core i5-14600K</td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-[#00D084]/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-[#00D084]">check</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                            <td class="py-3 px-4 text-center"><div class="w-5 h-5 rounded-full bg-red-500/20 flex items-center justify-center mx-auto"><span class="material-symbols-outlined text-[12px] text-red-500">close</span></div></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    
                    <!-- COLUMN 3: Live Preview & Issues (Right) -->
                    <div class="w-80 shrink-0 flex flex-col gap-4">
                        
                        <!-- Live Compatibility Preview -->
                        <div class="flex items-center justify-between">
                            <h3 class="text-xs font-bold text-white tracking-wider">3. LIVE COMPATIBILITY PREVIEW</h3>
                            <a href="#" class="text-[11px] font-medium text-primary hover:underline">Clear All</a>
                        </div>
                        
                        <div class="bg-surface-container border border-white/5 rounded-xl p-5 flex flex-col gap-4">
                            <!-- Timeline items -->
                            <div class="relative flex flex-col gap-5 before:absolute before:left-3 before:top-4 before:bottom-4 before:w-[1px] before:bg-white/10">
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">memory</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">CPU</p>
                                        <p class="text-sm font-medium text-white">Ryzen 7 9700X</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">developer_board</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">Motherboard</p>
                                        <p class="text-sm font-medium text-white">MSI B650 Tomahawk WiFi</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">memory_alt</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">RAM</p>
                                        <p class="text-sm font-medium text-white">Corsair Vengeance DDR5 32GB</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">visibility</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">GPU</p>
                                        <p class="text-sm font-medium text-white">ASUS ROG Strix RTX 4090</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">power</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">PSU</p>
                                        <p class="text-sm font-medium text-white">Corsair RM850x 850W</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-6 h-6 rounded bg-surface-deep border border-white/10 flex items-center justify-center shrink-0 z-10 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[14px]">kitchen</span>
                                    </div>
                                    <div class="flex-1 mt-0.5">
                                        <p class="text-[10px] text-on-surface-variant font-medium">Cabinet</p>
                                        <p class="text-sm font-medium text-white">Lian Li Lancool 216</p>
                                    </div>
                                    <div class="w-4 h-4 rounded-full bg-[#00D084]/20 flex items-center justify-center shrink-0 mt-1">
                                        <span class="material-symbols-outlined text-[10px] text-[#00D084]">check</span>
                                    </div>
                                </div>
                                
                            </div>
                            
                            <div class="border-t border-white/5 pt-4 mt-2 flex items-center justify-between">
                                <div>
                                    <p class="text-xs font-medium text-white mb-1 flex items-center gap-2">Overall Compatibility <span class="text-[8px] font-bold tracking-widest text-[#00D084] bg-[#00D084]/10 border border-[#00D084]/20 px-1.5 py-0.5 rounded">COMPATIBLE</span></p>
                                    <p class="text-[10px] text-on-surface-variant flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span> No issues found</p>
                                </div>
                                <span class="text-2xl font-bold text-white">100%</span>
                            </div>
                        </div>
                        
                        <!-- Potential Issues Check -->
                        <div class="bg-[#00D084]/5 border border-[#00D084]/20 rounded-xl p-4 flex items-start gap-3">
                            <div class="w-8 h-8 rounded-lg bg-[#00D084]/20 flex items-center justify-center shrink-0 border border-[#00D084]/30">
                                <span class="material-symbols-outlined text-[#00D084] text-[18px]">gpp_good</span>
                            </div>
                            <div>
                                <h4 class="text-[11px] font-bold text-white tracking-widest uppercase mb-1">POTENTIAL ISSUES CHECK</h4>
                                <p class="text-xs text-[#00D084]/80 leading-relaxed">No potential issues detected.<br/>All selected components are fully compatible.</p>
                            </div>
                        </div>
                        
                        <!-- Recently Added/Updated Rules -->
                        <div class="bg-surface-container border border-white/5 rounded-xl p-5 flex-1">
                            <div class="flex items-center justify-between mb-4">
                                <h4 class="text-[10px] font-bold text-on-surface-variant tracking-widest uppercase">RECENTLY ADDED/UPDATED RULES</h4>
                                <a href="#" class="text-[10px] font-medium text-primary hover:underline flex items-center gap-1">View All <span class="material-symbols-outlined text-[12px]">arrow_forward</span></a>
                            </div>
                            
                            <div class="space-y-4">
                                <div class="flex items-start gap-3">
                                    <div class="w-5 h-5 rounded-full bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                                        <span class="material-symbols-outlined text-[12px] text-primary">update</span>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-xs font-medium text-white">AM5 Socket supports DDR5 memory only</p>
                                        <p class="text-[10px] text-on-surface-variant">Updated by Admin</p>
                                    </div>
                                    <span class="text-[10px] text-on-surface-variant/70 shrink-0">2 hours ago</span>
                                </div>
                                <div class="flex items-start gap-3">
                                    <div class="w-5 h-5 rounded-full bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                                        <span class="material-symbols-outlined text-[12px] text-primary">add</span>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-xs font-medium text-white">RTX 4090 requires minimum 850W PSU</p>
                                        <p class="text-[10px] text-on-surface-variant">Added by Admin</p>
                                    </div>
                                    <span class="text-[10px] text-on-surface-variant/70 shrink-0">1 day ago</span>
                                </div>
                                <div class="flex items-start gap-3">
                                    <div class="w-5 h-5 rounded-full bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                                        <span class="material-symbols-outlined text-[12px] text-primary">update</span>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-xs font-medium text-white">Intel 14th Gen supports LGA1700 only</p>
                                        <p class="text-[10px] text-on-surface-variant">Updated by Admin</p>
                                    </div>
                                    <span class="text-[10px] text-on-surface-variant/70 shrink-0">2 days ago</span>
                                </div>
                                <div class="flex items-start gap-3">
                                    <div class="w-5 h-5 rounded-full bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                                        <span class="material-symbols-outlined text-[12px] text-primary">add</span>
                                    </div>
                                    <div class="flex-1">
                                        <p class="text-xs font-medium text-white">B650 chipset compatible with Ryzen 7000 series</p>
                                        <p class="text-[10px] text-on-surface-variant">Added by Admin</p>
                                    </div>
                                    <span class="text-[10px] text-on-surface-variant/70 shrink-0">3 days ago</span>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
"""

    new_content = content[:match.start(1)] + '<main class="ml-64 relative h-screen">' + new_main_content + '</main>' + content[match.end(2):]
    
    with open('product-compatibility.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done generating product-compatibility.html!")

update_compatibility_matrix()
