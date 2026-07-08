import os
import re
import shutil

PAGES_DIR = r"c:\Projects\MakeMyPC"
html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]

# 1. Update the Analytics link in all HTML files
count = 0
for fname in html_files:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to replace href="#" with href="admin-analytics.html" strictly for the Analytics link
    # We can match the Analytics block
    def fix_analytics_link(match):
        block = match.group(0)
        return block.replace('href="#"', 'href="admin-analytics.html"')

    new_content = re.sub(
        r'<a[^>]*href="#"[^>]*>\s*<span[^>]*>analytics</span>\s*<span[^>]*>Analytics</span>\s*</a>',
        fix_analytics_link,
        content,
        flags=re.IGNORECASE
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        print(f"Fixed Analytics link in {fname}")

print(f"Total files updated: {count}")

# 2. Create admin-analytics.html if it doesn't exist
analytics_path = os.path.join(PAGES_DIR, "admin-analytics.html")
if not os.path.exists(analytics_path):
    print("Creating admin-analytics.html...")
    # Use admin_template.html as base
    with open(os.path.join(PAGES_DIR, 'admin_template.html'), 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Fix the active states
    template = template.replace('<title>MakeMyPC Admin</title>', '<title>Analytics | MakeMyPC Admin</title>')
    
    # Remove Dashboard active state
    template = re.sub(
        r'<a href="admin-dashboard\.html" class="flex items-center gap-3 px-4 py-1\.5 rounded-xl transition-all duration-300 text-primary bg-primary/10 hover:bg-white/5 hover:text-primary">',
        '<a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">',
        template
    )
    
    # Make Analytics active
    template = re.sub(
        r'<a href="admin-analytics\.html" class="flex items-center gap-3 px-4 py-1\.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\s*<span class="material-symbols-outlined">analytics</span>\s*<span class="text-body-sm font-medium">Analytics</span>\s*</a>',
        '<a href="admin-analytics.html" class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 bg-primary/10 text-primary">\n            <span class="material-symbols-outlined">analytics</span>\n            <span class="text-body-sm font-medium">Analytics</span>\n        </a>',
        template
    )
    
    main_content = """
    <div class="w-full space-y-6">
        <div class="flex items-center justify-between mt-2">
            <div>
                <h1 class="text-2xl font-bold text-white mb-1">Analytics Overview</h1>
                <p class="text-sm text-on-surface-variant">View all key performance indicators and reports.</p>
            </div>
        </div>
        <div class="bg-surface-deep border border-white/5 rounded-xl p-8 text-center mt-6">
            <span class="material-symbols-outlined text-4xl text-primary mb-4 block">query_stats</span>
            <h2 class="text-xl text-white font-medium">Advanced Analytics</h2>
            <p class="text-on-surface-variant mt-2 max-w-md mx-auto">This section is currently under development. Detailed revenue and traffic analytics will be available here soon.</p>
        </div>
    </div>
    """
    
    final_html = template.replace('<!-- INSERT CONTENT HERE -->', main_content)
    with open(analytics_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Created admin-analytics.html")
