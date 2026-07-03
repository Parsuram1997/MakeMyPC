import re

def main():
    filepath = 'c:/Projects/MakeMyPC/compare-products.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Replace the graph section
    graph_pattern = re.compile(r'<div class="space-y-12 relative z-10">\s*<!-- Graph Row 1 -->.*?<!-- Graph Row 2 -->.*?</div>\s*<!-- Background decoration -->', re.DOTALL)
    
    new_graphs = r'''<div class="space-y-12 relative z-10">
<!-- Power Draw Section -->
<div class="space-y-2">
    <h3 class="font-label-mono text-label-mono text-on-surface mb-6 uppercase tracking-widest border-b border-white/10 pb-2">Power Draw (W) <span class="text-[10px] text-on-surface-variant normal-case tracking-normal ml-2">Lower is better</span></h3>
    
    <!-- Intel -->
    <div class="flex justify-between items-center text-xs mb-2">
        <span class="text-on-surface-variant font-label-mono">Intel Core i9-14900K</span>
        <span class="text-electric-blue font-bold">253W</span>
    </div>
    <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6">
        <div class="h-full bg-electric-blue w-[85%] rounded-full shadow-[0_0_10px_rgba(0,122,255,0.5)]"></div>
    </div>
    
    <!-- AMD 1 -->
    <div class="flex justify-between items-center text-xs mb-2">
        <span class="text-on-surface-variant font-label-mono">AMD Ryzen 7950X3D</span>
        <span class="text-cyber-teal font-bold">120W</span>
    </div>
    <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6">
        <div class="h-full bg-cyber-teal w-[40%] rounded-full shadow-[0_0_10px_rgba(0,164,166,0.5)]"></div>
    </div>
    
    <!-- CPU 3 Slot for Power -->
    <div id="power-cpu3-slot"></div>
</div>

<!-- Thermal Section -->
<div class="space-y-2">
    <h3 class="font-label-mono text-label-mono text-on-surface mb-6 uppercase tracking-widest border-b border-white/10 pb-2">Thermal Junction (°C) <span class="text-[10px] text-on-surface-variant normal-case tracking-normal ml-2">Lower is better</span></h3>
    
    <!-- Intel -->
    <div class="flex justify-between items-center text-xs mb-2">
        <span class="text-on-surface-variant font-label-mono">Intel Core i9-14900K</span>
        <span class="text-electric-blue font-bold">100°C</span>
    </div>
    <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6">
        <div class="h-full bg-electric-blue w-[100%] rounded-full shadow-[0_0_10px_rgba(0,122,255,0.5)]"></div>
    </div>
    
    <!-- AMD 1 -->
    <div class="flex justify-between items-center text-xs mb-2">
        <span class="text-on-surface-variant font-label-mono">AMD Ryzen 7950X3D</span>
        <span class="text-cyber-teal font-bold">89°C</span>
    </div>
    <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6">
        <div class="h-full bg-cyber-teal w-[89%] rounded-full shadow-[0_0_10px_rgba(0,164,166,0.5)]"></div>
    </div>
    
    <!-- CPU 3 Slot for Thermal -->
    <div id="thermal-cpu3-slot"></div>
</div>
</div>
<!-- Background decoration -->'''

    if not graph_pattern.search(content):
        print("Graph pattern not found!")
    else:
        content = graph_pattern.sub(new_graphs, content)
        print("Graphs replaced.")

    # Now update selectThirdItem to inject the 3rd bars
    js_pattern = re.compile(r'(function selectThirdItem\(\) \{.*?if\(cpu3Slot\) \{.*?cpu3Slot\.innerHTML = `.*?`;\s*\})', re.DOTALL)
    
    new_js_addition = r'''\1
            
            // Also add to the Power & Thermal Efficiency chart
            const powerSlot = document.getElementById('power-cpu3-slot');
            const thermalSlot = document.getElementById('thermal-cpu3-slot');
            const legendContainer = document.querySelector('.flex.gap-4.font-label-mono.text-label-mono');
            
            if(powerSlot) {
                powerSlot.innerHTML = `
                <div class="flex justify-between items-center text-xs mb-2 animate-fade-in mt-4">
                    <span class="text-on-surface-variant font-label-mono">AMD Ryzen 7800X3D</span>
                    <span class="text-primary font-bold">120W</span>
                </div>
                <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6 animate-fade-in">
                    <div class="h-full bg-primary w-[40%] rounded-full shadow-[0_0_10px_rgba(173,198,255,0.5)] transition-all duration-1000" style="width: 0%" data-target-width="40%"></div>
                </div>
                `;
                
                // Animate the new bar
                setTimeout(() => {
                    const bar = powerSlot.querySelector('.bg-primary');
                    if(bar) bar.style.width = bar.getAttribute('data-target-width');
                }, 100);
            }
            
            if(thermalSlot) {
                thermalSlot.innerHTML = `
                <div class="flex justify-between items-center text-xs mb-2 animate-fade-in mt-4">
                    <span class="text-on-surface-variant font-label-mono">AMD Ryzen 7800X3D</span>
                    <span class="text-primary font-bold">89°C</span>
                </div>
                <div class="h-3 w-full bg-white/5 rounded-full overflow-hidden mb-6 animate-fade-in">
                    <div class="h-full bg-primary w-[89%] rounded-full shadow-[0_0_10px_rgba(173,198,255,0.5)] transition-all duration-1000" style="width: 0%" data-target-width="89%"></div>
                </div>
                `;
                
                // Animate the new bar
                setTimeout(() => {
                    const bar = thermalSlot.querySelector('.bg-primary');
                    if(bar) bar.style.width = bar.getAttribute('data-target-width');
                }, 100);
            }
            
            if (legendContainer && !legendContainer.innerHTML.includes('3rd CPU')) {
                legendContainer.innerHTML += `
                <div class="flex items-center gap-2 animate-fade-in">
                    <span class="w-3 h-3 rounded-full bg-primary"></span>
                    3rd CPU
                </div>`;
            }'''
            
    if not js_pattern.search(content):
        print("JS pattern not found!")
    else:
        content = js_pattern.sub(new_js_addition, content)
        print("JS updated.")
        
    # Also update the global bar animation script to include the primary class
    anim_pattern = re.compile(r"document\.querySelectorAll\('\.h-full\.bg-electric-blue, \.h-full\.bg-cyber-teal'\)")
    content = anim_pattern.sub(r"document.querySelectorAll('.h-full.bg-electric-blue, .h-full.bg-cyber-teal, .h-full.bg-primary')", content)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated compare-products.html")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
