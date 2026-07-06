import sys

with open('generate_shop.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update "Buy Now" button
old_buy = """<button class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Buy Now</button>"""
new_buy = """<button onclick="addToCartShop({id:'${p.id}',name:'${p.name}',price:${p.price},type:'prebuilt',image:'${p.img||''}',category:'Prebuilt PC',parts:null})" class="py-2 rounded-lg text-xs font-bold" style="background:#007AFF;color:#fff;border:none;cursor:pointer;" onmouseover="this.style.background='#005ec4'" onmouseout="this.style.background='#007AFF'">Add to Cart</button>"""

if old_buy in text:
    text = text.replace(old_buy, new_buy)
    print("Buy Now button updated.")

# 2. Inject addToCartShop script
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

script_block = f"""
{fn_code}
</script>
"""

if "window.addToCartShop" not in text:
    text = text.replace("</script>\n</body>", script_block + "</body>")
    print("addToCartShop function injected.")

with open('generate_shop.py', 'w', encoding='utf-8') as f:
    f.write(text)

