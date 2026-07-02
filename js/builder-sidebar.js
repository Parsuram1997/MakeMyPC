// builder-sidebar.js
// Advanced Sidebar Rendering for MakeMyPC Custom Builder

let activeTab = 'summary'; // 'summary', 'checklist', 'components'
let fpsResolution = '1440p'; // '1080p', '1440p', '4k'

function renderAdvancedSidebar() {
    const root = document.getElementById('sidebar-root');
    if (!root) return;

    // Calculate totals
    let total = 0;
    const selectedCount = Object.keys(state.selections).filter(k => state.selections[k]).length;
    
    // Mock Data Generators
    let gamingScore = 0;
    let powerW = 0;
    let hasCpu = !!state.selections.cpu;
    let hasGpu = !!state.selections.gpu;
    let hasRam = !!state.selections.ram;

    steps.filter(s => s.key).forEach(step => {
        const part = state.selections[step.key];
        if (part) {
            total += part.price;
            if (part.power) powerW += part.power;
        }
    });

    if (hasCpu && hasGpu) {
        gamingScore = Math.min(100, Math.floor((total / 300000) * 100)); // Mock logic
    }

    const recPsu = powerW > 0 ? powerW + 150 : 0;
    const isPsuSufficient = state.selections.psu ? state.selections.psu.power >= recPsu : false;

    // Compatibility Status
    let compatStatus = 'Clear';
    let compatColor = 'text-cyber-teal';
    let compatIcon = 'check_circle';
    let compatMessages = [];

    if (hasCpu) compatMessages.push('✓ CPU Selected');
    if (hasGpu) compatMessages.push('✓ GPU Selected');
    
    if (selectedCount === 0) {
        compatStatus = 'Waiting for Parts';
        compatColor = 'text-on-surface-variant';
        compatIcon = 'inventory_2';
    } else if (state.selections.psu && !isPsuSufficient) {
        compatStatus = 'Warning';
        compatColor = 'text-warning';
        compatIcon = 'warning';
        compatMessages.push('⚠ PSU capacity might be insufficient');
    }

    const gst = total * 0.18;
    const subtotal = total - gst;
    const grandTotal = total;

    // FPS Mock Data
    const fpsData = {
        'Cyberpunk 2077': { '1080p': 120, '1440p': 85, '4k': 45 },
        'Call of Duty': { '1080p': 240, '1440p': 165, '4k': 95 },
        'Valorant': { '1080p': 500, '1440p': 350, '4k': 200 },
        'Black Myth: Wukong': { '1080p': 90, '1440p': 65, '4k': 40 },
    };

    let html = `
        <!-- Sticky Tabs -->
        <div class="flex-shrink-0 bg-surface-deep/95 backdrop-blur-md z-10 border-b border-white/5 p-4 flex gap-2">
            <button onclick="setSidebarTab('summary')" class="flex-1 py-1.5 text-xs font-bold rounded-lg transition-all ${activeTab === 'summary' ? 'bg-primary text-on-primary' : 'bg-white/5 text-on-surface-variant hover:bg-white/10'}">Summary</button>
            <button onclick="setSidebarTab('checklist')" class="flex-1 py-1.5 text-xs font-bold rounded-lg transition-all ${activeTab === 'checklist' ? 'bg-primary text-on-primary' : 'bg-white/5 text-on-surface-variant hover:bg-white/10'}">Checklist</button>
            <button onclick="setSidebarTab('components')" class="flex-1 py-1.5 text-xs font-bold rounded-lg transition-all ${activeTab === 'components' ? 'bg-primary text-on-primary' : 'bg-white/5 text-on-surface-variant hover:bg-white/10'}">Parts</button>
        </div>
        
        <div class="p-6 flex-1 flex flex-col gap-6 overflow-y-auto custom-scrollbar">
    `;

    if (activeTab === 'summary') {
        html += `
            <!-- Compatibility Status -->
            <div class="bg-white/5 border border-white/10 rounded-xl p-4 relative overflow-hidden group">
                <div class="absolute -right-6 -top-6 w-24 h-24 bg-${compatColor.split('-')[1]}/20 rounded-full blur-2xl group-hover:bg-${compatColor.split('-')[1]}/30 transition-all"></div>
                <div class="flex items-center gap-3 mb-2">
                    <span class="material-symbols-outlined text-2xl ${compatColor}">${compatIcon}</span>
                    <h3 class="font-headline-sm text-sm uppercase tracking-widest ${compatColor}">Compatibility ${compatStatus}</h3>
                </div>
                <div class="text-[11px] text-on-surface-variant space-y-1 font-label-mono">
                    ${compatMessages.length > 0 ? compatMessages.map(m => `<div>${m}</div>`).join('') : 'Select parts to check compatibility.'}
                </div>
            </div>

            <!-- Price Breakdown -->
            <div>
                <span class="text-label-mono text-on-surface-variant uppercase text-[10px] mb-1 block">Total Price</span>
                <div class="text-3xl font-headline-lg text-primary tracking-tighter mb-2">${formatPrice(grandTotal)}</div>
                
                <details class="group cursor-pointer">
                    <summary class="text-[11px] text-on-surface-variant hover:text-white transition-colors font-label-mono outline-none list-none flex items-center justify-between border-t border-white/5 pt-2">
                        <span>View Breakdown</span>
                        <span class="material-symbols-outlined text-[14px] group-open:rotate-180 transition-transform">expand_more</span>
                    </summary>
                    <div class="mt-2 space-y-1 text-[11px] font-label-mono text-on-surface-variant">
                        <div class="flex justify-between"><span>Components (Subtotal)</span><span>${formatPrice(subtotal)}</span></div>
                        <div class="flex justify-between"><span>GST (18%)</span><span>${formatPrice(gst)}</span></div>
                        <div class="flex justify-between"><span>Assembly & Testing</span><span class="text-cyber-teal">FREE</span></div>
                        <div class="flex justify-between"><span>Premium Shipping</span><span class="text-cyber-teal">FREE</span></div>
                    </div>
                </details>
            </div>

            <!-- Estimated Power -->
            <div class="bg-white/5 rounded-lg p-3 border border-white/5">
                <div class="flex justify-between items-center mb-2">
                    <span class="text-label-mono text-on-surface-variant uppercase text-[10px]">Estimated Power</span>
                    <div class="flex items-center gap-1 text-tertiary">
                        <span class="material-symbols-outlined text-[14px]">bolt</span>
                        <span class="font-label-mono text-[11px] font-bold">${powerW}W</span>
                    </div>
                </div>
                <div class="w-full bg-black/50 h-1.5 rounded-full overflow-hidden mb-1">
                    <div class="h-full bg-gradient-to-r from-tertiary to-error transition-all" style="width: ${Math.min(100, (powerW/1200)*100)}%"></div>
                </div>
                <div class="text-[9px] font-label-mono text-on-surface-variant text-right">${recPsu}W Recommended PSU</div>
            </div>

            <!-- Gaming Performance -->
            <div>
                <div class="flex justify-between items-center mb-3">
                    <span class="text-label-mono text-on-surface-variant uppercase text-[10px]">Gaming Performance</span>
                    <div class="flex bg-white/5 rounded-md p-0.5">
                        <button onclick="setFpsRes('1080p')" class="px-2 py-0.5 text-[9px] font-label-mono rounded ${fpsResolution==='1080p'?'bg-primary text-white':'text-on-surface-variant'}">1080p</button>
                        <button onclick="setFpsRes('1440p')" class="px-2 py-0.5 text-[9px] font-label-mono rounded ${fpsResolution==='1440p'?'bg-primary text-white':'text-on-surface-variant'}">1440p</button>
                        <button onclick="setFpsRes('4k')" class="px-2 py-0.5 text-[9px] font-label-mono rounded ${fpsResolution==='4k'?'bg-primary text-white':'text-on-surface-variant'}">4K</button>
                    </div>
                </div>
                
                ${hasCpu && hasGpu && hasRam ? 
                Object.keys(fpsData).map(game => {
                    // Adjust FPS based on total price as a mock indicator
                    const baseFps = fpsData[game][fpsResolution];
                    const multiplier = total > 0 ? Math.min(1.5, Math.max(0.5, total / 200000)) : 1;
                    const estFps = Math.round(baseFps * multiplier);
                    return `
                    <div class="mb-2">
                        <div class="flex justify-between text-[10px] mb-1 font-label-mono">
                            <span>${game}</span>
                            <span class="text-primary font-bold">${estFps} FPS</span>
                        </div>
                        <div class="w-full bg-white/5 h-1 rounded-full overflow-hidden">
                            <div class="h-full bg-primary transition-all duration-500" style="width: ${Math.min(100, (estFps/240)*100)}%"></div>
                        </div>
                    </div>
                    `;
                }).join('') 
                : 
                '<div class="text-[10px] text-on-surface-variant italic text-center p-4 bg-white/5 rounded border border-white/5">Select CPU, GPU, and RAM to view estimates.</div>'
                }
            </div>

            <!-- Health Scores -->
            <div>
                <span class="text-label-mono text-on-surface-variant uppercase text-[10px] mb-2 block">Build Scores</span>
                <div class="grid grid-cols-2 gap-2">
                    <div class="bg-white/5 p-2 rounded flex flex-col gap-1">
                        <span class="text-[9px] font-label-mono text-on-surface-variant">Gaming</span>
                        <div class="text-sm font-bold text-cyber-teal">${gamingScore}/100</div>
                    </div>
                    <div class="bg-white/5 p-2 rounded flex flex-col gap-1">
                        <span class="text-[9px] font-label-mono text-on-surface-variant">Productivity</span>
                        <div class="text-sm font-bold text-electric-blue">${hasCpu ? 85 : 0}/100</div>
                    </div>
                </div>
            </div>
        `;
    } else if (activeTab === 'checklist') {
        html += `
            <div class="space-y-4">
                <div>
                    <h3 class="text-sm font-bold mb-2">Detailed Compatibility</h3>
                    <p class="text-[11px] text-on-surface-variant mb-4">Our engine checks 20+ parameters to ensure a perfect fit.</p>
                </div>

                <div class="space-y-2">
                    ${['CPU Socket', 'Motherboard Chipset', 'BIOS Support', 'RAM Type (DDR4/DDR5)', 'RAM Capacity', 'GPU PCIe Match', 'GPU Length vs Cabinet', 'CPU Cooler Socket', 'Radiator Support', 'PSU Wattage'].map(check => {
                        const isDone = Math.random() > 0.5 && selectedCount > 2; // Mock logic
                        return `
                        <div class="flex items-center gap-2 text-[11px] font-label-mono">
                            <span class="material-symbols-outlined text-[14px] ${isDone ? 'text-cyber-teal' : 'text-white/20'}">${isDone ? 'check_circle' : 'radio_button_unchecked'}</span>
                            <span class="${isDone ? 'text-white' : 'text-on-surface-variant'}">${check}</span>
                        </div>
                        `;
                    }).join('')}
                </div>
                
                <div class="mt-4 pt-4 border-t border-white/5 space-y-2">
                    <h4 class="text-[10px] uppercase font-label-mono text-on-surface-variant mb-2">Expected Characteristics</h4>
                    <div class="flex justify-between items-center text-[10px] font-label-mono">
                        <span>Noise Level</span>
                        <span class="text-tertiary">Moderate</span>
                    </div>
                    <div class="flex justify-between items-center text-[10px] font-label-mono">
                        <span>Airflow Rating</span>
                        <span class="text-cyber-teal">Excellent</span>
                    </div>
                </div>
            </div>
        `;
    } else if (activeTab === 'components') {
        html += `
            <div class="space-y-2">
                <span class="text-label-mono text-on-surface-variant uppercase text-[10px] mb-2 block">Selected Parts</span>
        `;
        
        const icons = {
            cpu: 'memory', mobo: 'dns', ram: 'memory_alt', gpu: 'developer_board',
            storage: 'hard_drive', cooler: 'ac_unit', psu: 'power', case: 'desktop_windows',
            fans: 'mode_fan', accessories: 'keyboard'
        };

        steps.filter(s => s.key).forEach(step => {
            const part = state.selections[step.key];
            if (part) {
                html += `
                <div class="flex gap-3 bg-white/5 p-2 rounded-lg border border-white/5 relative group">
                    <div class="w-10 h-10 rounded bg-black/50 flex-shrink-0 flex items-center justify-center overflow-hidden">
                        ${part.image ? `<img src="${part.image}" class="w-full h-full object-cover">` : `<span class="material-symbols-outlined text-[16px] text-primary">${icons[step.key]}</span>`}
                    </div>
                    <div class="flex-1 min-w-0 flex flex-col justify-center">
                        <span class="text-[9px] font-label-mono text-on-surface-variant uppercase truncate">${step.label}</span>
                        <span class="text-xs font-bold truncate">${part.model}</span>
                        <span class="text-[10px] text-primary font-label-mono">${formatPrice(part.price)}</span>
                    </div>
                    <div class="absolute right-2 top-1/2 -translate-y-1/2 flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity bg-surface p-1 rounded border border-white/10 shadow-lg">
                        <button onclick="goToStep(${steps.findIndex(s=>s.key===step.key)})" title="Replace" class="w-6 h-6 flex items-center justify-center hover:bg-white/10 rounded text-electric-blue"><span class="material-symbols-outlined text-[14px]">swap_horiz</span></button>
                        <button onclick="removePart('${step.key}')" title="Remove" class="w-6 h-6 flex items-center justify-center hover:bg-error/20 rounded text-error"><span class="material-symbols-outlined text-[14px]">delete</span></button>
                    </div>
                </div>
                `;
            } else {
                html += `
                <div onclick="goToStep(${steps.findIndex(s=>s.key===step.key)})" class="flex items-center gap-3 p-2 rounded-lg border border-dashed border-white/10 opacity-40 hover:opacity-100 transition-opacity cursor-pointer">
                    <div class="w-10 h-10 rounded flex-shrink-0 flex items-center justify-center bg-white/5">
                        <span class="material-symbols-outlined text-[16px] text-white/50">${icons[step.key]}</span>
                    </div>
                    <span class="text-xs">Select ${step.label}</span>
                </div>
                `;
            }
        });
        html += `</div>`;
    }

    html += `
        </div>
        
        <!-- Sticky Action Buttons -->
        <div class="flex-shrink-0 p-4 bg-surface-deep/95 backdrop-blur-md border-t border-white/10 space-y-2">
            <div class="flex gap-2 mb-2">
                <button onclick="window.showToast('Save feature coming soon', 'info')" class="flex-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded font-label-mono text-[10px] uppercase flex items-center justify-center gap-1 transition-colors"><span class="material-symbols-outlined text-[14px]">save</span> Save</button>
                <button onclick="window.showToast('Share link copied to clipboard!', 'success')" class="flex-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded font-label-mono text-[10px] uppercase flex items-center justify-center gap-1 transition-colors"><span class="material-symbols-outlined text-[14px]">share</span> Share</button>
                <button onclick="window.showToast('Generating PDF...', 'info')" class="flex-1 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded font-label-mono text-[10px] uppercase flex items-center justify-center gap-1 transition-colors"><span class="material-symbols-outlined text-[14px]">picture_as_pdf</span> PDF</button>
            </div>
            <button id="sidebar-checkout-btn" class="w-full bg-electric-blue text-white py-3 rounded-lg font-bold flex items-center justify-center gap-2 shadow-[0_0_20px_rgba(0,122,255,0.3)] hover:brightness-110 active:scale-95 transition-all ${total > 0 ? '' : 'opacity-50 pointer-events-none'}">
                <span class="material-symbols-outlined text-[18px]">shopping_cart_checkout</span>
                <span>${total > 0 ? 'Checkout' : 'Add Parts First'}</span>
            </button>
            <div class="text-center text-[9px] text-cyber-teal font-label-mono mt-2">
                <span class="material-symbols-outlined text-[10px] align-middle">local_shipping</span> Est. Delivery: 3-5 Business Days
            </div>
        </div>
    `;

    root.innerHTML = html;
    
    // Bind checkout button if ready
    if (total > 0) {
        document.getElementById('sidebar-checkout-btn').onclick = () => { 
            const build = {
                id: 'MPC-' + Math.floor(100000 + Math.random() * 900000),
                name: 'Custom PC Build',
                parts: state.selections,
                price: total
            };
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            cart.push(build);
            localStorage.setItem('cart', JSON.stringify(cart));
            window.location.href = 'shopping-cart.html'; 
        };
    }
}

window.setSidebarTab = function(tab) {
    activeTab = tab;
    renderAdvancedSidebar();
};

window.setFpsRes = function(res) {
    fpsResolution = res;
    renderAdvancedSidebar();
};
