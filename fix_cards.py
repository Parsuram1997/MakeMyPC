import re

with open('support-faq.html', encoding='utf-8') as f:
    content = f.read()

OLD = '''        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="aspect-square bg-surface-container rounded-2xl overflow-hidden relative group">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity">
                    <div class="text-white font-bold text-sm">RTX 4090 Custom Watercooled</div>
                    <div class="text-electric-blue text-xs font-label-mono">Mumbai, MH</div>
                </div>
                <!-- Placeholder for image -->
                <div class="w-full h-full bg-surface-deep flex items-center justify-center text-on-surface-variant border border-white/5 group-hover:scale-110 transition-transform duration-700">Build Image</div>
            </div>
            <div class="aspect-square bg-surface-container rounded-2xl overflow-hidden relative group">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity">
                    <div class="text-white font-bold text-sm">Armored Packaging</div>
                    <div class="text-electric-blue text-xs font-label-mono">Quality Control</div>
                </div>
                <!-- Placeholder for image -->
                <div class="w-full h-full bg-surface-deep flex items-center justify-center text-on-surface-variant border border-white/5 group-hover:scale-110 transition-transform duration-700">Packaging Photo</div>
            </div>
            <div class="aspect-square bg-surface-container rounded-2xl overflow-hidden relative group">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity">
                    <div class="text-white font-bold text-sm">Benchmark Report</div>
                    <div class="text-electric-blue text-xs font-label-mono">Passed 24h Stress Test</div>
                </div>
                <!-- Placeholder for image -->
                <div class="w-full h-full bg-surface-deep flex items-center justify-center text-on-surface-variant border border-white/5 group-hover:scale-110 transition-transform duration-700">Benchmark PDF</div>
            </div>
            <div class="aspect-square bg-surface-container rounded-2xl overflow-hidden relative group">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity">
                    <div class="text-white font-bold text-sm">Clean Cable Management</div>
                    <div class="text-electric-blue text-xs font-label-mono">Behind the Motherboard</div>
                </div>
                <!-- Placeholder for image -->
                <div class="w-full h-full bg-surface-deep flex items-center justify-center text-on-surface-variant border border-white/5 group-hover:scale-110 transition-transform duration-700">Cable Routing</div>
            </div>
        </div>'''

