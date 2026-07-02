with open(r'c:\Projects\MakeMyPC\custom-pc-builder.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Make header compact
c = c.replace('<div class="mb-8">\n<h2 class="text-headline-sm', '<div class="mb-4">\n<h2 class="text-headline-sm')

# Make sections closer
c = c.replace('<div class="space-y-6 mb-8 flex-1">', '<div class="space-y-4 mb-4 flex-1">')

# Price size
c = c.replace('id="sidebar-total-price" class="text-headline-lg font-headline-lg text-primary tracking-tighter"', 'id="sidebar-total-price" class="text-headline-md font-headline-md text-primary tracking-tighter"')

# Performance space
c = c.replace('<div class="space-y-3">\n<div class="flex justify-between items-center">\n<span class="text-label-mono text-on-surface-variant uppercase text-[10px]">Est. 4K Performance</span>', '<div class="space-y-2">\n<div class="flex justify-between items-center">\n<span class="text-label-mono text-on-surface-variant uppercase text-[10px]">Est. 4K Performance</span>')

# Selection list top padding
c = c.replace('<div class="pt-6 border-t border-white/5">\n<span class="text-label-mono text-on-surface-variant uppercase text-[10px] mb-4 block">Selection List</span>', '<div class="pt-4 border-t border-white/5">\n<span class="text-label-mono text-on-surface-variant uppercase text-[10px] mb-2 block">Selection List</span>')

# Selection list spacing
c = c.replace('<ul id="sidebar-selection-list" class="space-y-3">', '<ul id="sidebar-selection-list" class="space-y-1.5">')

# Checkout section top padding
c = c.replace('<div class="mt-auto pt-6 border-t border-white/10 space-y-4">', '<div class="mt-auto pt-4 border-t border-white/10 space-y-2">')

# Checkout button padding
c = c.replace('id="sidebar-checkout-btn" class="w-full bg-electric-blue text-white py-4', 'id="sidebar-checkout-btn" class="w-full bg-electric-blue text-white py-3')

with open(r'c:\Projects\MakeMyPC\custom-pc-builder.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated HTML')
