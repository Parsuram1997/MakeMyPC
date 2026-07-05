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
<div class="flex items-center gap-x-4 md:gap-x-6">
<div class="relative hidden lg:block">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
<input class="bg-surface-container-low border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-body-sm font-body-sm focus:outline-none focus:border-electric-blue w-64 transition-all" placeholder="Search Components" type="text"/>
</div>
<div class="flex gap-x-2 md:gap-x-4">
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
<!-- Hamburger Menu Button -->
<button id="mobile-menu-btn" class="md:hidden text-on-surface-variant hover:text-primary transition-colors active:scale-95 duration-100 flex items-center pl-2">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
</div>
</div>
</nav>

<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-[#00081C]/95 backdrop-blur-xl z-[60] transform translate-x-full transition-transform duration-300 md:hidden flex flex-col">
    <div class="flex justify-between items-center p-6 border-b border-white/10">
        <span class="text-xl font-black text-white tracking-tighter">Menu</span>
        <button id="mobile-menu-close" class="text-on-surface-variant hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">close</span>
        </button>
    </div>
    <div class="flex flex-col gap-6 p-6 overflow-y-auto">
        <!-- Search -->
        <div class="relative w-full">
            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
            <input class="bg-surface-container-low border border-white/10 rounded-lg pl-10 pr-4 py-3 text-body-sm focus:outline-none focus:border-primary w-full transition-all text-white placeholder:text-on-surface-variant/50" placeholder="Search Components" type="text"/>
        </div>
        
        <div class="flex flex-col gap-4 border-b border-white/10 pb-6">
            <a href="prebuilt-pcs.html" class="text-lg font-bold text-white hover:text-primary flex justify-between items-center">
                Shop <span class="material-symbols-outlined text-sm">chevron_right</span>
            </a>
            <a href="builder-landing.html" class="text-lg font-bold text-white hover:text-primary flex justify-between items-center">
                Builder <span class="material-symbols-outlined text-sm">chevron_right</span>
            </a>
            <a href="support-faq.html" class="text-lg font-bold text-white hover:text-primary flex justify-between items-center">
                Resources <span class="material-symbols-outlined text-sm">chevron_right</span>
            </a>
        </div>
    </div>
</div>

<script>
    // Mobile Menu Logic
    document.addEventListener('DOMContentLoaded', () => {
        const menuBtn = document.getElementById('mobile-menu-btn');
        const closeBtn = document.getElementById('mobile-menu-close');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (menuBtn && closeBtn && mobileMenu) {
            menuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-full');
            });
            closeBtn.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
            });
        }
    });
</script>
"""

active_class = 'text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-label-mono'
inactive_class = 'text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono'

active_map = {
    'index.html': None,
    'prebuilt-pcs.html': 'Shop',
    'product-details.html': 'Shop',
    'builder-landing.html': 'Builder',
    'custom-pc-builder.html': 'Builder',
    'smart-builder.html': 'Builder',
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
        
        # Check if mobile menu is already there and remove it to avoid duplicates
        next_tag_start = content.find('<!-- Mobile Menu Overlay -->', end_nav)
        if next_tag_start != -1 and (next_tag_start - end_nav) < 50:
            end_script = content.find('</script>', next_tag_start)
            # Find the end of the mobile menu script block
            replacement_end = end_script + 9 if end_script != -1 else end_nav + 6
        else:
            replacement_end = end_nav + 6
            
        # Inject master nav
        content = content[:start_nav] + master_nav + content[replacement_end:]
        
        # Apply active states
        if active_item == 'Shop':
            content = content.replace(f'<a class="{inactive_class}" href="prebuilt-pcs.html">Shop</a>', f'<a class="{active_class}" href="prebuilt-pcs.html">Shop</a>')
        elif active_item == 'Builder':
            content = content.replace(f'<a class="{inactive_class}" href="custom-pc-builder.html">Builder</a>', f'<a class="{active_class}" href="custom-pc-builder.html">Builder</a>')
        elif active_item == 'Resources':
            content = content.replace(f'<a class="{inactive_class}" href="support-faq.html">Resources</a>', f'<a class="{active_class}" href="support-faq.html">Resources</a>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print(f"Master nav with mobile menu applied to {len(html_files)} files")
