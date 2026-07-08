import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MakeMyPC - Custom PC Builder</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Material Symbols -->
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
            colors: {
                primary: {
                    DEFAULT: '#2563EB',
                    light: '#60A5FA',
                    dark: '#1D4ED8'
                },
                surface: {
                    DEFAULT: '#0B1120',
                    alt: '#060B14'
                },
                'on-surface': '#F8FAFC',
                'on-surface-variant': '#94A3B8'
            }
          },
        },
      }
    </script>
    <style>
        body {
            background-color: #060B14;
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        /* Hexagon Logo */
        .hexagon {
            width: 28px;
            height: 32px;
            background-color: #2563EB;
            position: relative;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0B1120;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
    </style>
</head>
<body class="flex flex-col min-h-screen">

    <!-- Navbar -->
    <nav class="bg-[#0B1120]/80 backdrop-blur-md border-b border-white/5 sticky top-0 z-50">
        <div class="max-w-[1400px] mx-auto px-6 h-[72px] flex items-center justify-between">
            
            <!-- Left: Logo & Links -->
            <div class="flex items-center gap-12">
                <a href="index.html" class="flex items-center gap-3">
                    <div class="hexagon">
                        <span class="text-white font-bold text-sm">M</span>
                    </div>
                    <span class="text-lg font-bold tracking-wide text-white">MakeMyPC</span>
                </a>
                
                <div class="hidden md:flex items-center gap-8 text-sm">
                    <a href="shop.html" class="text-on-surface-variant hover:text-white transition-colors">Shop</a>
                    <a href="builder-landing.html" class="text-primary font-medium border-b-2 border-primary pb-1">Builder</a>
                    <a href="support-faq.html" class="text-on-surface-variant hover:text-white transition-colors">Resources</a>
                </div>
            </div>
            
            <!-- Right: Search & Icons -->
            <div class="flex items-center gap-6">
                <div class="relative hidden lg:block">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                    <input type="text" placeholder="Search components..." 
                        class="bg-white/5 border border-white/10 rounded-full py-2 pl-10 pr-4 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:border-primary/50 w-[240px] transition-all">
                </div>
                <div class="flex items-center gap-4">
                    <a href="shopping-cart.html" class="text-on-surface-variant hover:text-white transition-colors">
                        <span class="material-symbols-outlined text-[22px]">shopping_cart</span>
                    </a>
                    <a href="login.html" class="text-on-surface-variant hover:text-white transition-colors">
                        <span class="material-symbols-outlined text-[22px]">account_circle</span>
                    </a>
                </div>
            </div>
            
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow max-w-[1400px] mx-auto w-full px-6 py-8 flex gap-8">
        
        <!-- Left Side: Builder Process & Components -->
        <div class="flex-grow">
            
            <!-- Stepper -->
            <div class="flex items-center justify-between mb-10 relative">
                <div class="absolute left-0 right-0 top-1/2 -translate-y-1/2 h-[1px] bg-white/10 z-0 border-t border-dashed border-white/20"></div>
                
                <!-- Steps (Mocked 1 to 14) -->
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white text-xs font-semibold shadow-[0_0_15px_rgba(37,99,235,0.4)]">1</div>
                    <span class="text-[10px] text-primary font-medium uppercase tracking-wider">OS</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">2</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">CPU</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">3</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Board</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">4</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">RAM</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">5</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">SSD</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">6</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">HDD</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">7</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Cooler</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">8</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">PSU</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2 opacity-50">
                    <div class="w-8 h-8 rounded-full bg-transparent text-on-surface-variant text-xs font-semibold">...</div>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">14</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Review</span>
                </div>
            </div>
            
            <!-- Step Header -->
            <div class="mb-6">
                <h1 class="text-3xl font-bold text-white mb-2">Choose your OS</h1>
                <p class="text-sm text-on-surface-variant">Select a compatible OS for your build. Incompatible parts are automatically hidden.</p>
            </div>
            
            <!-- Utility Bar -->
            <div class="flex items-center justify-between glass-card rounded-2xl p-2 mb-6">
                <div class="px-4 py-2 bg-white/5 rounded-xl text-xs font-semibold text-white">4 Items</div>
                
                <div class="relative flex-grow max-w-md mx-6">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                    <input type="text" placeholder="Search components..." 
                        class="w-full bg-transparent border-none py-2 pl-10 pr-4 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:ring-0">
                </div>
                
                <div class="flex items-center gap-3">
                    <button class="flex items-center gap-2 px-4 py-2 hover:bg-white/5 rounded-xl text-xs font-medium text-on-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[16px]">sort</span>
                        Popularity
                    </button>
                    <div class="w-[1px] h-4 bg-white/10"></div>
                    <button class="flex items-center gap-2 px-4 py-2 hover:bg-white/5 rounded-xl text-xs font-medium text-white transition-colors">
                        Brand
                        <span class="material-symbols-outlined text-[16px]">expand_more</span>
                    </button>
                </div>
            </div>
            
            <!-- Product List -->
            <div class="space-y-4">
                
                <!-- Product Card 1 -->
                <div class="glass-card rounded-2xl p-4 flex gap-6 hover:border-primary/30 transition-colors group">
                    <!-- Image -->
                    <div class="w-[180px] h-[120px] rounded-xl overflow-hidden shrink-0 bg-[#0F172A]">
                        <img src="https://images.unsplash.com/photo-1633469924738-52101af51d87?auto=format&fit=crop&w=300&q=80" alt="Windows 11" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    
                    <!-- Details -->
                    <div class="flex flex-col justify-center flex-grow">
                        <span class="text-[10px] font-bold text-primary bg-primary/10 px-2 py-0.5 rounded w-max mb-1.5 uppercase tracking-wider">STANDARD</span>
                        <p class="text-xs text-on-surface-variant font-medium">Microsoft</p>
                        <h3 class="text-lg font-bold text-white mb-3">Windows 11 Home</h3>
                        
                        <div class="flex gap-2 mb-3">
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">DirectX 12 Ultimate</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Auto HDR</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Seamless Gaming</span>
                        </div>
                        
                        <p class="text-[11px] text-on-surface-variant leading-relaxed max-w-sm">The best Windows yet for home use.<br>Designed for productivity and entertainment.</p>
                    </div>
                    
                    <!-- Actions -->
                    <div class="flex flex-col justify-between items-end shrink-0 w-[180px]">
                        <div class="text-right">
                            <div class="text-xl font-bold text-white mb-1">₹9,500.00</div>
                            <div class="text-[10px] text-on-surface-variant">Digital License</div>
                        </div>
                        
                        <div class="flex gap-2 mt-auto mb-3">
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" class="w-4 opacity-70"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Flipkart-logo.png" class="w-4 opacity-70 grayscale"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px]">info</span></button>
                        </div>
                        
                        <button class="w-full bg-primary hover:bg-primary-light text-white text-sm font-semibold py-2 rounded-lg flex items-center justify-between px-4 transition-colors">
                            Add to Build
                            <span class="material-symbols-outlined text-[18px]">add_box</span>
                        </button>
                    </div>
                </div>
                
                <!-- Product Card 2 -->
                <div class="glass-card rounded-2xl p-4 flex gap-6 hover:border-primary/30 transition-colors group">
                    <div class="w-[180px] h-[120px] rounded-xl overflow-hidden shrink-0 bg-[#0F172A]">
                        <img src="https://images.unsplash.com/photo-1633469924738-52101af51d87?auto=format&fit=crop&w=300&q=80" alt="Windows 11" class="w-full h-full object-cover hue-rotate-90 group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="flex flex-col justify-center flex-grow">
                        <span class="text-[10px] font-bold text-[#A855F7] bg-[#A855F7]/10 px-2 py-0.5 rounded w-max mb-1.5 uppercase tracking-wider">PROFESSIONAL</span>
                        <p class="text-xs text-on-surface-variant font-medium">Microsoft</p>
                        <h3 class="text-lg font-bold text-white mb-3">Windows 11 Pro</h3>
                        
                        <div class="flex gap-2 mb-3">
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">BitLocker</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Remote Desktop</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Hyper-V</span>
                        </div>
                        
                        <p class="text-[11px] text-on-surface-variant leading-relaxed max-w-sm">Powerful tools for professionals and business.<br>Enhanced security and productivity.</p>
                    </div>
                    <div class="flex flex-col justify-between items-end shrink-0 w-[180px]">
                        <div class="text-right">
                            <div class="text-xl font-bold text-white mb-1">₹14,500.00</div>
                            <div class="text-[10px] text-on-surface-variant">Digital License</div>
                        </div>
                        <div class="flex gap-2 mt-auto mb-3">
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" class="w-4 opacity-70"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Flipkart-logo.png" class="w-4 opacity-70 grayscale"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px]">info</span></button>
                        </div>
                        <button class="w-full bg-[#8B5CF6] hover:bg-[#A855F7] text-white text-sm font-semibold py-2 rounded-lg flex items-center justify-between px-4 transition-colors">
                            Add to Build
                            <span class="material-symbols-outlined text-[18px]">add_box</span>
                        </button>
                    </div>
                </div>
                
                <!-- Product Card 3 -->
                <div class="glass-card rounded-2xl p-4 flex gap-6 hover:border-primary/30 transition-colors group">
                    <div class="w-[180px] h-[120px] rounded-xl overflow-hidden shrink-0 bg-[#0F172A]">
                        <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=300&q=80" alt="Windows 10" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="flex flex-col justify-center flex-grow">
                        <span class="text-[10px] font-bold text-primary bg-primary/10 px-2 py-0.5 rounded w-max mb-1.5 uppercase tracking-wider">STANDARD</span>
                        <p class="text-xs text-on-surface-variant font-medium">Microsoft</p>
                        <h3 class="text-lg font-bold text-white mb-3">Windows 10 Home</h3>
                        
                        <div class="flex gap-2 mb-3">
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Familiar Interface</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Lightweight</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Efficient</span>
                        </div>
                        
                        <p class="text-[11px] text-on-surface-variant leading-relaxed max-w-sm">The most familiar Windows experience.<br>Reliable and easy to use.</p>
                    </div>
                    <div class="flex flex-col justify-between items-end shrink-0 w-[180px]">
                        <div class="text-right">
                            <div class="text-xl font-bold text-white mb-1">₹8,000.00</div>
                            <div class="text-[10px] text-on-surface-variant">Digital License</div>
                        </div>
                        <div class="flex gap-2 mt-auto mb-3">
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" class="w-4 opacity-70"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Flipkart-logo.png" class="w-4 opacity-70 grayscale"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px]">info</span></button>
                        </div>
                        <button class="w-full bg-primary hover:bg-primary-light text-white text-sm font-semibold py-2 rounded-lg flex items-center justify-between px-4 transition-colors">
                            Add to Build
                            <span class="material-symbols-outlined text-[18px]">add_box</span>
                        </button>
                    </div>
                </div>
                
                <!-- Product Card 4 -->
                <div class="glass-card rounded-2xl p-4 flex gap-6 hover:border-primary/30 transition-colors group">
                    <div class="w-[180px] h-[120px] rounded-xl overflow-hidden shrink-0 bg-[#0F172A]">
                        <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=300&q=80" alt="Windows 10" class="w-full h-full object-cover hue-rotate-90 group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="flex flex-col justify-center flex-grow">
                        <span class="text-[10px] font-bold text-[#A855F7] bg-[#A855F7]/10 px-2 py-0.5 rounded w-max mb-1.5 uppercase tracking-wider">PROFESSIONAL</span>
                        <p class="text-xs text-on-surface-variant font-medium">Microsoft</p>
                        <h3 class="text-lg font-bold text-white mb-3">Windows 10 Pro</h3>
                        
                        <div class="flex gap-2 mb-3">
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">BitLocker</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Group Policy</span>
                            <span class="text-[10px] px-2 py-1 bg-white/5 border border-white/10 rounded-md text-on-surface-variant">Remote Desktop</span>
                        </div>
                        
                        <p class="text-[11px] text-on-surface-variant leading-relaxed max-w-sm">Built for business with advanced management<br>and security features.</p>
                    </div>
                    <div class="flex flex-col justify-between items-end shrink-0 w-[180px]">
                        <div class="text-right">
                            <div class="text-xl font-bold text-white mb-1">₹12,000.00</div>
                            <div class="text-[10px] text-on-surface-variant">Digital License</div>
                        </div>
                        <div class="flex gap-2 mt-auto mb-3">
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" class="w-4 opacity-70"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-colors"><img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Flipkart-logo.png" class="w-4 opacity-70 grayscale"></button>
                            <button class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors"><span class="material-symbols-outlined text-[16px]">info</span></button>
                        </div>
                        <button class="w-full bg-[#8B5CF6] hover:bg-[#A855F7] text-white text-sm font-semibold py-2 rounded-lg flex items-center justify-between px-4 transition-colors">
                            Add to Build
                            <span class="material-symbols-outlined text-[18px]">add_box</span>
                        </button>
                    </div>
                </div>

            </div>
        </div>
        
        <!-- Right Side: Sidebar -->
        <div class="w-[320px] shrink-0">
            <div class="glass-card rounded-3xl p-5 sticky top-[96px]">
                
                <!-- Tabs -->
                <div class="flex gap-2 mb-6">
                    <button class="flex-1 py-1.5 bg-primary text-white text-[11px] font-semibold rounded-lg shadow-[0_0_10px_rgba(37,99,235,0.3)]">Summary</button>
                    <button class="flex-1 py-1.5 bg-white/5 text-on-surface-variant hover:text-white text-[11px] font-semibold rounded-lg transition-colors">Checklist</button>
                    <button class="flex-1 py-1.5 bg-white/5 text-on-surface-variant hover:text-white text-[11px] font-semibold rounded-lg transition-colors">Parts</button>
                </div>
                
                <!-- Compatibility -->
                <div class="flex gap-3 mb-6">
                    <div class="w-8 h-8 rounded-lg bg-[#EAB308]/10 flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[#EAB308] text-[18px]">library_add_check</span>
                    </div>
                    <div>
                        <h4 class="text-xs font-semibold text-white">Compatibility</h4>
                        <p class="text-sm font-bold text-white mb-1">Waiting for parts</p>
                        <p class="text-[10px] text-on-surface-variant italic">Select parts to run compatibility checks.</p>
                    </div>
                </div>
                
                <div class="h-[1px] bg-white/10 mb-6 w-full"></div>
                
                <!-- Total Price -->
                <div class="mb-6">
                    <p class="text-xs text-on-surface-variant mb-1">Total Price</p>
                    <h2 class="text-3xl font-bold text-white mb-2">₹0.00</h2>
                    <div class="flex items-center justify-between text-[11px] text-on-surface-variant cursor-pointer hover:text-white transition-colors">
                        View Breakdown
                        <span class="material-symbols-outlined text-[14px]">expand_more</span>
                    </div>
                </div>
                
                <div class="h-[1px] bg-white/10 mb-6 w-full"></div>
                
                <!-- Estimated Power -->
                <div class="mb-6">
                    <p class="text-[11px] font-semibold text-white mb-2">Estimated Power</p>
                    <div class="h-2 w-full bg-white/5 rounded-full overflow-hidden flex mb-2">
                        <div class="h-full bg-[#10B981] w-[20%] rounded-full shadow-[0_0_10px_rgba(16,185,129,0.5)]"></div>
                    </div>
                    <div class="flex justify-between items-center text-[10px]">
                        <span class="text-on-surface-variant">0W Recommended</span>
                        <span class="text-white font-bold">0W / 0W</span>
                    </div>
                </div>
                
                <div class="h-[1px] bg-white/10 mb-6 w-full"></div>
                
                <!-- Gaming Performance -->
                <div class="mb-6">
                    <div class="flex justify-between items-center mb-3">
                        <p class="text-[11px] font-semibold text-white">Gaming Performance</p>
                        <div class="flex gap-1">
                            <span class="text-[8px] bg-primary text-white px-1.5 py-0.5 rounded font-bold">1080p</span>
                            <span class="text-[8px] bg-white/10 text-on-surface-variant px-1.5 py-0.5 rounded font-bold">1440p</span>
                            <span class="text-[8px] bg-white/10 text-on-surface-variant px-1.5 py-0.5 rounded font-bold">4K</span>
                        </div>
                    </div>
                    <div class="bg-white/5 rounded-xl p-6 text-center">
                        <p class="text-[10px] text-on-surface-variant">Select CPU, GPU, and RAM<br>to view estimates.</p>
                    </div>
                </div>
                
                <!-- Build Scores -->
                <div class="mb-8">
                    <p class="text-[11px] font-semibold text-white mb-2">Build Scores</p>
                    <div class="grid grid-cols-2 gap-2">
                        <div class="bg-white/5 rounded-xl p-3 border border-white/5">
                            <p class="text-[10px] text-on-surface-variant mb-1">Gaming</p>
                            <p class="text-lg font-bold text-[#10B981]">0<span class="text-[11px] text-on-surface-variant font-normal">/100</span></p>
                        </div>
                        <div class="bg-white/5 rounded-xl p-3 border border-white/5">
                            <p class="text-[10px] text-on-surface-variant mb-1">Productivity</p>
                            <p class="text-lg font-bold text-primary">0<span class="text-[11px] text-on-surface-variant font-normal">/100</span></p>
                        </div>
                    </div>
                </div>
                
                <!-- Action Buttons -->
                <div class="flex gap-2 mb-4">
                    <button class="flex-1 flex items-center justify-center gap-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-[10px] text-on-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[14px]">save</span> Save Build
                    </button>
                    <button class="flex-1 flex items-center justify-center gap-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-[10px] text-on-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[14px]">share</span> Share
                    </button>
                    <button class="flex-1 flex items-center justify-center gap-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-[10px] text-on-surface-variant transition-colors">
                        <span class="material-symbols-outlined text-[14px]">picture_as_pdf</span> Export PDF
                    </button>
                </div>
                
                <!-- Main CTA -->
                <button class="w-full flex items-center justify-center gap-2 bg-white/5 text-on-surface-variant/50 border border-white/5 py-3 rounded-xl text-sm font-bold cursor-not-allowed mb-4">
                    <span class="material-symbols-outlined text-[18px]">visibility</span>
                    Complete Build First
                </button>
                
                <!-- Footer Note -->
                <div class="flex items-center justify-center gap-2 text-[10px] text-on-surface-variant">
                    <span class="material-symbols-outlined text-[12px] text-[#10B981]">local_shipping</span>
                    Est. Delivery: 3-5 Business Days
                </div>
                
            </div>
        </div>
        
    </main>

    <!-- Footer -->
    <footer class="bg-surface border-t border-white/5 mt-auto">
        <div class="max-w-[1400px] mx-auto px-6 py-4 flex flex-wrap items-center justify-between gap-4 text-xs text-on-surface-variant">
            <div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px]">gpp_good</span> 100% Secure Checkout<br><span class="text-[10px] opacity-70">Safe and encrypted payments</span></div>
            <div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px]">replay</span> Easy Returns<br><span class="text-[10px] opacity-70">Hassle free returns</span></div>
            <div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px]">local_shipping</span> Fast Delivery<br><span class="text-[10px] opacity-70">Pan India delivery</span></div>
            <div class="flex items-center gap-2"><span class="material-symbols-outlined text-[16px]">support_agent</span> Expert Support<br><span class="text-[10px] opacity-70">We're here to help</span></div>
        </div>
    </footer>
    
    <!-- Retaining original JS includes just in case -->
    <script src="js/global.js"></script>
    <script src="js/builder-data.js"></script>
    <script src="js/builder-sidebar.js"></script>
    <script src="js/builder-app.js"></script>
    <script type="module" src="js/auth.js"></script>
</body>
</html>
"""

with open('custom-pc-builder.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("custom-pc-builder.html updated successfully!")
