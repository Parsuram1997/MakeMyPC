text = open('shopping-cart.js', encoding='utf-8').read()

old = """        // Full Build Logic
        const build = item;
        const { parts, price, name, id } = build;
        overallPrice += price;
        
        let totalWattage = 0;
        let numComponents = 0;
        Object.values(parts).forEach(p => {
            if(p) {
                if(p.power) totalWattage += p.power;
                numComponents++;
            }
        });"""

new = """        // Full Build Logic
        const build = item;
        const { parts, price, name, id } = build;
        overallPrice += (price || 0);
        
        let totalWattage = 0;
        let numComponents = 0;
        if (parts && typeof parts === 'object') {
            Object.values(parts).forEach(p => {
                if(p) {
                    if(p.power) totalWattage += p.power;
                    numComponents++;
                }
            });
        }"""

if old in text:
    open('shopping-cart.js', 'w', encoding='utf-8').write(text.replace(old, new, 1))
    print('Fixed: parts null check added')
else:
    # Find approximation
    idx = text.find('Object.values(parts)')
    print('Pattern not found. Context:', repr(text[max(0,idx-200):idx+50]))
