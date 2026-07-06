"""
apply_consistent_nav_v2.py
--------------------------
FINAL FIX: Applies identical navbar to ALL public pages.

KEY FIX: Uses inline style for max-width instead of Tailwind's
max-w-container-max, which was breaking on pages with different
Tailwind configs. Now navbar looks 100% identical on every page,
no more layout shift or "vibration" on page change.
"""

import os, glob, re

# ─────────────────────────────────────────────
# ACTIVE / INACTIVE link classes
# ─────────────────────────────────────────────
INACTIVE = "text-on-surface-variant font-medium hover:text-primary transition-colors duration-200 font-label-mono"
ACTIVE   = "text-primary font-bold border-b-2 border-primary pb-1 font-label-mono"

# ─────────────────────────────────────────────
# MASTER NAV  (uses inline style for width — Tailwind-config-independent)
# ─────────────────────────────────────────────
MASTER_NAV = """\
<!-- ═══ NAVBAR START (auto-generated v2) ═══ -->
<nav style="position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.1);box-shadow:0 8px 32px 0 rgba(0,0,0,0.3);" id="main-nav">
  <div style="display:flex;justify-content:space-between;align-items:center;max-width:1280px;margin:0 auto;padding:0 64px;height:72px;">

    <!-- Logo -->
    <a href="index.html" style="font-size:24px;font-weight:900;color:#d7e2ff;text-decoration:none;letter-spacing:-0.03em;white-space:nowrap;flex-shrink:0;font-family:'Inter',sans-serif;">MakeMyPC</a>

    <!-- Desktop Links -->
    <div class="hidden md:flex" style="gap:32px;align-items:center;">
      <a class="%%SHOP%%"      href="shop.html"            style="text-decoration:none;font-size:12px;letter-spacing:0.05em;font-family:'JetBrains Mono','Inter',sans-serif;">Shop</a>
      <a class="%%BUILDER%%"   href="builder-landing.html" style="text-decoration:none;font-size:12px;letter-spacing:0.05em;font-family:'JetBrains Mono','Inter',sans-serif;">Builder</a>
      <a class="%%RESOURCES%%" href="support-faq.html"     style="text-decoration:none;font-size:12px;letter-spacing:0.05em;font-family:'JetBrains Mono','Inter',sans-serif;">Resources</a>
    </div>

    <!-- Right Controls -->
    <div style="display:flex;align-items:center;gap:16px;">

      <!-- Search (lg+) -->
      <div class="hidden lg:flex" style="position:relative;">
        <span class="material-symbols-outlined" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#c1c6d7;font-size:18px;">search</span>
        <input style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:7px 14px 7px 34px;font-size:13px;color:#d7e2ff;width:220px;outline:none;transition:border-color 0.2s;font-family:'Inter',sans-serif;" placeholder="Search Components" type="text"
          onfocus="this.style.borderColor='#007AFF'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'"/>
      </div>

      <!-- Cart -->
      <button onclick="window.location.href='shopping-cart.html'" style="background:none;border:none;cursor:pointer;color:#c1c6d7;position:relative;padding:4px;display:flex;align-items:center;" onmouseover="this.style.color='#adc6ff'" onmouseout="this.style.color='#c1c6d7'">
        <span class="material-symbols-outlined" style="font-size:24px;" data-icon="shopping_cart">shopping_cart</span>
        <span id="cart-badge" style="display:none;position:absolute;top:-4px;right:-4px;background:#ffb4ab;color:#690005;font-size:10px;font-weight:700;width:16px;height:16px;border-radius:50%;align-items:center;justify-content:center;font-family:'Inter',sans-serif;">0</span>
      </button>

      <!-- Login btn (logged out) -->
      <a href="login.html" id="auth-login-btn" style="color:#c1c6d7;text-decoration:none;display:flex;align-items:center;" onmouseover="this.style.color='#adc6ff'" onmouseout="this.style.color='#c1c6d7'">
        <span class="material-symbols-outlined" style="font-size:24px;" data-icon="account_circle">account_circle</span>
      </a>

      <!-- Avatar (logged in, hidden by default) -->
      <a href="account-settings.html" id="auth-avatar-btn" style="display:none;width:36px;height:36px;border-radius:50%;background:#adc6ff;color:#002e69;align-items:center;justify-content:center;font-weight:700;font-size:14px;text-decoration:none;flex-shrink:0;transition:filter 0.2s;" onmouseover="this.style.filter='brightness(1.1)'" onmouseout="this.style.filter='none'">
        <span id="avatar-initial">U</span>
      </a>

      <!-- Hamburger (mobile only) -->
      <button id="mobile-menu-btn" style="display:none;background:none;border:none;cursor:pointer;color:#c1c6d7;align-items:center;" onmouseover="this.style.color='#adc6ff'" onmouseout="this.style.color='#c1c6d7'">
        <span class="material-symbols-outlined" style="font-size:28px;">menu</span>
      </button>
    </div>

  </div>
</nav>

<!-- ═══ MOBILE MENU ═══ -->
<div id="mobile-menu" style="position:fixed;inset:0;background:rgba(0,8,28,0.97);backdrop-filter:blur(20px);z-index:60;transform:translateX(100%);transition:transform 0.3s ease;display:none;flex-direction:column;">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:20px 24px;border-bottom:1px solid rgba(255,255,255,0.1);">
    <a href="index.html" style="font-size:20px;font-weight:900;color:#d7e2ff;text-decoration:none;letter-spacing:-0.03em;font-family:'Inter',sans-serif;">MakeMyPC</a>
    <button id="mobile-menu-close" style="background:none;border:none;cursor:pointer;color:#c1c6d7;display:flex;align-items:center;">
      <span class="material-symbols-outlined" style="font-size:28px;">close</span>
    </button>
  </div>
  <div style="display:flex;flex-direction:column;gap:24px;padding:24px;overflow-y:auto;flex:1;">
    <!-- Mobile Search -->
    <div style="position:relative;">
      <span class="material-symbols-outlined" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#c1c6d7;">search</span>
      <input style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px 14px 12px 36px;font-size:14px;color:#d7e2ff;width:100%;outline:none;box-sizing:border-box;font-family:'Inter',sans-serif;" placeholder="Search Components" type="text"/>
    </div>
    <!-- Mobile Nav Links -->
    <div style="display:flex;flex-direction:column;gap:16px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:24px;">
      <a href="shop.html" style="font-size:18px;font-weight:700;color:#d7e2ff;text-decoration:none;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;">
        Shop <span class="material-symbols-outlined" style="font-size:18px;">chevron_right</span>
      </a>
      <a href="builder-landing.html" style="font-size:18px;font-weight:700;color:#d7e2ff;text-decoration:none;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;">
        Builder <span class="material-symbols-outlined" style="font-size:18px;">chevron_right</span>
      </a>
      <a href="support-faq.html" style="font-size:18px;font-weight:700;color:#d7e2ff;text-decoration:none;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;">
        Resources <span class="material-symbols-outlined" style="font-size:18px;">chevron_right</span>
      </a>
    </div>
    <!-- Mobile Auth -->
    <div style="display:flex;flex-direction:column;gap:12px;">
      <a id="mobile-auth-login" href="login.html" style="display:flex;align-items:center;gap:12px;color:#c1c6d7;text-decoration:none;font-family:'Inter',sans-serif;">
        <span class="material-symbols-outlined">account_circle</span> Log In
      </a>
      <a id="mobile-auth-account" href="account-settings.html" style="display:none;align-items:center;gap:12px;color:#c1c6d7;text-decoration:none;font-family:'Inter',sans-serif;">
        <span class="material-symbols-outlined">manage_accounts</span> My Account
      </a>
      <a href="shopping-cart.html" style="display:flex;align-items:center;gap:12px;color:#c1c6d7;text-decoration:none;font-family:'Inter',sans-serif;">
        <span class="material-symbols-outlined">shopping_cart</span> Cart
      </a>
    </div>
  </div>
</div>

<!-- Spacer so content doesn't hide under fixed nav -->
<div style="height:72px;"></div>

<!-- Mobile Menu JS -->
<script>
(function(){
  var btn=document.getElementById('mobile-menu-btn');
  var cls=document.getElementById('mobile-menu-close');
  var mnu=document.getElementById('mobile-menu');

  // Show hamburger only on mobile screens (no Tailwind dependency)
  function updateHamburger(){
    if(btn){
      btn.style.display = window.innerWidth < 768 ? 'flex' : 'none';
    }
    // Close mobile menu if window resized to desktop
    if(mnu && window.innerWidth >= 768){
      mnu.style.display='none';
      mnu.style.transform='translateX(100%)';
    }
  }
  updateHamburger();
  window.addEventListener('resize', updateHamburger);

  if(btn && cls && mnu){
    btn.addEventListener('click',function(){
      mnu.style.display='flex';
      // Small delay so display:flex kicks in before transform
      setTimeout(function(){ mnu.style.transform='translateX(0)'; }, 10);
    });
    cls.addEventListener('click',function(){
      mnu.style.transform='translateX(100%)';
      setTimeout(function(){ mnu.style.display='none'; }, 310);
    });
  }
})();
</script>
<!-- ═══ NAVBAR END ═══ -->
"""

