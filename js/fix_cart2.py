text = open('shopping-cart.js', encoding='utf-8').read()

# The condition currently only handles 'component' type separately
# We need to also handle 'prebuilt' type similarly (single product card)
old = "    cartData.forEach((item, index) => {\n        if (item.type === 'component') {"
new = "    cartData.forEach((item, index) => {\n        // Single product items (component or prebuilt from shop)\n        if (item.type === 'component' || item.type === 'prebuilt' || item.type === 'laptop' || item.type === 'monitor') {"

if old in text:
    open('shopping-cart.js', 'w', encoding='utf-8').write(text.replace(old, new, 1))
    print('Fixed: cart now handles prebuilt/laptop/monitor types')
else:
    idx = text.find("item.type === 'component'")
    print('Context:', repr(text[max(0,idx-50):idx+60]))
