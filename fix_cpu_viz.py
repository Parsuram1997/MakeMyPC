with open('index.html', encoding='utf-8') as f:
    c = f.read()

OLD = '''                <div class="relative flex justify-center items-center h-full min-h-[400px]">
                    <!-- Glowing AI Brain / Chip visualization placeholder -->
                    <div class="absolute w-64 h-64 bg-electric-blue/30 rounded-full blur-[100px] animate-pulse-slow"></div>
                    <img src="https://images.unsplash.com/photo-1620283085439-3f6285a21976?auto=format&fit=crop&q=80&w=800" class="w-full max-w-md rounded-2xl glass-card border border-electric-blue/30 p-2 object-cover" alt="AI CPU Visualization"/>
                </div>'''

NEW = '''                <div class="relative flex justify-center items-center h-full min-h-[400px]">
                    <!-- Glowing pulse bg -->
                    <div class="absolute w-64 h-64 bg-electric-blue/30 rounded-full blur-[100px] animate-pulse-slow"></div>

                    <!-- CPU Chip Visualization (pure CSS/HTML, no external image) -->
                    <div class="relative w-80 h-80 flex items-center justify-center">

                        <!-- Outer rotating ring -->
                        <div class="absolute w-72 h-72 rounded-full border border-electric-blue/20"
                             style="animation:spin 20s linear infinite;">
                            <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-electric-blue shadow-[0_0_10px_#007AFF]"></div>
                            <div class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 w-2 h-2 rounded-full bg-cyber-teal shadow-[0_0_8px_#00A4A6]"></div>
                        </div>

                        <!-- Middle ring (counter-rotate) -->
                        <div class="absolute w-56 h-56 rounded-full border border-cyber-teal/30"
                             style="animation:spin 12s linear infinite reverse;">
                            <div class="absolute top-0 right-0 translate-x-1/4 -translate-y-1/4 w-2 h-2 rounded-full bg-success shadow-[0_0_8px_#34d399]"></div>
                            <div class="absolute bottom-0 left-0 -translate-x-1/4 translate-y-1/4 w-2 h-2 rounded-full bg-electric-blue/80"></div>
                        </div>

                        <!-- CPU Die (center chip) -->
                        <div class="relative w-40 h-40 rounded-2xl flex items-center justify-center z-10"
                             style="background:linear-gradient(135deg,#0d1b3e,#1a2d5a);border:1px solid rgba(0,122,255,0.5);box-shadow:0 0 40px rgba(0,122,255,0.3),inset 0 0 20px rgba(0,122,255,0.05);">

                            <!-- Circuit grid lines -->
                            <div class="absolute inset-2 opacity-30"
                                 style="background-image:linear-gradient(rgba(0,122,255,0.5) 1px,transparent 1px),linear-gradient(90deg,rgba(0,122,255,0.5) 1px,transparent 1px);background-size:16px 16px;border-radius:12px;"></div>

                            <!-- Core glow -->
                            <div class="absolute w-16 h-16 rounded-full"
                                 style="background:radial-gradient(circle,rgba(0,122,255,0.4) 0%,transparent 70%);animation:pulse 2s ease-in-out infinite;"></div>

                            <!-- Center icon -->
                            <span class="material-symbols-outlined z-10 text-5xl" style="color:#007AFF;filter:drop-shadow(0 0 12px #007AFF);">memory</span>

                            <!-- Corner pads -->
                            <div class="absolute top-2 left-2 w-3 h-3 rounded-sm bg-electric-blue/40 border border-electric-blue/60"></div>
                            <div class="absolute top-2 right-2 w-3 h-3 rounded-sm bg-electric-blue/40 border border-electric-blue/60"></div>
                            <div class="absolute bottom-2 left-2 w-3 h-3 rounded-sm bg-electric-blue/40 border border-electric-blue/60"></div>
                            <div class="absolute bottom-2 right-2 w-3 h-3 rounded-sm bg-electric-blue/40 border border-electric-blue/60"></div>
                        </div>

                        <!-- Floating data nodes -->
                        <div class="absolute top-8 right-8 px-2 py-1 rounded-lg text-xs font-bold z-20"
                             style="background:rgba(0,164,166,0.15);border:1px solid rgba(0,164,166,0.4);color:#00A4A6;animation:float 3s ease-in-out infinite;">AI</div>
                        <div class="absolute bottom-10 left-6 px-2 py-1 rounded-lg text-xs font-bold z-20"
                             style="background:rgba(52,211,153,0.15);border:1px solid rgba(52,211,153,0.4);color:#34d399;animation:float 4s ease-in-out infinite 0.5s;">CHECK OK</div>
                        <div class="absolute top-12 left-4 px-2 py-1 rounded-lg text-xs font-bold z-20"
                             style="background:rgba(0,122,255,0.15);border:1px solid rgba(0,122,255,0.4);color:#60a5fa;animation:float 3.5s ease-in-out infinite 1s;">PCIe</div>
                        <div class="absolute bottom-8 right-4 px-2 py-1 rounded-lg text-xs font-bold z-20"
                             style="background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.4);color:#a78bfa;animation:float 5s ease-in-out infinite 0.8s;">DDR5</div>

                    </div>
                </div>'''

new_c = c.replace(OLD, NEW)
if new_c == c:
    # Try to find around the img tag
    idx = c.find('AI CPU Visualization')
    print('Not matched. Context around img tag:')
    print(repr(c[max(0,idx-300):idx+100]))
else:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_c)
    print('SUCCESS!')