# ─────────────────────────────────────────────
# PER-PAGE ACTIVE STATE MAP
# ─────────────────────────────────────────────
ACTIVE_MAP = {
    'index.html':                None,
    'shop.html':                 'shop',
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

SKIP_FILES = {
    'admin-dashboard.html',
    'admin-dashboard-overview.html',
    'orders-management.html',
    'product-management.html',
}

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
# REMOVE old navbar blocks (all variants)
# ─────────────────────────────────────────────
OLD_NAV_PATTERNS = [
    # v2 auto-generated block
    re.compile(r'<!-- ═══ NAVBAR START.*?<!-- ═══ NAVBAR END ═══ -->\n?', re.DOTALL),
    # v1 auto-generated block
    re.compile(r'<!-- ═══════════ CONSISTENT NAVBAR.*?<!-- ═══════════════════════════════════════════ -->\n?', re.DOTALL),
    # Any fixed top-0 nav + optional mobile-menu + optional script
    re.compile(
        r'<nav\b[^>]*?(?:fixed|position:fixed)[^>]*?>.*?</nav>'
        r'(?:\s*<!--[^\n]*-->\s*)?'
        r'(?:\s*<div\s+id=["\']mobile-menu["\'].*?</div>\s*)?'
        r'(?:\s*<div\s+style=["\']height:72px["\'].*?</div>\s*)?'
        r'(?:\s*<!--[^\n]*-->\s*)?'
        r'(?:\s*<script>[\s\S]*?</script>\s*)?'
        r'(?:\s*<!--[^\n]*-->\s*)?',
        re.DOTALL
    ),
]

OLD_PT_PATTERN = re.compile(r'<main\s[^>]*?pt-28[^>]*?>', re.DOTALL)

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
        print(f"  SKIP (unmapped) {basename}")
        skipped += 1
        continue

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Strip ALL old nav variants
        for pat in OLD_NAV_PATTERNS:
            content = pat.sub('', content, count=1)

        # Also strip lingering <!-- Top Navbar --> comments
        content = re.sub(r'\s*<!--\s*Top Navbar\s*-->\s*', '\n', content)

        # Fix: remove extra top padding from <main> that old nav left behind
        # The spacer div now handles the 72px offset
        content = re.sub(r'(<main\b[^>]*?)pt-28', r'\1pt-0', content)
        content = re.sub(r'(<main\b[^>]*?)pt-20', r'\1pt-0', content)

        # Insert the new nav right after <body ...>
        body_match = re.search(r'(<body\b[^>]*>)', content)
        if not body_match:
            errors.append(f"{basename}: no <body> tag")
            continue

        active_key = ACTIVE_MAP[basename]
        new_nav    = build_nav(active_key)

        insert_pos = body_match.end()
        content = content[:insert_pos] + '\n' + new_nav + content[insert_pos:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  OK    {basename}  (active={active_key})")
        changed += 1

    except Exception as e:
        errors.append(f"{basename}: {e}")
        import traceback; traceback.print_exc()

print(f"\n{'='*55}")
print(f"Done. {changed} updated, {skipped} skipped.")
if errors:
    print("ERRORS:")
    for e in errors: print(f"  ✗ {e}")
else:
    print("No errors.")
