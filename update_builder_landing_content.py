import re

html_main_content = """
<main class="flex-1 flex flex-col items-center pt-16 pb-20 px-4 md:px-8 max-w-[1200px] mx-auto w-full z-10 relative">
    
    <!-- Background Elements -->
    <div class="absolute top-20 left-0 w-[400px] h-[400px] bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900/20 via-transparent to-transparent opacity-50 pointer-events-none mix-blend-screen -z-10"></div>
    <div class="absolute top-40 right-0 w-[400px] h-[400px] bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-purple-900/20 via-transparent to-transparent opacity-50 pointer-events-none mix-blend-screen -z-10"></div>
    
    <!-- Header -->
    <div class="text-center mb-16 relative">
        <h1 class="text-4xl md:text-5xl font-bold text-white mb-4 flex items-center justify-center gap-3">
            How do you want to <span class="text-[#3b82f6]">build?</span>
            <span class="material-symbols-outlined text-[#3b82f6] text-[32px] absolute -right-12 top-[-10px] animate-pulse">auto_awesome</span>
        </h1>
        <p class="text-[15px] text-[#94a3b8] max-w-[600px] mx-auto">
            Choose your path. Let our AI guide you, or take complete control over every single component.
        </p>
    </div>

    <!-- Cards Container -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full mb-12">
        
        <!-- Smart Builder Card -->
        <div class="relative bg-[#0F172A]/80 backdrop-blur-md rounded-2xl border border-blue-500/30 overflow-hidden flex flex-col h-full hover:border-blue-500/60 transition-colors shadow-[0_0_40px_-15px_rgba(59,130,246,0.2)]">
            <!-- Badge -->
            <div class="absolute top-4 left-4 bg-[#3b82f6] text-white text-[10px] font-bold px-2 py-1 rounded flex items-center gap-1 uppercase tracking-wider z-20">
                <span class="material-symbols-outlined text-[14px]">star</span> RECOMMENDED
            </div>
            
            <!-- Graphic Header -->
            <div class="h-[200px] w-full bg-gradient-to-b from-[#1e3a8a]/20 to-transparent relative flex items-center justify-center border-b border-blue-500/10">
                <img src="https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&w=400&q=80" alt="AI Chip" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-screen">
                <div class="relative z-10 w-24 h-24 bg-blue-600 rounded-2xl shadow-[0_0_30px_rgba(37,99,235,0.6)] flex items-center justify-center rotate-12 hover:rotate-0 transition-transform duration-500">
                    <span class="text-3xl font-black text-white -rotate-12 hover:rotate-0 transition-transform duration-500">AI</span>
                </div>
                
                <!-- Floating Icon Badge -->
                <div class="absolute -bottom-6 w-12 h-12 rounded-full bg-[#1e293b] border-4 border-[#060B14] flex items-center justify-center z-20 shadow-lg">
                    <span class="material-symbols-outlined text-[#3b82f6]">auto_awesome</span>
                </div>
            </div>
            
            <!-- Content -->
            <div class="p-8 pt-10 flex flex-col flex-grow text-center">
                <h2 class="text-2xl font-bold text-white mb-2">Smart Builder</h2>
                <p class="text-[13px] text-[#94a3b8] mb-8">Perfect for beginners. Answer 2 simple questions and let our AI build the perfect PC for you.</p>
                
                <ul class="text-left space-y-4 mb-8 text-[13px] text-[#cbd5e1]">
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-[#3b82f6] text-[18px]">check_circle</span>
                        AI-Powered intelligent component selection
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-[#3b82f6] text-[18px]">check_circle</span>
                        Guaranteed 100% hardware compatibility
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-[#3b82f6] text-[18px]">check_circle</span>
                        Optimized for your specific budget & use-case
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-[#3b82f6] text-[18px]">check_circle</span>
                        Saves time and reduces guesswork
                    </li>
                </ul>
                
                <a href="smart-builder.html" class="mt-auto w-full py-3.5 rounded-xl bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 text-white font-bold flex items-center justify-center gap-2 transition-all shadow-[0_5px_20px_-5px_rgba(59,130,246,0.5)]">
                    Start Smart Build <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
                </a>
            </div>
        </div>

        <!-- Custom Builder Card -->
        <div class="relative bg-[#0F172A]/80 backdrop-blur-md rounded-2xl border border-emerald-500/30 overflow-hidden flex flex-col h-full hover:border-emerald-500/60 transition-colors shadow-[0_0_40px_-15px_rgba(16,185,129,0.15)]">
            <!-- Graphic Header -->
            <div class="h-[200px] w-full bg-gradient-to-b from-[#064e3b]/20 to-transparent relative flex items-center justify-center border-b border-emerald-500/10">
                <img src="https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80" alt="PC Build" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-screen hue-rotate-180">
                <div class="relative z-10 w-24 h-24 border border-emerald-500/50 bg-[#064e3b]/50 backdrop-blur-md rounded-2xl flex items-center justify-center shadow-[0_0_30px_rgba(16,185,129,0.3)]">
                    <span class="material-symbols-outlined text-4xl text-emerald-400">computer</span>
                </div>
                
                <!-- Floating Icon Badge -->
                <div class="absolute -bottom-6 w-12 h-12 rounded-full bg-[#1e293b] border-4 border-[#060B14] flex items-center justify-center z-20 shadow-lg">
                    <span class="material-symbols-outlined text-emerald-500">build</span>
                </div>
            </div>
            
            <!-- Content -->
            <div class="p-8 pt-10 flex flex-col flex-grow text-center">
                <h2 class="text-2xl font-bold text-white mb-2">Custom Builder</h2>
                <p class="text-[13px] text-[#94a3b8] mb-8">For experienced enthusiasts. Take complete control and hand-pick every single component.</p>
                
                <ul class="text-left space-y-4 mb-8 text-[13px] text-[#cbd5e1]">
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-emerald-500 text-[18px]">check_circle</span>
                        Complete freedom over parts selection
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-emerald-500 text-[18px]">check_circle</span>
                        Deep performance analytics & FPS estimates
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-emerald-500 text-[18px]">check_circle</span>
                        Real-time power draw calculations
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-emerald-500 text-[18px]">check_circle</span>
                        Advanced filters and sorting options
                    </li>
                </ul>
                
                <a href="custom-pc-builder.html" class="mt-auto w-full py-3.5 rounded-xl border border-emerald-500/50 hover:border-emerald-400 hover:bg-emerald-500/10 text-emerald-500 hover:text-emerald-400 font-bold flex items-center justify-center gap-2 transition-all">
                    Start Custom Build <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
                </a>
            </div>
        </div>

    </div>
    
    <!-- Footer Features Bar -->
    <div class="w-full bg-[#0F172A]/50 border border-white/5 rounded-2xl p-6 md:p-8 flex flex-col md:flex-row justify-between gap-6 md:gap-4 divide-y md:divide-y-0 md:divide-x divide-white/10 backdrop-blur-sm">
        
        <div class="flex gap-4 items-center flex-1 px-2 pt-4 md:pt-0 first:pt-0">
            <span class="material-symbols-outlined text-[#3b82f6] text-[28px] shrink-0">gpp_good</span>
            <div>
                <h4 class="text-white text-sm font-bold mb-0.5">100% Compatible</h4>
                <p class="text-[11px] text-[#94a3b8] leading-tight">Every build is checked for compatibility</p>
            </div>
        </div>
        
        <div class="flex gap-4 items-center flex-1 px-2 pt-4 md:pt-0">
            <span class="material-symbols-outlined text-[#a855f7] text-[28px] shrink-0">currency_rupee</span>
            <div>
                <h4 class="text-white text-sm font-bold mb-0.5">Best Price Guarantee</h4>
                <p class="text-[11px] text-[#94a3b8] leading-tight">Get the best prices from trusted sellers</p>
            </div>
        </div>
        
        <div class="flex gap-4 items-center flex-1 px-2 pt-4 md:pt-0">
            <span class="material-symbols-outlined text-[#10b981] text-[28px] shrink-0">local_shipping</span>
            <div>
                <h4 class="text-white text-sm font-bold mb-0.5">Fast & Secure Delivery</h4>
                <p class="text-[11px] text-[#94a3b8] leading-tight">Pan India delivery with secure packaging</p>
            </div>
        </div>
        
        <div class="flex gap-4 items-center flex-1 px-2 pt-4 md:pt-0">
            <span class="material-symbols-outlined text-[#f59e0b] text-[28px] shrink-0">support_agent</span>
            <div>
                <h4 class="text-white text-sm font-bold mb-0.5">Expert Support</h4>
                <p class="text-[11px] text-[#94a3b8] leading-tight">We're here to help you build your dream PC</p>
            </div>
        </div>
        
    </div>

</main>
"""

def update_builder_landing():
    with open('builder-landing.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The content is between <!-- ═══ NEW PREMIUM NAVBAR END ═══ --> and <footer
    
    # Let's find the start and end indices
    start_str = "<!-- ═══ NEW PREMIUM NAVBAR END ═══ -->"
    end_str = "<footer"
    
    start_idx = content.find(start_str)
    if start_idx == -1:
        print("Could not find start str")
        return
        
    start_idx += len(start_str)
    
    end_idx = content.find(end_str, start_idx)
    if end_idx == -1:
        print("Could not find end str")
        return
        
    new_content = content[:start_idx] + "\n" + html_main_content + "\n" + content[end_idx:]
    
    with open('builder-landing.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("builder-landing.html updated successfully!")

update_builder_landing()
