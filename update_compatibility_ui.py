import re

sidebar_file = "c:/Projects/MakeMyPC/js/builder-sidebar.js"
with open(sidebar_file, "r", encoding="utf-8") as f:
    content = f.read()

# Update Compatibility Status logic
old_logic = """    // Compatibility Status
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
    }"""

new_logic = """    // Compatibility Status
    let compatStatus = 'Clear';
    let compatColor = 'text-cyber-teal';
    let compatIcon = 'check_circle';
    let compatBg = 'bg-cyber-teal/5 border-cyber-teal/20';
    let compatMessages = [];
    let criticalWarnings = [];

    if (hasCpu) compatMessages.push({ icon: 'memory', text: 'CPU Socket Compatible', type: 'success' });
    if (hasGpu) compatMessages.push({ icon: 'developer_board', text: 'PCIe Generation Matches', type: 'success' });
    if (state.selections.mobo && state.selections.case) {
        compatMessages.push({ icon: 'aspect_ratio', text: 'Motherboard fits in Cabinet', type: 'success' });
    }
    
    if (selectedCount === 0) {
        compatStatus = 'Waiting for Parts';
        compatColor = 'text-on-surface-variant';
        compatIcon = 'inventory_2';
        compatBg = 'bg-white/5 border-white/10';
    } else if (state.selections.psu && !isPsuSufficient) {
        compatStatus = 'Action Required';
        compatColor = 'text-error';
        compatIcon = 'error';
        compatBg = 'bg-error/5 border-error/20';
        
        criticalWarnings.push(`
            <div class="mt-3 bg-error/10 border border-error/20 rounded p-3 text-error flex gap-3 items-start">
                <span class="material-symbols-outlined text-[18px]">bolt</span>
                <div class="flex-1">
                    <strong class="block text-[11px] uppercase tracking-wider mb-1">Power Bottleneck Detected</strong>
                    <span class="text-[10px] text-error/80 leading-relaxed block">Your system requires an estimated <strong>${recPsu}W</strong>, but the selected PSU provides only <strong>${state.selections.psu.power}W</strong>. This can cause unexpected shutdowns and instability.</span>
                    <button onclick="window.goToStep(7)" class="mt-2 px-3 py-1.5 bg-error/20 hover:bg-error/30 rounded text-[9px] font-bold tracking-widest transition-colors uppercase w-full">Upgrade PSU</button>
                </div>
            </div>
        `);
    }"""

content = content.replace(old_logic, new_logic)

# Update HTML rendering
old_html = """            <!-- Compatibility Status -->
            <div class="bg-white/5 border border-white/10 rounded-xl p-4 relative overflow-hidden group">
                <div class="absolute -right-6 -top-6 w-24 h-24 bg-${compatColor.split('-')[1]}/20 rounded-full blur-2xl group-hover:bg-${compatColor.split('-')[1]}/30 transition-all"></div>
                <div class="flex items-center gap-3 mb-2">
                    <span class="material-symbols-outlined text-2xl ${compatColor}">${compatIcon}</span>
                    <h3 class="font-headline-sm text-sm uppercase tracking-widest ${compatColor}">Compatibility ${compatStatus}</h3>
                </div>
                <div class="text-[11px] text-on-surface-variant space-y-1 font-label-mono">
                    ${compatMessages.length > 0 ? compatMessages.map(m => `<div>${m}</div>`).join('') : 'Select parts to check compatibility.'}
                </div>
            </div>"""

new_html = """            <!-- Compatibility Status -->
            <div class="${compatBg} rounded-xl p-4 relative overflow-hidden group transition-all duration-300">
                <div class="absolute -right-6 -top-6 w-24 h-24 bg-${compatColor.split('-')[1]}/10 rounded-full blur-2xl group-hover:bg-${compatColor.split('-')[1]}/20 transition-all"></div>
                
                <div class="flex items-center gap-3 mb-3 relative z-10">
                    <span class="material-symbols-outlined text-2xl ${compatColor}">${compatIcon}</span>
                    <h3 class="font-headline-sm text-sm uppercase tracking-widest ${compatColor}">Compatibility ${compatStatus}</h3>
                </div>
                
                <div class="space-y-1.5 relative z-10">
                    ${compatMessages.length > 0 ? compatMessages.map(m => `
                        <div class="flex items-center gap-2 text-[10px] font-label-mono text-on-surface-variant bg-black/20 px-2 py-1.5 rounded">
                            <span class="material-symbols-outlined text-[14px] text-cyber-teal">check_circle</span>
                            <span>${m.text}</span>
                        </div>
                    `).join('') : '<div class="text-[11px] text-on-surface-variant font-label-mono italic">Select parts to run compatibility checks.</div>'}
                </div>
                
                <div class="relative z-10">
                    ${criticalWarnings.join('')}
                </div>
            </div>"""

content = content.replace(old_html, new_html)

with open(sidebar_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Compatibility Warning UI.")
