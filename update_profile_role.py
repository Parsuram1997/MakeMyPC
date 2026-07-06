import sys

with open('js/profile.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add variable for profile-role-badge
if "const profileRoleBadge = document.getElementById('profile-role-badge');" not in text:
    text = text.replace(
        "const profileDisplayName = document.getElementById('profile-display-name');",
        "const profileDisplayName = document.getElementById('profile-display-name');\n    const profileRoleBadge = document.getElementById('profile-role-badge');"
    )

# 2. Add logic to update the badge based on role
logic = """
                    if (profileRoleBadge && data.role) {
                        if (data.role === 'admin') {
                            profileRoleBadge.innerHTML = '<span class="material-symbols-outlined text-[14px]">admin_panel_settings</span> SYSTEM ADMIN';
                            profileRoleBadge.className = 'bg-red-500/20 border border-red-500 text-red-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';
                        } else if (data.role === 'customer') {
                            profileRoleBadge.innerHTML = '<span class="material-symbols-outlined text-[14px]">person</span> CUSTOMER';
                            profileRoleBadge.className = 'bg-green-500/20 border border-green-500 text-green-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';
                        }
                    }
"""

if "profileRoleBadge && data.role" not in text:
    text = text.replace(
        "if (data.name) {",
        logic.strip() + "\n                    if (data.name) {"
    )
    
    with open('js/profile.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated profile.js to dynamically render role badge.")
else:
    print("profile.js already has role logic.")
