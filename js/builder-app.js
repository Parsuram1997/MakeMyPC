// builder-app.js
// Logic for MakeMyPC Custom Builder

const steps = [
    { id: 'os', label: 'OS', key: 'os' },
    { id: 'cpu', label: 'CPU', key: 'cpu' },
    { id: 'mobo', label: 'Board', key: 'mobo' },
    { id: 'ram', label: 'RAM', key: 'ram' },
    { id: 'ssd', label: 'SSD', key: 'ssd' },
    { id: 'hdd', label: 'HDD', key: 'hdd' },
    { id: 'cooler', label: 'Cooler', key: 'cooler' },
    { id: 'psu', label: 'PSU', key: 'psu' },
    { id: 'case', label: 'Case', key: 'case' },
    { id: 'gpu', label: 'GPU', key: 'gpu' },
    { id: 'fans', label: 'Fans', key: 'fans' },
    { id: 'rgb', label: 'RGB', key: 'rgb' },
    { id: 'accessories', label: 'Accessories', key: 'accessories' },
    { id: 'review', label: 'Review', key: null }
];

const state = {
    currentStepIndex: 0,
    filters: { searchQuery: '', sortBy: 'popularity', activeFilters: {} },
    selections: {
        cpu: null,
        mobo: null,
        ram: null,
        gpu: null,
        ssd: null,
        hdd: null,
        cooler: null,
        psu: null,
        case: null,
        fans: null,
        rgb: null,
        accessories: null,
        os: null
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

function renderTopBar() {
    let containerWrapper = document.getElementById('step-bar-wrapper');
    const oldContainer = document.getElementById('step-bar-container');
    
    // Create wrapper if not exists to fix cutoff
    if (oldContainer && !containerWrapper) {
        containerWrapper = document.createElement('div');
        containerWrapper.id = 'step-bar-wrapper';
        containerWrapper.className = 'w-full overflow-x-auto custom-scrollbar pb-2 mb-4';
        oldContainer.parentNode.insertBefore(containerWrapper, oldContainer);
        containerWrapper.appendChild(oldContainer);
        oldContainer.classList.add('min-w-max');
        oldContainer.classList.remove('mb-6');
    }
    
    const container = document.getElementById('step-bar-container');
    if (!container) return;
    
    let html = '';
    steps.forEach((step, index) => {
        let isCompleted = !!(step.key && state.selections[step.key]);
        if (step.id === 'review') {
            const requiredParts = ['cpu', 'mobo', 'ram', 'ssd', 'psu', 'case', 'os'];
            isCompleted = requiredParts.every(part => state.selections[part]);
        }
        
        const isSkipped = index < state.currentStepIndex && !isCompleted;
        const isActive = index === state.currentStepIndex;
        
        let circleClass = 'border border-white/20';
        let textClass = 'opacity-50';
        let icon = index + 1;
        
        if (isActive && isCompleted) {
            circleClass = 'bg-cyber-teal text-on-primary font-bold hardware-glow border-none';
            textClass = 'text-cyber-teal font-bold';
            icon = '✓';
        } else if (isActive) {
            circleClass = 'bg-primary text-on-primary font-bold hardware-glow border-none';
            textClass = 'text-primary font-bold';
            icon = index + 1;
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
                <span class="text-label-mono font-label-mono text-[11px] whitespace-nowrap ${textClass}">${step.label}</span>
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
    state.filters.searchQuery = '';
    const searchInput = document.getElementById('filter-search');
    if(searchInput) searchInput.value = '';
        renderTopBar();
        renderMainContent();
        renderSidebar();
    }
};

window.nextStep = function() {
    goToStep(state.currentStepIndex + 1);
};


// 2.5 Filtering Engine
const filterDefinitions = {
    cpu: [
        { key: 'brand', label: 'Brand', options: ['Intel', 'AMD'] },
        { key: 'socket', label: 'Socket', options: ['LGA1700', 'AM4', 'AM5'] },
        { key: 'core_count', label: 'Cores', options: ['6', '8', '12', '16', '24'] }
    ],
    mobo: [
        { key: 'brand', label: 'Brand', options: ['ASUS', 'MSI', 'Gigabyte', 'ASRock'] },
        { key: 'socket', label: 'Socket', options: ['LGA1700', 'AM4', 'AM5'] },
        { key: 'form_factor', label: 'Size', options: ['ATX', 'Micro ATX', 'Mini ITX'] }
    ],
    ram: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'G.Skill', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['16GB', '32GB', '64GB'] },
        { key: 'type', label: 'Type', options: ['DDR4', 'DDR5'] }
    ],
    gpu: [
        { key: 'brand', label: 'Brand', options: ['NVIDIA', 'AMD', 'Intel'] },
        { key: 'vram', label: 'VRAM', options: ['8GB', '12GB', '16GB', '24GB'] },
        { key: 'memory_type', label: 'Mem Type', options: ['GDDR6', 'GDDR6X'] }
    ],
    ssd: [
        { key: 'brand', label: 'Brand', options: ['Samsung', 'Western Digital', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB'] },
        { key: 'pcie_gen', label: 'Generation', options: ['Gen3', 'Gen4', 'Gen5'] }
    ],
    hdd: [
        { key: 'brand', label: 'Brand', options: ['Seagate', 'Western Digital'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB', '8TB'] },
        { key: 'rpm', label: 'Speed', options: ['5400', '7200'] }
    ],
    cooler: [
        { key: 'brand', label: 'Brand', options: ['NZXT', 'Corsair', 'Noctua', 'Deepcool'] },
        { key: 'type', label: 'Type', options: ['Air Cooler', 'Liquid Cooler'] },
        { key: 'radiator_size', label: 'Rad Size', options: ['120mm', '240mm', '360mm'] }
    ],
    psu: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'EVGA', 'Seasonic'] },
        { key: 'wattage', label: 'Wattage', options: ['650W', '750W', '850W', '1000W'] },
        { key: 'efficiency', label: 'Rating', options: ['Bronze', 'Gold', 'Platinum'] }
    ],
    case: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'NZXT', 'Corsair'] },
        { key: 'form_factor', label: 'Size', options: ['ATX', 'Micro ATX', 'Mini ITX'] },
        { key: 'color', label: 'Color', options: ['Black', 'White'] }
    ],
        os: [
        { key: 'brand', label: 'Brand', options: ['Microsoft', 'Canonical', 'Custom'] }
    ],
        rgb: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'DeepCool'] },
        { key: 'type', label: 'Type', options: ['LED Strip'] }
    ],
    fans: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'Corsair', 'Noctua'] },
        { key: 'size', label: 'Size', options: ['120mm', '140mm'] },
        { key: 'rgb', label: 'RGB', options: ['Yes', 'No', 'ARGB'] }
    ]
};

