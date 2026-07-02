import os
import glob
import re

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')

new_auth_icons = '''<div class="flex gap-x-4">
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
</div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We match <div class="flex gap-x-4">...</div> inside nav
    content = re.sub(r'<div class="flex gap-x-4">[\s\S]*?(?=</div>\s*</div>\s*</div>\s*</nav>)</div>', new_auth_icons, content)
    
    # 2. Add auth.js script before </body>
    if '<script type="module" src="js/auth.js"></script>' not in content:
        content = content.replace('</body>', '<script type="module" src="js/auth.js"></script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
