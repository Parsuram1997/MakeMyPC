import sys

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_badge = """<span class="bg-electric-blue/20 border border-electric-blue text-electric-blue px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1">
                                    <span class="material-symbols-outlined text-[14px]">workspace_premium</span> Elite Builder
                                </span>"""

new_badge = """<span id="profile-role-badge" class="bg-electric-blue/20 border border-electric-blue text-electric-blue px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1">
                                    <span class="material-symbols-outlined text-[14px]">workspace_premium</span> Elite Builder
                                </span>"""

if old_badge in text:
    text = text.replace(old_badge, new_badge)
    with open('account-settings.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added profile-role-badge ID successfully.")
else:
    print("Could not find the role badge in account-settings.html")
