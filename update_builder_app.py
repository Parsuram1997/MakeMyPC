import re

def main():
    filepath = 'c:/Projects/MakeMyPC/js/builder-app.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add filters state
    if 'filters: {' not in content:
        content = content.replace("currentStepIndex: 0,", "currentStepIndex: 0,\n    filters: { searchQuery: '', sortBy: 'popularity', activeFilters: {} },")

    # 2. Add filter definitions and functions right before getCompatibleParts
    filters_code = """
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
        { key: 'form_factor', label: 'Form Factor', options: ['ATX', 'Micro ATX', 'Mini ITX'] },
        { key: 'ram_support', label: 'Memory', options: ['DDR4', 'DDR5'] }
    ],
    ram: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'G.Skill', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['16GB', '32GB', '64GB'] },
        { key: 'type', label: 'Type', options: ['DDR4', 'DDR5'] }
    ],
    gpu: [
        { key: 'brand', label: 'Brand', options: ['NVIDIA', 'AMD', 'Intel'] },
        { key: 'vram', label: 'VRAM', options: ['8GB', '12GB', '16GB', '24GB'] }
    ],
    ssd: [
        { key: 'brand', label: 'Brand', options: ['Samsung', 'Western Digital', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB'] },
        { key: 'pcie_gen', label: 'Generation', options: ['Gen3', 'Gen4', 'Gen5'] }
    ],
    hdd: [
        { key: 'brand', label: 'Brand', options: ['Seagate', 'Western Digital'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB', '8TB'] }
    ],
    cooler: [
        { key: 'brand', label: 'Brand', options: ['NZXT', 'Corsair', 'Noctua', 'Deepcool'] },
        { key: 'type', label: 'Type', options: ['Air Cooler', 'Liquid Cooler'] },
        { key: 'radiator_size', label: 'Size', options: ['120mm', '240mm', '360mm'] }
    ],
    psu: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'EVGA', 'Seasonic'] },
        { key: 'wattage', label: 'Wattage', options: ['650W', '750W', '850W', '1000W'] },
        { key: 'efficiency', label: '80+ Rating', options: ['Bronze', 'Gold', 'Platinum'] }
    ],
    case: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'NZXT', 'Corsair'] },
        { key: 'form_factor', label: 'Form Factor', options: ['ATX', 'Micro ATX', 'Mini ITX'] }
    ],
    fans: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'Corsair', 'Noctua'] },
        { key: 'size', label: 'Size', options: ['120mm', '140mm'] }
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
            <button class="bg-surface-container-low border border-white/10 rounded-lg px-3 py-1.5 text-xs flex items-center gap-2 hover:bg-white/5 transition-all">
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
"""
    if 'function applyFilters' not in content:
        content = content.replace("// 3. Compatibility Engine", filters_code + "\n// 3. Compatibility Engine")

    # 3. Modify renderMainContent to use applyFilters and renderFiltersUI
    if 'const parts = getCompatibleParts(step.key);' in content:
        replacement = """
    const rawParts = getCompatibleParts(step.key);
    renderFiltersUI(step.key);
    const parts = applyFilters(rawParts, step.key);
    
    const countSpan = document.getElementById('product-count');
    if (countSpan) countSpan.textContent = `${parts.length} items`;
    """
        content = content.replace("    const parts = getCompatibleParts(step.key);", replacement)

    # 4. Clear search when changing steps
    if 'state.currentStepIndex = index;' in content:
        content = content.replace("state.currentStepIndex = index;", "state.currentStepIndex = index;\n    state.filters.searchQuery = '';\n    const searchInput = document.getElementById('filter-search');\n    if(searchInput) searchInput.value = '';")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("builder-app.js updated.")

if __name__ == '__main__':
    main()
