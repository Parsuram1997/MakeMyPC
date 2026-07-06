"""
apply_consistent_nav.py
-----------------------
Applies a 100% consistent header (nav + mobile menu + mobile script)
to ALL public-facing HTML pages. Admin pages are skipped.

The ONLY thing that varies per page is the active nav item highlight.
Everything else — height, logo, font size, icons, spacing — is identical.
"""

import os, glob, re

# ─────────────────────────────────────────────
# 1.  MASTER NAV BLOCK (desktop top bar)
# ─────────────────────────────────────────────
# Placeholders that get swapped per-page:
#   %%SHOP%%      – active class for Shop link
#   %%BUILDER%%   – active class for Builder link
#   %%RESOURCES%% – active class for Resources link

INACTIVE = "text-on-surface-variant font-medium hover:text-primary transition-colors duration-200 font-label-mono text-label-mono"
ACTIVE   = "text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-label-mono"

MASTER_NAV = """\
<!-- ═══════════ CONSISTENT NAVBAR (auto-generated) ═══════════ -->
<nav class="fixed top-0 w-full z-50 bg-surface-glass backdrop-blur-xl border-b border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.3)]">
  <div class="flex justify-between items-center max-w-container-max mx-auto px-margin-desktop h-20">

    <!-- Logo -->
    <a href="index.html" class="text-headline-lg font-headline-lg font-black text-on-surface tracking-tighter shrink-0">MakeMyPC</a>

    <!-- Desktop Links -->
    <div class="hidden md:flex gap-x-8 items-center">
      <a class="%%SHOP%%"      href="prebuilt-pcs.html">Shop</a>
      <a class="%%BUILDER%%"   href="builder-landing.html">Builder</a>
      <a class="%%RESOURCES%%" href="support-faq.html">Resources</a>
    </div>

    <!-- Right Controls -->
    <div class="flex items-center gap-x-4">
      <!-- Search (hidden on small screens) -->
      <div class="relative hidden lg:block">
        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]">search</span>
        <input class="bg-surface-container-low border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-body-sm font-body-sm focus:outline-none focus:border-electric-blue w-56 transition-all text-white placeholder:text-on-surface-variant/60" placeholder="Search Components" type="text"/>
      </div>

      <!-- Cart -->
      <button class="text-on-surface-variant hover:text-primary transition-colors duration-200 relative" onclick="window.location.href='shopping-cart.html'">
        <span class="material-symbols-outlined text-[24px]" data-icon="shopping_cart">shopping_cart</span>
        <span id="cart-badge" class="absolute -top-1 -right-1 bg-error text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center hidden">0</span>
      </button>

      <!-- Login Icon (shown when logged out) -->
      <a href="login.html" id="auth-login-btn" class="text-on-surface-variant hover:text-primary transition-colors duration-200 flex items-center">
        <span class="material-symbols-outlined text-[24px]" data-icon="account_circle">account_circle</span>
      </a>

      <!-- Avatar (shown when logged in, hidden by default) -->
      <a href="account-settings.html" id="auth-avatar-btn" class="hidden w-9 h-9 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold text-sm hover:brightness-110 transition-all shrink-0">
        <span id="avatar-initial">U</span>
      </a>

      <!-- Hamburger (mobile only) -->
      <button id="mobile-menu-btn" class="md:hidden text-on-surface-variant hover:text-primary transition-colors duration-200 flex items-center">
        <span class="material-symbols-outlined text-[28px]">menu</span>
      </button>
    </div>

  </div>
</nav>

<!-- ═══════════ MOBILE MENU OVERLAY ═══════════ -->
<div id="mobile-menu" class="fixed inset-0 bg-[#00081C]/95 backdrop-blur-xl z-[60] transform translate-x-full transition-transform duration-300 md:hidden flex flex-col">
  <div class="flex justify-between items-center p-6 border-b border-white/10">
    <a href="index.html" class="text-xl font-black text-white tracking-tighter">MakeMyPC</a>
    <button id="mobile-menu-close" class="text-on-surface-variant hover:text-white transition-colors">
      <span class="material-symbols-outlined text-3xl">close</span>
    </button>
  </div>
  <div class="flex flex-col gap-6 p-6 overflow-y-auto">
    <!-- Mobile Search -->
    <div class="relative w-full">
      <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
      <input class="bg-surface-container-low border border-white/10 rounded-lg pl-10 pr-4 py-3 text-body-sm focus:outline-none focus:border-primary w-full transition-all text-white placeholder:text-on-surface-variant/50" placeholder="Search Components" type="text"/>
    </div>
    <!-- Mobile Nav Links -->
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
    <!-- Mobile Auth Links -->
    <div class="flex flex-col gap-3">
      <a id="mobile-auth-login" href="login.html" class="flex items-center gap-3 text-on-surface-variant hover:text-white transition-colors">
        <span class="material-symbols-outlined">account_circle</span> Log In
      </a>
      <a id="mobile-auth-account" href="account-settings.html" class="hidden flex items-center gap-3 text-on-surface-variant hover:text-white transition-colors">
        <span class="material-symbols-outlined">manage_accounts</span> My Account
      </a>
      <a href="shopping-cart.html" class="flex items-center gap-3 text-on-surface-variant hover:text-white transition-colors">
        <span class="material-symbols-outlined">shopping_cart</span> Cart
      </a>
    </div>
  </div>
</div>

<!-- Mobile Menu Script -->
<script>
(function() {
  var btn   = document.getElementById('mobile-menu-btn');
  var close = document.getElementById('mobile-menu-close');
  var menu  = document.getElementById('mobile-menu');
  if (btn && close && menu) {
    btn.addEventListener('click',   function() { menu.classList.remove('translate-x-full'); });
    close.addEventListener('click', function() { menu.classList.add('translate-x-full'); });
  }
})();
</script>
<!-- ═══════════════════════════════════════════ -->
"""

