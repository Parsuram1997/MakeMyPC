import os
import glob

master_nav = """<nav class="fixed top-0 w-full z-50 bg-surface-glass backdrop-blur-xl border-b border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.3)]">
<div class="flex justify-between items-center max-w-container-max mx-auto px-margin-desktop h-20">
<a href="index.html" class="text-headline-lg font-headline-lg font-black text-on-surface tracking-tighter">MakeMyPC</a>
<div class="hidden md:flex gap-x-8 items-center">
<a class="text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono" href="prebuilt-pcs.html">Shop</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono" href="custom-pc-builder.html">Builder</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono" href="support-faq.html">Resources</a>
</div>
<div class="flex items-center gap-x-6">
<div class="relative hidden lg:block">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
<input class="bg-surface-container-low border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-body-sm font-body-sm focus:outline-none focus:border-electric-blue w-64 transition-all" placeholder="Search Components" type="text"/>
</div>
<div class="flex gap-x-4">
<button class="text-on-surface-variant hover:text-primary transition-colors active:scale-95 duration-100 relative" onclick="window.location.href='shopping-cart.html'">
<span class="material-symbols-outlined" data-icon="shopping_cart">shopping_cart</span>
<span id="cart-badge" class="absolute -top-1 -right-1 bg-error text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center hidden">0</span>
</button>
<a href="login.html" id="auth-login-btn" class="text-on-surface-variant hover:text-primary transition-colors active:scale-95 duration-100 flex items-center">
<span class="material-symbols-outlined" data-icon="account_circle">account_circle</span>
</a>
<a href="account-settings.html" id="auth-avatar-btn" class="hidden w-8 h-8 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold text-sm hover:brightness-110 transition-all">
<span id="avatar-initial">U</span>
</a>
</div>
</div>
</div>
</nav>"""

active_class = 'text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-label-mono'
inactive_class = 'text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono'

active_map = {
    'index.html': None,
    'prebuilt-pcs.html': 'Shop',
    'product-details.html': 'Shop',
    'custom-pc-builder.html': 'Builder',
    'support-faq.html': 'Resources',
    'submit-ticket.html': 'Resources',
    'ticket-submitted.html': 'Resources',
    'order-tracking.html': 'Resources',
    'calculators-tools.html': 'Resources'
}

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')

for file in html_files:
    basename = os.path.basename(file)
    active_item = active_map.get(basename)
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    start_nav = content.find('<nav')
    if start_nav != -1:
        end_nav = content.find('</nav>', start_nav)
        
        # Inject master nav
        content = content[:start_nav] + master_nav + content[end_nav+6:]
        
        # Apply active states
        if active_item == 'Shop':
            content = content.replace(f'<a class="{inactive_class}" href="prebuilt-pcs.html">Shop</a>', f'<a class="{active_class}" href="prebuilt-pcs.html">Shop</a>')
        elif active_item == 'Builder':
            content = content.replace(f'<a class="{inactive_class}" href="custom-pc-builder.html">Builder</a>', f'<a class="{active_class}" href="custom-pc-builder.html">Builder</a>')
        elif active_item == 'Resources':
            content = content.replace(f'<a class="{inactive_class}" href="support-faq.html">Resources</a>', f'<a class="{active_class}" href="support-faq.html">Resources</a>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Master nav applied everywhere")
