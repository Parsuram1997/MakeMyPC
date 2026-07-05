import re

with open('js/smart-builder.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace updateProgress
old_progress_match = re.search(r'updateProgress\(\)\s*\{.*?progressContainer\.innerHTML = html;\s*\},', content, re.DOTALL)
if old_progress_match:
    new_progress = """updateProgress() {
        const container = document.getElementById('wizard-progress');
        if (!container) return;
        
        let html = '';
        const builderSteps = ['Purpose', 'Budget', 'Review'];
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
    },"""
    content = content.replace(old_progress_match.group(0), new_progress)

# Replace generateBuild
old_gen_match = re.search(r'generateBuild\(\)\s*\{.*?1500\);\s*// Simulate processing delay\s*\},', content, re.DOTALL)
if old_gen_match:
    new_gen = """generateBuild() {
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
    },"""
    content = content.replace(old_gen_match.group(0), new_gen)

# Replace reset
old_reset_match = re.search(r'reset\(\)\s*\{.*?this\.goToStep\(1\);\s*\},', content, re.DOTALL)
if old_reset_match:
    new_reset = """reset() {
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
    },"""
    content = content.replace(old_reset_match.group(0), new_reset)

with open('js/smart-builder.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated js/smart-builder.js")
