import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the bottom profile section
    # Now it starts with <div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4 pb-4">
    pattern = r'<div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4 pb-4">.*?</aside>'
    
    new_widget = """<div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4 pb-4">
        <details class="group" name="sidebar-profile-menu">
            <summary class="list-none outline-none">
                <div class="flex items-center justify-between p-3 rounded-t-xl group-open:bg-white/[0.02] bg-surface-container border border-white/5 group-open:border-b-0 hover:bg-white/5 transition-colors cursor-pointer group-open:rounded-b-none rounded-b-xl">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-[#B3D4FF] text-[#0A1929] flex items-center justify-center font-bold text-sm">AD</div>
                        <div class="overflow-hidden">
                            <p class="text-xs font-bold text-white truncate mb-0.5">Admin Profile</p>
                            <p class="text-[10px] text-on-surface-variant truncate mb-1">Super Admin</p>
                            <div class="flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                <span class="text-[9px] text-[#00D084]/70">Online</span>
                            </div>
                        </div>
                    </div>
                    <span class="material-symbols-outlined text-[18px] text-on-surface-variant group-open:rotate-180 transition-transform">expand_more</span>
                </div>
            </summary>
            
            <div class="bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl p-2 flex flex-col gap-0.5">
                <a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">person</span>
                    Profile Settings
                </a>
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">lock</span>
                    Security
                </a>
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">settings</span>
                    Preferences
                </a>
                <div class="h-[1px] bg-white/5 my-1 mx-2"></div>
                <a href="add_global_logout.py" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-[#F87171] hover:bg-[#F87171]/10 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">logout</span>
                    Sign out
                </a>
            </div>
        </details>
    </div>
</aside>"""

    if file == 'admin-profile.html':
        # Automatically open the widget on admin-profile.html
        new_widget = new_widget.replace('<details class="group"', '<details class="group" open')
        # Highlight active menu
        new_widget = new_widget.replace(
            '<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">',
            '<a href="admin-profile.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-[11px] font-medium text-white bg-white/5 transition-colors">'
        )

    new_content = re.sub(pattern, new_widget, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated sidebar profile in {file}")

print("Sidebar profile widget update complete.")
