import os
import glob
import re

def update_sidebar_profile_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Security link in the bottom profile menu
    security_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">lock</span>\s*Security\s*</a>'
    new_security = '<a href="admin-security.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">lock</span>\n                    Security\n                </a>'
    
    if re.search(security_pattern, content):
        content = re.sub(security_pattern, new_security, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_security_page():
    base_file = 'admin-profile.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    # We will use a unique sidebar for the profile pages if needed, but since we are replacing main, let's keep the standard sidebar
    # Wait, the screenshot has a specific sidebar. Let's just build the main content to match the right side of the screenshot.
    
    security_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div>
                    <h2 class="text-2xl font-bold text-white mb-1">Security</h2>
                    <p class="text-on-surface-variant text-sm">Manage your account security, access, and authentication settings.</p>
                </div>
                <div>
                    <button class="px-4 py-2 rounded-lg border border-white/10 hover:bg-white/5 transition-colors text-sm flex items-center gap-2 text-white">
                        <span class="material-symbols-outlined text-[18px]">devices</span>
                        Login Sessions
                    </button>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="grid grid-cols-[1fr_1fr] gap-6 relative z-10">
                
                <!-- Left Column -->
                <div class="flex flex-col gap-6">
                    
                    <!-- Change Password -->
                    <div class="glass-card rounded-xl border border-white/5 p-6 bg-surface-container/30">
                        <div class="flex items-center gap-3 mb-6">
                            <span class="material-symbols-outlined text-primary text-[20px]">lock</span>
                            <div>
                                <h3 class="text-sm font-medium text-white">Change Password</h3>
                                <p class="text-[11px] text-on-surface-variant mt-0.5">Update your password regularly to keep your account secure.</p>
                            </div>
                        </div>
                        
                        <div class="space-y-4">
                            <div>
                                <label class="block text-[11px] text-on-surface-variant mb-1.5">Current Password</label>
                                <div class="relative">
                                    <input type="password" placeholder="Enter current password" class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-3 py-2 text-[12px] text-white placeholder-on-surface-variant/50 focus:outline-none focus:border-primary/50">
                                    <button class="absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">visibility</span>
                                    </button>
                                </div>
                            </div>
                            <div>
                                <label class="block text-[11px] text-on-surface-variant mb-1.5">New Password</label>
                                <div class="relative">
                                    <input type="password" placeholder="Enter new password" class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-3 py-2 text-[12px] text-white placeholder-on-surface-variant/50 focus:outline-none focus:border-primary/50">
                                    <button class="absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">visibility</span>
                                    </button>
                                </div>
                                <div class="flex items-center gap-2 mt-2">
                                    <span class="text-[10px] text-on-surface-variant">Password strength: <span class="text-white">Strong</span></span>
                                    <div class="flex gap-1 flex-1 max-w-[150px]">
                                        <div class="h-1 flex-1 bg-[#00D084] rounded-full"></div>
                                        <div class="h-1 flex-1 bg-[#00D084] rounded-full"></div>
                                        <div class="h-1 flex-1 bg-[#00D084] rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <label class="block text-[11px] text-on-surface-variant mb-1.5">Confirm New Password</label>
                                <div class="relative">
                                    <input type="password" placeholder="Confirm new password" class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-3 py-2 text-[12px] text-white placeholder-on-surface-variant/50 focus:outline-none focus:border-primary/50">
                                    <button class="absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant hover:text-white">
                                        <span class="material-symbols-outlined text-[16px]">visibility</span>
                                    </button>
                                </div>
                            </div>
                            <div class="pt-2 flex justify-end">
                                <button class="bg-primary hover:bg-primary-hover text-on-primary font-medium px-4 py-2 rounded-lg text-sm transition-colors flex items-center gap-2">
                                    <span class="material-symbols-outlined text-[16px]">check_circle</span>
                                    Update Password
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Security Options -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden">
                        <div class="p-4 border-b border-white/5">
                            <h3 class="text-sm font-medium text-white">Security Options</h3>
                        </div>
                        <div class="divide-y divide-white/5">
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant">mail</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Email Verification</p>
                                        <p class="text-[10px] text-on-surface-variant">Verify your email address to secure your account.</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-[11px] text-[#00D084]">Verified</span>
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">chevron_right</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant">phone_iphone</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Phone Verification</p>
                                        <p class="text-[10px] text-on-surface-variant">Verify your phone number for account recovery.</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-[11px] text-[#00D084]">Verified</span>
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">chevron_right</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant">key</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Backup Codes</p>
                                        <p class="text-[10px] text-on-surface-variant">Use backup codes to access your account if 2FA is unavailable.</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3">
                                    <button class="text-[11px] text-primary border border-primary/30 px-3 py-1 rounded hover:bg-primary/10 transition-colors">View Codes</button>
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">chevron_right</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant">notifications</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Login Alerts</p>
                                        <p class="text-[10px] text-on-surface-variant">Get notified about new logins to your account.</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-[11px] text-[#00D084]">Enabled</span>
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">chevron_right</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 transition-colors">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant">devices_other</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Device Management</p>
                                        <p class="text-[10px] text-on-surface-variant">Manage devices that have access to your account.</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-3">
                                    <button class="text-[11px] text-primary border border-primary/30 px-3 py-1 rounded hover:bg-primary/10 transition-colors">Manage</button>
                                    <span class="material-symbols-outlined text-[16px] text-on-surface-variant">chevron_right</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Deactivate Account -->
                    <div class="rounded-xl border border-[#FC8181]/20 bg-surface-container/30 overflow-hidden flex items-center justify-between p-6">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-[#FC8181]/10 text-[#FC8181] flex items-center justify-center">
                                <span class="material-symbols-outlined text-[20px]">delete_forever</span>
                            </div>
                            <div>
                                <h3 class="text-sm font-medium text-[#FC8181]">Deactivate Account</h3>
                                <p class="text-[11px] text-on-surface-variant mt-0.5">Temporarily deactivate your account. You can reactivate it anytime.</p>
                            </div>
                        </div>
                        <button class="px-4 py-2 border border-[#FC8181]/30 text-[#FC8181] hover:bg-[#FC8181]/10 rounded-lg text-sm font-medium transition-colors">
                            Deactivate Account
                        </button>
                    </div>

                </div>

                <!-- Right Column -->
                <div class="flex flex-col gap-6">
                    
                    <!-- 2FA -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-6">
                        <div class="flex items-start justify-between mb-6">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-lg bg-primary/10 text-primary flex items-center justify-center">
                                    <span class="material-symbols-outlined text-[20px]">security</span>
                                </div>
                                <div>
                                    <h3 class="text-sm font-medium text-white">Two-Factor Authentication (2FA)</h3>
                                    <p class="text-[11px] text-on-surface-variant mt-0.5">Add an extra layer of security to your account.</p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="flex items-center gap-2 mb-4 text-[11px]">
                            <span class="text-on-surface-variant">Status</span>
                            <span class="text-[#00D084] font-medium">Enabled</span>
                        </div>
                        <p class="text-[11px] text-on-surface-variant mb-4">You will be asked for a verification code in addition to your password.</p>
                        
                        <div class="flex items-center justify-between p-4 bg-surface-deep/50 rounded-lg border border-white/5 mb-4">
                            <div class="flex items-center gap-3">
                                <span class="material-symbols-outlined text-[20px] text-on-surface-variant">qr_code_scanner</span>
                                <div>
                                    <p class="text-[12px] font-medium text-white">Authenticator App</p>
                                    <p class="text-[10px] text-on-surface-variant">Google Authenticator</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-1 text-[#00D084] text-[11px]">
                                <span class="material-symbols-outlined text-[14px]">check</span>
                                Configured
                            </div>
                        </div>
                        
                        <button class="w-full py-2 border border-white/10 hover:bg-white/5 rounded-lg text-sm font-medium text-white transition-colors">
                            Manage 2FA
                        </button>
                    </div>

                    <!-- Active Login Sessions -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col">
                        <div class="p-6 pb-4 flex items-center gap-3">
                            <span class="material-symbols-outlined text-[20px] text-primary">devices</span>
                            <div>
                                <h3 class="text-sm font-medium text-white">Active Login Sessions</h3>
                                <p class="text-[11px] text-on-surface-variant mt-0.5">Manage your active sessions across different devices.</p>
                            </div>
                        </div>
                        <div class="divide-y divide-white/5 px-2">
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 rounded-lg transition-colors group">
                                <div class="flex items-center gap-4">
                                    <span class="material-symbols-outlined text-[20px] text-[#63B3ED]">window</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white flex items-center gap-2">
                                            Windows • Chrome 
                                            <span class="text-[9px] bg-primary/20 text-primary px-2 py-0.5 rounded">Current Session</span>
                                        </p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Bhubaneswar, India</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4 text-right">
                                    <span class="text-[10px] text-on-surface-variant">12 May 2024, 10:30 AM</span>
                                    <button class="text-on-surface-variant hover:text-white opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span class="material-symbols-outlined text-[16px]">more_vert</span>
                                    </button>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 rounded-lg transition-colors group">
                                <div class="flex items-center gap-4">
                                    <span class="material-symbols-outlined text-[20px] text-on-surface-variant">smartphone</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Android • Chrome</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Bhubaneswar, India</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4 text-right">
                                    <span class="text-[10px] text-on-surface-variant">11 May 2024, 04:15 PM</span>
                                    <button class="text-on-surface-variant hover:text-white opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span class="material-symbols-outlined text-[16px]">more_vert</span>
                                    </button>
                                </div>
                            </div>
                            <div class="flex items-center justify-between p-4 hover:bg-white/5 rounded-lg transition-colors group">
                                <div class="flex items-center gap-4">
                                    <span class="material-symbols-outlined text-[20px] text-[#63B3ED]">window</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Windows • Edge</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Cuttack, India</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4 text-right">
                                    <span class="text-[10px] text-on-surface-variant">10 May 2024, 09:20 AM</span>
                                    <button class="text-on-surface-variant hover:text-white opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span class="material-symbols-outlined text-[16px]">more_vert</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="p-4 pt-2 border-t border-white/5 mt-2">
                            <button class="text-[12px] text-primary hover:underline flex items-center justify-between w-full">
                                View All Sessions
                                <span class="material-symbols-outlined text-[16px]">chevron_right</span>
                            </button>
                        </div>
                    </div>

                    <!-- Recent Security Activity -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col">
                        <div class="p-6 pb-4 flex items-center gap-3">
                            <span class="material-symbols-outlined text-[20px] text-primary">history</span>
                            <h3 class="text-sm font-medium text-white">Recent Security Activity</h3>
                        </div>
                        <div class="divide-y divide-white/5 px-2">
                            <div class="flex items-start justify-between p-4">
                                <div class="flex gap-4">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant mt-0.5">key</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">Password changed</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Password was successfully updated</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <span class="text-[10px] text-on-surface-variant">12 May 2024, 10:30 AM</span>
                                    <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                </div>
                            </div>
                            <div class="flex items-start justify-between p-4">
                                <div class="flex gap-4">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant mt-0.5">my_location</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">New login detected</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Windows • Chrome • Bhubaneswar, India</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <span class="text-[10px] text-on-surface-variant">12 May 2024, 10:30 AM</span>
                                    <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                </div>
                            </div>
                            <div class="flex items-start justify-between p-4">
                                <div class="flex gap-4">
                                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant mt-0.5">security</span>
                                    <div>
                                        <p class="text-[12px] font-medium text-white">2FA enabled</p>
                                        <p class="text-[10px] text-on-surface-variant mt-0.5">Two-factor authentication was enabled</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-2">
                                    <span class="text-[10px] text-on-surface-variant">10 May 2024, 04:15 PM</span>
                                    <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                </div>
                            </div>
                        </div>
                        <div class="p-4 pt-2 border-t border-white/5 mt-2">
                            <button class="text-[12px] text-primary hover:underline flex items-center justify-between w-full">
                                View Full Activity
                                <span class="material-symbols-outlined text-[16px]">chevron_right</span>
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{security_content}</main>', base_html)
    
    # We will modify the profile menu in the left sidebar to show Security as active
    profile_active_pattern = r'<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-white bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">person</span>\s*Profile Settings\s*</a>'
    profile_inactive = '<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">person</span>\n                    Profile Settings\n                </a>'
    
    security_inactive_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">lock</span>\s*Security\s*</a>'
    security_active = '<a href="admin-security.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-white bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">lock</span>\n                    Security\n                </a>'
    
    if re.search(profile_active_pattern, new_html):
        new_html = re.sub(profile_active_pattern, profile_inactive, new_html)
    
    if re.search(security_inactive_pattern, new_html):
        new_html = re.sub(security_inactive_pattern, security_active, new_html)

    with open('admin-security.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-security.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-security.html':
            update_sidebar_profile_links(filepath)
            print(f"Updated profile sidebar link in {filepath}")
            
    generate_security_page()

if __name__ == '__main__':
    main()
