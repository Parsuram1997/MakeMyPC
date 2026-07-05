import re

with open('smart-builder.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace main tag
content = content.replace('<main class="pt-24 min-h-screen flex max-w-5xl mx-auto px-8 pb-32">', '<main class="pt-20 min-h-screen flex max-w-container-max mx-auto">\n<div class="flex-1 min-w-0 px-margin-desktop py-6 pb-32">')

# Add aside before </main>
aside_html = """</div>
<!-- Right: SideNavBar (Build Summary) -->
<aside class="hidden md:flex flex-col w-80 lg:w-96 flex-shrink-0 bg-surface-deep/80 backdrop-blur-2xl border border-white/10 sticky top-24 h-[calc(100vh-120px)] rounded-2xl shadow-[0_0_30px_rgba(0,150,255,0.05)] overflow-hidden z-20">
    <!-- Sidebar rendered via JS -->
    <div id="sidebar-root" class="flex flex-col h-full relative"></div>
</aside>
</main>"""

content = content.replace('</div>\n</main>', aside_html)
content = content.replace('</div>\r\n</main>', aside_html)

# If it didn't replace, try a regex
if '<!-- Right: SideNavBar' not in content:
    content = re.sub(r'</div>\s*</main>', aside_html, content)

# Add script tags
script_html = """<script>
// Mock steps for builder-sidebar.js so it can calculate price correctly
const steps = [
    { id: 'cpu', label: 'CPU', key: 'cpu' },
    { id: 'mobo', label: 'Motherboard', key: 'mobo' },
    { id: 'ram', label: 'Memory', key: 'ram' },
    { id: 'gpu', label: 'Graphics', key: 'gpu' },
    { id: 'ssd', label: 'SSD', key: 'ssd' },
    { id: 'hdd', label: 'HDD', key: 'hdd' },
    { id: 'cooler', label: 'Cooler', key: 'cooler' },
    { id: 'psu', label: 'Power Supply', key: 'psu' },
    { id: 'case', label: 'Cabinet', key: 'case' },
    { id: 'fans', label: 'Fans/RGB', key: 'fans' },
    { id: 'accessories', label: 'Accessories', key: 'accessories' }
];
const state = {
    currentStepIndex: 0,
    selections: {}
};
</script>
<script src="js/builder-sidebar.js"></script>
<script src="js/auth-utils.js"></script>"""

content = content.replace('<script src="js/auth-utils.js"></script>', script_html)

with open('smart-builder.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated smart-builder.html layout")
