import os
import glob

directory = "c:/Projects/MakeMyPC/"
html_files = glob.glob(os.path.join(directory, "*.html"))

target_block = """            <!-- Social Links -->
            <div class="flex gap-4">
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="text-lg font-bold">f</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="material-symbols-outlined text-lg">photo_camera</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="text-lg font-bold">X</span>
                </a>
            </div>"""

replacement_block = """            <!-- Social Links -->
            <div class="flex gap-4">
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center hover:bg-white/10 transition-all group">
                    <img src="https://cdn.simpleicons.org/facebook/1877F2" alt="Facebook" class="h-5 opacity-70 group-hover:opacity-100 transition-opacity">
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center hover:bg-white/10 transition-all group">
                    <img src="https://cdn.simpleicons.org/instagram/E4405F" alt="Instagram" class="h-5 opacity-70 group-hover:opacity-100 transition-opacity">
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center hover:bg-white/10 transition-all group">
                    <img src="https://cdn.simpleicons.org/x/FFFFFF" alt="X (Twitter)" class="h-4 opacity-70 group-hover:opacity-100 transition-opacity">
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center hover:bg-white/10 transition-all group">
                    <img src="https://cdn.simpleicons.org/youtube/FF0000" alt="YouTube" class="h-5 opacity-70 group-hover:opacity-100 transition-opacity">
                </a>
            </div>"""

count = 0
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if target_block in content:
        new_content = content.replace(target_block, replacement_block)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Successfully updated social icons in {count} HTML files.")
