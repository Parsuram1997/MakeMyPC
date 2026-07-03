import re

def update_cart():
    filepath = 'c:/Projects/MakeMyPC/js/shopping-cart.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change cartData loading
    content = re.sub(
        r'if \(parsed\.length > 0\) \{\s+cartData = parsed\[parsed\.length - 1\]; // Get the latest build\s+\}',
        'if (parsed.length > 0) { cartData = parsed; }',
        content
    )
    content = re.sub(
        r'if \(!cartData\) \{',
        'if (!cartData || cartData.length === 0) {',
        content
    )

    # Modify renderCheckoutUI to iterate over cartData
    # First, let's extract the part from Hero Section to Warranty
    # Actually, we can just replace the whole renderCheckoutUI function with a mapped version.

    script = """
function renderCheckoutUI() {
    const root = document.getElementById('checkout-root');
    
    let overallPrice = 0;
    let buildsHtml = '';
    
    cartData.forEach((build, index) => {
        const { parts, price, name, id } = build;
        overallPrice += price;
        
        let totalWattage = 0;
        Object.values(parts).forEach(p => {
            if(p && p.power) totalWattage += p.power;
        });
        const recPsu = Math.ceil((totalWattage * 1.5) / 50) * 50;
        
        // Mock delivery date
        const deliveryDate = new Date();
        deliveryDate.setDate(deliveryDate.getDate() + 5);
        const dateStr = deliveryDate.toLocaleDateString('en-IN', { weekday: 'short', month: 'short', day: 'numeric' });
        
        buildsHtml += `
            <div class="mb-12 border-b border-white/10 pb-8 last:border-0">
                <!-- Hero Section for Build -->
                <div class="glass-card rounded-3xl overflow-hidden mb-8 relative border border-white/10">
                    <div class="absolute inset-0 bg-gradient-to-r from-primary/20 via-transparent to-transparent opacity-50"></div>
                    
                    <div class="flex flex-col md:flex-row relative z-10">
                        <div class="flex-1 p-6 md:p-8 flex flex-col justify-center">
                            <div class="flex items-center justify-between mb-4">
                                <span class="px-3 py-1 bg-green-500/20 text-green-400 border border-green-500/30 rounded-full text-[10px] font-bold uppercase tracking-wider flex items-center gap-1">
                                    <span class="material-symbols-outlined text-[14px]">verified</span> 100% Compatible
                                </span>
                                <span class="font-label-mono text-xs text-on-surface-variant">REF: ${id}</span>
                            </div>
                            <h2 class="text-2xl md:text-3xl font-black mb-4 tracking-tight">${name || 'Custom PC Build'} #${index + 1}</h2>
                            
                            <div class="flex items-center gap-4 text-xs text-on-surface-variant mb-6">
                                <div class="flex items-center gap-1"><span class="material-symbols-outlined text-primary text-sm">bolt</span> ${totalWattage}W Est. Draw</div>
                                <div class="w-1 h-1 rounded-full bg-white/20"></div>
                                <div class="flex items-center gap-1"><span class="material-symbols-outlined text-secondary text-sm">local_shipping</span> Est. Delivery: ${dateStr}</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Selected Components -->
                <section class="mb-8">
                    <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                        <span class="material-symbols-outlined text-primary">view_list</span> Specifications
                    </h3>
                    <div class="glass-card rounded-2xl border border-white/10 overflow-hidden divide-y divide-white/10">
                        ${Object.keys(parts).map(key => {
                            const part = parts[key];
                            if(!part) return '';
                            return \\`
                            <div class="p-3 flex items-center gap-4 hover:bg-white/5 transition-colors group">
                                <div class="w-12 h-12 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center overflow-hidden flex-shrink-0 relative">
                                    ${part.image ? \\`<img src="${part.image}" class="w-full h-full object-cover">\\` : \\`<span class="material-symbols-outlined text-white/30 text-xl">memory</span>\\`}
                                </div>
                                <div class="flex-1">
                                    <div class="text-[10px] text-primary uppercase font-bold tracking-wider mb-0.5">${key}</div>
                                    <div class="font-bold text-sm leading-tight">${part.model}</div>
                                </div>
                                <div class="text-right">
                                    <div class="font-bold text-sm">₹${part.price.toLocaleString('en-IN')}</div>
                                    <div class="text-[10px] text-on-surface-variant">Qty: 1</div>
                                </div>
                            </div>
                            \\`;
                        }).join('')}
                    </div>
                </section>
            </div>
        `;
    });

    const gst = overallPrice * 0.18;
    const subtotal = overallPrice - gst;
    const grandTotal = overallPrice;
    
    const html = `
        <div class="max-w-[1400px] mx-auto px-4 md:px-8">
            <h1 class="text-3xl font-black mb-8">Your Cart (${cartData.length} items)</h1>
            <!-- Two Column Layout -->
            <div class="flex flex-col lg:flex-row gap-8">
                
                <!-- Left Content: Components & Details -->
                <div class="flex-1">
                    ${buildsHtml}

                    <!-- Trust & Timeline (Once at the bottom) -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
                        <div class="glass-card rounded-2xl border border-white/10 p-6">
                            <h3 class="font-bold mb-3 flex items-center gap-2"><span class="material-symbols-outlined text-primary">shield</span> MakeMyPC Promise</h3>
                            <ul class="space-y-2 text-sm text-on-surface-variant">
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> Professional Assembly & Cable Management</li>
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> 24-Hour Stress Testing & Benchmarking</li>
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> BIOS Update & OS Installation</li>
                            </ul>
                        </div>
                        <div class="glass-card rounded-2xl border border-white/10 p-6">
                            <h3 class="font-bold mb-3 flex items-center gap-2"><span class="material-symbols-outlined text-secondary">workspace_premium</span> Warranty & Support</h3>
                            <ul class="space-y-2 text-sm text-on-surface-variant">
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> 3-Year Comprehensive Warranty</li>
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> Lifetime Technical Support</li>
                                <li class="flex gap-2"><span class="material-symbols-outlined text-green-400 text-lg">check_circle</span> Free Shipping & Secure Packaging</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Right Sticky Sidebar: Order Summary -->
                <div class="w-full lg:w-96 flex-shrink-0">
                    <div class="sticky top-24 space-y-6">
                        
                        <!-- Order Summary Card -->
                        <div class="glass-card rounded-3xl border border-white/10 overflow-hidden shadow-2xl relative">
                            <!-- Background glow -->
                            <div class="absolute -inset-1 bg-gradient-to-b from-primary/10 to-transparent blur-xl pointer-events-none"></div>
                            
                            <div class="p-6 relative z-10 border-b border-white/5">
                                <h2 class="text-xl font-bold mb-6">Order Summary</h2>
                                
                                <div class="space-y-3 text-sm">
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Subtotal (Excl. GST)</span>
                                        <span class="text-white">₹${subtotal.toLocaleString('en-IN', {minimumFractionDigits: 2})}</span>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>GST (18%)</span>
                                        <span class="text-white">₹${gst.toLocaleString('en-IN', {minimumFractionDigits: 2})}</span>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Professional Assembly</span>
                                        <span class="text-white">₹0.00 <span class="line-through text-white/30 text-xs ml-1">₹2,500</span></span>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Prime Packaging</span>
                                        <span class="text-white">FREE</span>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Secure Shipping</span>
                                        <span class="text-white">FREE</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="p-6 bg-white/5 relative z-10">
                                <div class="flex justify-between items-end mb-1">
                                    <span class="text-sm text-on-surface-variant uppercase font-bold tracking-wider">Grand Total</span>
                                    <span class="text-3xl font-black text-primary">₹${grandTotal.toLocaleString('en-IN', {minimumFractionDigits: 2})}</span>
                                </div>
                                <div class="text-xs text-right text-green-400 mb-6">You saved ₹2,500 on assembly!</div>
                                
                                <!-- Promo Code -->
                                <div class="flex gap-2 mb-6">
                                    <input type="text" placeholder="Promo Code" class="flex-1 bg-surface-deep/50 border border-white/10 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-primary/50 transition-colors">
                                    <button class="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-sm font-bold transition-all border border-white/5">Apply</button>
                                </div>
                                
                                <!-- EMI Banner -->
                                <div class="bg-primary/10 border border-primary/20 rounded-lg p-3 flex items-center gap-3 mb-6 cursor-pointer hover:bg-primary/20 transition-all">
                                    <span class="material-symbols-outlined text-primary">credit_card</span>
                                    <div class="flex-1">
                                        <div class="text-xs font-bold">EMI Starts at ₹${Math.floor(grandTotal / 12).toLocaleString('en-IN')}/mo</div>
                                        <div class="text-[10px] text-on-surface-variant">View all EMI options</div>
                                    </div>
                                    <span class="material-symbols-outlined text-on-surface-variant">chevron_right</span>
                                </div>
                                
                                <!-- Primary Action -->
                                <button class="w-full py-4 bg-primary hover:bg-primary/90 text-on-primary font-black text-lg rounded-xl shadow-[0_0_20px_rgba(0,150,255,0.3)] hover:shadow-[0_0_30px_rgba(0,150,255,0.5)] hover:-translate-y-0.5 transition-all flex items-center justify-center gap-2 mb-4">
                                    <span class="material-symbols-outlined">lock</span> Secure Checkout
                                </button>
                                
                                <button onclick="clearCart()" class="w-full py-3 bg-error/20 hover:bg-error/30 text-error font-bold text-sm rounded-xl transition-all mb-4">
                                    Clear Cart
                                </button>
                                
                                <p class="text-[10px] text-center text-on-surface-variant">We accept all major Credit Cards, UPI, NetBanking, and EMI.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    root.innerHTML = html;
}

window.clearCart = function() {
    localStorage.removeItem('cart');
    window.location.reload();
};
"""
    
    # Replace the old renderCheckoutUI and updateFps functions with the new one
    content = re.sub(r'function renderCheckoutUI\(\) \{.*?(?=window\.updateCartFps)', script, content, flags=re.DOTALL)
    
    # Remove the old updateCartFps function as it's no longer used or needed for simple lists
    content = re.sub(r'window\.updateCartFps = function\(res\) \{.*?\};', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_cart()
