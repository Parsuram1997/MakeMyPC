import re

with open(r'c:\Projects\MakeMyPC\custom-pc-builder.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything inside <aside> ... </aside> with an empty container
aside_pattern = re.compile(r'<aside[^>]*>.*?</aside>', re.DOTALL)
new_aside = '''<aside class="hidden md:flex flex-col w-80 lg:w-96 flex-shrink-0 bg-surface-deep/80 backdrop-blur-2xl border border-white/10 sticky top-24 h-[calc(100vh-120px)] rounded-2xl shadow-[0_0_30px_rgba(0,150,255,0.05)] overflow-hidden z-20">
    <!-- Sidebar rendered via JS -->
    <div id="sidebar-root" class="flex flex-col h-full overflow-y-auto custom-scrollbar relative"></div>
</aside>'''

new_html = aside_pattern.sub(new_aside, html)

with open(r'c:\Projects\MakeMyPC\custom-pc-builder.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Replaced aside in HTML')
