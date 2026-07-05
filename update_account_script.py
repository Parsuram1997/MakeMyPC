import re

file_path = "c:/Projects/MakeMyPC/account-settings.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the new main section replacement
new_main_content = """<main class="pt-28 pb-20 max-w-container-max mx-auto px-gutter">
    <!-- Breadcrumbs & Title -->
    <div class="text-xs text-outline font-label-mono uppercase tracking-widest mb-2">
        <a href="index.html" class="hover:text-primary transition-colors">Home</a> &gt; <span class="text-on-surface">Account Settings</span>
    </div>
    <h1 class="font-headline-lg text-headline-lg mb-8">Account Settings</h1>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- Sidebar Navigation -->
        <aside class="lg:col-span-3 flex flex-col gap-6">
            <div class="glass-card rounded-xl p-4 sticky top-28">
                <nav class="flex flex-col gap-2">
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-electric-blue bg-white/5 border-l-2 border-electric-blue font-bold transition-all" onclick="switchTab('profile')">
                        <span class="material-symbols-outlined">person</span>
                        <span class="font-headline-sm text-headline-sm">Profile</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('security')">
                        <span class="material-symbols-outlined">security</span>
                        <span class="font-headline-sm text-headline-sm">Security</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('builds')">
                        <span class="material-symbols-outlined">layers</span>
                        <span class="font-headline-sm text-headline-sm">My Builds</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all">
                        <span class="material-symbols-outlined">local_shipping</span>
                        <span class="font-headline-sm text-headline-sm">Orders &amp; Tracking</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('billing')">
                        <span class="material-symbols-outlined">payments</span>
                        <span class="font-headline-sm text-headline-sm">Billing &amp; Payments</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('notifications')">
                        <span class="material-symbols-outlined">notifications</span>
                        <span class="font-headline-sm text-headline-sm">Notifications</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all">
                        <span class="material-symbols-outlined">location_on</span>
                        <span class="font-headline-sm text-headline-sm">Address Book</span>
                    </button>
                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all">
                        <span class="material-symbols-outlined">favorite</span>
                        <span class="font-headline-sm text-headline-sm">Saved Items</span>
                    </button>
                </nav>
            </div>
            
            <!-- Need Help Card -->
            <div class="glass-card rounded-xl p-6 sticky top-[500px]">
                <h3 class="font-headline-sm text-headline-sm mb-2">Need Help?</h3>
                <p class="text-body-sm text-outline mb-6">Our support team is here to help you<br>Mon - Sat, 10 AM - 7 PM</p>
                <div class="flex flex-col gap-3">
                    <button class="w-full bg-white/5 hover:bg-white/10 border border-white/10 py-2 rounded-lg text-body-sm transition-all flex items-center justify-center gap-2">
                        <span class="material-symbols-outlined text-electric-blue text-sm">chat_bubble</span> Live Chat
                    </button>
                    <button class="w-full bg-white/5 hover:bg-white/10 border border-white/10 py-2 rounded-lg text-body-sm transition-all flex items-center justify-center gap-2">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" class="w-4 h-4 opacity-70 grayscale"> WhatsApp Us
                    </button>
                </div>
            </div>
        </aside>

        <!-- Content Area -->
        <section class="lg:col-span-9 space-y-8" id="settings-canvas">
            
            <!-- Profile Section -->
            <div class="section-content animate-in fade-in slide-in-from-bottom-4 duration-500" id="section-profile">
                <!-- Profile Information Card -->
                <div class="glass-card rounded-xl p-8 mb-6">
                    <h2 class="font-headline-lg text-headline-lg mb-8">Profile Information</h2>
                    <div class="flex flex-col md:flex-row gap-8 items-start mb-10">
                        <div class="flex flex-col items-center gap-3">
                            <div class="relative group">
                                <div class="w-32 h-32 rounded-full border-2 border-electric-blue overflow-hidden p-1 bg-surface-deep">
                                    <img class="w-full h-full object-cover rounded-full group-hover:opacity-80 transition-opacity" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDi_JFuKxItd-O8ZZ1hqqxZcc3IrWCswrcefpV86CZBQlpUjkGzfbqfa6PtCvjr-4titC5wZZWUibCLjYdwZrOPZk1ace6qEVRiy3QWqFL4xbo9wf9ScTiZ0VImGkHW8NhmNnbFh6I_x8nc6T9o0wNe8AGaa6hwaxPNDuX9q6cAld6Ni8gXvIE0-TvYC4qR5EJi-WP7-D1JweNdiCen1CltRhXsRKSR1Id3vwD288eD8UjJr7hUEsbYPbm7lOqpbrXzv1rexah4QvLn" alt="Alex Vandal"/>
                                </div>
                                <button class="absolute bottom-1 right-1 bg-electric-blue text-white p-2 rounded-full shadow-lg hover:scale-110 transition-transform">
                                    <span class="material-symbols-outlined text-sm">photo_camera</span>
                                </button>
                            </div>
                            <div class="text-center">
                                <button class="text-electric-blue text-xs font-bold hover:underline">Change Photo</button>
                                <p class="text-[10px] text-outline mt-1 font-label-mono uppercase tracking-widest">JPG, PNG (max. 2MB)</p>
                            </div>
                        </div>

                        <div class="flex-1 w-full text-left pt-2">
                            <div class="flex flex-wrap items-center gap-4 mb-2">
                                <h3 class="font-headline-lg text-headline-lg text-3xl font-bold">Alex Vandal</h3>
                                <span class="bg-electric-blue/20 border border-electric-blue text-electric-blue px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1">
                                    <span class="material-symbols-outlined text-[14px]">workspace_premium</span> Elite Builder
                                </span>
                            </div>
                            <p class="text-outline text-sm mb-6 flex items-center gap-2">
                                Member since Jan 2024 &nbsp;&bull;&nbsp; 12 Builds &nbsp;&bull;&nbsp; <span class="text-green-500 font-medium">98% Positive Feedback</span>
                            </p>
                            
                            <!-- Form Grid -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-8">
                                <div class="space-y-2">
                                    <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Display Name</label>
                                    <input class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" value="Alex Vandal"/>
                                </div>
                                <div class="space-y-2">
                                    <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Primary Email</label>
                                    <input class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="email" value="alex.vandal@techforge.io"/>
                                </div>
                                <div class="space-y-2">
                                    <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Phone Number</label>
                                    <input class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="tel" value="+91 98765 43210"/>
                                </div>
                                <div class="space-y-2">
                                    <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Location</label>
                                    <div class="relative">
                                        <select class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none appearance-none text-sm text-on-surface">
                                            <option value="bengaluru" selected class="bg-surface-deep text-on-surface">Bengaluru, Karnataka, India</option>
                                            <option value="mumbai" class="bg-surface-deep text-on-surface">Mumbai, Maharashtra, India</option>
                                            <option value="delhi" class="bg-surface-deep text-on-surface">New Delhi, Delhi, India</option>
                                        </select>
                                        <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-outline">expand_more</span>
                                    </div>
                                </div>
                                <div class="space-y-2 sm:col-span-2">
                                    <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Bio</label>
                                    <textarea class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm resize-y" rows="3">PC enthusiast & builder. Love crafting high performance setups!</textarea>
                                </div>
                            </div>
                            
                            <div class="flex justify-between items-center border-t border-white/10 pt-6">
                                <button class="bg-electric-blue text-white px-6 py-2.5 rounded-lg font-bold hover:shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:bg-blue-600 active:scale-95 transition-all text-sm">Save Changes</button>
                                <button class="text-outline hover:text-white text-sm transition-colors border-b border-transparent hover:border-white pb-0.5">Discard Changes</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Quick Stats Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <!-- Stat 1 -->
                    <div class="glass-card rounded-xl p-5 flex items-center justify-between group cursor-pointer hover:border-white/20 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-full bg-green-500/10 flex items-center justify-center border border-green-500/30">
                                <span class="material-symbols-outlined text-green-500 text-xl">shield</span>
                            </div>
                            <div>
                                <p class="text-label-mono font-label-mono text-outline uppercase text-[10px] mb-0.5 tracking-wider">Account Security</p>
                                <p class="text-green-500 font-bold text-sm">Strong</p>
                                <p class="text-[10px] text-outline mt-1 font-label-mono">Last login: 2 hours ago</p>
                            </div>
                        </div>
                        <span class="material-symbols-outlined text-outline group-hover:text-white transition-colors text-sm">chevron_right</span>
                    </div>

                    <!-- Stat 2 -->
                    <div class="glass-card rounded-xl p-5 flex items-center justify-between group cursor-pointer hover:border-white/20 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-full bg-purple-500/10 flex items-center justify-center border border-purple-500/30">
                                <span class="material-symbols-outlined text-purple-400 text-xl">computer</span>
                            </div>
                            <div>
                                <p class="text-label-mono font-label-mono text-outline uppercase text-[10px] mb-0.5 tracking-wider">Total Builds</p>
                                <p class="text-white font-bold text-lg leading-tight">12</p>
                                <p class="text-[10px] text-outline mt-1 font-label-mono">View your all builds</p>
                            </div>
                        </div>
                        <span class="material-symbols-outlined text-outline group-hover:text-white transition-colors text-sm">chevron_right</span>
                    </div>

                    <!-- Stat 3 -->
                    <div class="glass-card rounded-xl p-5 flex items-center justify-between group cursor-pointer hover:border-white/20 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-full bg-electric-blue/10 flex items-center justify-center border border-electric-blue/30">
                                <span class="material-symbols-outlined text-electric-blue text-xl">receipt_long</span>
                            </div>
                            <div>
                                <p class="text-label-mono font-label-mono text-outline uppercase text-[10px] mb-0.5 tracking-wider">Orders Completed</p>
                                <p class="text-white font-bold text-lg leading-tight">8</p>
                                <p class="text-[10px] text-outline mt-1 font-label-mono">Track all your orders</p>
                            </div>
                        </div>
                        <span class="material-symbols-outlined text-outline group-hover:text-white transition-colors text-sm">chevron_right</span>
                    </div>

                    <!-- Stat 4 -->
                    <div class="glass-card rounded-xl p-5 flex items-center justify-between group cursor-pointer hover:border-white/20 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-full bg-yellow-500/10 flex items-center justify-center border border-yellow-500/30">
                                <span class="material-symbols-outlined text-yellow-500 text-xl">stars</span>
                            </div>
                            <div>
                                <p class="text-label-mono font-label-mono text-outline uppercase text-[10px] mb-0.5 tracking-wider">Rewards Points</p>
                                <p class="text-white font-bold text-lg leading-tight">1,250</p>
                                <p class="text-[10px] text-outline mt-1 font-label-mono">Available to redeem</p>
                            </div>
                        </div>
                        <span class="material-symbols-outlined text-outline group-hover:text-white transition-colors text-sm">chevron_right</span>
                    </div>
                </div>
            </div>"""

try:
    part1, rest = content.split('<main class="pt-28 pb-20 max-w-container-max mx-auto px-gutter grid grid-cols-1 md:grid-cols-12 gap-8">')
    part2, rest2 = rest.split('<!-- Security Section (Hidden by Default) -->')

    new_content = part1 + new_main_content + '\\n            <!-- Security Section (Hidden by Default) -->' + rest2

    new_content = new_content.replace('</section>\\n</main>', '</section>\\n    </div>\\n</main>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated account-settings.html")
except Exception as e:
    print(f"Error: {e}")
