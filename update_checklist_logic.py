import re

sidebar_file = "c:/Projects/MakeMyPC/js/builder-sidebar.js"
with open(sidebar_file, "r", encoding="utf-8") as f:
    content = f.read()

old_logic = """                <div class="space-y-2">
                    ${['CPU Socket', 'Motherboard Chipset', 'BIOS Support', 'RAM Type (DDR4/DDR5)', 'RAM Capacity', 'GPU PCIe Match', 'GPU Length vs Cabinet', 'CPU Cooler Socket', 'Radiator Support', 'PSU Wattage'].map(check => {
                        const isDone = Math.random() > 0.5 && selectedCount > 2; // Mock logic
                        return `
                        <div class="flex items-center gap-2 text-[11px] font-label-mono">
                            <span class="material-symbols-outlined text-[14px] ${isDone ? 'text-cyber-teal' : 'text-white/20'}">${isDone ? 'check_circle' : 'radio_button_unchecked'}</span>
                            <span class="${isDone ? 'text-white' : 'text-on-surface-variant'}">${check}</span>
                        </div>
                        `;
                    }).join('')}
                </div>"""

new_logic = """                <div class="space-y-2">
                    ${[
                        { label: 'CPU Socket', done: !!(state.selections.cpu && state.selections.mobo) },
                        { label: 'Motherboard Chipset', done: !!state.selections.mobo },
                        { label: 'BIOS Support', done: !!state.selections.mobo },
                        { label: 'RAM Type (DDR4/DDR5)', done: !!(state.selections.ram && state.selections.mobo) },
                        { label: 'RAM Capacity', done: !!state.selections.ram },
                        { label: 'GPU PCIe Match', done: !!(state.selections.gpu && state.selections.mobo) },
                        { label: 'GPU Length vs Cabinet', done: !!(state.selections.gpu && state.selections.case) },
                        { label: 'CPU Cooler Socket', done: !!(state.selections.cpu && state.selections.cooler) },
                        { label: 'Radiator Support', done: !!(state.selections.cooler && state.selections.case) },
                        { label: 'PSU Wattage', done: !!(state.selections.psu && isPsuSufficient) }
                    ].map(check => {
                        const isDone = check.done;
                        return `
                        <div class="flex items-center gap-2 text-[11px] font-label-mono">
                            <span class="material-symbols-outlined text-[14px] ${isDone ? 'text-cyber-teal' : 'text-white/20'}">${isDone ? 'check_circle' : 'radio_button_unchecked'}</span>
                            <span class="${isDone ? 'text-white' : 'text-on-surface-variant'}">${check.label}</span>
                        </div>
                        `;
                    }).join('')}
                </div>"""

content = content.replace(old_logic, new_logic)

with open(sidebar_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated checklist mock logic.")
