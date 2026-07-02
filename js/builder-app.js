// builder-app.js
// Logic for MakeMyPC Custom Builder

const steps = [
    { id: 'cpu', label: 'CPU', key: 'cpu' },
    { id: 'mobo', label: 'Motherboard', key: 'mobo' },
    { id: 'ram', label: 'Memory', key: 'ram' },
    { id: 'gpu', label: 'Graphics', key: 'gpu' },
    { id: 'storage', label: 'Storage', key: 'storage' },
    { id: 'cooler', label: 'Cooler', key: 'cooler' },
    { id: 'psu', label: 'Power Supply', key: 'psu' },
    { id: 'case', label: 'Cabinet', key: 'case' },
    { id: 'fans', label: 'Fans/RGB', key: 'fans' },
    { id: 'accessories', label: 'Accessories', key: 'accessories' }
];

const state = {
    currentStepIndex: 0,
    selections: {
        cpu: null,
        mobo: null,
        ram: null,
        gpu: null,
        storage: null,
        cooler: null,
        psu: null,
        case: null,
        fans: null,
        accessories: null
    }
};

// Formatting currency
const formatPrice = (price) => {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(price);
};

// Initialize App
function initApp() {
    renderTopBar();
    renderSidebar();
    renderMainContent();
}

// 1. Render Top Bar
function renderTopBar() {
    const container = document.getElementById('step-bar-container');
    if (!container) return;
    
    let html = '';
    steps.forEach((step, index) => {
        const isCompleted = !!(step.key && state.selections[step.key]);
        const isSkipped = index < state.currentStepIndex && !isCompleted;
        const isActive = index === state.currentStepIndex;
        
        let circleClass = 'border border-white/20';
        let textClass = 'opacity-50';
        let icon = index + 1;
        
        if (isActive) {
            circleClass = 'bg-primary text-on-primary font-bold hardware-glow border-none';
            textClass = 'text-primary font-bold';
        } else if (isCompleted) {
            circleClass = 'bg-cyber-teal text-on-primary border-none';
            textClass = 'text-cyber-teal';
            icon = '✓';
        } else if (isSkipped) {
            circleClass = 'border-2 border-white/40 text-white/60';
            textClass = 'opacity-60';
            icon = '−'; // A dash to indicate skipped
        }
        
        html += `
            <div class="flex flex-col items-center gap-2 group cursor-pointer transition-all ${!isActive && !isCompleted ? 'hover:opacity-100 opacity-50' : ''}" onclick="goToStep(${index})">
                <div class="w-10 h-10 rounded-full flex items-center justify-center transition-all ${circleClass}">${icon}</div>
                <span class="text-label-mono font-label-mono uppercase text-[10px] whitespace-nowrap ${textClass}">${step.label}</span>
            </div>
        `;
        if (index < steps.length - 1) {
            html += `<div class="h-px flex-1 bg-white/10 mt-[-20px] min-w-[10px]"></div>`;
        }
    });
    
    container.innerHTML = html;
}

// 2. Navigation
window.goToStep = function(index) {
    if (index >= 0 && index < steps.length) {
        state.currentStepIndex = index;
        renderTopBar();
        renderMainContent();
        renderSidebar();
    }
};

window.nextStep = function() {
    goToStep(state.currentStepIndex + 1);
};

// 3. Compatibility Engine
function getCompatibleParts(categoryKey) {
    const allParts = db[categoryKey] || [];
    const cpu = state.selections.cpu;
    const mobo = state.selections.mobo;
    const psu = state.selections.psu;
    const pccase = state.selections.case;

    return allParts.filter(part => {
        // Motherboard -> CPU Socket Match
        if (categoryKey === 'mobo' && cpu) {
            if (part.socket !== cpu.socket) return false;
        }
        // RAM -> Mobo RAM Type Match
        if (categoryKey === 'ram' && mobo) {
            if (part.ram_support !== mobo.ram_support) return false;
        }
        // RAM -> CPU RAM Support (if mobo not selected yet)
        if (categoryKey === 'ram' && !mobo && cpu) {
            if (!cpu.ram_support.includes(part.ram_support)) return false;
        }
        // GPU -> Case clearance
        if (categoryKey === 'gpu' && pccase && part.length > 0) {
            if (part.length > pccase.max_gpu_length) return false;
        }
        // Cooler -> CPU Socket Match & Case clearance
        if (categoryKey === 'cooler') {
            if (cpu && !part.sockets.includes(cpu.socket)) return false;
            if (pccase && part.height > pccase.max_cooler_height) return false;
        }
        return true;
    });
}

