import os

file_path = r'c:\Projects\MakeMyPC\js\shopping-cart.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_loop_start = """    cartData.forEach((build, index) => {
        const { parts, price, name, id } = build;
        overallPrice += price;
        
        let totalWattage = 0;"""

new_loop_start = """    cartData.forEach((item, index) => {
        if (item.type === 'component') {
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
        overallPrice += price;
        
        let totalWattage = 0;"""

content = content.replace(old_loop_start, new_loop_start)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated shopping-cart.js")
