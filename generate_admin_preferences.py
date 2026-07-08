import os
import glob
import re

def update_sidebar_profile_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Preferences link in the bottom profile menu
    preferences_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">settings</span>\s*Preferences\s*</a>'
    new_preferences = '<a href="admin-preferences.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">settings</span>\n                    Preferences\n                </a>'
    
    if re.search(preferences_pattern, content):
        content = re.sub(preferences_pattern, new_preferences, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_preferences_page():
    base_file = 'admin-profile.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    preferences_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div>
                    <h2 class="text-2xl font-bold text-white mb-1">Preferences</h2>
                    <p class="text-on-surface-variant text-sm">Manage your account preferences and application settings.</p>
                </div>
                <div>
                    <button class="bg-primary hover:bg-primary-hover text-on-primary px-4 py-2 rounded-lg text-sm font-medium transition-colors flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">check</span>
                        Save Changes
                    </button>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="grid grid-cols-[280px_1fr] gap-6 relative z-10">
                
                <!-- Left Column: Preferences Navigation -->
                <div class="flex flex-col gap-2">
                    <button class="flex items-start gap-4 p-4 rounded-xl bg-primary-container/10 border-l-2 border-primary text-left transition-colors">
                        <span class="material-symbols-outlined text-[20px] text-primary mt-0.5">settings</span>
                        <div>
                            <p class="text-[13px] font-medium text-primary">General</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Basic app preferences</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">palette</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Appearance</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Theme and display</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">notifications</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Notifications</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Email and in-app alerts</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">language</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Language & Region</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Language and timezone</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">dashboard</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Dashboard</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Dashboard preferences</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">shield</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Privacy</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Privacy and data</p>
                        </div>
                    </button>
                    
                    <button class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 border-l-2 border-transparent text-left transition-colors group">
                        <span class="material-symbols-outlined text-[20px] text-on-surface-variant group-hover:text-white mt-0.5">tune</span>
                        <div>
                            <p class="text-[13px] font-medium text-white">Advanced</p>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Advanced preferences</p>
                        </div>
                    </button>
                </div>

                <!-- Right Column: Settings Content -->
                <div class="flex flex-col gap-6">
                    
                    <!-- General Preferences -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30">
                        <div class="p-6 border-b border-white/5">
                            <h3 class="text-sm font-medium text-white">General Preferences</h3>
                            <p class="text-[11px] text-on-surface-variant mt-0.5">Configure general settings for your account and application.</p>
                        </div>
                        
                        <div class="p-6 flex flex-col gap-6">
                            <div class="flex items-center justify-between gap-8 pb-6 border-b border-white/5">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Default Dashboard</h4>
                                    <p class="text-[10px] text-on-surface-variant">Choose your default landing page after login.</p>
                                </div>
                                <div class="w-64 relative">
                                    <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-4 py-2.5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                        <option>Dashboard</option>
                                        <option>Products</option>
                                        <option>Orders</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[18px] text-on-surface-variant pointer-events-none">expand_more</span>
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8 pb-6 border-b border-white/5">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Items Per Page</h4>
                                    <p class="text-[10px] text-on-surface-variant">Select how many items to display in lists.</p>
                                </div>
                                <div class="w-64 relative">
                                    <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-4 py-2.5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                        <option>10</option>
                                        <option>25</option>
                                        <option>50</option>
                                        <option>100</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[18px] text-on-surface-variant pointer-events-none">expand_more</span>
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8 pb-6 border-b border-white/5">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Date Format</h4>
                                    <p class="text-[10px] text-on-surface-variant">Choose your preferred date format.</p>
                                </div>
                                <div class="w-64 relative">
                                    <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-4 py-2.5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                        <option>12 May 2024 (DD MMM YYYY)</option>
                                        <option>05/12/2024 (MM/DD/YYYY)</option>
                                        <option>2024-05-12 (YYYY-MM-DD)</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[18px] text-on-surface-variant pointer-events-none">expand_more</span>
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8 pb-6 border-b border-white/5">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Time Format</h4>
                                    <p class="text-[10px] text-on-surface-variant">Choose your preferred time format.</p>
                                </div>
                                <div class="w-64 flex items-center gap-6">
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="time_format" checked class="w-4 h-4 text-primary bg-surface-deep/50 border-white/20 focus:ring-primary focus:ring-offset-surface-deep focus:ring-offset-2">
                                        <span class="text-[12px] text-white">12 Hour (AM/PM)</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="time_format" class="w-4 h-4 text-primary bg-surface-deep/50 border-white/20 focus:ring-primary focus:ring-offset-surface-deep focus:ring-offset-2">
                                        <span class="text-[12px] text-white">24 Hour</span>
                                    </label>
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8 pb-6 border-b border-white/5">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Timezone</h4>
                                    <p class="text-[10px] text-on-surface-variant">Select your timezone.</p>
                                </div>
                                <div class="w-64 relative">
                                    <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-4 py-2.5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                        <option>(GMT+05:30) Asia/Kolkata</option>
                                        <option>(GMT+00:00) UTC</option>
                                        <option>(GMT-05:00) Eastern Time</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[18px] text-on-surface-variant pointer-events-none">expand_more</span>
                                </div>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8">
                                <div class="flex-1">
                                    <h4 class="text-[12px] font-medium text-white mb-1">Default Currency</h4>
                                    <p class="text-[10px] text-on-surface-variant">Select your default currency.</p>
                                </div>
                                <div class="w-64 relative">
                                    <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-4 py-2.5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                        <option>INR (₹)</option>
                                        <option>USD ($)</option>
                                        <option>EUR (€)</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[18px] text-on-surface-variant pointer-events-none">expand_more</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Other Preferences -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30">
                        <div class="p-6 border-b border-white/5">
                            <h3 class="text-sm font-medium text-white">Other Preferences</h3>
                        </div>
                        
                        <div class="p-6 flex flex-col gap-6">
                            <div class="flex items-center justify-between gap-8">
                                <div class="flex items-center gap-4 flex-1">
                                    <div class="w-10 h-10 rounded-lg bg-white/5 text-on-surface-variant border border-white/5 flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-[20px]">aspect_ratio</span>
                                    </div>
                                    <div>
                                        <h4 class="text-[12px] font-medium text-white mb-0.5">Enable Compact Mode</h4>
                                        <p class="text-[10px] text-on-surface-variant">Reduce spacing for more content on screen.</p>
                                    </div>
                                </div>
                                <label class="relative inline-flex items-center cursor-pointer">
                                    <input type="checkbox" value="" class="sr-only peer">
                                    <div class="w-11 h-6 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
                                </label>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8">
                                <div class="flex items-center gap-4 flex-1">
                                    <div class="w-10 h-10 rounded-lg bg-white/5 text-on-surface-variant border border-white/5 flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-[20px]">animation</span>
                                    </div>
                                    <div>
                                        <h4 class="text-[12px] font-medium text-white mb-0.5">Enable Animations</h4>
                                        <p class="text-[10px] text-on-surface-variant">Show UI animations and transitions.</p>
                                    </div>
                                </div>
                                <label class="relative inline-flex items-center cursor-pointer">
                                    <input type="checkbox" value="" class="sr-only peer" checked>
                                    <div class="w-11 h-6 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
                                </label>
                            </div>
                            
                            <div class="flex items-center justify-between gap-8">
                                <div class="flex items-center gap-4 flex-1">
                                    <div class="w-10 h-10 rounded-lg bg-white/5 text-on-surface-variant border border-white/5 flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-[20px]">lightbulb</span>
                                    </div>
                                    <div>
                                        <h4 class="text-[12px] font-medium text-white mb-0.5">Show Hints & Tips</h4>
                                        <p class="text-[10px] text-on-surface-variant">Display helpful tips and suggestions.</p>
                                    </div>
                                </div>
                                <label class="relative inline-flex items-center cursor-pointer">
                                    <input type="checkbox" value="" class="sr-only peer" checked>
                                    <div class="w-11 h-6 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
                                </label>
                            </div>
                        </div>
                        
                        <div class="p-4 border-t border-white/5 bg-primary-container/5 m-4 rounded-lg flex items-center gap-3">
                            <span class="material-symbols-outlined text-primary text-[18px]">info</span>
                            <span class="text-[11px] text-primary font-medium">These preferences are only applied to your account and device.</span>
                        </div>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{preferences_content}</main>', base_html)
    
    # We will modify the profile menu in the left sidebar to show Preferences as active
    profile_active_pattern = r'<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-white bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">person</span>\s*Profile Settings\s*</a>'
    profile_inactive = '<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">person</span>\n                    Profile Settings\n                </a>'
    
    preferences_inactive_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-\[11px\] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">\s*<span class="material-symbols-outlined text-\[16px\]">settings</span>\s*Preferences\s*</a>'
    preferences_active = '<a href="admin-preferences.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-white bg-white/5 transition-colors">\n                    <span class="material-symbols-outlined text-[16px]">settings</span>\n                    Preferences\n                </a>'
    
    if re.search(profile_active_pattern, new_html):
        new_html = re.sub(profile_active_pattern, profile_inactive, new_html)
    
    if re.search(preferences_inactive_pattern, new_html):
        new_html = re.sub(preferences_inactive_pattern, preferences_active, new_html)

    with open('admin-preferences.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-preferences.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-preferences.html':
            update_sidebar_profile_links(filepath)
            print(f"Updated profile sidebar link in {filepath}")
            
    generate_preferences_page()

if __name__ == '__main__':
    main()
