import sys

with open('js/profile.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = "profileRoleBadge.innerHTML = '<span class=\"material-symbols-outlined text-[14px]\">person</span> CUSTOMER';"
new_logic = "profileRoleBadge.innerHTML = '<span class=\"material-symbols-outlined text-[14px]\">workspace_premium</span> ELITE BUILDER';"

old_class = "profileRoleBadge.className = 'bg-green-500/20 border border-green-500 text-green-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';"
new_class = "profileRoleBadge.className = 'bg-electric-blue/20 border border-electric-blue text-electric-blue px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';"

if old_logic in text and old_class in text:
    text = text.replace(old_logic, new_logic).replace(old_class, new_class)
    with open('js/profile.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Reverted customer badge to ELITE BUILDER in profile.js")
else:
    print("Could not find the target string in profile.js")
