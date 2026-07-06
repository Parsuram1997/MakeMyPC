
document.addEventListener('DOMContentLoaded', () => {
    initShoppingCart();
});

let cartData = null;
let currentFpsRes = '1440p';

function initShoppingCart() {
    const root = document.getElementById('checkout-root');
    if (!root) return;
    
    // Load data
    try {
        const checkoutStr = localStorage.getItem('checkout_item');
        if (checkoutStr) {
            const parsed = JSON.parse(checkoutStr);
            if (parsed) {
                cartData = [parsed];
            }
        } else {
            const cartStr = localStorage.getItem('cart');
            if (cartStr) {
                const parsed = JSON.parse(cartStr);
                if (parsed.length > 0) { cartData = parsed; }
            }
        }
    } catch(e) {
        console.error("Error loading cart", e);
    }
    
    if (!cartData || cartData.length === 0) {
        root.innerHTML = `
            <div class="max-w-4xl mx-auto text-center py-32">
                <span class="material-symbols-outlined text-6xl text-on-surface-variant mb-4">shopping_cart</span>
                <h1 class="text-3xl font-bold mb-4">Your Build is Empty</h1>
                <p class="text-on-surface-variant mb-8">Head back to the builder to create your dream PC.</p>
                <a href="custom-pc-builder.html" class="px-8 py-3 bg-primary text-on-primary rounded-lg font-bold hover:bg-primary/90 transition-all">Go to Builder</a>
            </div>
        `;
        return;
    }

    renderCheckoutUI();
}

