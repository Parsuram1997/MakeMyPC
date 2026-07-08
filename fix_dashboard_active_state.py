import os
import re

files_to_fix = [
    r"c:\Projects\MakeMyPC\admin-dashboard.html",
    r"c:\Projects\MakeMyPC\admin-dashboard-overview.html"
]

for fpath in files_to_fix:
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Make the dashboard link active
    new_content = content.replace(
        'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\n            <span class="material-symbols-outlined">dashboard</span>',
        'class="flex items-center gap-3 px-4 py-1.5 rounded-xl transition-all duration-300 bg-primary/10 text-primary">\n            <span class="material-symbols-outlined">dashboard</span>'
    )
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed active state in {os.path.basename(fpath)}")
    else:
        print(f"No changes needed for {os.path.basename(fpath)}")