// Calculate Total Power
function calculateTotalPower() {
    let power = 50; // Base power for fans/drives
    Object.values(state.selections).forEach(part => {
        if (part && part.power) power += part.power;
    });
    return power;
}

// 4. Render Main Content (Grid or Review)
function renderMainContent() {
    const header = document.getElementById('step-header');
    const desc = document.getElementById('step-desc');
    const grid = document.getElementById('component-grid');
    
    const step = steps[state.currentStepIndex];
    
    if (step.id === 'review') {
        renderReviewPage();
        return;
    }
    if (step.id === 'checkout') {
        renderCheckoutPage();
        return;
    }
    
    header.textContent = `Choose your ${step.label}`;
    desc.textContent = `Select a compatible ${step.label.toLowerCase()} for your build. Incompatible parts are automatically hidden.`;
    
    const parts = getCompatibleParts(step.key);
    
    let html = '';
    if (parts.length === 0) {
        html = `<div class="p-8 text-center text-on-surface-variant glass-card rounded-xl">No compatible parts found based on your previous selections.</div>`;
    } else {
        parts.forEach(part => {
            const isSelected = state.selections[step.key] && state.selections[step.key].id === part.id;
            
            html += `
            <div class="glass-card rounded-xl p-6 flex flex-col md:flex-row items-center gap-8 group transition-all ${isSelected ? 'border-primary shadow-[0_0_20px_rgba(0,122,255,0.2)]' : ''}">
                <div class="w-48 h-48 flex-shrink-0 relative overflow-hidden rounded-lg bg-black/20 flex items-center justify-center p-4">
                    ${part.image ? `<img src="${part.image}" class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-500 hardware-glow" alt="${part.model}">` : `<span class="material-symbols-outlined text-4xl text-on-surface-variant">hardware</span>`}
                </div>
                <div class="flex-1 w-full">
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            ${part.badge ? `<span class="bg-primary/10 text-primary px-2 py-1 rounded text-[10px] font-label-mono uppercase mb-2 inline-block">${part.badge}</span>` : ''}
                            <div class="text-on-surface-variant text-[10px] uppercase tracking-widest">${part.brand}</div>
                            <h3 class="text-headline-sm font-headline-sm leading-tight">${part.model}</h3>
                        </div>
                        <div class="text-right">
                            <div class="text-headline-sm font-headline-sm text-primary">${formatPrice(part.price)}</div>
                            <div class="text-label-mono text-on-surface-variant text-[10px]">${part.stock}</div>
                        </div>
                    </div>
                    
                    <div class="flex flex-wrap gap-2 mb-6">
                        ${part.features.map(f => `<div class="bg-white/5 px-3 py-1.5 rounded-lg border border-white/5 text-[11px] font-label-mono text-cyber-teal">${f}</div>`).join('')}
                    </div>
                    
                    <div class="flex gap-3">
                        <button onclick="selectPart('${step.key}', '${part.id}')" class="flex-1 py-3 rounded-lg font-bold transition-all active:scale-95 ${isSelected ? 'bg-white/10 text-primary border border-primary/50' : 'bg-primary text-on-primary hover:brightness-110'}">
                            ${isSelected ? 'Selected' : 'Add to Build'}
                        </button>
                        <button title="${part.features.join(', ')}" onclick="window.showToast('Specs: ' + decodeURIComponent('${encodeURIComponent(part.features.join(', '))}'), 'info')" class="w-12 h-12 flex items-center justify-center border border-white/10 rounded-lg hover:bg-white/5 transition-all text-on-surface-variant">
                            <span class="material-symbols-outlined">info</span>
                        </button>
                    </div>
                </div>
            </div>
            `;
        });
    }
    grid.innerHTML = html;
}

window.selectPart = function(categoryKey, partId) {
    const part = db[categoryKey].find(p => p.id === partId);
    state.selections[categoryKey] = part;
    
    // Auto-advance if not the last step
    if (state.currentStepIndex < steps.length - 1) {
        goToStep(state.currentStepIndex + 1);
    } else {
        renderMainContent();
        renderSidebar();
        renderTopBar();
    }
};

window.removePart = function(categoryKey) {
    state.selections[categoryKey] = null;
    renderSidebar();
    renderMainContent();
    renderTopBar();
};

// 5. Render Sidebar
function renderSidebar() {
    if (typeof window.renderAdvancedSidebar === 'function') {
        window.renderAdvancedSidebar();
    }
}

window.removePart = function(stepKey) {
    state.selections[stepKey] = null;
    initApp();
};

// 6. Review Page
function renderReviewPage() {
    const header = document.getElementById('step-header');
    const desc = document.getElementById('step-desc');
    const grid = document.getElementById('component-grid');
    
    header.textContent = `Review Your Custom PC`;
    desc.textContent = `Everything looks great! Check your compatibility report and final pricing below.`;
    
    let subtotal = 0;
    let partsHtml = '';
    
    steps.filter(s => s.key).forEach(step => {
        const part = state.selections[step.key];
        if (part) {
            subtotal += part.price;
            partsHtml += `
            <div class="flex justify-between items-center py-4 border-b border-white/5">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-white/5 rounded p-1">
                        ${part.image ? `<img src="${part.image}" class="w-full h-full object-contain">` : ''}
                    </div>
                    <div>
                        <div class="text-[10px] text-on-surface-variant uppercase">${step.label}</div>
                        <div class="font-medium">${part.brand} ${part.model}</div>
                    </div>
                </div>
                <div class="font-label-mono text-primary">${formatPrice(part.price)}</div>
            </div>
            `;
        }
    });
    
    const gst = subtotal * 0.18;
    const assembly = 1500;
    const shipping = subtotal > 100000 ? 0 : 500;
    const grandTotal = subtotal + gst + assembly + shipping;
    
    grid.innerHTML = `
    <div class="glass-card rounded-xl p-8">
        <h3 class="text-headline-sm font-headline-sm mb-6 flex items-center gap-2 text-cyber-teal">
            <span class="material-symbols-outlined">verified</span> All parts are 100% compatible
        </h3>
        
        <div class="mb-8">
            ${partsHtml}
        </div>
        
        <div class="bg-surface-container rounded-lg p-6 space-y-3 font-label-mono text-sm">
            <div class="flex justify-between text-on-surface-variant">
                <span>Subtotal (Excl. Tax)</span>
                <span>${formatPrice(subtotal)}</span>
            </div>
            <div class="flex justify-between text-on-surface-variant">
                <span>GST (18%)</span>
                <span>${formatPrice(gst)}</span>
            </div>
            <div class="flex justify-between text-on-surface-variant">
                <span>Professional Assembly</span>
                <span>${formatPrice(assembly)}</span>
            </div>
            <div class="flex justify-between text-on-surface-variant">
                <span>Shipping (Pan-India)</span>
                <span>${shipping === 0 ? 'FREE' : formatPrice(shipping)}</span>
            </div>
            <div class="h-px w-full bg-white/10 my-4"></div>
            <div class="flex justify-between text-headline-sm font-headline-sm text-primary">
                <span>Grand Total</span>
                <span>${formatPrice(grandTotal)}</span>
            </div>
        </div>
        
        <div class="mt-8 flex gap-4">
            <button class="flex-1 bg-electric-blue text-white py-4 rounded-xl font-bold shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:brightness-110 active:scale-95 transition-all" onclick="goToStep(11)">
                Proceed to Secure Checkout
            </button>
            <button class="px-6 py-4 rounded-xl border border-white/20 hover:bg-white/5 font-medium flex items-center gap-2 transition-all">
                <span class="material-symbols-outlined">download</span> Download PDF
            </button>
        </div>
    </div>
    `;
}

function renderCheckoutPage() {
    const build = {
        id: 'MPC-' + Math.floor(Math.random() * 1000000),
        name: 'Custom PC Build',
        parts: state.selections,
        price: Object.values(state.selections).reduce((sum, p) => sum + (p ? p.price : 0), 0)
    };
    
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    cart.push(build);
    localStorage.setItem('cart', JSON.stringify(cart));
    
    window.location.href = 'shopping-cart.html';
}

// Ensure init when DOM loads
document.addEventListener('DOMContentLoaded', initApp);
