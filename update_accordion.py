import re

def update_cart():
    filepath = 'c:/Projects/MakeMyPC/js/shopping-cart.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

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
            <div class="glass-card rounded-2xl border border-white/10 mb-6 overflow-hidden transition-all duration-300">
                <!-- Accordion Header (Summary) -->
                <div class="p-5 md:p-6 cursor-pointer flex justify-between items-center hover:bg-white/5 transition-colors group" onclick="toggleBuildDetails(${index})">
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full bg-primary/20 text-primary flex items-center justify-center font-bold text-xl border border-primary/30 group-hover:scale-110 transition-transform">
                            ${index + 1}
                        </div>
                        <div>
                            <h3 class="text-xl md:text-2xl font-black">${name || 'Custom PC Build'} #${index + 1}</h3>
                            <div class="text-sm text-on-surface-variant flex items-center gap-2 mt-1">
                                <span class="font-label-mono">REF: ${id}</span>
                                <div class="w-1 h-1 rounded-full bg-white/20"></div>
                                <span class="text-white font-bold">₹${price.toLocaleString('en-IN')}</span>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <button onclick="window.removeBuild(event, ${index})" class="w-10 h-10 rounded-full bg-error/10 text-error flex items-center justify-center hover:bg-error/20 hover:scale-110 transition-all border border-error/20" title="Remove Build">
                            <span class="material-symbols-outlined text-[18px]">delete</span>
                        </button>
                        <span class="material-symbols-outlined text-3xl text-on-surface-variant group-hover:text-white transform transition-transform duration-300" id="icon-build-${index}">expand_more</span>
                    </div>
                </div>
                
                <!-- Accordion Body (Details) -->
                <div id="details-build-${index}" class="hidden border-t border-white/10 bg-black/40">
                    <div class="p-6 md:p-8">
                        <!-- Hero Section for Build -->
                        <div class="glass-card rounded-3xl overflow-hidden mb-8 relative border border-white/10">
                            <div class="absolute inset-0 bg-gradient-to-r from-primary/20 via-transparent to-transparent opacity-50"></div>
                            <div class="absolute -top-24 -right-24 w-96 h-96 bg-primary/20 rounded-full blur-3xl"></div>
                            
                            <div class="flex flex-col md:flex-row relative z-10">
                                <div class="flex-1 p-8 md:p-12 flex flex-col justify-center">
                                    <div class="flex items-center gap-3 mb-4">
                                        <span class="px-3 py-1 bg-green-500/20 text-green-400 border border-green-500/30 rounded-full text-xs font-bold uppercase tracking-wider flex items-center gap-1">
                                            <span class="material-symbols-outlined text-[14px]">verified</span> 100% Compatible
                                        </span>
                                    </div>
                                    <h2 class="text-4xl md:text-5xl font-black mb-6 tracking-tight">Build Details</h2>
                                    
                                    <div class="flex flex-wrap gap-4 mb-8">
                                        <div class="bg-white/5 border border-white/10 rounded-xl p-4 flex-1 min-w-[120px]">
                                            <div class="text-on-surface-variant text-xs uppercase font-bold tracking-wider mb-1">Gaming Score</div>
                                            <div class="text-3xl font-black text-primary">98<span class="text-lg text-white/50">/100</span></div>
                                        </div>
                                        <div class="bg-white/5 border border-white/10 rounded-xl p-4 flex-1 min-w-[120px]">
                                            <div class="text-on-surface-variant text-xs uppercase font-bold tracking-wider mb-1">Productivity</div>
                                            <div class="text-3xl font-black text-secondary">94<span class="text-lg text-white/50">/100</span></div>
                                        </div>
                                        <div class="bg-white/5 border border-white/10 rounded-xl p-4 flex-1 min-w-[120px]">
                                            <div class="text-on-surface-variant text-xs uppercase font-bold tracking-wider mb-1">Upgradability</div>
                                            <div class="text-3xl font-black text-tertiary">90<span class="text-lg text-white/50">/100</span></div>
                                        </div>
                                    </div>
                                    
                                    <div class="flex items-center gap-4 text-sm text-on-surface-variant">
                                        <div class="flex items-center gap-1"><span class="material-symbols-outlined text-primary">bolt</span> ${totalWattage}W Est. Draw</div>
                                        <div class="w-1 h-1 rounded-full bg-white/20"></div>
                                        <div class="flex items-center gap-1"><span class="material-symbols-outlined text-secondary">local_shipping</span> Est. Delivery: ${dateStr}</div>
                                    </div>
                                </div>
                                <div class="w-full md:w-1/3 min-h-[300px] bg-gradient-to-br from-surface-deep to-surface-container flex items-center justify-center relative border-l border-white/10">
                                    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1587831990711-23ca6441447b?q=80&w=1000&auto=format&fit=crop')] bg-cover bg-center opacity-40 mix-blend-screen"></div>
                                    <div class="absolute inset-0 bg-gradient-to-t from-surface-deep via-transparent to-transparent"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Selected Components -->
                        <section>
                            <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                                <span class="material-symbols-outlined text-primary">view_list</span> Specifications
                            </h3>
                            <div class="glass-card rounded-2xl border border-white/10 overflow-hidden divide-y divide-white/10">
                                ${Object.keys(parts).filter(k => parts[k]).map((key, partIndex) => {
                                    const part = parts[key];
                                    return `
                                    <div class="p-2 px-3 flex items-center gap-3 hover:bg-white/5 transition-colors group">
                                        <div class="w-5 h-5 flex items-center justify-center bg-white/5 text-white/50 text-[10px] font-bold rounded">
                                            ${partIndex + 1}
                                        </div>
                                        <div class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center overflow-hidden flex-shrink-0 relative">
                                            ${part.image ? `<img src="${part.image}" class="w-full h-full object-cover">` : `<span class="material-symbols-outlined text-white/30 text-[16px]">memory</span>`}
                                        </div>
                                        <div class="flex-1 flex items-center gap-2">
                                            <span class="text-[10px] text-primary uppercase font-bold tracking-wider w-16">${key}</span>
                                            <span class="font-bold text-xs">${part.model}</span>
                                        </div>
                                        <div class="text-right flex items-center gap-3">
                                            <div class="text-[10px] text-on-surface-variant">Qty: 1</div>
                                            <div class="font-bold text-sm">₹${part.price.toLocaleString('en-IN')}</div>
                                        </div>
                                    </div>
                                    `;
                                }).join('')}
                            </div>
                        </section>
                    </div>
                </div>
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

                        <!-- Secondary Actions -->
                        <div class="flex flex-col gap-2">
                            <div class="flex gap-2">
                                <button onclick="window.showToast('Link copied to clipboard!', 'success')" class="flex-1 py-3 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-bold uppercase tracking-wider flex items-center justify-center gap-2 transition-all">
                                    <span class="material-symbols-outlined text-[16px]">share</span> Share
                                </button>
                                <button onclick="window.showToast('Generating PDF...', 'info')" class="flex-1 py-3 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-bold uppercase tracking-wider flex items-center justify-center gap-2 transition-all">
                                    <span class="material-symbols-outlined text-[16px]">picture_as_pdf</span> Save PDF
                                </button>
                            </div>
                            <button onclick="window.location.href='custom-pc-builder.html'" class="w-full py-3 bg-transparent border border-white/10 hover:bg-white/5 rounded-xl text-xs font-bold uppercase tracking-wider transition-all">
                                ← Edit Build
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    root.innerHTML = html;
}
"""
    
    # Replace the renderCheckoutUI function
    content = re.sub(r'function renderCheckoutUI\(\) \{.*?(?=window\.toggleBuildDetails = function\()', script, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_cart()
