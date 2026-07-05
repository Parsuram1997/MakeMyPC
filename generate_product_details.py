import os

HTML_CONTENT = """<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Intel Core i9-14900K | MakeMyPC Premium Builder</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
    
    <script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "primary": "#adc6ff",
                    "on-tertiary-container": "#4c1a00",
                    "inverse-on-surface": "#263046",
                    "secondary-fixed-dim": "#5cd8da",
                    "surface-container-low": "#101b30",
                    "surface-container": "#142034",
                    "primary-fixed-dim": "#adc6ff",
                    "outline-variant": "#414755",
                    "electric-blue": "#007AFF",
                    "background": "#071327",
                    "surface-bright": "#2e394f",
                    "secondary": "#5cd8da",
                    "surface": "#071327",
                    "on-primary-container": "#00285c",
                    "tertiary-container": "#ef6719",
                    "hardware-gray": "#111111",
                    "on-background": "#d7e2ff",
                    "on-tertiary-fixed": "#351000",
                    "tertiary": "#ffb595",
                    "primary-container": "#4b8eff",
                    "surface-tint": "#adc6ff",
                    "surface-container-lowest": "#030e22",
                    "primary-fixed": "#d8e2ff",
                    "on-primary": "#002e69",
                    "on-secondary-fixed": "#002020",
                    "surface-deep": "#00081C",
                    "secondary-container": "#00a4a6",
                    "on-secondary-fixed-variant": "#004f50",
                    "cyber-teal": "#00A4A6",
                    "on-surface": "#d7e2ff",
                    "tertiary-fixed": "#ffdbcc",
                    "error": "#ffb4ab",
                    "on-surface-variant": "#c1c6d7",
                    "on-tertiary-fixed-variant": "#7c2e00",
                    "outline": "#8b90a0",
                    "surface-dim": "#071327",
                    "on-error": "#690005",
                    "on-primary-fixed": "#001a41",
                    "surface-container-highest": "#2a354a",
                    "inverse-primary": "#005bc1",
                    "on-primary-fixed-variant": "#004493",
                    "secondary-fixed": "#7cf5f7",
                    "surface-variant": "#2a354a",
                    "inverse-surface": "#d7e2ff",
                    "on-tertiary": "#571e00",
                    "on-error-container": "#ffdad6",
                    "surface-glass": "rgba(255, 255, 255, 0.03)",
                    "error-container": "#93000a",
                    "on-secondary": "#003738",
                    "on-secondary-container": "#003233",
                    "tertiary-fixed-dim": "#ffb595",
                    "surface-container-high": "#1f2a3f"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "fontFamily": {
                    "body-md": ["Inter"],
                    "body-sm": ["Inter"],
                    "headline-sm": ["Inter"],
                    "headline-lg": ["Inter"],
                    "display-lg": ["Inter"],
                    "label-mono": ["JetBrains Mono"]
            }
          }
        }
      }
    </script>
    <style>
        body {
            background-color: #00081C;
            color: #d7e2ff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 40px 40px -20px rgba(0, 0, 0, 0.3);
        }
        .glow-blue {
            box-shadow: 0 0 30px rgba(0, 122, 255, 0.15);
        }
        .glow-hover:hover {
            box-shadow: 0 0 30px rgba(0, 122, 255, 0.4);
            border-color: rgba(0, 122, 255, 0.5);
        }
        .text-gradient {
            background: linear-gradient(135deg, #adc6ff 0%, #007AFF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Skeleton */
        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }
        .skeleton {
            background: linear-gradient(90deg, rgba(255,255,255,0.05) 25%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0.05) 75%);
            background-size: 1000px 100%;
            animation: shimmer 2s infinite linear;
        }

        /* Sticky Nav Active State */
        .sticky-nav-item.active {
            color: #adc6ff;
            border-bottom: 2px solid #adc6ff;
        }
        
        /* Sticky Panel */
        #sticky-purchase {
            transform: translateY(150%);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        #sticky-purchase.visible {
            transform: translateY(0);
        }
    </style>
</head>
<body class="dark bg-surface-deep text-on-surface">

<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-[#00081C]/80 backdrop-blur-xl border-b border-white/10 shadow-lg">
    <div class="flex justify-between items-center max-w-[1400px] mx-auto px-6 h-20">
        <a href="index.html" class="text-3xl font-black text-on-surface tracking-tighter text-gradient">MakeMyPC</a>
        <div class="hidden md:flex gap-x-8 items-center">
            <a class="text-on-surface-variant font-medium hover:text-primary transition-colors font-label-mono text-sm" href="prebuilt-pcs.html">Shop</a>
            <a class="text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-sm" href="builder-landing.html">Builder</a>
            <a class="text-on-surface-variant font-medium hover:text-primary transition-colors font-label-mono text-sm" href="#">Resources</a>
        </div>
        <div class="flex items-center gap-x-6">
            <div class="relative hidden lg:block">
                <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
                <input class="bg-surface-container border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-sm focus:outline-none focus:border-electric-blue w-64 transition-all placeholder:text-on-surface-variant/50" placeholder="Search Components" type="text"/>
            </div>
            <div class="flex gap-x-4">
                <button class="text-on-surface-variant hover:text-primary transition-colors active:scale-95 relative" onclick="window.location.href='shopping-cart.html'">
                    <span class="material-symbols-outlined">shopping_cart</span>
                </button>
                <a href="account-settings.html" class="text-on-surface-variant hover:text-primary transition-colors active:scale-95">
                    <span class="material-symbols-outlined">account_circle</span>
                </a>
            </div>
        </div>
    </div>
</nav>

<!-- Page Content -->
<main class="pt-24 pb-32 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col gap-12">
    
    <!-- Breadcrumbs -->
    <div class="flex items-center gap-2 text-sm font-label-mono text-on-surface-variant/70 mt-4">
        <a href="#" class="hover:text-primary transition-colors">Components</a>
        <span class="material-symbols-outlined text-[16px]">chevron_right</span>
        <a href="#" class="hover:text-primary transition-colors">Processors</a>
        <span class="material-symbols-outlined text-[16px]">chevron_right</span>
        <a href="#" class="hover:text-primary transition-colors">Intel</a>
        <span class="material-symbols-outlined text-[16px]">chevron_right</span>
        <span class="text-on-surface">Core i9-14900K</span>
    </div>

    <!-- 1. HERO SECTION -->
    <section class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Gallery -->
        <div class="flex flex-col gap-4">
            <div class="glass-card aspect-square rounded-2xl flex items-center justify-center p-12 relative group cursor-zoom-in glow-blue">
                <!-- 360 Badge -->
                <div class="absolute top-4 left-4 bg-white/10 backdrop-blur-md border border-white/20 px-3 py-1 rounded-full flex items-center gap-2 text-xs font-bold text-primary">
                    <span class="material-symbols-outlined text-[16px]">360</span>
                    Interactive View
                </div>
                <img src="images/i9-14900k-box.png" alt="Intel Core i9-14900K" class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-500 drop-shadow-2xl" onerror="this.src='https://placehold.co/600x600/101b30/d7e2ff?text=i9-14900K'"/>
            </div>
            <div class="grid grid-cols-4 gap-4">
                <div class="glass-card aspect-square rounded-xl cursor-pointer border-primary/50 hover:bg-white/5 transition-colors p-4"><img src="https://placehold.co/150x150/101b30/d7e2ff?text=Angle+1" class="w-full h-full object-cover rounded-lg"/></div>
                <div class="glass-card aspect-square rounded-xl cursor-pointer hover:bg-white/5 transition-colors p-4"><img src="https://placehold.co/150x150/101b30/d7e2ff?text=Angle+2" class="w-full h-full object-cover rounded-lg"/></div>
                <div class="glass-card aspect-square rounded-xl cursor-pointer hover:bg-white/5 transition-colors p-4"><img src="https://placehold.co/150x150/101b30/d7e2ff?text=Socket" class="w-full h-full object-cover rounded-lg"/></div>
                <div class="glass-card aspect-square rounded-xl cursor-pointer hover:bg-white/5 transition-colors p-4 flex items-center justify-center">
                    <span class="material-symbols-outlined text-4xl text-on-surface-variant">play_circle</span>
                </div>
            </div>
        </div>
        
        <!-- Product Details -->
        <div class="flex flex-col justify-center">
            <div class="flex items-center gap-3 mb-2">
                <img src="images/intel-logo.png" alt="Intel" class="h-6 object-contain grayscale brightness-200 opacity-80" onerror="this.src='https://placehold.co/80x30/transparent/d7e2ff?text=INTEL'"/>
                <span class="text-xs font-label-mono text-on-surface-variant bg-white/5 px-2 py-1 rounded border border-white/10">SKU: BX8071514900K</span>
            </div>
            
            <h1 class="text-4xl md:text-5xl font-black tracking-tight text-on-surface mb-4 leading-tight">Intel Core i9-14900K <br/><span class="text-primary font-light text-2xl md:text-3xl">24-Core (8P+16E) Processor</span></h1>
            
            <div class="flex items-center gap-4 mb-8">
                <div class="flex text-[#FFB800] text-sm">
                    <span class="material-symbols-outlined filled">star</span>
                    <span class="material-symbols-outlined filled">star</span>
                    <span class="material-symbols-outlined filled">star</span>
                    <span class="material-symbols-outlined filled">star</span>
                    <span class="material-symbols-outlined">star_half</span>
                </div>
                <span class="text-sm text-on-surface-variant font-medium">4.8 (2,104 Reviews)</span>
            </div>

            <!-- Price & Stock -->
            <div class="glass-card rounded-2xl p-6 mb-8 border-l-4 border-l-primary relative overflow-hidden">
                <div class="absolute -right-10 -top-10 w-40 h-40 bg-primary/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="flex flex-col gap-1">
                    <div class="flex items-end gap-3">
                        <span class="text-4xl font-black text-white">₹52,499</span>
                        <span class="text-lg text-on-surface-variant line-through mb-1">₹65,000</span>
                        <span class="bg-error/20 text-error px-2 py-0.5 rounded text-xs font-bold mb-2">-19%</span>
                    </div>
                    <p class="text-xs text-on-surface-variant/70 font-label-mono">Inclusive of all taxes (GST Invoice Available)</p>
                </div>
                
                <div class="mt-6 flex flex-wrap gap-4 text-sm font-medium">
                    <div class="flex items-center gap-2 text-secondary">
                        <span class="material-symbols-outlined text-[18px]">check_circle</span>
                        In Stock
                    </div>
                    <div class="flex items-center gap-2 text-on-surface-variant">
                        <span class="material-symbols-outlined text-[18px]">local_shipping</span>
                        Delivery by Tomorrow, 8 PM
                    </div>
                    <div class="flex items-center gap-2 text-on-surface-variant">
                        <span class="material-symbols-outlined text-[18px]">verified_user</span>
                        3 Years Warranty
                    </div>
                </div>
            </div>

            <!-- Actions -->
            <div class="flex flex-col sm:flex-row gap-4 mb-8">
                <button class="flex-1 bg-primary text-on-primary font-bold py-4 px-6 rounded-xl hover:brightness-110 active:scale-95 transition-all flex items-center justify-center gap-2 shadow-[0_0_20px_rgba(173,198,255,0.3)]">
                    <span class="material-symbols-outlined">build</span>
                    Add to Custom Build
                </button>
                <button class="flex-1 glass-card text-on-surface font-bold py-4 px-6 rounded-xl hover:bg-white/10 active:scale-95 transition-all glow-hover flex items-center justify-center gap-2">
                    <span class="material-symbols-outlined">shopping_bag</span>
                    Buy Now
                </button>
            </div>
            
            <div class="flex gap-6 text-sm font-medium text-on-surface-variant">
                <button class="flex items-center gap-2 hover:text-primary transition-colors">
                    <span class="material-symbols-outlined text-[20px]">compare_arrows</span> Compare
                </button>
                <button class="flex items-center gap-2 hover:text-error transition-colors">
                    <span class="material-symbols-outlined text-[20px]">favorite_border</span> Wishlist
                </button>
                <button class="flex items-center gap-2 hover:text-primary transition-colors">
                    <span class="material-symbols-outlined text-[20px]">share</span> Share
                </button>
            </div>
        </div>
    </section>

    <!-- Navigation Tabs for the rest of the page -->
    <div class="sticky top-20 z-40 bg-[#00081C]/90 backdrop-blur-md border-b border-white/10 py-4 -mx-4 px-4 sm:mx-0 sm:px-0 flex gap-6 overflow-x-auto no-scrollbar font-label-mono text-sm font-bold text-on-surface-variant">
        <a href="#specs" class="sticky-nav-item active whitespace-nowrap px-1 py-2 transition-all">Specifications</a>
        <a href="#performance" class="sticky-nav-item whitespace-nowrap px-1 py-2 hover:text-white transition-all">Performance & Benchmarks</a>
        <a href="#compatibility" class="sticky-nav-item whitespace-nowrap px-1 py-2 hover:text-white transition-all">Compatibility</a>
        <a href="#gallery" class="sticky-nav-item whitespace-nowrap px-1 py-2 hover:text-white transition-all">Gallery & Media</a>
        <a href="#support" class="sticky-nav-item whitespace-nowrap px-1 py-2 hover:text-white transition-all">Support & Reviews</a>
    </div>

    <!-- 2 & 5. SPECIFICATIONS -->
    <section id="specs" class="scroll-mt-40 space-y-8">
        <h2 class="text-2xl font-bold flex items-center gap-3">
            <span class="material-symbols-outlined text-primary">memory</span>
            Technical Specifications
        </h2>
        
        <!-- Quick Specs Chips -->
        <div class="flex flex-wrap gap-3">
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Socket</span>
                <span class="font-bold">LGA 1700</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Cores / Threads</span>
                <span class="font-bold">24 (8P+16E) / 32</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Max Boost</span>
                <span class="font-bold">6.0 GHz</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Base Power (TDP)</span>
                <span class="font-bold">125W</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">L3 Cache</span>
                <span class="font-bold">36 MB</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Memory Support</span>
                <span class="font-bold">DDR5-5600 / DDR4-3200</span>
            </div>
            <div class="glass-card px-4 py-2 rounded-lg flex flex-col">
                <span class="text-[10px] font-label-mono text-on-surface-variant/70 uppercase">Integrated Graphics</span>
                <span class="font-bold">Intel UHD 770</span>
            </div>
        </div>

        <!-- Detailed Table -->
        <div class="glass-card rounded-2xl overflow-hidden border border-white/10">
            <table class="w-full text-sm text-left">
                <tbody>
                    <tr class="bg-white/5 border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">Manufacturer</th>
                        <td class="py-4 px-6 font-medium text-white">Intel</td>
                    </tr>
                    <tr class="border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">Core Architecture</th>
                        <td class="py-4 px-6 font-medium text-white">Raptor Lake Refresh (14th Gen)</td>
                    </tr>
                    <tr class="bg-white/5 border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">PCIe Version</th>
                        <td class="py-4 px-6 font-medium text-white">PCIe 5.0 and 4.0</td>
                    </tr>
                    <tr class="border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">Thermal Solution Included</th>
                        <td class="py-4 px-6 font-medium text-white">No (Liquid Cooler Recommended)</td>
                    </tr>
                    <tr class="bg-white/5 border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">Max Turbo Power</th>
                        <td class="py-4 px-6 font-medium text-white">253W</td>
                    </tr>
                    <tr class="border-b border-white/5">
                        <th class="py-4 px-6 font-semibold w-1/3 text-on-surface-variant">Box Contents</th>
                        <td class="py-4 px-6 font-medium text-white">Processor, Manual, Sticker</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- 3 & 6 & 8. PERFORMANCE & BENCHMARKS -->
    <section id="performance" class="scroll-mt-40 space-y-8 pt-8 border-t border-white/10">
        <h2 class="text-2xl font-bold flex items-center gap-3">
            <span class="material-symbols-outlined text-primary">speed</span>
            Performance & Benchmarks
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Overall Score -->
            <div class="glass-card rounded-2xl p-8 flex flex-col items-center justify-center text-center relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-primary/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-32 h-32 rounded-full border-8 border-primary/20 border-t-primary flex items-center justify-center mb-4">
                    <span class="text-4xl font-black text-white">98<span class="text-lg text-primary">/100</span></span>
                </div>
                <h3 class="font-bold text-lg">Elite Tier</h3>
                <p class="text-sm text-on-surface-variant mt-2">Uncompromising performance for gaming and creator workloads.</p>
            </div>

            <!-- Workloads -->
            <div class="md:col-span-2 glass-card rounded-2xl p-6 grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-6">
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">Gaming (4K/1440p)</span><span class="text-primary text-sm font-bold">5/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 100%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">Video Editing (Premiere/Resolve)</span><span class="text-primary text-sm font-bold">5/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 100%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">3D Rendering (Blender)</span><span class="text-primary text-sm font-bold">4.8/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 95%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">Streaming & Multitasking</span><span class="text-primary text-sm font-bold">5/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 100%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">Programming & Compiling</span><span class="text-primary text-sm font-bold">4.9/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 98%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="font-bold text-sm">AI Workloads (Local Inference)</span><span class="text-primary text-sm font-bold">4.2/5</span></div>
                    <div class="performance-bar"><div class="performance-fill" style="width: 84%"></div></div>
                </div>
            </div>
        </div>

        <!-- Benchmarks Chart (Simulated) -->
        <div class="glass-card rounded-2xl p-6">
            <h3 class="font-bold mb-6">Cinebench R23 Multi-Core Score</h3>
            <div class="space-y-4">
                <div class="flex items-center gap-4">
                    <span class="w-32 text-sm font-medium text-white">i9-14900K</span>
                    <div class="flex-1 bg-white/5 rounded h-6 relative overflow-hidden">
                        <div class="absolute inset-y-0 left-0 bg-primary/80 w-[95%]"></div>
                        <span class="absolute inset-y-0 right-2 flex items-center text-xs font-bold text-white z-10">40,000+</span>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <span class="w-32 text-sm text-on-surface-variant">i9-13900K</span>
                    <div class="flex-1 bg-white/5 rounded h-6 relative overflow-hidden">
                        <div class="absolute inset-y-0 left-0 bg-white/20 w-[88%]"></div>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <span class="w-32 text-sm text-on-surface-variant">Ryzen 9 7950X</span>
                    <div class="flex-1 bg-white/5 rounded h-6 relative overflow-hidden">
                        <div class="absolute inset-y-0 left-0 bg-white/20 w-[92%]"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Used in Builds -->
        <div>
            <h3 class="font-bold mb-4 text-on-surface-variant">Featured In MakeMyPC Masterpieces</h3>
            <div class="flex gap-4 overflow-x-auto pb-4 no-scrollbar">
                <div class="min-w-[280px] glass-card rounded-xl p-4 hover:bg-white/5 cursor-pointer transition-colors border border-white/5">
                    <img src="https://placehold.co/300x200/142034/adc6ff?text=Project+Nova" class="w-full h-32 object-cover rounded-lg mb-3"/>
                    <h4 class="font-bold text-sm text-white">Project Nova (4K Gaming)</h4>
                    <p class="text-xs text-on-surface-variant mt-1">i9-14900K + RTX 4090</p>
                </div>
                <div class="min-w-[280px] glass-card rounded-xl p-4 hover:bg-white/5 cursor-pointer transition-colors border border-white/5">
                    <img src="https://placehold.co/300x200/142034/adc6ff?text=Creator+Pro" class="w-full h-32 object-cover rounded-lg mb-3"/>
                    <h4 class="font-bold text-sm text-white">Creator Pro Workstation</h4>
                    <p class="text-xs text-on-surface-variant mt-1">i9-14900K + 128GB RAM</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. COMPATIBILITY CHECKER -->
    <section id="compatibility" class="scroll-mt-40 space-y-6 pt-8 border-t border-white/10">
        <div class="flex justify-between items-end mb-4">
            <div>
                <h2 class="text-2xl font-bold flex items-center gap-3">
                    <span class="material-symbols-outlined text-[#00A4A6]">verified</span>
                    Compatibility & Pairings
                </h2>
                <p class="text-sm text-on-surface-variant mt-2">Components guaranteed to work perfectly with the i9-14900K.</p>
            </div>
            <button class="text-sm font-label-mono text-primary hover:underline hidden sm:block">View All Compatible Parts</button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <!-- Motherboards -->
            <div class="glass-card rounded-xl p-5 border-l-4 border-l-[#00A4A6] flex justify-between items-center group glow-hover">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-surface flex items-center justify-center p-2"><img src="https://placehold.co/40x40/101b30/d7e2ff?text=Z790" class="rounded object-cover"/></div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold bg-[#00A4A6]/20 text-[#00A4A6] px-2 py-0.5 rounded">100% Compatible</span>
                            <span class="text-xs font-label-mono text-on-surface-variant">Motherboards</span>
                        </div>
                        <h4 class="font-bold text-sm">Z790 & Z690 Chipsets (LGA 1700)</h4>
                    </div>
                </div>
                <button class="text-primary hover:text-white bg-primary/10 hover:bg-primary/20 p-2 rounded-lg transition-colors"><span class="material-symbols-outlined">add</span></button>
            </div>
            
            <!-- Cooling -->
            <div class="glass-card rounded-xl p-5 border-l-4 border-l-[#00A4A6] flex justify-between items-center group glow-hover">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-surface flex items-center justify-center p-2"><img src="https://placehold.co/40x40/101b30/d7e2ff?text=AIO" class="rounded object-cover"/></div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold bg-error/20 text-error px-2 py-0.5 rounded">Highly Recommended</span>
                            <span class="text-xs font-label-mono text-on-surface-variant">Cooling</span>
                        </div>
                        <h4 class="font-bold text-sm">360mm+ Liquid Coolers (AIO)</h4>
                    </div>
                </div>
                <button class="text-primary hover:text-white bg-primary/10 hover:bg-primary/20 p-2 rounded-lg transition-colors"><span class="material-symbols-outlined">add</span></button>
            </div>
            
            <!-- RAM -->
            <div class="glass-card rounded-xl p-5 border-l-4 border-l-[#00A4A6] flex justify-between items-center group glow-hover">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-surface flex items-center justify-center p-2"><img src="https://placehold.co/40x40/101b30/d7e2ff?text=RAM" class="rounded object-cover"/></div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold bg-[#00A4A6]/20 text-[#00A4A6] px-2 py-0.5 rounded">Optimal Performance</span>
                            <span class="text-xs font-label-mono text-on-surface-variant">Memory</span>
                        </div>
                        <h4 class="font-bold text-sm">DDR5 RAM (6000MHz+)</h4>
                    </div>
                </div>
                <button class="text-primary hover:text-white bg-primary/10 hover:bg-primary/20 p-2 rounded-lg transition-colors"><span class="material-symbols-outlined">add</span></button>
            </div>

            <!-- PSU -->
            <div class="glass-card rounded-xl p-5 border-l-4 border-l-[#00A4A6] flex justify-between items-center group glow-hover">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-surface flex items-center justify-center p-2"><img src="https://placehold.co/40x40/101b30/d7e2ff?text=PSU" class="rounded object-cover"/></div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-bold bg-primary/20 text-primary px-2 py-0.5 rounded">Requirement</span>
                            <span class="text-xs font-label-mono text-on-surface-variant">Power Supply</span>
                        </div>
                        <h4 class="font-bold text-sm">850W+ Gold/Platinum ATX 3.0</h4>
                    </div>
                </div>
                <button class="text-primary hover:text-white bg-primary/10 hover:bg-primary/20 p-2 rounded-lg transition-colors"><span class="material-symbols-outlined">add</span></button>
            </div>
        </div>

        <!-- Bundle Card -->
        <div class="mt-4 glass-card rounded-2xl p-6 bg-gradient-to-r from-primary/10 to-transparent border-primary/30 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="flex-1">
                <h3 class="font-bold text-lg text-white mb-2">AI Recommended Pro Bundle</h3>
                <p class="text-sm text-on-surface-variant mb-4">Pair with ASUS ROG Maximus Z790 Hero and Corsair Dominator Titanium 64GB DDR5 for ultimate stability and overclocking potential.</p>
                <div class="flex gap-2">
                    <img src="https://placehold.co/30x30/101b30/d7e2ff?text=M" class="rounded"/>
                    <img src="https://placehold.co/30x30/101b30/d7e2ff?text=R" class="rounded"/>
                    <img src="https://placehold.co/30x30/101b30/d7e2ff?text=C" class="rounded"/>
                </div>
            </div>
            <div class="text-right flex flex-col gap-3 w-full md:w-auto">
                <span class="text-xl font-bold text-primary">₹1,45,000 <span class="text-xs text-on-surface-variant line-through">₹1,60,000</span></span>
                <button class="bg-white text-[#00081C] font-bold px-6 py-2 rounded-lg hover:bg-gray-200 transition-colors w-full md:w-auto whitespace-nowrap">Add Bundle to Build</button>
            </div>
        </div>
    </section>

    <!-- 9, 10, 11. MEDIA & DOWNLOADS -->
    <section id="gallery" class="scroll-mt-40 space-y-8 pt-8 border-t border-white/10">
        <h2 class="text-2xl font-bold flex items-center gap-3">
            <span class="material-symbols-outlined text-primary">photo_library</span>
            Gallery, Videos & Downloads
        </h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="md:col-span-2 glass-card rounded-2xl p-2 relative group overflow-hidden border-white/10 h-[300px]">
                <img src="https://placehold.co/800x400/101b30/d7e2ff?text=Installation+Guide+Video" class="w-full h-full object-cover rounded-xl"/>
                <div class="absolute inset-0 bg-black/40 flex items-center justify-center group-hover:bg-black/20 transition-all">
                    <span class="material-symbols-outlined text-6xl text-white drop-shadow-lg cursor-pointer hover:scale-110 transition-transform">play_circle</span>
                </div>
            </div>
            <div class="glass-card rounded-2xl p-6 flex flex-col gap-4 border-white/10">
                <h3 class="font-bold text-white mb-2">Support & Downloads</h3>
                <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors border border-transparent hover:border-white/10 group">
                    <div class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">memory</span><span class="text-sm font-medium text-on-surface-variant group-hover:text-white transition-colors">Intel Extreme Tuning Utility</span></div>
                    <span class="material-symbols-outlined text-on-surface-variant text-sm">download</span>
                </a>
                <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors border border-transparent hover:border-white/10 group">
                    <div class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">article</span><span class="text-sm font-medium text-on-surface-variant group-hover:text-white transition-colors">Datasheet & Specs PDF</span></div>
                    <span class="material-symbols-outlined text-on-surface-variant text-sm">download</span>
                </a>
                <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors border border-transparent hover:border-white/10 group">
                    <div class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">verified</span><span class="text-sm font-medium text-on-surface-variant group-hover:text-white transition-colors">Warranty Info PDF</span></div>
                    <span class="material-symbols-outlined text-on-surface-variant text-sm">download</span>
                </a>
            </div>
        </div>
    </section>

    <!-- 12-18. SUPPORT, REVIEWS, TRUST -->
    <section id="support" class="scroll-mt-40 space-y-8 pt-8 border-t border-white/10">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            
            <!-- Reviews -->
            <div class="lg:col-span-2 space-y-6">
                <h2 class="text-2xl font-bold flex items-center gap-3">
                    <span class="material-symbols-outlined text-primary">reviews</span>
                    Customer Reviews
                </h2>
                
                <div class="flex items-center gap-8 glass-card p-6 rounded-2xl border-white/10">
                    <div class="text-center">
                        <div class="text-5xl font-black text-white mb-2">4.8</div>
                        <div class="flex text-[#FFB800] text-sm justify-center mb-1">
                            <span class="material-symbols-outlined filled">star</span><span class="material-symbols-outlined filled">star</span><span class="material-symbols-outlined filled">star</span><span class="material-symbols-outlined filled">star</span><span class="material-symbols-outlined">star_half</span>
                        </div>
                        <div class="text-xs font-label-mono text-on-surface-variant">2,104 Ratings</div>
                    </div>
                    <div class="flex-1 space-y-2 border-l border-white/10 pl-8">
                        <div class="flex items-center gap-2"><span class="text-xs w-2">5</span><div class="flex-1 h-2 bg-white/10 rounded overflow-hidden"><div class="h-full bg-[#FFB800]" style="width: 85%"></div></div></div>
                        <div class="flex items-center gap-2"><span class="text-xs w-2">4</span><div class="flex-1 h-2 bg-white/10 rounded overflow-hidden"><div class="h-full bg-[#FFB800]" style="width: 10%"></div></div></div>
                        <div class="flex items-center gap-2"><span class="text-xs w-2">3</span><div class="flex-1 h-2 bg-white/10 rounded overflow-hidden"><div class="h-full bg-[#FFB800]" style="width: 3%"></div></div></div>
                        <div class="flex items-center gap-2"><span class="text-xs w-2">2</span><div class="flex-1 h-2 bg-white/10 rounded overflow-hidden"><div class="h-full bg-[#FFB800]" style="width: 1%"></div></div></div>
                        <div class="flex items-center gap-2"><span class="text-xs w-2">1</span><div class="flex-1 h-2 bg-white/10 rounded overflow-hidden"><div class="h-full bg-[#FFB800]" style="width: 1%"></div></div></div>
                    </div>
                </div>

                <!-- Review Items -->
                <div class="space-y-4">
                    <div class="border-b border-white/10 pb-6">
                        <div class="flex justify-between items-start mb-2">
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <div class="flex text-[#FFB800] text-sm"><span class="material-symbols-outlined text-[14px] filled">star</span><span class="material-symbols-outlined text-[14px] filled">star</span><span class="material-symbols-outlined text-[14px] filled">star</span><span class="material-symbols-outlined text-[14px] filled">star</span><span class="material-symbols-outlined text-[14px] filled">star</span></div>
                                    <span class="text-xs font-bold text-[#00A4A6] bg-[#00A4A6]/10 px-2 py-0.5 rounded flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">verified</span>Verified Purchase</span>
                                </div>
                                <h4 class="font-bold text-sm text-white">Absolute beast for rendering. Runs hot though.</h4>
                                <span class="text-xs text-on-surface-variant font-label-mono">Rahul S. - 2 weeks ago</span>
                            </div>
                        </div>
                        <p class="text-sm text-on-surface-variant mt-2 leading-relaxed">Upgraded from a 12th gen i7. The compile times and rendering speeds in Premiere Pro are mind-blowing. However, you absolutely need a 360mm AIO cooler. Don't cheap out on cooling or motherboard VRMs.</p>
                        <div class="flex gap-4 mt-3">
                            <span class="text-xs text-on-surface-variant hover:text-white cursor-pointer flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">thumb_up</span> 42 Helpful</span>
                        </div>
                    </div>
                </div>
                <button class="w-full glass-card py-3 rounded-lg text-sm font-bold hover:bg-white/5 transition-colors">Load More Reviews</button>
            </div>

            <!-- Trust, Warranty & Shipping -->
            <div class="space-y-6">
                <!-- Trust Badges -->
                <div class="glass-card rounded-2xl p-6 border-white/10">
                    <h3 class="font-bold text-white mb-4">MakeMyPC Premium Promise</h3>
                    <ul class="space-y-3">
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-primary text-[20px]">verified</span> 100% Genuine Components</li>
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-[#00A4A6] text-[20px]">monitor_heart</span> Stress Tested & Benchmarked</li>
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-primary text-[20px]">shield</span> 3 Years Manufacturer Warranty</li>
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-primary text-[20px]">local_shipping</span> Insured Pan-India Delivery</li>
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-primary text-[20px]">receipt_long</span> GST Invoice Available</li>
                        <li class="flex items-center gap-3 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-primary text-[20px]">support_agent</span> Dedicated Expert Support</li>
                    </ul>
                </div>

                <!-- Shipping -->
                <div class="glass-card rounded-2xl p-6 border-white/10">
                    <h3 class="font-bold text-white mb-4">Delivery & Returns</h3>
                    <div class="flex items-start gap-3 mb-4">
                        <span class="material-symbols-outlined text-on-surface-variant mt-1">location_on</span>
                        <div>
                            <p class="text-sm font-bold text-white">Deliver to: <span class="text-primary font-normal cursor-pointer hover:underline">Mumbai, 400001</span></p>
                            <p class="text-xs text-on-surface-variant mt-1">Estimated delivery by Tomorrow, 8 PM if ordered within 2 hours.</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3 pt-4 border-t border-white/10">
                        <span class="material-symbols-outlined text-on-surface-variant mt-1">settings_backup_restore</span>
                        <div>
                            <p class="text-sm font-bold text-white">7 Days Replacement</p>
                            <p class="text-xs text-on-surface-variant mt-1">Only in case of manufacturing defects or dead on arrival (DOA).</p>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

</main>

<!-- Sticky Purchase Panel (Bottom) -->
<div id="sticky-purchase" class="fixed bottom-0 left-0 w-full z-50 bg-[#00081C]/95 backdrop-blur-xl border-t border-white/10 shadow-[0_-10px_40px_rgba(0,0,0,0.5)] p-4 sm:p-0">
    <div class="max-w-[1400px] mx-auto px-6 h-20 flex items-center justify-between gap-4">
        <div class="hidden sm:flex items-center gap-4">
            <img src="images/i9-14900k-box.png" class="h-12 w-12 object-contain bg-white/5 rounded-lg p-1" onerror="this.src='https://placehold.co/50x50/101b30/d7e2ff'"/>
            <div>
                <h4 class="font-bold text-sm text-white line-clamp-1">Intel Core i9-14900K</h4>
                <div class="text-xs text-secondary font-medium">In Stock</div>
            </div>
        </div>
        <div class="flex items-center gap-4 w-full sm:w-auto justify-between sm:justify-end">
            <div class="text-right flex flex-col">
                <span class="text-xl sm:text-2xl font-black text-white leading-none">₹52,499</span>
                <span class="text-[10px] text-on-surface-variant font-label-mono">Inclusive of GST</span>
            </div>
            <div class="flex gap-2">
                <button class="bg-primary text-on-primary font-bold px-4 sm:px-6 py-2.5 rounded-lg hover:brightness-110 active:scale-95 transition-all text-sm whitespace-nowrap shadow-[0_0_15px_rgba(173,198,255,0.3)]">Add to Build</button>
                <button class="glass-card text-on-surface font-bold px-4 py-2.5 rounded-lg hover:bg-white/10 active:scale-95 transition-all text-sm hidden md:block">Buy Now</button>
            </div>
        </div>
    </div>
</div>

<script>
    // Sticky Nav active state logic
    const sections = document.querySelectorAll("section");
    const navItems = document.querySelectorAll(".sticky-nav-item");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 150) {
                current = section.getAttribute("id");
            }
        });

        navItems.forEach((item) => {
            item.classList.remove("active", "text-primary", "border-primary", "border-b-2");
            if (item.getAttribute("href").includes(current)) {
                item.classList.add("active", "text-primary", "border-primary", "border-b-2");
                item.classList.remove("text-on-surface-variant");
            } else {
                item.classList.add("text-on-surface-variant");
            }
        });

        // Sticky Purchase Panel Logic
        const stickyPanel = document.getElementById("sticky-purchase");
        if (window.scrollY > 600) {
            stickyPanel.classList.add("visible");
        } else {
            stickyPanel.classList.remove("visible");
        }
    });
</script>

</body>
</html>
"""

# Write the file directly using python script
with open("product-details.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)