# ─────────────────────────────────────────────
# 2.  PER-PAGE ACTIVE-STATE MAP
# ─────────────────────────────────────────────
# Each entry: filename -> which nav link is active ('shop'|'builder'|'resources'|None)
ACTIVE_MAP = {
    # Public pages
    'index.html':                None,
    'prebuilt-pcs.html':         'shop',
    'product-details.html':      'shop',
    'custom-pc-builder.html':    'builder',
    'smart-builder.html':        'builder',
    'builder-landing.html':      'builder',
    'compare-products.html':     'shop',
    'shopping-cart.html':        None,
    'support-faq.html':          'resources',
    'submit-ticket.html':        'resources',
    'ticket-submitted.html':     'resources',
    'order-tracking.html':       'resources',
    'calculators-tools.html':    'resources',
    'compatibility-manager.html':'builder',
    'my-builds.html':            'builder',
    'account-settings.html':     None,
    'login.html':                None,
    'signup.html':               None,
}

# Pages to SKIP (admin or special)
SKIP_FILES = {
    'admin-dashboard.html',
    'admin-dashboard-overview.html',
    'orders-management.html',
    'product-management.html',
}

# ─────────────────────────────────────────────
# 3.  HELPER: build the nav block for a page
# ─────────────────────────────────────────────
def build_nav(active_key):
    shop      = ACTIVE if active_key == 'shop'      else INACTIVE
    builder   = ACTIVE if active_key == 'builder'   else INACTIVE
    resources = ACTIVE if active_key == 'resources' else INACTIVE
    nav = MASTER_NAV
    nav = nav.replace('%%SHOP%%',      shop)
    nav = nav.replace('%%BUILDER%%',   builder)
    nav = nav.replace('%%RESOURCES%%', resources)
    return nav

# ─────────────────────────────────────────────
# 4.  PATTERN: everything from <nav to after mobile script
# We replace:
#   a) The top <nav>…</nav>
#   b) Optional mobile-menu div
#   c) Optional inline mobile script block
# ─────────────────────────────────────────────
# Regex: matches the first <nav ...> block and optionally the mobile menu + script that follow
NAV_PATTERN = re.compile(
    r'<!--\s*═+\s*CONSISTENT NAVBAR.*?<!--\s*═+\s*-->\n?',
    re.DOTALL
)

LEGACY_PATTERN = re.compile(
    r'<nav\b[^>]*fixed top-0[^>]*>.*?</nav>'          # top nav
    r'(?:\s*<!--[^>]*-->\s*)?'                          # optional comment
    r'(?:\s*<div\s+id=["\']mobile-menu["\'][^>]*>.*?</div>\s*)?'   # optional mobile menu
    r'(?:\s*<script>\s*(?://[^\n]*\n)?\s*document\.addEventListener[^<]*</script>\s*)?'
    r'(?:\s*<script>\s*\(function\(\).*?</script>\s*)?',
    re.DOTALL
)

# ─────────────────────────────────────────────
# 5.  PROCESS EACH FILE
# ─────────────────────────────────────────────
html_files = glob.glob('c:/Projects/MakeMyPC/*.html')
changed = 0
skipped = 0
errors  = []

for fpath in sorted(html_files):
    basename = os.path.basename(fpath)

    if basename in SKIP_FILES:
        print(f"  SKIP  {basename}")
        skipped += 1
        continue

    if basename not in ACTIVE_MAP:
        print(f"  SKIP (not in map)  {basename}")
        skipped += 1
        continue

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        active_key = ACTIVE_MAP[basename]
        new_nav    = build_nav(active_key)

        # Try removing auto-generated block first
        if '═══════════ CONSISTENT NAVBAR' in content:
            new_content = NAV_PATTERN.sub('', content)
        else:
            new_content = content

        # Now remove the legacy nav + mobile-menu + script
        new_content, n_subs = LEGACY_PATTERN.subn('', new_content, count=1)

        # Insert the new nav right after <body ...>
        body_match = re.search(r'(<body\b[^>]*>)', new_content)
        if not body_match:
            errors.append(f"{basename}: no <body> tag found")
            continue

        insert_pos = body_match.end()
        new_content = new_content[:insert_pos] + '\n' + new_nav + new_content[insert_pos:]

        # Write back
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  OK    {basename}  (active={active_key})")
        changed += 1

    except Exception as e:
        errors.append(f"{basename}: {e}")

print(f"\n{'='*50}")
print(f"Done. {changed} files updated, {skipped} skipped.")
if errors:
    print("\nERRORS:")
    for e in errors:
        print(f"  ✗ {e}")
else:
    print("No errors.")