function renderCheckoutUI() {
    const root = document.getElementById('checkout-root');
    
    let overallPrice = 0;
    let buildsHtml = '';
    
    cartData.forEach((item, index) => {
        // Single product items (component or prebuilt from shop)
        if (item.type === 'component' || item.type === 'prebuilt' || item.type === 'laptop' || item.type === 'monitor') {
            overallPrice += item.price;
            
            buildsHtml += `
                <div class="mb-4">
                    <!-- Single Component Card -->
                    <div class="glass-card rounded-2xl border border-white/10 p-6 flex flex-col md:flex-row items-center justify-between mb-8 shadow-lg hover:border-white/20 transition-all group">
                        <div class="flex items-center gap-6 w-full md:w-1/2 mb-4 md:mb-0">
                            <div class="w-24 h-24 bg-surface-container-low rounded-xl flex items-center justify-center p-2 border border-white/5 relative overflow-hidden shrink-0">
                                <div class="absolute inset-0 bg-gradient-to-br from-electric-blue/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                                <img src="${item.image || 'https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&q=80&w=200'}" alt="${item.name}" class="w-full h-full object-contain relative z-10 drop-shadow-lg">
                            </div>
                            <div>
                                <div class="text-[10px] font-bold text-electric-blue uppercase tracking-wider mb-1 px-2 py-0.5 bg-electric-blue/10 border border-electric-blue/20 rounded-full inline-block">${item.category || 'Component'}</div>
                                <h3 class="text-lg md:text-xl font-bold text-white mb-1 line-clamp-2">${item.name}</h3>
                                <div class="flex items-center gap-2">
                                    <div class="text-xs text-on-surface-variant font-label-mono bg-white/5 px-2 py-0.5 rounded">ID: ${item.id}</div>
                                    <div class="text-xs text-green-400 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">local_shipping</span> 2 Days</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="flex items-center justify-between md:justify-end gap-6 w-full md:w-1/2">
                            <div class="hidden md:block text-right">
                                <div class="text-xs text-on-surface-variant mb-1 uppercase tracking-wider">Unit Price</div>
                                <div class="font-bold text-white font-label-mono">₹${item.price.toLocaleString('en-IN')}</div>
                            </div>
                            
                            <!-- Quantity Selector -->
                            <div class="flex items-center bg-black/40 border border-white/10 rounded-lg overflow-hidden h-10">
                                <button class="w-8 flex items-center justify-center hover:bg-white/10 transition-colors text-on-surface-variant hover:text-white">-</button>
                                <div class="w-8 flex items-center justify-center font-bold text-sm text-white">1</div>
                                <button class="w-8 flex items-center justify-center hover:bg-white/10 transition-colors text-on-surface-variant hover:text-white">+</button>
                            </div>
                            
                            <div class="text-right w-32">
                                <div class="text-xs text-on-surface-variant mb-1 uppercase tracking-wider">Total</div>
                                <div class="font-bold text-xl text-primary font-label-mono">₹${item.price.toLocaleString('en-IN')}</div>
                            </div>
                            
                            <button onclick="window.removeBuild(event, ${index})" class="w-10 h-10 rounded border border-error/30 hover:bg-error/20 flex items-center justify-center transition-colors">
                                <span class="material-symbols-outlined text-[18px] text-error">delete</span>
                            </button>
                        </div>
                    </div>
                </div>
            `;
            return;
        }

        // Full Build Logic
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
        }
        
        // Mock delivery date
        const deliveryDate = new Date();
        deliveryDate.setDate(deliveryDate.getDate() + 5);
        const dateStr = deliveryDate.toLocaleDateString('en-IN', { weekday: 'short', month: 'short', day: 'numeric' });
        
        buildsHtml += `
            <div class="mb-8">
                <!-- Build Card Redesign -->
                <div onclick="window.toggleBuildDetails(${index})" class="glass-card rounded-2xl border border-white/10 overflow-hidden mb-8 shadow-lg cursor-pointer hover:border-white/20 group/card">
                    <div class="flex flex-col md:flex-row">
                        <!-- Left PC Image (Dark theme placeholder) -->
                        <div class="w-full md:w-1/3 bg-[#0a1122] flex items-center justify-center p-6 border-r border-white/10 relative overflow-hidden">
                            <!-- Background accent glow -->
                            <div class="absolute inset-0 bg-gradient-to-tr from-electric-blue/10 to-transparent"></div>
                            <img src="https://images.unsplash.com/photo-1587831990711-23ca6441447b?q=80&w=600&auto=format&fit=crop" class="relative z-10 w-full h-auto object-cover rounded-xl shadow-[0_0_30px_rgba(0,150,255,0.2)]" alt="PC Case">
                            
                            <!-- Index Badge -->
                            <div class="absolute top-4 left-4 w-8 h-8 rounded-full border border-primary text-primary flex items-center justify-center font-bold text-sm bg-background/80 backdrop-blur-md z-20">
                                ${index + 1}
                            </div>
                        </div>
                        
                        <!-- Right Details -->
                        <div class="w-full md:w-2/3 p-6 md:p-8 flex flex-col justify-between">
                            <div>
                                <!-- Header Row -->
                                <div class="flex justify-between items-start mb-2">
                                    <div>
                                        <h2 class="text-2xl md:text-3xl font-black text-white flex items-center gap-2">
                                            ${name || 'Custom PC Build'} #${index + 1}
                                            <span class="material-symbols-outlined text-on-surface-variant text-sm cursor-pointer hover:text-white">edit</span>
                                        </h2>
                                        <div class="flex items-center gap-3 mt-1 text-sm font-label-mono">
                                            <span class="text-on-surface-variant">REF: ${id}</span>
                                            <span class="px-2 py-0.5 bg-blue-500/20 text-blue-400 border border-blue-500/30 rounded text-[10px] font-bold uppercase tracking-wider flex items-center gap-1">
                                                <span class="material-symbols-outlined text-[12px]">verified</span> 100% COMPATIBLE
                                            </span>
                                        </div>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <button onclick="event.stopPropagation()" class="w-8 h-8 rounded border border-white/10 hover:bg-white/10 flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant">content_copy</span>
                                        </button>
                                        <button onclick="window.removeBuild(event, ${index})" class="w-8 h-8 rounded border border-error/30 hover:bg-error/20 flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[16px] text-error">delete</span>
                                        </button>
                                        <button onclick="event.stopPropagation(); window.toggleBuildDetails(${index})" class="w-8 h-8 rounded border border-white/10 hover:bg-white/10 flex items-center justify-center transition-colors">
                                            <span id="icon-build-${index}" class="material-symbols-outlined text-[20px] text-on-surface-variant transform transition-transform duration-300 rotate-0">expand_more</span>
                                        </button>
                                    </div>
                                </div>
                                
                                <!-- Scores Row -->
                                <div class="grid grid-cols-3 gap-4 mt-8 mb-6">
                                    <div class="bg-[#0f172a] border border-white/5 rounded-xl p-4 relative overflow-hidden">
                                        <div class="absolute top-4 right-4"><span class="material-symbols-outlined text-on-surface-variant/50">sports_esports</span></div>
                                        <div class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider mb-2">Gaming Score</div>
                                        <div class="text-3xl font-black text-[#10b981]">98<span class="text-sm text-on-surface-variant">/100</span></div>
                                    </div>
                                    <div class="bg-[#0f172a] border border-white/5 rounded-xl p-4 relative overflow-hidden">
                                        <div class="absolute top-4 right-4"><span class="material-symbols-outlined text-on-surface-variant/50">work</span></div>
                                        <div class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider mb-2">Productivity</div>
                                        <div class="text-3xl font-black text-[#3b82f6]">94<span class="text-sm text-on-surface-variant">/100</span></div>
                                    </div>
                                    <div class="bg-[#0f172a] border border-white/5 rounded-xl p-4 relative overflow-hidden">
                                        <div class="absolute top-4 right-4"><span class="material-symbols-outlined text-on-surface-variant/50">trending_up</span></div>
                                        <div class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider mb-2">Upgradability</div>
                                        <div class="text-3xl font-black text-[#f59e0b]">90<span class="text-sm text-on-surface-variant">/100</span></div>
                                    </div>
                                </div>
                                
                                <!-- Info Row -->
                                <div class="flex items-center gap-6 text-xs text-on-surface-variant">
                                    <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-blue-400">bolt</span> ${totalWattage}W Est. Draw</div>
                                    <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-green-400">local_shipping</span> Est. Delivery: ${dateStr}</div>
                                    <div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-green-400">verified</span> 3-Year Warranty</div>
                                </div>
                            </div>
                            
                            <!-- Internal Card Footer (Guarantees) -->
                            <div class="mt-8 pt-4 border-t border-white/10 grid grid-cols-2 md:grid-cols-5 gap-4">
                                <div class="flex flex-col">
                                    <div class="flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-green-400">shield</span> <span class="text-xs font-bold text-white">Professional Assembly</span></div>
                                    <div class="text-[10px] text-on-surface-variant leading-tight">Expert cable management & clean build</div>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-green-400">timer</span> <span class="text-xs font-bold text-white">24H Stress Testing</span></div>
                                    <div class="text-[10px] text-on-surface-variant leading-tight">Rigorous testing for stability & performance</div>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-green-400">settings</span> <span class="text-xs font-bold text-white">BIOS & OS Setup</span></div>
                                    <div class="text-[10px] text-on-surface-variant leading-tight">Latest updates & optimized settings</div>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-green-400">inventory_2</span> <span class="text-xs font-bold text-white">Secure Packaging</span></div>
                                    <div class="text-[10px] text-on-surface-variant leading-tight">Premium packaging for safe delivery</div>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-center gap-1.5 mb-1"><span class="material-symbols-outlined text-[14px] text-green-400">support_agent</span> <span class="text-xs font-bold text-white">Lifetime Support</span></div>
                                    <div class="text-[10px] text-on-surface-variant leading-tight">Unlimited technical support & guidance</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Build Components Table (Accordion Body) -->
                <div id="details-build-${index}" class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)]">
                    <div class="overflow-hidden">
                        <div class="flex items-center gap-2 mb-4">
                            <span class="material-symbols-outlined text-primary">view_list</span>
                            <h3 class="text-lg font-bold text-white">Build Components (${numComponents})</h3>
                        </div>
                        
                        <div class="glass-card rounded-2xl border border-white/10 overflow-hidden">
                            <!-- Table Header -->
                            <div class="flex items-center px-6 py-3 bg-[#0a1122]/50 border-b border-white/10 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">
                                <div class="w-32">Component</div>
                                <div class="flex-1">Product</div>
                                <div class="w-32 text-right">Price</div>
                                <div class="w-32 text-center">Qty</div>
                                <div class="w-32 text-right">Total</div>
                                <div class="w-12"></div>
                            </div>
                            
                            <!-- Table Rows -->
                            <div class="divide-y divide-white/5">
                                ${Object.keys(parts).filter(k => parts[k]).map((key, partIndex) => {
                                    const part = parts[key];
                                    const subtitle = part.specs ? Object.values(part.specs).join(', ') : 'Premium Component';
                                    return `
                                    <div class="flex items-center px-6 py-4 hover:bg-white/5 transition-colors group">
                                        <!-- Image & Type -->
                                        <div class="w-32 flex items-center gap-4">
                                            <div class="w-10 h-10 rounded bg-[#0f172a] border border-white/5 flex items-center justify-center p-1 overflow-hidden">
                                                ${part.image ? `<img src="${part.image}" class="w-full h-full object-contain">` : `<span class="material-symbols-outlined text-white/30 text-[16px]">memory</span>`}
                                            </div>
                                            <span class="text-[10px] text-[#3b82f6] uppercase font-bold tracking-wider">${key}</span>
                                        </div>
                                        
                                        <!-- Product Name -->
                                        <div class="flex-1 pr-4">
                                            <div class="text-sm font-bold text-white mb-0.5">${part.model}</div>
                                            <div class="text-[10px] text-on-surface-variant truncate max-w-md">${subtitle}</div>
                                        </div>
                                        
                                        <!-- Price -->
                                        <div class="w-32 text-right text-sm font-bold text-white">
                                            ₹${part.price.toLocaleString('en-IN')}
                                        </div>
                                        
                                        <!-- Quantity -->
                                        <div class="w-32 flex justify-center">
                                            <div class="flex items-center bg-[#0f172a] border border-white/10 rounded-lg overflow-hidden">
                                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/10 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">remove</span>
                                                </button>
                                                <span class="w-8 text-center text-sm font-bold">1</span>
                                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/10 transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">add</span>
                                                </button>
                                            </div>
                                        </div>
                                        
                                        <!-- Total -->
                                        <div class="w-32 text-right text-sm font-bold text-white">
                                            ₹${part.price.toLocaleString('en-IN')}
                                        </div>
                                        
                                        <!-- Action Menu -->
                                        <div class="w-12 flex justify-end">
                                            <button class="text-on-surface-variant hover:text-white transition-colors">
                                                <span class="material-symbols-outlined text-[20px]">more_vert</span>
                                            </button>
                                        </div>
                                    </div>
                                    `;
                                }).join('')}
                            </div>
                        </div>
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
            <!-- Header Row -->
            <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-8 gap-4">
                <div>
                    <h1 class="text-3xl font-black text-white">Your Cart (${cartData.length} Item${cartData.length > 1 ? 's' : ''})</h1>
                    <p class="text-on-surface-variant text-sm mt-1">Review your build and proceed to secure checkout</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-4 py-2 bg-transparent border border-white/20 hover:bg-white/10 rounded-lg text-sm font-bold text-white flex items-center gap-2 transition-all">
                        <span class="material-symbols-outlined text-[18px]">save</span> Save Build
                    </button>
                    <button class="px-4 py-2 bg-transparent border border-white/20 hover:bg-white/10 rounded-lg text-sm font-bold text-white flex items-center gap-2 transition-all">
                        <span class="material-symbols-outlined text-[18px]">share</span> Share Build
                    </button>
                </div>
            </div>
            
            <!-- Two Column Layout -->
            <div class="flex flex-col lg:flex-row gap-8">
                
                <!-- Left Content: Components & Details -->
                <div class="flex-1">
                    ${buildsHtml}

                    <!-- Bottom Guarantees -->
                    <div class="glass-card rounded-2xl border border-white/10 p-6 flex flex-wrap justify-between gap-6 mt-8">
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-blue-400 text-2xl">verified</span>
                            <div>
                                <div class="text-sm font-bold text-white">100% Genuine Parts</div>
                                <div class="text-[10px] text-on-surface-variant">Original branded components</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-blue-400 text-2xl">speed</span>
                            <div>
                                <div class="text-sm font-bold text-white">24H Stress Tested</div>
                                <div class="text-[10px] text-on-surface-variant">Before shipping every build</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-blue-400 text-2xl">build</span>
                            <div>
                                <div class="text-sm font-bold text-white">Expert Assembly</div>
                                <div class="text-[10px] text-on-surface-variant">Clean cable management</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-green-400 text-2xl">inventory_2</span>
                            <div>
                                <div class="text-sm font-bold text-white">Secure & Insured</div>
                                <div class="text-[10px] text-on-surface-variant">Safe delivery pan India</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-green-400 text-2xl">shield</span>
                            <div>
                                <div class="text-sm font-bold text-white">3-Year Warranty</div>
                                <div class="text-[10px] text-on-surface-variant">On all custom PC builds</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-blue-400 text-2xl">support_agent</span>
                            <div>
                                <div class="text-sm font-bold text-white">Lifetime Support</div>
                                <div class="text-[10px] text-on-surface-variant">We're here for you</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar: Order Summary -->
                <div class="w-full lg:w-[400px] flex-shrink-0">
                    <div class="sticky top-24 space-y-6">
                        
                        <!-- Order Summary Card -->
                        <div class="bg-[#070e1d] rounded-2xl border border-white/10 overflow-hidden shadow-2xl relative">
                            <!-- Background glow -->
                            <div class="absolute -inset-1 bg-gradient-to-b from-primary/5 to-transparent blur-xl pointer-events-none"></div>
                            
                            <div class="p-6 md:p-8 relative z-10 border-b border-white/5">
                                <h2 class="text-xl font-black text-white mb-6">Order Summary</h2>
                                
                                <div class="space-y-4 text-sm">
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
                                        <div class="text-right">
                                            <span class="text-white font-bold">FREE</span>
                                            <span class="line-through text-white/30 text-xs ml-2">₹2,500</span>
                                        </div>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Prime Packaging</span>
                                        <div class="text-right">
                                            <span class="text-white font-bold">FREE</span>
                                            <span class="line-through text-white/30 text-xs ml-2">₹1,000</span>
                                        </div>
                                    </div>
                                    <div class="flex justify-between text-on-surface-variant">
                                        <span>Secure Shipping</span>
                                        <div class="text-right">
                                            <span class="text-white font-bold">FREE</span>
                                            <span class="line-through text-white/30 text-xs ml-2">₹500</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="p-6 md:p-8 bg-[#0a1122] relative z-10">
                                <div class="flex justify-between items-center mb-1">
                                    <span class="text-sm text-on-surface-variant">You Save</span>
                                    <span class="text-sm font-bold text-green-400">₹4,000</span>
                                </div>
                                <div class="flex justify-between items-end mb-1 mt-4">
                                    <span class="text-sm text-on-surface-variant uppercase font-bold tracking-wider">GRAND TOTAL</span>
                                    <span class="text-3xl font-black text-[#3b82f6]">₹${grandTotal.toLocaleString('en-IN', {minimumFractionDigits: 2})}</span>
                                </div>
                                <div class="text-[10px] text-right text-on-surface-variant mb-1">Inclusive of all taxes</div>
                                <div class="text-xs text-right text-green-400 mb-6 font-bold">You saved ₹2,500 on assembly!</div>
                                
                                <!-- Promo Code -->
                                <div class="flex gap-2 mb-6">
                                    <input type="text" placeholder="Enter promo code" class="flex-1 bg-[#0f172a] border border-white/10 rounded-lg px-4 py-3 text-sm text-white focus:outline-none focus:border-primary/50 transition-colors placeholder:text-on-surface-variant/50">
                                    <button class="px-6 py-3 bg-white/5 hover:bg-white/10 rounded-lg text-sm font-bold text-white transition-all border border-white/5">Apply</button>
                                </div>
                                
                                <!-- EMI Banner -->
                                <div class="bg-black border border-white/10 rounded-xl p-4 flex items-center gap-4 mb-8 cursor-pointer hover:bg-white/5 transition-all">
                                    <span class="material-symbols-outlined text-on-surface-variant text-2xl">credit_card</span>
                                    <div class="flex-1">
                                        <div class="text-sm font-bold text-white">EMI Starts at ₹${Math.floor(grandTotal / 12).toLocaleString('en-IN')}/mo</div>
                                        <div class="text-xs text-on-surface-variant">No Cost EMI available on select cards</div>
                                    </div>
                                    <span class="material-symbols-outlined text-on-surface-variant">chevron_right</span>
                                </div>
                                
                                <!-- Primary Action -->
                                <button class="w-full py-4 bg-[#3b82f6] hover:bg-blue-500 text-white font-black text-lg rounded-xl transition-all flex items-center justify-center gap-2 mb-3">
                                    <span class="material-symbols-outlined">lock</span> Secure Checkout
                                </button>
                                
                                <button class="w-full py-4 bg-white/5 hover:bg-white/10 border border-white/10 text-white font-bold text-sm rounded-xl transition-all mb-3">
                                    Buy Now
                                </button>
                                
                                <button onclick="clearCart()" class="w-full py-4 bg-transparent border border-error/20 hover:bg-error/10 text-error font-bold text-sm rounded-xl transition-all mb-8 flex items-center justify-center gap-2">
                                    <span class="material-symbols-outlined text-[18px]">delete</span> Clear Cart
                                </button>
                                
                                <p class="text-[10px] text-center text-on-surface-variant mb-4">We accept all major Credit Cards, UPI, NetBanking, and EMI.</p>
                                
                                <!-- Payment Logos -->
                                <div class="flex justify-center gap-3 items-center">
                                    <img src="https://cdn.simpleicons.org/visa/1434CB" alt="VISA" class="h-4 opacity-70">
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="MasterCard" class="h-4 opacity-70">
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/UPI-Logo-vector.svg" alt="UPI" class="h-4 opacity-70">
                                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/Paytm_logo.png" alt="Paytm" class="h-4 opacity-70">
                                </div>
                            </div>
                        </div>

                        <!-- Secondary Actions -->
                        <div class="flex gap-4">
                            <button onclick="window.showToast('Generating PDF...', 'info')" class="flex-1 py-3 bg-transparent hover:bg-white/5 border border-white/20 rounded-xl text-sm font-bold text-white flex items-center justify-center gap-2 transition-all">
                                <span class="material-symbols-outlined text-[18px]">picture_as_pdf</span> Save PDF
                            </button>
                            <button onclick="window.showToast('Link copied to clipboard!', 'success')" class="flex-1 py-3 bg-transparent hover:bg-white/5 border border-white/20 rounded-xl text-sm font-bold text-white flex items-center justify-center gap-2 transition-all">
                                <span class="material-symbols-outlined text-[18px]">share</span> Share Build
                            </button>
                        </div>
                        <div class="text-center mt-4">
                            <button onclick="window.location.href='custom-pc-builder.html'" class="text-blue-400 hover:text-blue-300 font-bold text-sm tracking-wider uppercase transition-colors">
                                ← EDIT BUILD
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    root.innerHTML = html;
}

window.toggleBuildDetails = function(index) {
    const details = document.getElementById('details-build-' + index);
    const icon = document.getElementById('icon-build-' + index);
    if (details) {
        if (details.classList.contains('grid-rows-[0fr]')) {
            details.classList.remove('grid-rows-[0fr]');
            details.classList.add('grid-rows-[1fr]');
            if(icon) icon.style.transform = 'rotate(0deg)';
        } else {
            details.classList.remove('grid-rows-[1fr]');
            details.classList.add('grid-rows-[0fr]');
            if(icon) icon.style.transform = 'rotate(180deg)';
        }
    }
};

window.clearCart = function() {
    localStorage.removeItem('cart');
    localStorage.removeItem('checkout_item');
    window.location.reload();
};

window.removeBuild = function(event, index) {
    event.stopPropagation();
    if (cartData && cartData.length > index) {
        cartData.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cartData));
        if (window.updateCartBadge) window.updateCartBadge();
        window.location.reload();
    }
};
