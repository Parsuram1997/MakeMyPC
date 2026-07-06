text = open('shop.html', encoding='utf-8').read()

# 1. Fix the "Buy Now" button in prebuilts to call addToCartShop
old_buy = """          <button class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Buy Now</button>"""

new_buy = """          <button onclick="addToCartShop(p)" class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Add to Cart</button>"""

# But the issue is 'p' is a template literal variable - we need to pass id/name/price
# Let's do it differently - pass data attributes via onclick
old_buy_js = "onclick=\"addToCompare('${p.id}','${p.name}')\""
# This tells us p is available in renderPrebuilts scope - but onclick can't capture it directly
# Better approach: encode as data in onclick
old_buy2 = """<button class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Buy Now</button>"""

new_buy2 = """<button onclick="addToCartShop({id:'${p.id}',name:'${p.name}',price:${p.price},type:'prebuilt',image:'${p.img||''}',category:'Prebuilt PC',parts:null})" class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Add to Cart</button>"""

if old_buy2 in text:
    text = text.replace(old_buy2, new_buy2, 1)
    print('Fixed: Buy Now -> addToCartShop')
else:
    print('Buy Now pattern not found exactly. Searching...')
    idx = text.find('Buy Now')
    print('Context:', repr(text[max(0,idx-150):idx+60]))

# 2. Add the addToCartShop function before </script> near end of file
fn_code = """
// Global cart add function for shop page
window.addToCartShop = function(item) {
  try {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    // Check if already in cart
    const exists = cart.find(c => c.id === item.id);
    if (exists) {
      exists.qty = (exists.qty || 1) + 1;
    } else {
      cart.push({...item, qty: 1});
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    // Update badge
    const badge = document.getElementById('cart-badge');
    if (badge) {
      badge.textContent = cart.length;
      badge.style.display = 'flex';
    }
    // Toast notification
    const toast = document.createElement('div');
    toast.style.cssText = 'position:fixed;bottom:24px;right:24px;z-index:9999;background:#00A4A6;color:#fff;padding:12px 20px;border-radius:12px;font-family:Inter,sans-serif;font-size:14px;font-weight:600;display:flex;align-items:center;gap:8px;box-shadow:0 8px 30px rgba(0,0,0,0.4);transform:translateY(20px);opacity:0;transition:all 0.3s ease;';
    toast.innerHTML = '<span style="font-size:18px">✓</span> Added to cart!';
    document.body.appendChild(toast);
    requestAnimationFrame(() => { toast.style.transform = 'translateY(0)'; toast.style.opacity = '1'; });
    setTimeout(() => { toast.style.opacity = '0'; toast.style.transform = 'translateY(20px)'; setTimeout(() => toast.remove(), 300); }, 2500);
  } catch(e) {
    console.error('addToCartShop error', e);
    window.location.href = 'shopping-cart.html';
  }
};
"""

# Inject before last </script>
last_script_end = text.rfind('</script>')
if last_script_end > 0:
    text = text[:last_script_end] + fn_code + '\n</script>' + text[last_script_end+9:]
    print('addToCartShop function injected')
else:
    print('No </script> found!')

open('shop.html', 'w', encoding='utf-8').write(text)
print('shop.html saved')
