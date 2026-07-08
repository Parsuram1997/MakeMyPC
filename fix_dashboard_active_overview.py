import re

with open('admin-dashboard-overview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix "Dashboard" link to be inactive
text = re.sub(
    r'<a href="admin-dashboard\.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 bg-primary/10 text-primary">\s*<span class="material-symbols-outlined">dashboard</span>\s*<span class="text-body-sm font-medium">Dashboard</span>\s*</a>',
    '<a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\\n            <span class="material-symbols-outlined">dashboard</span>\\n            <span class="text-body-sm font-medium">Dashboard</span>\\n        </a>',
    text,
    flags=re.DOTALL
)

with open('admin-dashboard-overview.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed Dashboard active state in admin-dashboard-overview.html")