NEW = '''        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">

            <!-- Card 1: RTX 4090 Build -->
            <div class="aspect-square rounded-2xl overflow-hidden relative group cursor-pointer" style="background:linear-gradient(135deg,#0d1b3e 0%,#0a2461 50%,#001f6b 100%);">
                <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500" style="background:radial-gradient(circle at 50% 50%,rgba(0,122,255,0.25) 0%,transparent 70%);"></div>
                <div class="absolute inset-0 opacity-20" style="background-image:linear-gradient(rgba(0,122,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,122,255,0.3) 1px,transparent 1px);background-size:32px 32px;"></div>
                <div class="absolute inset-0 flex flex-col items-center justify-center z-10">
                    <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform duration-500" style="background:rgba(0,122,255,0.2);border:1px solid rgba(0,122,255,0.4);">
                        <span class="material-symbols-outlined text-5xl" style="color:#007AFF;">memory</span>
                    </div>
                    <div class="text-white font-bold text-sm text-center px-4">RTX 4090 Custom</div>
                    <div class="text-xs mt-1" style="color:#60a5fa;font-family:'JetBrains Mono',monospace;">Watercooled Build</div>
                </div>
                <div class="absolute top-3 right-3 z-20 text-xs font-bold px-2 py-1 rounded-full" style="background:rgba(0,122,255,0.25);border:1px solid rgba(0,122,255,0.5);color:#60a5fa;">BUILD</div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div class="text-white font-bold text-sm">RTX 4090 Custom Watercooled</div>
                    <div class="text-xs" style="color:#60a5fa;">Mumbai, MH</div>
                </div>
            </div>

            <!-- Card 2: Packaging -->
            <div class="aspect-square rounded-2xl overflow-hidden relative group cursor-pointer" style="background:linear-gradient(135deg,#0d2e1a 0%,#0a3d22 50%,#053318 100%);">
                <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500" style="background:radial-gradient(circle at 50% 50%,rgba(0,164,166,0.25) 0%,transparent 70%);"></div>
                <div class="absolute inset-0 opacity-20" style="background-image:linear-gradient(rgba(0,164,166,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,164,166,0.3) 1px,transparent 1px);background-size:32px 32px;"></div>
                <div class="absolute inset-0 flex flex-col items-center justify-center z-10">
                    <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform duration-500" style="background:rgba(0,164,166,0.2);border:1px solid rgba(0,164,166,0.4);">
                        <span class="material-symbols-outlined text-5xl" style="color:#00A4A6;">inventory_2</span>
                    </div>
                    <div class="text-white font-bold text-sm text-center px-4">Armored Packaging</div>
                    <div class="text-xs mt-1" style="color:#34d399;font-family:'JetBrains Mono',monospace;">Quality Control</div>
                </div>
                <div class="absolute top-3 right-3 z-20 text-xs font-bold px-2 py-1 rounded-full" style="background:rgba(0,164,166,0.25);border:1px solid rgba(0,164,166,0.5);color:#34d399;">QC PASS</div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div class="text-white font-bold text-sm">Armored Packaging</div>
                    <div class="text-xs" style="color:#34d399;">Quality Control</div>
                </div>
            </div>

            <!-- Card 3: Benchmark -->
            <div class="aspect-square rounded-2xl overflow-hidden relative group cursor-pointer" style="background:linear-gradient(135deg,#2d1b00 0%,#3d2600 50%,#2a1a00 100%);">
                <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500" style="background:radial-gradient(circle at 50% 50%,rgba(251,191,36,0.25) 0%,transparent 70%);"></div>
                <div class="absolute inset-0 opacity-20" style="background-image:linear-gradient(rgba(251,191,36,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(251,191,36,0.3) 1px,transparent 1px);background-size:32px 32px;"></div>
                <div class="absolute inset-0 flex flex-col items-center justify-center z-10">
                    <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform duration-500" style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);">
                        <span class="material-symbols-outlined text-5xl" style="color:#fbbf24;">speed</span>
                    </div>
                    <div class="text-white font-bold text-sm text-center px-4">Benchmark Report</div>
                    <div class="text-xs mt-1" style="color:#fbbf24;font-family:'JetBrains Mono',monospace;">24h Stress Tested</div>
                </div>
                <div class="absolute top-3 right-3 z-20 text-xs font-bold px-2 py-1 rounded-full" style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.5);color:#fbbf24;">PASSED</div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div class="text-white font-bold text-sm">Benchmark Report</div>
                    <div class="text-xs" style="color:#fbbf24;">Passed 24h Stress Test</div>
                </div>
            </div>

            <!-- Card 4: Cable Management -->
            <div class="aspect-square rounded-2xl overflow-hidden relative group cursor-pointer" style="background:linear-gradient(135deg,#1e0d3e 0%,#2d1060 50%,#1a0a4a 100%);">
                <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500" style="background:radial-gradient(circle at 50% 50%,rgba(139,92,246,0.25) 0%,transparent 70%);"></div>
                <div class="absolute inset-0 opacity-20" style="background-image:linear-gradient(rgba(139,92,246,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,0.3) 1px,transparent 1px);background-size:32px 32px;"></div>
                <div class="absolute inset-0 flex flex-col items-center justify-center z-10">
                    <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform duration-500" style="background:rgba(139,92,246,0.2);border:1px solid rgba(139,92,246,0.4);">
                        <span class="material-symbols-outlined text-5xl" style="color:#a78bfa;">cable</span>
                    </div>
                    <div class="text-white font-bold text-sm text-center px-4">Cable Management</div>
                    <div class="text-xs mt-1" style="color:#a78bfa;font-family:'JetBrains Mono',monospace;">Behind Motherboard</div>
                </div>
                <div class="absolute top-3 right-3 z-20 text-xs font-bold px-2 py-1 rounded-full" style="background:rgba(139,92,246,0.2);border:1px solid rgba(139,92,246,0.5);color:#a78bfa;">CLEAN</div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div class="absolute bottom-4 left-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div class="text-white font-bold text-sm">Clean Cable Management</div>
                    <div class="text-xs" style="color:#a78bfa;">Behind the Motherboard</div>
                </div>
            </div>

        </div>'''

new_content = content.replace(OLD, NEW)
if new_content == content:
    print("ERROR: Pattern not matched!")
else:
    with open('support-faq.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Cards updated!")
