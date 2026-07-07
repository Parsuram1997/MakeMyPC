import re

with open('admin-customers.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_content = """        <!-- Main Content -->
        <main class="ml-64 overflow-y-auto h-screen p-6 custom-scrollbar relative z-10">
            <!-- Header -->
            <header class="flex items-center justify-between mb-8">
                <div>
                    <h1 class="text-2xl font-bold text-white mb-1">Admin Profile</h1>
                    <div class="flex items-center gap-2 text-xs text-on-surface-variant">
                        <a href="admin-dashboard.html" class="hover:text-primary transition-colors">Dashboard</a>
                        <span class="material-symbols-outlined text-[12px]">chevron_right</span>
                        <span class="text-white">Admin Profile</span>
                    </div>
                </div>
            </header>

            <!-- Profile Content -->
            <div class="flex flex-col gap-6 w-full">
                
                <!-- Top Row: Profile Card & Personal Info -->
                <div class="grid grid-cols-[1fr_2fr] gap-6 items-stretch">
                    
                    <!-- Left Card: Profile Overview -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-8 flex flex-col items-center relative overflow-hidden">
                        <!-- Background Glow -->
                        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-32 bg-primary/10 rounded-full blur-3xl pointer-events-none"></div>
                        
                        <div class="relative mb-6">
                            <div class="w-24 h-24 rounded-full bg-primary/20 text-primary flex items-center justify-center font-bold text-3xl border-[3px] border-surface-container shadow-[0_0_20px_rgba(0,122,255,0.2)]">
                                AD
                            </div>
                            <button class="absolute bottom-0 right-0 w-8 h-8 rounded-full bg-surface-deep border border-white/10 flex items-center justify-center text-white hover:bg-white/10 transition-colors">
                                <span class="material-symbols-outlined text-[14px]">photo_camera</span>
                            </button>
                        </div>
                        
                        <div class="flex items-center gap-2 mb-2">
                            <h2 class="text-lg font-bold text-white tracking-wide">Admin User</h2>
                            <span class="text-[9px] font-bold text-primary bg-primary/10 px-2 py-0.5 rounded-full border border-primary/20">Super Admin</span>
                        </div>
                        
                        <p class="text-xs text-on-surface-variant mb-4">admin@makemypc.com</p>
                        
                        <div class="flex items-center gap-1.5 mb-8">
                            <span class="w-2 h-2 rounded-full bg-[#00D084] shadow-[0_0_8px_rgba(0,208,132,0.5)]"></span>
                            <span class="text-[11px] text-white tracking-wider">Online</span>
                        </div>
                        
                        <div class="w-full space-y-4 mt-auto">
                            <div class="flex justify-between items-center pb-3 border-b border-white/5">
                                <div class="flex items-center gap-2 text-on-surface-variant">
                                    <span class="material-symbols-outlined text-[14px]">calendar_today</span>
                                    <span class="text-[11px]">Joined on</span>
                                </div>
                                <span class="text-[11px] text-white font-medium">12 May 2024</span>
                            </div>
                            <div class="flex justify-between items-center pb-3 border-b border-white/5">
                                <div class="flex items-center gap-2 text-on-surface-variant">
                                    <span class="material-symbols-outlined text-[14px]">schedule</span>
                                    <span class="text-[11px]">Last Login</span>
                                </div>
                                <span class="text-[11px] text-white font-medium">20 May 2024, 10:30 AM</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <div class="flex items-center gap-2 text-on-surface-variant">
                                    <span class="material-symbols-outlined text-[14px]">monitor</span>
                                    <span class="text-[11px]">IP Address</span>
                                </div>
                                <span class="text-[11px] text-white font-medium">192.168.1.24</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Right Card: Personal Information -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-8 flex flex-col">
                        <div class="flex items-center justify-between mb-8">
                            <h3 class="text-sm font-bold text-white tracking-wider">Personal Information</h3>
                            <button class="flex items-center gap-1.5 text-[11px] font-medium text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg border border-white/5 transition-all">
                                <span class="material-symbols-outlined text-[12px]">edit</span> Edit
                            </button>
                        </div>
                        
                        <div class="grid grid-cols-[160px_1fr] gap-y-6 gap-x-4">
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">person</span>
                                <span class="text-xs">Full Name</span>
                            </div>
                            <div class="text-xs text-white">Admin User</div>
                            
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">mail</span>
                                <span class="text-xs">Email Address</span>
                            </div>
                            <div class="text-xs text-white">admin@makemypc.com</div>
                            
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">call</span>
                                <span class="text-xs">Phone Number</span>
                            </div>
                            <div class="text-xs text-white">+91 98765 43210</div>
                            
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
                                <span class="text-xs">Role</span>
                            </div>
                            <div class="text-xs text-white">Super Administrator</div>
                            
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">language</span>
                                <span class="text-xs">Language</span>
                            </div>
                            <div class="text-xs text-white">English</div>
                            
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">schedule</span>
                                <span class="text-xs">Time Zone</span>
                            </div>
                            <div class="text-xs text-white">(GMT+5:30) Asia/Kolkata</div>
                        </div>
                    </div>
                </div>
                
                <!-- Middle Row: Security & 2FA -->
                <div class="grid grid-cols-2 gap-6">
                    
                    <!-- Account Security -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-6">
                        <div class="flex items-start gap-4 mb-6">
                            <div class="w-10 h-10 rounded-xl bg-primary/10 text-primary flex items-center justify-center shrink-0 border border-primary/20">
                                <span class="material-symbols-outlined text-[20px]">shield_person</span>
                            </div>
                            <div>
                                <h3 class="text-sm font-bold text-white mb-1">Account Security</h3>
                                <p class="text-[11px] text-on-surface-variant">Manage your password and security settings</p>
                            </div>
                        </div>
                        
                        <button class="w-full flex items-center justify-between p-4 rounded-xl bg-surface-deep border border-white/5 hover:bg-white/5 transition-colors group">
                            <div class="flex items-center gap-3 text-sm text-white font-medium">
                                <span class="material-symbols-outlined text-[18px] text-on-surface-variant">lock</span>
                                Change Password
                            </div>
                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                        </button>
                    </div>
                    
                    <!-- Two Factor Auth -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-6">
                        <div class="flex items-start gap-4 mb-6">
                            <div class="w-10 h-10 rounded-xl bg-[#00D084]/10 text-[#00D084] flex items-center justify-center shrink-0 border border-[#00D084]/20">
                                <span class="material-symbols-outlined text-[20px]">lock_clock</span>
                            </div>
                            <div>
                                <h3 class="text-sm font-bold text-white mb-1">Two Factor Authentication</h3>
                                <p class="text-[11px] text-on-surface-variant">Add an extra layer of security to your account</p>
                            </div>
                        </div>
                        
                        <div class="flex items-center justify-between bg-surface-deep border border-white/5 rounded-xl p-4">
                            <div class="flex items-center gap-2">
                                <span class="material-symbols-outlined text-[14px] text-[#00D084]">check_circle</span>
                                <span class="text-xs font-bold text-[#00D084] tracking-wider">Enabled</span>
                            </div>
                            
                            <button class="flex items-center gap-2 text-[11px] font-medium text-white bg-white/5 hover:bg-white/10 px-4 py-2 rounded-lg border border-white/5 transition-all group">
                                Manage 2FA <span class="material-symbols-outlined text-[14px] text-on-surface-variant group-hover:text-white transition-colors">chevron_right</span>
                            </button>
                        </div>
                    </div>
                </div>
                
                <!-- Bottom Row: Sessions & Activity -->
                <div class="grid grid-cols-2 gap-6">
                    
                    <!-- Login Sessions -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-6 flex flex-col">
                        <div class="flex items-start gap-4 mb-6">
                            <div class="w-10 h-10 rounded-xl bg-primary/10 text-primary flex items-center justify-center shrink-0 border border-primary/20">
                                <span class="material-symbols-outlined text-[20px]">devices</span>
                            </div>
                            <div>
                                <h3 class="text-sm font-bold text-white mb-1">Login Sessions</h3>
                                <p class="text-[11px] text-on-surface-variant">Manage your active sessions across devices</p>
                            </div>
                        </div>
                        
                        <div class="flex items-center justify-between mt-auto">
                            <button class="text-xs font-medium text-white bg-surface-deep border border-white/5 hover:bg-white/10 px-5 py-2.5 rounded-xl transition-all">
                                View Active Sessions
                            </button>
                            <span class="text-[10px] font-bold text-[#B14EEF] bg-[#B14EEF]/10 px-3 py-1.5 rounded-lg border border-[#B14EEF]/20">3 Active</span>
                        </div>
                    </div>
                    
                    <!-- Activity Summary -->
                    <div class="bg-surface-container border border-white/5 rounded-2xl p-6">
                        <div class="flex items-start gap-4 mb-6">
                            <div class="w-10 h-10 rounded-xl bg-yellow-500/10 text-yellow-500 flex items-center justify-center shrink-0 border border-yellow-500/20">
                                <span class="material-symbols-outlined text-[20px]">show_chart</span>
                            </div>
                            <div>
                                <h3 class="text-sm font-bold text-white mb-1">Activity Summary</h3>
                                <p class="text-[11px] text-on-surface-variant">Your account activity overview</p>
                            </div>
                        </div>
                        
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500">login</span>
                                    <span class="text-lg font-bold text-white">142</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Logins</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[14px] text-yellow-500">touch_app</span>
                                    <span class="text-lg font-bold text-white">28</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">Actions</p>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="material-symbols-outlined text-[14px] text-primary">swap_horiz</span>
                                    <span class="text-lg font-bold text-white">12</span>
                                </div>
                                <p class="text-[10px] text-on-surface-variant">IP Changes</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Danger Zone -->
                <div class="bg-surface-container border border-white/5 rounded-2xl p-6 flex items-center justify-between mb-8">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-xl bg-red-500/10 text-red-500 flex items-center justify-center shrink-0 border border-red-500/20">
                            <span class="material-symbols-outlined text-[20px]">warning</span>
                        </div>
                        <div>
                            <h3 class="text-sm font-bold text-red-500 mb-1">Danger Zone</h3>
                            <p class="text-[11px] text-on-surface-variant">Permanently delete your account and all related data</p>
                        </div>
                    </div>
                    
                    <button class="flex items-center gap-2 text-[11px] font-bold text-red-500 bg-transparent border border-red-500/30 hover:bg-red-500/10 px-5 py-2.5 rounded-xl transition-all">
                        <span class="material-symbols-outlined text-[16px]">delete</span> Delete Account
                    </button>
                </div>
                
            </div>
        </main>
"""

new_content = re.sub(r'<main.*?</main>', main_content, content, flags=re.DOTALL)

with open('admin-profile.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Admin profile overhauled!")
