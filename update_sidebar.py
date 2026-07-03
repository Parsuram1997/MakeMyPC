import re
import sys

def main():
    filepath = 'c:/Projects/MakeMyPC/compare-products.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Add IDs to the spans if they don't have them
    content = content.replace('<span class="font-label-mono text-label-mono">Compatibility: 100%</span>', '<span class="font-label-mono text-label-mono" id="compare-compat">Compatibility: 100%</span>')
    content = content.replace('<span class="font-label-mono text-label-mono">Performance: Elite</span>', '<span class="font-label-mono text-label-mono" id="compare-perf">Performance: Elite</span>')
    content = content.replace('<span class="font-label-mono text-label-mono">Power: 750W / 1000W</span>', '<span class="font-label-mono text-label-mono" id="compare-power">Power: 750W / 1000W</span>')
    content = content.replace('<span class="font-label-mono text-label-mono">Summary: 12 Items</span>', '<span class="font-label-mono text-label-mono" id="compare-items">Summary: 12 Items</span>')
    content = content.replace('<span class="text-on-surface text-xl font-bold">₹2,499.00</span>', '<span class="text-on-surface text-xl font-bold" id="compare-total">₹2,499.00</span>')

    # Add the javascript logic at the end of the body
    script_content = """
<!-- Compare Summary Script -->
<script>
document.addEventListener('DOMContentLoaded', () => {
    try {
        const parsed = JSON.parse(localStorage.getItem('cart'));
        if (parsed && Array.isArray(parsed) && parsed.length > 0) {
            const cartData = parsed[parsed.length - 1]; // Get latest build
            const parts = cartData.parts || {};
            
            let totalPower = 0;
            let itemsCount = 0;
            
            Object.values(parts).forEach(part => {
                if (part) {
                    itemsCount++;
                    if (part.power) totalPower += part.power;
                }
            });
            
            let compat = '100%';
            if (itemsCount === 0) compat = 'Waiting for Parts';
            
            let perf = 'Standard';
            if (cartData.price > 150000) perf = 'Elite';
            else if (cartData.price > 80000) perf = 'High-End';
            if (itemsCount === 0) perf = 'N/A';
            
            const recPsu = totalPower > 0 ? totalPower + 150 : 0;
            
            const formatPrice = (price) => new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(price);
            
            document.getElementById('compare-compat').innerText = `Compatibility: ${compat}`;
            document.getElementById('compare-perf').innerText = `Performance: ${perf}`;
            document.getElementById('compare-power').innerText = `Power: ${totalPower}W / ${recPsu}W`;
            document.getElementById('compare-items').innerText = `Summary: ${itemsCount} Items`;
            document.getElementById('compare-total').innerText = formatPrice(cartData.price || 0);
        } else {
            document.getElementById('compare-compat').innerText = 'Compatibility: Waiting';
            document.getElementById('compare-perf').innerText = 'Performance: N/A';
            document.getElementById('compare-power').innerText = 'Power: 0W / 0W';
            document.getElementById('compare-items').innerText = 'Summary: 0 Items';
            document.getElementById('compare-total').innerText = '₹0.00';
        }
    } catch(e) {
        console.error('Error loading compare summary', e);
    }
});
</script>
</body>"""

    if '<!-- Compare Summary Script -->' not in content:
        content = content.replace('</body>', script_content)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated compare-products.html with dynamic logic")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
