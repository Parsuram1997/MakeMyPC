
// smart-builder.js

const smartBuilder = {
    state: {
        step: 1,
        os: null,
        purpose: null,
        budget: null,
        generatedBuild: null,
        totalPrice: 0
    },

    selectOS(os) {
        this.state.os = os;
        this.goToStep(2);
    },

    selectPurpose(purpose) {
        this.state.purpose = purpose;
        this.goToStep(3);
    },

    selectBudget(budget) {
        this.state.budget = budget;
        this.goToStep(4);
        this.generateBuild();
    },

    goToStep(step) {
        this.state.step = step;
        
        // Hide all steps
        document.querySelectorAll('.wizard-step').forEach(el => {
            el.classList.remove('active');
        });
        
        // Show target step
        document.getElementById(`step-${step}`).classList.add('active');
        
        this.updateProgress();
    },

    prevStep() {
        if (this.state.step > 1) {
            this.goToStep(this.state.step - 1);
        }
    },

    reset() {
        this.state.os = null;
        this.state.purpose = null;
        this.state.budget = null;
        this.state.generatedBuild = null;
        this.state.totalPrice = 0;
        
        if (window.state && window.state.selections) {
            window.state.selections = {};
            if (typeof renderAdvancedSidebar === 'function') renderAdvancedSidebar();
        }
        
        document.getElementById('result-state').classList.add('hidden');
        document.getElementById('loading-state').classList.remove('hidden');
        this.goToStep(1);
    },

    updateProgress() {
        const container = document.getElementById('wizard-progress');
        if (!container) return;
        
        let html = '';
        const builderSteps = ['OS', 'Purpose', 'Budget', 'Review'];
        builderSteps.forEach((label, index) => {
            const stepNum = index + 1;
            const isActive = stepNum === this.state.step;
            const isCompleted = stepNum < this.state.step;
            const isSkipped = stepNum > this.state.step && !isCompleted;
            
            let circleClass = 'border border-white/20';
            let textClass = 'opacity-50';
            let icon = stepNum;
            
            if (isActive && isCompleted) {
                circleClass = 'bg-cyber-teal text-on-primary font-bold hardware-glow border-none';
                textClass = 'text-cyber-teal font-bold';
                icon = '✓';
            } else if (isActive) {
                circleClass = 'bg-primary text-on-primary font-bold hardware-glow border-none';
                textClass = 'text-primary font-bold';
                icon = stepNum;
            } else if (isCompleted) {
                circleClass = 'bg-cyber-teal text-on-primary border-none';
                textClass = 'text-cyber-teal';
                icon = '✓';
            } else if (isSkipped) {
                circleClass = 'border-2 border-white/40 text-white/60';
                textClass = 'opacity-60';
                icon = '−';
            }
            
            html += `
                <div class="flex flex-col items-center gap-2 group cursor-pointer transition-all ${!isActive && !isCompleted ? 'hover:opacity-100 opacity-50' : ''}" onclick="smartBuilder.goToStep(${stepNum})">
                    <div class="w-10 h-10 rounded-full flex items-center justify-center transition-all ${circleClass}">${icon}</div>
                    <span class="text-label-mono font-label-mono uppercase text-[10px] whitespace-nowrap ${textClass}">${label}</span>
                </div>
            `;
            if (index < builderSteps.length - 1) {
                html += `<div class="h-px flex-1 bg-white/10 mt-[-20px] min-w-[10px]"></div>`;
            }
        });
        
        container.className = 'flex items-center justify-between mb-6 w-full';
        container.innerHTML = html;
        
        if (typeof renderAdvancedSidebar === 'function') renderAdvancedSidebar();
    },

    generateBuild() {
        document.getElementById('loading-state').classList.remove('hidden');
        document.getElementById('result-state').classList.add('hidden');
        
        setTimeout(() => {
            this.runRecommendationEngine();
            
            if (window.state && window.state.selections) {
                Object.keys(this.state.generatedBuild).forEach(key => {
                    window.state.selections[key] = this.state.generatedBuild[key];
                });
                if (typeof renderAdvancedSidebar === 'function') renderAdvancedSidebar();
            }
            
            this.renderResult();
            
            document.getElementById('loading-state').classList.add('hidden');
            document.getElementById('result-state').classList.remove('hidden');
        }, 1500);
    },

    runRecommendationEngine() {
        const { os, purpose, budget } = this.state;
        const build = {};
        let remainingBudget = budget;
        
        // Define allocation ratios based on purpose
        let allocations = {};
        if (purpose === 'gaming') {
            allocations = { gpu: 0.45, cpu: 0.20, mobo: 0.10, ram: 0.08, storage: 0.07, psu: 0.05, case: 0.05 };
        } else if (purpose === 'creation') {
            allocations = { cpu: 0.35, gpu: 0.25, ram: 0.15, mobo: 0.10, storage: 0.10, psu: 0.05, case: 0.00 }; 
        } else if (purpose === 'developer') {
            allocations = { cpu: 0.45, ram: 0.25, storage: 0.15, mobo: 0.10, psu: 0.05, case: 0.00, gpu: 0.0 };
        } else { // office
            allocations = { cpu: 0.40, ram: 0.15, storage: 0.15, mobo: 0.15, psu: 0.10, case: 0.05, gpu: 0.0 };
        }

        // Helper to find best component within a target price
        const findBestComponent = (category, targetPrice) => {
            if (!db[category]) return null;
            
            let validParts = [...db[category]].sort((a, b) => b.price - a.price);
            
            // If we have a CPU, filter motherboards by socket
            if (category === 'mobo' && build.cpu) {
                validParts = validParts.filter(p => p.socket === build.cpu.socket);
            }
            
            // If we have a CPU/Mobo, filter RAM by generation
            if (category === 'ram' && build.cpu && build.cpu.ram_support) {
                validParts = validParts.filter(p => build.cpu.ram_support.includes(p.generation || (p.model.includes('DDR5') ? 'DDR5' : 'DDR4')));
            }
            
            // OS-specific filtering: If Linux, prioritize AMD GPUs (we'll filter out NVIDIA if there are AMD alternatives)
            if (category === 'gpu' && os === 'linux') {
                const amdGpus = validParts.filter(p => p.brand.toUpperCase().includes('AMD') || p.model.toUpperCase().includes('RADEON'));
                if (amdGpus.length > 0) {
                    validParts = amdGpus;
                }
            }
            
            // If office and no GPU allocation, try to get CPU with integrated graphics
            if (category === 'cpu' && purpose === 'office') {
                validParts = validParts.filter(p => p.integrated_graphics === true || p.integrated_graphics === 'Yes');
            }

            // Find the most expensive part that fits the target price
            let selected = validParts.find(p => p.price <= targetPrice);
            
            // Fallback: If nothing fits target price, just take the cheapest valid part
            if (!selected && validParts.length > 0) {
                selected = validParts[validParts.length - 1]; 
            }
            
            return selected || null;
        };

        // Pick parts in order of importance
        const order = ['cpu', 'gpu', 'mobo', 'ram', 'storage', 'psu', 'case'];
        let total = 0;

        order.forEach(cat => {
            const alloc = allocations[cat] || 0;
            let targetPrice = budget * alloc;
            
            // If budget is ultimate, just set target price super high
            if (budget === 999999) targetPrice = 999999;
            
            if (targetPrice > 0 || budget === 999999) {
                const part = findBestComponent(cat, targetPrice);
                if (part) {
                    build[cat] = part;
                    total += part.price;
                    remainingBudget -= part.price;
                }
            } else {
                build[cat] = null;
            }
        });
        
        // Ensure PSU if GPU exists
        if (build.gpu && !build.psu) {
            build.psu = findBestComponent('psu', 10000); // Default fallback PSU
            if(build.psu) total += build.psu.price;
        }

        // Add standard cooler if CPU doesn't have one and we have budget/need
        if (build.cpu && (!build.cpu.includes_cooler || purpose !== 'office')) {
            const cooler = findBestComponent('cooler', remainingBudget > 10000 ? 10000 : 3000);
            if (cooler) {
                build.cooler = cooler;
                total += cooler.price;
            }
        }
        
        this.state.generatedBuild = build;
        this.state.totalPrice = total;
    },

    renderResult() {
        const { purpose, budget, generatedBuild, totalPrice } = this.state;
        
        document.getElementById('res-purpose').textContent = purpose;
        document.getElementById('res-budget').textContent = budget === 999999 ? 'No Limit' : `₹${(budget/100000).toFixed(1)}L`;
        document.getElementById('res-total').textContent = `₹${totalPrice.toLocaleString('en-IN')}`;
        
        const container = document.getElementById('recommended-parts-container');
        let html = '<h3 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-electric-blue">memory</span> Recommended Components</h3>';
        
        const categories = {
            cpu: 'Processor', mobo: 'Motherboard', ram: 'Memory', 
            gpu: 'Graphics', storage: 'Storage', psu: 'Power Supply',
            case: 'Cabinet', cooler: 'Cooler'
        };
        
        Object.entries(categories).forEach(([key, label]) => {
            const part = generatedBuild[key];
            if (!part) return;
            
            html += `
                <div class="flex items-center gap-4 py-4 border-b border-white/5 last:border-0 group">
                    <div class="w-16 h-16 rounded-xl bg-surface-deep border border-white/10 flex items-center justify-center p-2 flex-shrink-0">
                        ${part.image ? `<img src="${part.image}" class="w-full h-full object-contain">` : `<span class="material-symbols-outlined text-white/30 text-2xl">hardware</span>`}
                    </div>
                    <div class="flex-1">
                        <div class="text-[10px] text-electric-blue font-bold tracking-wider uppercase mb-1">${label}</div>
                        <div class="font-bold text-sm">${part.model}</div>
                        <div class="text-xs text-on-surface-variant truncate">${part.brand} • ${(part.features || []).slice(0,2).join(' • ') || part.id}</div>
                    </div>
                    <div class="font-bold text-sm">₹${part.price.toLocaleString('en-IN')}</div>
                </div>
            `;
        });
        
        container.innerHTML = html;
    },

    addToCart() {
        if (!this.state.generatedBuild) return;
        
        const build = {
            id: 'SMART-' + Math.floor(100000 + Math.random() * 900000),
            name: `Smart ${this.state.purpose.charAt(0).toUpperCase() + this.state.purpose.slice(1)} Build`,
            parts: this.state.generatedBuild,
            price: this.state.totalPrice
        };
        
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        cart.push(build);
        localStorage.setItem('cart', JSON.stringify(cart));
        
        window.location.href = 'shopping-cart.html';
    },

    editInBuilder() {
        if (!this.state.generatedBuild) return;
        // The builder uses a different format, but we can pass it via localStorage
        // To simplify, we will just redirect for now. A robust implementation would map parts to the builder's state format.
        // Let's create a temporary session key that builder-app.js could theoretically pick up.
        localStorage.setItem('smart_builder_transfer', JSON.stringify(this.state.generatedBuild));
        window.location.href = 'custom-pc-builder.html';
    }
};

document.addEventListener('DOMContentLoaded', () => {
    smartBuilder.updateProgress();
});

window.smartBuilder = smartBuilder;
