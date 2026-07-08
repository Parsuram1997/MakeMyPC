import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

NEW_PROFILE_BLOCK = """</nav>

    <div class="mt-auto px-4 shrink-0 border-t border-white/5 pt-4 pb-4">
        <details class="group" name="sidebar-profile-menu">
            <summary class="list-none outline-none">
                <div class="flex items-center justify-between p-3 rounded-xl group-open:bg-white/[0.02] bg-surface-container border border-white/5 group-open:border-b-0 hover:bg-white/5 transition-colors cursor-pointer group-open:rounded-b-none">
                    <div class="flex items-center gap-3">
                        <div class="w-9 h-9 rounded-full bg-[#B3D4FF] text-[#0A1929] flex items-center justify-center font-bold text-sm">AD</div>
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
            <div class="bg-surface-container/50 border border-white/5 border-t-0 rounded-b-xl p-1.5 flex flex-col gap-0.5">
                <a href="admin-profile.html" class="flex items-center gap-3 px-3 py-1.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">person</span>
                    Profile Settings
                </a>
                <a href="admin-security.html" class="flex items-center gap-3 px-3 py-1.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">lock</span>
                    Security
                </a>
                <a href="admin-preferences.html" class="flex items-center gap-3 px-3 py-1.5 rounded-lg text-[11px] font-medium text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">settings</span>
                    Preferences
                </a>
                <div class="h-[1px] bg-white/5 my-1 mx-2"></div>
                <a href="index.html" class="flex items-center gap-3 px-3 py-1.5 rounded-lg text-[11px] font-medium text-[#F87171] hover:bg-[#F87171]/10 transition-colors">
                    <span class="material-symbols-outlined text-[16px]">logout</span>
                    Sign out
                </a>
            </div>
        </details>
    </div>
</aside>"""

count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace from </nav> to </aside>
    new_content = re.sub(
        r'</nav>\s*<div class="mt-auto px-4.*?</aside>',
        NEW_PROFILE_BLOCK,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Fixed Admin Profile section in {fname}")

print(f"Total files updated: {count}")
