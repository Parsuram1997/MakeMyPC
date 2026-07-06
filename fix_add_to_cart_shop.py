import sys

with open('shop.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = """    // Update badge
    const badge = document.getElementById('cart-badge');
    if (badge) {
      badge.textContent = cart.length;
      badge.style.display = 'flex';
    }"""

new_block = """    // Update badge using global function
    if (window.updateCartBadge) {
      window.updateCartBadge();
    }"""

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated addToCartShop in shop.html to use global updateCartBadge.")
else:
    print("Could not find the target block in shop.html.")
