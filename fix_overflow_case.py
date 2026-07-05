import re

sidebar_file = "c:/Projects/MakeMyPC/js/builder-sidebar.js"
with open(sidebar_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Change to sentence case
content = content.replace(
    '<strong class="block text-[11px] uppercase tracking-wider mb-1">Power Bottleneck Detected</strong>',
    '<strong class="block text-[12px] mb-1">Power bottleneck detected</strong>'
)
content = content.replace(
    '<button onclick="window.goToStep(7)" class="mt-2 px-3 py-1.5 bg-error/20 hover:bg-error/30 rounded text-[9px] font-bold tracking-widest transition-colors uppercase w-full">Upgrade PSU</button>',
    '<button onclick="window.goToStep(7)" class="mt-2 px-3 py-1.5 bg-error/20 hover:bg-error/30 rounded text-[11px] font-bold transition-colors w-full">Upgrade PSU</button>'
)

# 2. Fix the overflow issue and uppercase in the main box
old_html = """            <!-- Compatibility Status -->
            <div class="${compatBg} rounded-xl p-4 relative overflow-hidden group transition-all duration-300">
                <div class="absolute -right-6 -top-6 w-24 h-24 bg-${compatColor.split('-')[1]}/10 rounded-full blur-2xl group-hover:bg-${compatColor.split('-')[1]}/20 transition-all"></div>
                
                <div class="flex items-center gap-3 mb-3 relative z-10">
                    <span class="material-symbols-outlined text-2xl ${compatColor}">${compatIcon}</span>
                    <h3 class="font-headline-sm text-sm uppercase tracking-widest ${compatColor}">Compatibility ${compatStatus}</h3>
                </div>"""

new_html = """            <!-- Compatibility Status -->
            <div class="${compatBg} rounded-xl p-4 relative group transition-all duration-300">
                <div class="absolute inset-0 overflow-hidden rounded-xl pointer-events-none">
                    <div class="absolute -right-6 -top-6 w-24 h-24 bg-${compatColor.split('-')[1]}/10 rounded-full blur-2xl group-hover:bg-${compatColor.split('-')[1]}/20 transition-all"></div>
                </div>
                
                <div class="flex items-center gap-3 mb-3 relative z-10">
                    <span class="material-symbols-outlined text-2xl ${compatColor}">${compatIcon}</span>
                    <h3 class="font-headline-sm text-sm ${compatColor}">Compatibility: ${compatStatus}</h3>
                </div>"""

content = content.replace(old_html, new_html)

with open(sidebar_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Compatibility Warning UI with sentence case and fixed overflow.")
