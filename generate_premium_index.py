import os

HTML_CONTENT = """<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>MakeMyPC | India's Smartest AI-Powered Custom PC Builder</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
              "primary": "#adc6ff",
              "electric-blue": "#007AFF",
              "cyber-teal": "#00A4A6",
              "background": "#071327",
              "surface": "#071327",
              "surface-deep": "#00081C",
              "surface-container-low": "#101b30",
              "surface-container": "#142034",
              "surface-container-high": "#1f2a3f",
              "on-surface": "#d7e2ff",
              "on-surface-variant": "#c1c6d7",
              "outline-variant": "#414755",
              "error": "#ffb4ab",
              "success": "#34d399",
            },
            "fontFamily": {
              "body": ["Inter", "sans-serif"],
              "heading": ["Inter", "sans-serif"],
              "mono": ["JetBrains Mono", "monospace"]
            },
            "animation": {
              "float": "float 6s ease-in-out infinite",
              "pulse-slow": "pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite",
              "glow": "glow 2s ease-in-out infinite alternate"
            },
            "keyframes": {
              float: {
                "0%, 100%": { transform: "translateY(0)" },
                "50%": { transform: "translateY(-10px)" }
              },
              glow: {
                "from": { boxShadow: "0 0 10px #007AFF, 0 0 20px #007AFF" },
                "to": { boxShadow: "0 0 20px #00A4A6, 0 0 30px #00A4A6" }
              }
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
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        }
        .hero-glow {
            position: absolute;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(0, 122, 255, 0.12) 0%, rgba(0, 8, 28, 0) 70%);
            z-index: -1;
            border-radius: 50%;
        }
        .hide-scrollbar::-webkit-scrollbar {
            display: none;
        }
        .hide-scrollbar {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        .timeline-line::after {
            content: '';
            position: absolute;
            top: 50%;
            right: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #007AFF, rgba(0, 164, 166, 0.2));
            z-index: -1;
        }
        .timeline-step:last-child .timeline-line::after {
            display: none;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .clip-slant {
            clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
        }
        
        /* Accordion CSS */
        .faq-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
        }
        .faq-card.active .faq-content {
            max-height: 500px;
        }
        .faq-card.active .faq-icon {
            transform: rotate(180deg);
        }
    </style>
</head>
<body class="bg-surface-deep text-on-surface pb-16 md:pb-0">

    <!-- Top Navbar -->
    <nav class="fixed top-0 w-full z-[100] bg-surface-deep/80 backdrop-blur-xl border-b border-white/10">
        <div class="flex justify-between items-center max-w-7xl mx-auto px-6 h-20">
            <a href="index.html" class="text-2xl font-black tracking-tighter bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">MakeMyPC</a>
            
            <div class="hidden md:flex gap-x-8 items-center font-mono text-sm">
                <a class="text-on-surface-variant hover:text-white transition-colors" href="prebuilt-pcs.html">Shop</a>
                <a class="text-on-surface-variant hover:text-white transition-colors" href="custom-pc-builder.html">Builder</a>
                <a class="text-on-surface-variant hover:text-white transition-colors" href="support-faq.html">Resources</a>
            </div>

            <div class="flex items-center gap-x-6">
                <div class="relative hidden lg:block group">
                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant group-focus-within:text-electric-blue">search</span>
                    <input class="bg-white/5 border border-white/10 rounded-full pl-10 pr-4 py-2 text-sm focus:outline-none focus:border-electric-blue focus:bg-white/10 w-64 transition-all text-white" placeholder="Search RTX 4090..." type="text"/>
                </div>
                <div class="flex gap-x-4">
                    <button class="text-on-surface-variant hover:text-white transition-colors relative" onclick="window.location.href='shopping-cart.html'">
                        <span class="material-symbols-outlined">shopping_cart</span>
                        <span class="absolute -top-2 -right-2 bg-electric-blue text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center">2</span>
                    </button>
                    <a href="login.html" class="text-on-surface-variant hover:text-white transition-colors hidden md:block">
                        <span class="material-symbols-outlined">account_circle</span>
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <main class="pt-20">
        <!-- 1. Hero Section -->
        <section class="relative min-h-[90vh] flex items-center overflow-hidden pt-10 lg:pt-0">
            <div class="hero-glow top-0 left-0"></div>
            <div class="hero-glow bottom-0 right-0 opacity-40"></div>
            
            <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center z-10 w-full">
                <!-- Left Content -->
                <div class="space-y-8 mt-10 lg:mt-0">
                    <div class="inline-flex items-center gap-2 py-1.5 px-4 rounded-full bg-white/5 border border-white/10 backdrop-blur-md">
                        <span class="text-yellow-400 text-sm">⭐⭐⭐⭐⭐</span>
                        <span class="text-xs font-mono text-on-surface-variant uppercase">Rated 4.9/5 by 15,000+ Builders</span>
                    </div>
                    
                    <h1 class="text-5xl lg:text-7xl font-black leading-[1.1] tracking-tight">
                        Build Your <br/>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-electric-blue to-cyber-teal">Dream PC.</span>
                    </h1>
                    
                    <p class="text-lg text-on-surface-variant max-w-lg">
                        India's Smartest AI-Powered Custom PC Builder. Select flagship hardware, ensure 100% compatibility, and let our master technicians assemble your masterpiece.
                    </p>
                    
                    <ul class="space-y-3 font-mono text-sm text-on-surface-variant">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-success text-lg">check_circle</span> AI Compatibility Check</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-success text-lg">check_circle</span> Cable Managed by Experts</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-success text-lg">check_circle</span> 3-Year Doorstep Warranty</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-success text-lg">check_circle</span> Pan India Secure Delivery</li>
                    </ul>

                    <div class="flex flex-wrap gap-4 pt-4">
                        <button onclick="window.location.href='builder-landing.html'" class="bg-electric-blue text-white px-8 py-4 rounded-lg font-bold text-lg hover:shadow-[0_0_25px_rgba(0,122,255,0.6)] transition-all active:scale-95 flex items-center gap-2">
                            Start Building <span class="material-symbols-outlined">build</span>
                        </button>
                        <button onclick="window.location.href='prebuilt-pcs.html'" class="glass-card text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-white/10 transition-all active:scale-95">
                            Explore Builds
                        </button>
                    </div>
                    
                    <div class="pt-6 border-t border-white/10 flex items-center gap-6 text-sm font-mono text-on-surface-variant">
                        <span>Trusted by Creators & Pros</span>
                    </div>
                </div>
                
                <!-- Right Content (Image) -->
                <div class="relative group mt-10 lg:mt-0 pb-20 lg:pb-0">
                    <div class="absolute inset-0 bg-gradient-to-tr from-electric-blue/20 to-cyber-teal/20 blur-3xl opacity-50"></div>
                    <img class="relative w-full z-10 drop-shadow-2xl animate-float" src="https://images.unsplash.com/photo-1587202372634-32705e3bf49c?q=80&w=1000&auto=format&fit=crop" alt="Premium RGB Gaming PC"/>
                    
                    <!-- Floating Data Tags -->
                    <div class="absolute top-10 -left-6 lg:-left-12 glass-card p-4 rounded-xl border-l-4 border-electric-blue z-20 animate-float" style="animation-delay: 1s;">
                        <div class="text-xs font-mono text-on-surface-variant">RTX 4090</div>
                        <div class="text-lg font-bold text-electric-blue">240+ FPS</div>
                    </div>
                    <div class="absolute bottom-20 -right-4 lg:-right-8 glass-card p-4 rounded-xl border-l-4 border-cyber-teal z-20 animate-float" style="animation-delay: 2s;">
                        <div class="text-xs font-mono text-on-surface-variant">AI ENGINE</div>
                        <div class="text-lg font-bold text-cyber-teal">100% Compatible</div>
                    </div>
                    
                    <!-- Brand Partners -->
                    <div class="absolute -bottom-10 left-1/2 -translate-x-1/2 w-full flex justify-center gap-6 lg:gap-12 opacity-50 grayscale">
                        <span class="font-black text-xl lg:text-2xl">INTEL</span>
                        <span class="font-black text-xl lg:text-2xl">NVIDIA</span>
                        <span class="font-black text-xl lg:text-2xl">AMD</span>
                        <span class="font-black text-xl lg:text-2xl">CORSAIR</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Trust Statistics Section -->
        <section class="py-20 bg-black/40 border-y border-white/5 relative z-20">
            <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 text-center">
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-electric-blue text-3xl mb-2">computer</span>
                    <div class="text-3xl font-black text-white counter" data-target="15000">0</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">PCs Built</div>
                </div>
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-cyber-teal text-3xl mb-2">groups</span>
                    <div class="text-3xl font-black text-white counter" data-target="50000">0</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">Happy Customers</div>
                </div>
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-success text-3xl mb-2">verified</span>
                    <div class="text-3xl font-black text-white">99.9%</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">Compatibility</div>
                </div>
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-electric-blue text-3xl mb-2">local_shipping</span>
                    <div class="text-3xl font-black text-white counter" data-target="120">0</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">Cities Delivered</div>
                </div>
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-yellow-400 text-3xl mb-2">star</span>
                    <div class="text-3xl font-black text-white">4.9★</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">Average Rating</div>
                </div>
                <div class="glass-card p-6 rounded-2xl hover:-translate-y-2 transition-transform">
                    <span class="material-symbols-outlined text-cyber-teal text-3xl mb-2">security</span>
                    <div class="text-3xl font-black text-white">3 Years</div>
                    <div class="text-xs font-mono text-on-surface-variant mt-1">Warranty</div>
                </div>
            </div>
        </section>

        <!-- 3. Shop by Purpose -->
        <section class="py-32 relative">
            <div class="max-w-7xl mx-auto px-6">
                <div class="text-center mb-16">
                    <h2 class="text-4xl md:text-5xl font-black mb-4">Choose Your Arena</h2>
                    <p class="text-on-surface-variant max-w-2xl mx-auto">We've engineered perfect starting points for every professional and enthusiast.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
                    <!-- Cards -->
                    <div class="glass-card p-6 rounded-2xl hover:bg-white/5 hover:border-electric-blue/50 transition-all group flex flex-col">
                        <span class="material-symbols-outlined text-4xl text-electric-blue mb-4 group-hover:scale-110 transition-transform">sports_esports</span>
                        <h3 class="text-xl font-bold mb-2">Gaming</h3>
                        <p class="text-sm text-on-surface-variant mb-6 flex-grow">Max FPS, Ray Tracing, zero bottlenecks.</p>
                        <div class="text-xs font-mono text-on-surface-variant mb-4">From ₹60,000</div>
                        <button class="w-full py-2 rounded bg-white/10 hover:bg-electric-blue text-white transition-colors text-sm font-bold">Start Building</button>
                    </div>
                    
                    <div class="glass-card p-6 rounded-2xl hover:bg-white/5 hover:border-cyber-teal/50 transition-all group flex flex-col">
                        <span class="material-symbols-outlined text-4xl text-cyber-teal mb-4 group-hover:scale-110 transition-transform">movie_edit</span>
                        <h3 class="text-xl font-bold mb-2">Video Editing</h3>
                        <p class="text-sm text-on-surface-variant mb-6 flex-grow">4K/8K timeline playback without drops.</p>
                        <div class="text-xs font-mono text-on-surface-variant mb-4">From ₹95,000</div>
                        <button class="w-full py-2 rounded bg-white/10 hover:bg-cyber-teal text-white transition-colors text-sm font-bold">Start Building</button>
                    </div>

                    <div class="glass-card p-6 rounded-2xl hover:bg-white/5 hover:border-purple-500/50 transition-all group flex flex-col">
                        <span class="material-symbols-outlined text-4xl text-purple-500 mb-4 group-hover:scale-110 transition-transform">memory</span>
                        <h3 class="text-xl font-bold mb-2">AI & ML</h3>
                        <p class="text-sm text-on-surface-variant mb-6 flex-grow">Massive VRAM and tensor core power.</p>
                        <div class="text-xs font-mono text-on-surface-variant mb-4">From ₹1,50,000</div>
                        <button class="w-full py-2 rounded bg-white/10 hover:bg-purple-600 text-white transition-colors text-sm font-bold">Start Building</button>
                    </div>

                    <div class="glass-card p-6 rounded-2xl hover:bg-white/5 hover:border-orange-500/50 transition-all group flex flex-col">
                        <span class="material-symbols-outlined text-4xl text-orange-500 mb-4 group-hover:scale-110 transition-transform">architecture</span>
                        <h3 class="text-xl font-bold mb-2">Architecture</h3>
                        <p class="text-sm text-on-surface-variant mb-6 flex-grow">Flawless AutoCAD & Revit rendering.</p>
                        <div class="text-xs font-mono text-on-surface-variant mb-4">From ₹85,000</div>
                        <button class="w-full py-2 rounded bg-white/10 hover:bg-orange-600 text-white transition-colors text-sm font-bold">Start Building</button>
                    </div>

                    <div class="glass-card p-6 rounded-2xl hover:bg-white/5 hover:border-pink-500/50 transition-all group flex flex-col">
                        <span class="material-symbols-outlined text-4xl text-pink-500 mb-4 group-hover:scale-110 transition-transform">podcasts</span>
                        <h3 class="text-xl font-bold mb-2">Streaming</h3>
                        <p class="text-sm text-on-surface-variant mb-6 flex-grow">Dual-PC setup power in one silent rig.</p>
                        <div class="text-xs font-mono text-on-surface-variant mb-4">From ₹1,10,000</div>
                        <button class="w-full py-2 rounded bg-white/10 hover:bg-pink-600 text-white transition-colors text-sm font-bold">Start Building</button>
                    </div>
                    
                </div>
            </div>
        </section>

        <!-- 4. How It Works -->
        <section class="py-24 bg-surface-container/30">
            <div class="max-w-7xl mx-auto px-6">
                <h2 class="text-4xl font-black text-center mb-16">The MakeMyPC Experience</h2>
                <div class="flex flex-col md:flex-row justify-between relative">
                    <!-- Lines for Desktop -->
                    <div class="hidden md:block absolute top-10 left-10 right-10 h-1 bg-white/10 rounded">
                        <div class="h-full bg-electric-blue w-0" id="timeline-progress"></div>
                    </div>
                    
                    <!-- Steps -->
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6 mb-8 md:mb-0">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-electric-blue/30 text-electric-blue">1</div>
                        <h4 class="font-bold mb-2">Choose Purpose</h4>
                        <p class="text-xs text-on-surface-variant px-2">Select your workflow</p>
                    </div>
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6 mb-8 md:mb-0">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-white/10 text-white">2</div>
                        <h4 class="font-bold mb-2">Pick Parts</h4>
                        <p class="text-xs text-on-surface-variant px-2">Select premium components</p>
                    </div>
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6 mb-8 md:mb-0">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-white/10 text-white"><span class="material-symbols-outlined text-cyber-teal">smart_toy</span></div>
                        <h4 class="font-bold mb-2">AI Check</h4>
                        <p class="text-xs text-on-surface-variant px-2">100% compatibility verified</p>
                    </div>
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6 mb-8 md:mb-0">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-white/10 text-white"><span class="material-symbols-outlined">precision_manufacturing</span></div>
                        <h4 class="font-bold mb-2">Expert Build</h4>
                        <p class="text-xs text-on-surface-variant px-2">Surgical assembly</p>
                    </div>
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6 mb-8 md:mb-0">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-white/10 text-white"><span class="material-symbols-outlined">speed</span></div>
                        <h4 class="font-bold mb-2">Stress Test</h4>
                        <p class="text-xs text-on-surface-variant px-2">Thermals & OS configured</p>
                    </div>
                    <div class="timeline-step relative flex flex-col items-center text-center z-10 w-full md:w-1/6">
                        <div class="w-20 h-20 rounded-full glass-card flex items-center justify-center text-3xl mb-4 border-2 border-white/10 text-white"><span class="material-symbols-outlined">package</span></div>
                        <h4 class="font-bold mb-2">Safe Delivery</h4>
                        <p class="text-xs text-on-surface-variant px-2">Wooden crate packaging</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. AI Compatibility Engine (USP) -->
        <section class="py-32 relative overflow-hidden">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-electric-blue/10 via-surface-deep to-surface-deep z-0"></div>
            <div class="max-w-7xl mx-auto px-6 relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div>
                    <div class="inline-flex items-center gap-2 py-1.5 px-4 rounded-full bg-electric-blue/10 border border-electric-blue/30 text-electric-blue text-xs font-mono uppercase mb-6">
                        <span class="material-symbols-outlined text-sm">memory</span> Proprietary Tech
                    </div>
                    <h2 class="text-4xl md:text-6xl font-black mb-6">Zero Errors.<br/>Total Harmony.</h2>
                    <p class="text-on-surface-variant text-lg mb-10">Our AI Compatibility Engine checks millions of data points in real-time. If it doesn't fit, bottleneck, or power up correctly, we won't let you build it.</p>
                    
                    <div class="grid grid-cols-2 gap-4 font-mono text-sm">
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>CPU Socket</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>RAM Speed</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>PSU Wattage</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>BIOS Ver.</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>GPU Length</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>Cooler Hgt.</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>Cabinet Size</span><span class="material-symbols-outlined text-success">check</span></div>
                        <div class="glass-card p-3 rounded flex justify-between items-center bg-white/5 border-l-2 border-success"><span>PCIe Lanes</span><span class="material-symbols-outlined text-success">check</span></div>
                    </div>
                </div>
                <div class="relative flex justify-center items-center h-full min-h-[400px]">
                    <!-- Glowing AI Brain / Chip visualization placeholder -->
                    <div class="absolute w-64 h-64 bg-electric-blue/30 rounded-full blur-[100px] animate-pulse-slow"></div>
                    <img src="https://images.unsplash.com/photo-1620283085439-3f6285a21976?auto=format&fit=crop&q=80&w=800" class="w-full max-w-md rounded-2xl glass-card border border-electric-blue/30 p-2 object-cover" alt="AI CPU Visualization"/>
                </div>
            </div>
        </section>

        <!-- 6. Featured Components -->
        <section class="py-24 border-t border-white/5">
            <div class="max-w-7xl mx-auto px-6 mb-12 flex justify-between items-end">
                <div>
                    <h2 class="text-3xl font-black mb-2">Featured Hardware</h2>
                    <p class="text-on-surface-variant">The latest tech in stock and ready to build.</p>
                </div>
                <a href="#" class="hidden md:flex items-center gap-2 text-electric-blue hover:text-white transition-colors font-mono text-sm">View All <span class="material-symbols-outlined text-sm">arrow_forward</span></a>
            </div>
            
            <!-- Horizontal Carousel -->
            <div class="w-full overflow-x-auto hide-scrollbar pb-10 px-6 max-w-[1400px] mx-auto">
                <div class="flex gap-6 w-max">
                    <!-- Component Card -->
                    <div class="glass-card w-72 rounded-2xl overflow-hidden group">
                        <div class="h-48 p-6 bg-white/5 relative flex justify-center items-center">
                            <span class="absolute top-3 left-3 bg-red-500/20 text-red-400 text-[10px] font-bold px-2 py-1 rounded uppercase">Hot</span>
                            <div class="absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">favorite</span></button>
                            </div>
                            <img src="https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&q=80&w=300" class="w-32 object-contain group-hover:scale-110 transition-transform duration-500" alt="GPU"/>
                        </div>
                        <div class="p-5">
                            <div class="flex justify-between items-start mb-2">
                                <div class="text-xs font-mono text-on-surface-variant">Graphics Card</div>
                                <div class="flex items-center text-yellow-400 text-[10px]"><span class="material-symbols-outlined text-[14px]">star</span> 4.9</div>
                            </div>
                            <h4 class="font-bold text-lg mb-1 line-clamp-1">NVIDIA RTX 4090 OC</h4>
                            <div class="flex items-end gap-2 mb-4">
                                <span class="text-xl font-bold text-electric-blue">₹1,85,990</span>
                                <span class="text-xs text-on-surface-variant line-through mb-1">₹2,05,000</span>
                            </div>
                            <button class="w-full py-2 bg-white/10 hover:bg-white/20 rounded font-bold text-sm transition-colors text-center border border-white/5">Add to Build</button>
                        </div>
                    </div>
                    
                    <div class="glass-card w-72 rounded-2xl overflow-hidden group">
                        <div class="h-48 p-6 bg-white/5 relative flex justify-center items-center">
                            <div class="absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">favorite</span></button>
                            </div>
                            <img src="https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&q=80&w=300" class="w-32 object-contain group-hover:scale-110 transition-transform duration-500" alt="CPU"/>
                        </div>
                        <div class="p-5">
                            <div class="flex justify-between items-start mb-2">
                                <div class="text-xs font-mono text-on-surface-variant">Processor</div>
                                <div class="flex items-center text-yellow-400 text-[10px]"><span class="material-symbols-outlined text-[14px]">star</span> 4.8</div>
                            </div>
                            <h4 class="font-bold text-lg mb-1 line-clamp-1">AMD Ryzen 9 7950X3D</h4>
                            <div class="flex items-end gap-2 mb-4">
                                <span class="text-xl font-bold text-electric-blue">₹58,490</span>
                            </div>
                            <button class="w-full py-2 bg-white/10 hover:bg-white/20 rounded font-bold text-sm transition-colors text-center border border-white/5">Add to Build</button>
                        </div>
                    </div>

                    <div class="glass-card w-72 rounded-2xl overflow-hidden group">
                        <div class="h-48 p-6 bg-white/5 relative flex justify-center items-center">
                            <div class="absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">visibility</span></button>
                                <button class="w-8 h-8 rounded-full bg-surface-deep/80 text-white flex items-center justify-center hover:bg-electric-blue transition-colors"><span class="material-symbols-outlined text-[16px]">favorite</span></button>
                            </div>
                            <span class="material-symbols-outlined text-6xl text-white/50 group-hover:scale-110 transition-transform duration-500">memory</span>
                        </div>
                        <div class="p-5">
                            <div class="flex justify-between items-start mb-2">
                                <div class="text-xs font-mono text-on-surface-variant">Motherboard</div>
                            </div>
                            <h4 class="font-bold text-lg mb-1 line-clamp-1">ASUS ROG Crosshair X670E</h4>
                            <div class="flex items-end gap-2 mb-4">
                                <span class="text-xl font-bold text-electric-blue">₹45,990</span>
                            </div>
                            <button class="w-full py-2 bg-white/10 hover:bg-white/20 rounded font-bold text-sm transition-colors text-center border border-white/5">Add to Build</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. Featured Builds (3 Categories) -->
        <section class="py-24 bg-surface-container/30">
            <div class="max-w-7xl mx-auto px-6">
                <h2 class="text-4xl font-black text-center mb-16">Curated For You</h2>
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <!-- Budget -->
                    <div class="glass-card rounded-2xl p-1 relative overflow-hidden group">
                        <div class="absolute inset-0 bg-gradient-to-b from-white/5 to-transparent"></div>
                        <div class="relative bg-surface-deep rounded-xl p-8 h-full flex flex-col">
                            <h3 class="text-2xl font-black mb-1">Starter Core</h3>
                            <p class="text-sm text-on-surface-variant mb-6">1080p Gaming & Daily Tasks</p>
                            <img src="https://images.unsplash.com/photo-1593640408182-31c70c8268f5?auto=format&fit=crop&q=80&w=400" class="h-48 w-full object-cover rounded-lg mb-6 group-hover:opacity-80 transition-opacity" alt="Budget PC"/>
                            
                            <div class="space-y-3 font-mono text-sm mb-8 flex-grow">
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>Core i5 13400F</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>RTX 4060 8GB</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>16GB DDR5 5200</span></div>
                                <div class="flex justify-between pb-2 text-cyber-teal"><span>Avg FPS (1080p)</span><span>~120</span></div>
                            </div>
                            
                            <div class="flex items-center justify-between mt-auto">
                                <div class="text-2xl font-bold">₹75,490</div>
                                <button class="p-3 bg-white/10 rounded-lg hover:bg-white/20 transition-colors"><span class="material-symbols-outlined">arrow_forward</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Mid -->
                    <div class="glass-card rounded-2xl p-1 relative overflow-hidden group transform lg:-translate-y-4">
                        <div class="absolute inset-0 bg-gradient-to-b from-electric-blue/30 to-transparent"></div>
                        <div class="relative bg-surface-deep rounded-xl p-8 h-full flex flex-col">
                            <div class="absolute top-0 right-8 bg-electric-blue text-white text-xs font-bold px-3 py-1 rounded-b-lg">Most Popular</div>
                            <h3 class="text-2xl font-black mb-1">Elite Performance</h3>
                            <p class="text-sm text-on-surface-variant mb-6">1440p Gaming & Streaming</p>
                            <img src="https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&q=80&w=400" class="h-48 w-full object-cover rounded-lg mb-6 group-hover:opacity-80 transition-opacity" alt="Mid PC"/>
                            
                            <div class="space-y-3 font-mono text-sm mb-8 flex-grow">
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>Ryzen 7 7800X3D</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>RTX 4070 SUPER</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>32GB DDR5 6000</span></div>
                                <div class="flex justify-between pb-2 text-electric-blue"><span>Avg FPS (1440p)</span><span>~144</span></div>
                            </div>
                            
                            <div class="flex items-center justify-between mt-auto">
                                <div class="text-2xl font-bold">₹1,45,990</div>
                                <button class="px-6 py-3 bg-electric-blue text-white font-bold rounded-lg hover:bg-blue-600 transition-colors w-full ml-4 text-center">Customize</button>
                            </div>
                        </div>
                    </div>

                    <!-- High End -->
                    <div class="glass-card rounded-2xl p-1 relative overflow-hidden group">
                        <div class="absolute inset-0 bg-gradient-to-b from-purple-500/20 to-transparent"></div>
                        <div class="relative bg-surface-deep rounded-xl p-8 h-full flex flex-col">
                            <h3 class="text-2xl font-black mb-1">God Tier</h3>
                            <p class="text-sm text-on-surface-variant mb-6">4K Extreme & Heavy Rendering</p>
                            <img src="https://images.unsplash.com/photo-1624705002806-5d72df19c3ad?auto=format&fit=crop&q=80&w=400" class="h-48 w-full object-cover rounded-lg mb-6 group-hover:opacity-80 transition-opacity" alt="High End PC"/>
                            
                            <div class="space-y-3 font-mono text-sm mb-8 flex-grow">
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>Core i9 14900K</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>RTX 4090 24GB</span></div>
                                <div class="flex justify-between border-b border-white/5 pb-2"><span>64GB DDR5 6400</span></div>
                                <div class="flex justify-between pb-2 text-purple-400"><span>Avg FPS (4K)</span><span>~120+</span></div>
                            </div>
                            
                            <div class="flex items-center justify-between mt-auto">
                                <div class="text-2xl font-bold">₹3,85,000</div>
                                <button class="p-3 bg-white/10 rounded-lg hover:bg-white/20 transition-colors"><span class="material-symbols-outlined">arrow_forward</span></button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. Customer Reviews & 9. Gallery Masonry -->
        <section class="py-24">
            <div class="max-w-7xl mx-auto px-6">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-black mb-4">The Community</h2>
                    <p class="text-on-surface-variant max-w-2xl mx-auto">Real builds by real gamers across India.</p>
                </div>
                
                <!-- Masonry Gallery -->
                <div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">
                    
                    <!-- Review Item 1 -->
                    <div class="glass-card rounded-xl overflow-hidden break-inside-avoid">
                        <img src="https://images.unsplash.com/photo-1593640495253-23196b27a87f?auto=format&fit=crop&q=80&w=600" class="w-full object-cover" alt="Customer Build"/>
                        <div class="p-5 bg-surface-deep">
                            <div class="flex items-center gap-2 text-yellow-400 text-sm mb-2">★★★★★ <span class="text-on-surface-variant text-xs ml-2">Verified Purchase</span></div>
                            <p class="text-sm italic mb-4">"Absolutely flawless cable management. The AI compatibility engine caught my PSU mistake before I ordered. Masterpiece indeed!"</p>
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-electric-blue flex items-center justify-center font-bold text-xs">R</div>
                                <div>
                                    <div class="text-sm font-bold">Rahul Sharma</div>
                                    <div class="text-xs text-on-surface-variant font-mono">RTX 4070 Build</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Gallery Item 2 -->
                    <div class="glass-card rounded-xl overflow-hidden break-inside-avoid relative group cursor-pointer">
                        <img src="https://images.unsplash.com/photo-1616588589676-62b3bd4ff6d2?auto=format&fit=crop&q=80&w=600" class="w-full object-cover" alt="Gallery Build"/>
                        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-center items-center backdrop-blur-sm">
                            <button class="bg-white/20 hover:bg-white/40 border border-white/50 text-white px-4 py-2 rounded-full text-sm font-bold flex items-center gap-2 mb-2"><span class="material-symbols-outlined text-sm">content_copy</span> Clone Build</button>
                            <div class="flex gap-4 text-xs font-mono">
                                <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm">favorite</span> 1.2k</span>
                                <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm">visibility</span> 4.5k</span>
                            </div>
                        </div>
                    </div>

                    <!-- Review Item 3 -->
                    <div class="glass-card rounded-xl overflow-hidden break-inside-avoid">
                        <div class="p-5 bg-surface-deep">
                            <div class="flex items-center gap-2 text-yellow-400 text-sm mb-2">★★★★★ <span class="text-on-surface-variant text-xs ml-2">Verified Purchase</span></div>
                            <p class="text-sm italic mb-4">"The packaging was insanely secure. Wooden crate for the PC! It booted perfectly on first try. Highly recommend MakeMyPC."</p>
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-cyber-teal flex items-center justify-center font-bold text-xs">A</div>
                                <div>
                                    <div class="text-sm font-bold">Aditi Patel</div>
                                    <div class="text-xs text-on-surface-variant font-mono">White Out Build</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Gallery Item 4 -->
                    <div class="glass-card rounded-xl overflow-hidden break-inside-avoid relative group cursor-pointer">
                        <img src="https://images.unsplash.com/photo-1544652478-6653e09f18a2?auto=format&fit=crop&q=80&w=600" class="w-full object-cover" alt="Gallery Build"/>
                    </div>
                </div>
                
                <div class="text-center mt-10">
                    <button class="px-6 py-3 border border-white/20 rounded-full font-mono text-sm hover:bg-white/5 transition-colors">Load More Builds</button>
                </div>
            </div>
        </section>

        <!-- 10. Comparison Section -->
        <section class="py-24 bg-surface-container/20 border-y border-white/5">
            <div class="max-w-4xl mx-auto px-6">
                <h2 class="text-3xl font-black text-center mb-12">The MakeMyPC Difference</h2>
                <div class="glass-card rounded-2xl overflow-hidden">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-white/10 bg-white/5">
                                <th class="p-4 font-bold w-1/3">Feature</th>
                                <th class="p-4 font-bold text-on-surface-variant w-1/3 text-center">Standard Stores</th>
                                <th class="p-4 font-bold text-electric-blue w-1/3 text-center">MakeMyPC</th>
                            </tr>
                        </thead>
                        <tbody class="text-sm font-mono">
                            <tr class="border-b border-white/5">
                                <td class="p-4">Compatibility Check</td>
                                <td class="p-4 text-center text-on-surface-variant"><span class="material-symbols-outlined text-error">close</span> (Manual)</td>
                                <td class="p-4 text-center"><span class="material-symbols-outlined text-success">check_circle</span> (Real-time AI)</td>
                            </tr>
                            <tr class="border-b border-white/5">
                                <td class="p-4">Cable Management</td>
                                <td class="p-4 text-center text-on-surface-variant"><span class="material-symbols-outlined text-error">close</span> (Basic zip ties)</td>
                                <td class="p-4 text-center"><span class="material-symbols-outlined text-success">check_circle</span> (Premium Sleeved/Routed)</td>
                            </tr>
                            <tr class="border-b border-white/5">
                                <td class="p-4">BIOS & OS Setup</td>
                                <td class="p-4 text-center text-on-surface-variant"><span class="material-symbols-outlined text-error">close</span> (DIY)</td>
                                <td class="p-4 text-center"><span class="material-symbols-outlined text-success">check_circle</span> (Plug & Play)</td>
                            </tr>
                            <tr class="border-b border-white/5">
                                <td class="p-4">24hr Stress Testing</td>
                                <td class="p-4 text-center text-on-surface-variant"><span class="material-symbols-outlined text-error">close</span></td>
                                <td class="p-4 text-center"><span class="material-symbols-outlined text-success">check_circle</span> (Included)</td>
                            </tr>
                            <tr>
                                <td class="p-4">Warranty</td>
                                <td class="p-4 text-center text-on-surface-variant">Individual Parts</td>
                                <td class="p-4 text-center text-electric-blue font-bold">3-Year Full System</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- 11. FAQ -->
        <section class="py-24 max-w-3xl mx-auto px-6">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-black mb-4">Frequently Asked Questions</h2>
            </div>
            
            <div class="space-y-4">
                <div class="faq-card glass-card rounded-lg overflow-hidden cursor-pointer bg-white/5" onclick="this.classList.toggle('active')">
                    <div class="p-5 flex justify-between items-center font-bold">
                        <span>How long does it take to build and ship?</span>
                        <span class="material-symbols-outlined faq-icon transition-transform">expand_more</span>
                    </div>
                    <div class="faq-content bg-surface-deep px-5 text-sm text-on-surface-variant">
                        <div class="pb-5">Most standard builds take 3-5 business days for assembly, BIOS flashing, and 24-hour stress testing. Shipping anywhere in India takes an additional 2-4 days via our secure logistics partners.</div>
                    </div>
                </div>

                <div class="faq-card glass-card rounded-lg overflow-hidden cursor-pointer bg-white/5" onclick="this.classList.toggle('active')">
                    <div class="p-5 flex justify-between items-center font-bold">
                        <span>What if a part arrives damaged?</span>
                        <span class="material-symbols-outlined faq-icon transition-transform">expand_more</span>
                    </div>
                    <div class="faq-content bg-surface-deep px-5 text-sm text-on-surface-variant">
                        <div class="pb-5">We use custom wooden crates and internal foam packaging for all fully built PCs. If damage occurs during transit, our 100% transit insurance covers it. Contact support within 24 hours of delivery.</div>
                    </div>
                </div>

                <div class="faq-card glass-card rounded-lg overflow-hidden cursor-pointer bg-white/5" onclick="this.classList.toggle('active')">
                    <div class="p-5 flex justify-between items-center font-bold">
                        <span>Can I upgrade my PC later?</span>
                        <span class="material-symbols-outlined faq-icon transition-transform">expand_more</span>
                    </div>
                    <div class="faq-content bg-surface-deep px-5 text-sm text-on-surface-variant">
                        <div class="pb-5">Absolutely! We use standard non-proprietary parts. You can upgrade any component in the future without voiding our labor warranty on the original parts.</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 14. Final CTA -->
        <section class="py-24 relative overflow-hidden">
            <div class="absolute inset-0 bg-electric-blue/10 clip-slant z-0"></div>
            <div class="max-w-4xl mx-auto px-6 relative z-10 text-center">
                <h2 class="text-5xl font-black mb-6">Ready to Build Your Dream PC?</h2>
                <p class="text-xl text-on-surface-variant mb-10">Start customizing with our AI Engine or talk to an expert for advice.</p>
                
                <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
                    <button class="w-full sm:w-auto px-10 py-5 bg-electric-blue text-white rounded-lg font-bold text-lg hover:bg-blue-600 transition-colors shadow-[0_0_20px_rgba(0,122,255,0.4)]">Start Building</button>
                    <span class="text-on-surface-variant font-mono">OR</span>
                    <button class="w-full sm:w-auto px-10 py-5 glass-card text-white rounded-lg font-bold text-lg hover:bg-white/10 transition-colors flex items-center justify-center gap-2">Talk to an Expert <span class="material-symbols-outlined text-green-400">chat</span></button>
                </div>
            </div>
        </section>
    </main>

    <!-- 12. Premium Footer -->
    <footer class="bg-black pt-20 pb-24 md:pb-10 border-t border-white/10">
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-10 mb-16">
            <div class="col-span-2">
                <h3 class="text-2xl font-black mb-4 tracking-tighter">MakeMyPC</h3>
                <p class="text-sm text-on-surface-variant mb-6 pr-4">India's Smartest AI-Powered Custom PC Builder. Precision engineering, premium parts, and unparalleled support.</p>
                <div class="flex gap-4">
                    <!-- Social icons placeholders -->
                    <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-electric-blue cursor-pointer transition-colors"><span class="font-bold text-xs">IG</span></div>
                    <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-electric-blue cursor-pointer transition-colors"><span class="font-bold text-xs">YT</span></div>
                    <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-electric-blue cursor-pointer transition-colors"><span class="font-bold text-xs">X</span></div>
                    <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-electric-blue cursor-pointer transition-colors"><span class="font-bold text-xs">DC</span></div>
                </div>
            </div>
            
            <div>
                <h4 class="font-bold mb-4">Company</h4>
                <ul class="space-y-2 text-sm text-on-surface-variant">
                    <li><a href="#" class="hover:text-white transition-colors">About Us</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Careers</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Affiliate Program</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Become a Partner</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Blog</a></li>
                </ul>
            </div>
            
            <div>
                <h4 class="font-bold mb-4">Support</h4>
                <ul class="space-y-2 text-sm text-on-surface-variant">
                    <li><a href="order-tracking.html" class="hover:text-white transition-colors">Track Order</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Warranty Info</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Returns & Refunds</a></li>
                    <li><a href="support-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
                    <li><a href="#" class="hover:text-white transition-colors">Contact Us</a></li>
                </ul>
            </div>
            
            <div class="col-span-2 lg:col-span-2">
                <h4 class="font-bold mb-4">Newsletter</h4>
                <p class="text-sm text-on-surface-variant mb-4">Get hardware drops and exclusive build discounts.</p>
                <div class="flex gap-2">
                    <input type="email" placeholder="Enter email" class="bg-white/5 border border-white/10 rounded px-3 py-2 text-sm w-full focus:border-electric-blue outline-none"/>
                    <button class="bg-electric-blue px-4 py-2 rounded text-sm font-bold hover:bg-blue-600 transition-colors">Subscribe</button>
                </div>
            </div>
        </div>
        
        <div class="max-w-7xl mx-auto px-6 border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-on-surface-variant font-mono">
            <p>© 2024 MakeMyPC. All Rights Reserved. GSTIN: 27AAAAA0000A1Z5</p>
            <div class="flex gap-4">
                <span>100% Genuine Products</span>
                <span>|</span>
                <span>SSL Secured</span>
                <span>|</span>
                <span>PCI DSS Compliant</span>
            </div>
        </div>
    </footer>

    <!-- 13. Floating Sticky Build Summary (Desktop) -->
    <div class="hidden md:flex fixed bottom-6 right-6 glass-card border border-electric-blue/30 rounded-xl p-4 shadow-2xl items-center gap-4 z-50 transform hover:scale-105 transition-transform cursor-pointer">
        <div class="bg-electric-blue/20 p-2 rounded-lg text-electric-blue">
            <span class="material-symbols-outlined">memory</span>
        </div>
        <div>
            <div class="text-xs font-mono text-on-surface-variant uppercase">My Build</div>
            <div class="font-bold text-white">8 Components</div>
        </div>
        <div class="ml-4 text-right">
            <div class="text-lg font-black text-electric-blue">₹84,990</div>
            <div class="text-[10px] text-success flex items-center gap-1 justify-end"><span class="material-symbols-outlined text-[12px]">check_circle</span> Compatible</div>
        </div>
        <div class="ml-2 bg-electric-blue text-white w-8 h-8 rounded flex items-center justify-center">
            <span class="material-symbols-outlined text-sm">arrow_forward</span>
        </div>
    </div>

    <!-- 15. Mobile Sticky Bottom Navigation -->
    <div class="md:hidden fixed bottom-0 w-full glass-card border-t border-white/10 bg-black/90 backdrop-blur-xl z-[100] pb-safe">
        <div class="flex justify-around items-center p-2">
            <a href="index.html" class="flex flex-col items-center gap-1 p-2 text-electric-blue">
                <span class="material-symbols-outlined">home</span>
                <span class="text-[10px] font-bold">Home</span>
            </a>
            <a href="prebuilt-pcs.html" class="flex flex-col items-center gap-1 p-2 text-on-surface-variant hover:text-white transition-colors">
                <span class="material-symbols-outlined">store</span>
                <span class="text-[10px]">Shop</span>
            </a>
            <a href="builder-landing.html" class="flex flex-col items-center gap-1 p-2 -mt-6">
                <div class="w-14 h-14 rounded-full bg-electric-blue text-white flex items-center justify-center shadow-[0_0_15px_rgba(0,122,255,0.5)] border-4 border-black">
                    <span class="material-symbols-outlined">build</span>
                </div>
            </a>
            <a href="shopping-cart.html" class="flex flex-col items-center gap-1 p-2 text-on-surface-variant hover:text-white transition-colors relative">
                <span class="material-symbols-outlined">shopping_cart</span>
                <span class="text-[10px]">Cart</span>
                <span class="absolute top-1 right-2 w-2 h-2 bg-electric-blue rounded-full"></span>
            </a>
            <a href="login.html" class="flex flex-col items-center gap-1 p-2 text-on-surface-variant hover:text-white transition-colors">
                <span class="material-symbols-outlined">account_circle</span>
                <span class="text-[10px]">Profile</span>
            </a>
        </div>
    </div>

    <script>
        // Number Counter Animation for Trust Stats
        const counters = document.querySelectorAll('.counter');
        const speed = 200; 

        const animateCounters = (counter) => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const inc = target / speed;
            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(() => animateCounters(counter), 10);
            } else {
                counter.innerText = target + (target > 1000 ? "+" : "");
            }
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    animateCounters(el);
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            observer.observe(counter);
        });
    </script>
    <script type="module" src="js/auth.js"></script>
    <script src="js/global.js"></script>
</body>
</html>
"""

with open("c:/Projects/MakeMyPC/index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Premium index.html generated successfully!")