window.updateSearch = function(query) {
    state.filters.searchQuery = query.toLowerCase();
    renderMainContent();
};

window.setSort = function(sortType) {
    state.filters.sortBy = sortType;
    const sortBtn = document.getElementById('current-sort');
    if (sortBtn) {
        if (sortType === 'popularity') sortBtn.textContent = 'Popularity';
        if (sortType === 'price_asc') sortBtn.textContent = 'Price: Low to High';
        if (sortType === 'price_desc') sortBtn.textContent = 'Price: High to Low';
    }
    renderMainContent();
};

window.toggleFilter = function(category, key, value) {
    if (!state.filters.activeFilters[category]) {
        state.filters.activeFilters[category] = {};
    }
    if (!state.filters.activeFilters[category][key]) {
        state.filters.activeFilters[category][key] = [];
    }
    
    const arr = state.filters.activeFilters[category][key];
    const index = arr.indexOf(value);
    if (index > -1) {
        arr.splice(index, 1);
        if (arr.length === 0) delete state.filters.activeFilters[category][key];
    } else {
        arr.push(value);
    }
    renderMainContent();
};

window.clearFilters = function() {
    state.filters.activeFilters = {};
    state.filters.searchQuery = '';
    const searchInput = document.getElementById('filter-search');
    if (searchInput) searchInput.value = '';
    renderMainContent();
};

