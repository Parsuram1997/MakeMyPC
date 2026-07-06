import sys

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add the Admin Dashboard Link to the sidebar
admin_link = """
                    <a id="admin-dashboard-link" href="admin-dashboard.html" class="w-full flex items-center gap-3 px-4 py-3 mt-2 rounded-lg text-green-500 hover:bg-green-500/10 transition-all border border-green-500/20" style="display:none;">
                        <span class="material-symbols-outlined">admin_panel_settings</span>
                        <span class="font-headline-sm text-headline-sm">Admin Dashboard</span>
                    </a>
"""

if '<a id="admin-dashboard-link"' not in text:
    text = text.replace(
        '<button class="w-full flex items-center gap-3 px-4 py-3 mt-4 rounded-lg text-error hover:bg-error/10 transition-all border border-error/20"',
        admin_link.strip() + '\n                    <button class="w-full flex items-center gap-3 px-4 py-3 mt-2 rounded-lg text-error hover:bg-error/10 transition-all border border-error/20"'
    )
    with open('account-settings.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added admin dashboard link to account-settings.html sidebar.")
else:
    print("Admin dashboard link already exists in account-settings.html.")

with open('js/profile.js', 'r', encoding='utf-8') as f:
    profile_text = f.read()

# 2. Update profile.js to show it
if "const adminDashboardLink = document.getElementById('admin-dashboard-link');" not in profile_text:
    profile_text = profile_text.replace(
        "const profileRoleBadge = document.getElementById('profile-role-badge');",
        "const profileRoleBadge = document.getElementById('profile-role-badge');\n    const adminDashboardLink = document.getElementById('admin-dashboard-link');"
    )

if "if (adminDashboardLink) adminDashboardLink.style.display = 'flex';" not in profile_text:
    profile_text = profile_text.replace(
        "profileRoleBadge.className = 'bg-red-500/20 border border-red-500 text-red-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';",
        "profileRoleBadge.className = 'bg-red-500/20 border border-red-500 text-red-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';\n                            if (adminDashboardLink) adminDashboardLink.style.display = 'flex';"
    )
    with open('js/profile.js', 'w', encoding='utf-8') as f:
        f.write(profile_text)
    print("Updated profile.js to show admin dashboard link.")
else:
    print("profile.js already has the logic to show admin dashboard link.")
