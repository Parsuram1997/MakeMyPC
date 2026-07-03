import re

right_nav_full = '''<div class="flex items-center gap-x-6">
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
</div>'''

for file in ['builder-landing.html', 'smart-builder.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The existing right nav is probably just:
    # <div class="flex items-center gap-x-6">
    # <div class="flex gap-x-4">
    # ...
    # </div>
    # </div>
    # Let's replace the whole block up to </nav>
    
    # We'll use a regex that captures from <div class="flex items-center gap-x-6"> to the closing </div></div> of the nav, or just replace it.
    old_nav = re.search(r'(<div class="flex items-center gap-x-6">.*?</div>\s*</div>)', content, re.DOTALL)
    if old_nav:
        new_content = content.replace(old_nav.group(1), right_nav_full)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