function applyFilters(parts, category) {
    let result = [...parts];
    
    // Search
    if (state.filters.searchQuery) {
        result = result.filter(p => 
            p.brand.toLowerCase().includes(state.filters.searchQuery) || 
            p.model.toLowerCase().includes(state.filters.searchQuery)
        );
    }
    
    // Active Filters
    const active = state.filters.activeFilters[category];
    if (active) {
        Object.keys(active).forEach(filterKey => {
            const selectedValues = active[filterKey];
            if (selectedValues.length > 0) {
                result = result.filter(p => {
                    const pVal = p[filterKey];
                    if (Array.isArray(pVal)) {
                        return pVal.some(v => selectedValues.includes(v));
                    }
                    return selectedValues.includes(pVal);
                });
            }
        });
    }
    
    // Sort
    if (state.filters.sortBy === 'price_asc') {
        result.sort((a, b) => a.price - b.price);
    } else if (state.filters.sortBy === 'price_desc') {
        result.sort((a, b) => b.price - a.price);
    }
    
    return result;
}

function renderFiltersUI(category) {
    const container = document.getElementById('dynamic-filters');
    const chipsContainer = document.getElementById('active-filters-container');
    const clearBtn = document.getElementById('clear-filters-btn');
    if (!container || !chipsContainer) return;
    
    const defs = filterDefinitions[category];
    if (!defs) {
        container.innerHTML = '';
        chipsContainer.innerHTML = '';
        if(clearBtn) clearBtn.classList.add('hidden');
        return;
    }
    
    let html = '';
    let chipsHtml = '';
    let hasFilters = false;
    const active = state.filters.activeFilters[category] || {};

    defs.forEach(def => {
        let activeCount = active[def.key] ? active[def.key].length : 0;
        
        html += `
        <div class="relative group/dropdown">
            <button class="bg-surface-container-low border border-white/10 rounded-lg px-3 py-1.5 text-xs flex items-center justify-between w-28 hover:bg-white/5 transition-all">
                ${def.label} ${activeCount > 0 ? `<span class="bg-primary text-on-primary rounded-full w-4 h-4 flex items-center justify-center text-[10px]">${activeCount}</span>` : '<span class="material-symbols-outlined text-[14px]">arrow_drop_down</span>'}
            </button>
            <div class="absolute left-0 top-full mt-2 w-48 bg-surface-deep border border-white/10 rounded-lg shadow-2xl opacity-0 invisible group-hover/dropdown:opacity-100 group-hover/dropdown:visible transition-all flex flex-col z-50 p-2 max-h-64 overflow-y-auto">
        `;
        
        def.options.forEach(opt => {
            const isChecked = active[def.key] && active[def.key].includes(opt);
            html += `
                <label class="flex items-center gap-2 px-2 py-1.5 hover:bg-white/5 rounded cursor-pointer text-sm">
                    <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="window.toggleFilter('${category}', '${def.key}', '${opt}')" class="rounded border-white/20 bg-black/50 text-primary focus:ring-primary focus:ring-offset-surface">
                    ${opt}
                </label>
            `;
            
            if (isChecked) {
                hasFilters = true;
                chipsHtml += `
                    <div class="bg-primary/10 text-primary border border-primary/20 rounded-full px-3 py-1 text-xs flex items-center gap-1">
                        ${opt}
                        <button onclick="window.toggleFilter('${category}', '${def.key}', '${opt}')" class="hover:text-white"><span class="material-symbols-outlined text-[14px]">close</span></button>
                    </div>
                `;
            }
        });
        
        html += `</div></div>`;
    });
    
    container.innerHTML = html;
    chipsContainer.innerHTML = chipsHtml;
    
    if (clearBtn) {
        if (hasFilters) clearBtn.classList.remove('hidden');
        else clearBtn.classList.add('hidden');
    }
}

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
            if (part.type !== mobo.ram_support) return false;
        }
        // RAM -> CPU RAM Support (if mobo not selected yet)
        if (categoryKey === 'ram' && !mobo && cpu) {
            if (!cpu.ram_support.includes(part.type)) return false;
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
    
    const filterContainer = document.getElementById('filter-container');
    
    if (step.id === 'review') {
        if (filterContainer) filterContainer.classList.add('hidden');
        renderReviewPage();
        return;
    }
    if (filterContainer) filterContainer.classList.remove('hidden');
    
    if (step.id === 'checkout') {
        renderCheckoutPage();
        return;
    }
    
    header.textContent = `Choose your ${step.label}`;
    desc.textContent = `Select a compatible ${step.label.toLowerCase()} for your build. Incompatible parts are automatically hidden.`;
    

    const rawParts = getCompatibleParts(step.key);
    renderFiltersUI(step.key);
    const parts = applyFilters(rawParts, step.key);
    
    const countSpan = document.getElementById('product-count');
    if (countSpan) countSpan.textContent = `${parts.length} items`;
    
    
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
                        
                        <a href="https://amazon.in/s?k=${encodeURIComponent(part.brand + ' ' + part.model)}" target="_blank" title="Buy on Amazon" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-[#FF9900]/10 transition-all text-[#FF9900] group/amz p-2">
                            <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-full h-full group-hover/amz:scale-110 transition-transform">
                                <path d="M13.882 17.587c-2.316.924-4.708 1.4-6.848 1.4-2.825 0-4.664-.476-4.664-.476.368.96 1.637 1.777 3.328 2.053 2.378.435 5.094.343 7.568-.313 1.15-.316 2.062-.843 2.062-.843l-1.446-1.82zM12.22 8.718c-.802 0-1.39.29-1.724.97-.13.3-.223.774-.223 1.258 0 1.22.28 1.968.805 2.502.493.523 1.144.693 1.956.693.687 0 1.206-.21 1.576-.412v-1.61c-.413.284-.91.433-1.343.433-.61 0-1.015-.226-1.223-.54-.22-.32-.224-.8-.224-1.35v-1.1h2.984v-1.2h-2.984V6.02h-1.61v2.33h-.995v1.2h.995v1.48c0 .927.203 1.636.577 2.128.434.524.966.71 1.868.71.97 0 1.79-.24 2.158-.403v-1.18c-.428-.276-1.14-.6-2.18-.6z"/>
                            </svg>
                        </a>

                        <a href="https://www.flipkart.com/search?q=${encodeURIComponent(part.brand + ' ' + part.model)}" target="_blank" title="Buy on Flipkart" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-[#2874F0]/10 transition-all group/fk p-2">
                            <img src="images/flipkart-icon.png" alt="Flipkart" class="w-full h-full object-contain group-hover/fk:scale-110 transition-transform">
                        </a>

                        <button title="${part.features.join(', ')}" onclick="window.showToast('Specs: ' + decodeURIComponent('${encodeURIComponent(part.features.join(', '))}'), 'info')" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-white/5 transition-all text-on-surface-variant">
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
            <div class="flex justify-between items-center py-2 border-b border-white/5">
                <div class="flex items-center gap-4">
                    <div class="w-10 h-10 bg-white/5 rounded p-1">
                        ${part.image ? `<img src="${part.image}" class="w-full h-full object-contain">` : ''}
                    </div>
                    <div>
                        <div class="text-[10px] text-on-surface-variant uppercase">${step.label}</div>
                        <div class="font-medium text-sm">${part.brand} ${part.model}</div>
                    </div>
                </div>
                <div class="font-label-mono text-primary text-sm">${formatPrice(part.price)}</div>
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
        
        <div class="mb-2">
            ${partsHtml}
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
