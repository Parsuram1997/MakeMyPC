import os

with open(r'c:\Projects\MakeMyPC\login.html', 'r', encoding='utf-8') as f:
    c = f.read()

bg_tags = """<body class="flex flex-col min-h-screen">
<!-- Background Layer -->
<div class="fixed inset-0 technical-grid pointer-events-none z-0"></div>
<div class="fixed top-[-10%] right-[-10%] w-[40%] h-[40%] bg-electric-blue/5 rounded-full blur-[120px] pointer-events-none"></div>
<div class="fixed bottom-[-10%] left-[-10%] w-[40%] h-[40%] bg-cyber-teal/5 rounded-full blur-[120px] pointer-events-none"></div>"""

c = c.replace('<body class="bg-surface-deep text-on-surface overflow-hidden">', '')
c = c.replace('<div class="circuit-bg"></div>', bg_tags)

with open(r'c:\Projects\MakeMyPC\login.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done')
