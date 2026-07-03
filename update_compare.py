import re
import sys

def main():
    filepath = 'c:/Projects/MakeMyPC/compare-products.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # 1. Remove the floating left labels
    # Look for the exact block
    pattern_labels = re.compile(r'<!-- Column Labels \(Visible on Desktop\) -->\s*<div class="hidden lg:block absolute -left-48[^>]+>.*?</div>\s*<!-- CPU 1: Intel Core i9 -->', re.DOTALL)
    content = pattern_labels.sub('<!-- CPU 1: Intel Core i9 -->', content)

    # 2. Refactor Intel Spec List
    intel_spec_pattern = re.compile(r'(<!-- Spec List -->\s*<div class="flex flex-col gap-4">)\s*(<!-- Benchmarking Card -->\s*<div class="glass-card rounded-2xl p-5 border-l-4 border-electric-blue">.*?</div>)\s*<!-- Specs Bento -->\s*<div class="grid grid-cols-2 gap-4">\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">Raptor Lake</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">6\.0 GHz</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">24 \(8P\+16E\)</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">125W - 253W</p>\s*</div>)\s*</div>', re.DOTALL)
    
    intel_replacement = r'''\1
    <h4 class="font-label-mono text-[10px] text-electric-blue uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Gaming Performance</h4>
    \2
    
    <h4 class="font-label-mono text-[10px] text-electric-blue uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Architecture & Speeds</h4>
    <div class="grid grid-cols-2 gap-4">
        \3
        \4
    </div>
    
    <h4 class="font-label-mono text-[10px] text-electric-blue uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Cores & Efficiency</h4>
    <div class="grid grid-cols-2 gap-4">
        \5
        \6
    </div>'''
    
    content = intel_spec_pattern.sub(intel_replacement, content)

    # 3. Refactor AMD Spec List
    amd_spec_pattern = re.compile(r'(<!-- Spec List -->\s*<div class="flex flex-col gap-4">)\s*(<!-- Benchmarking Card -->\s*<div class="glass-card rounded-2xl p-5 border-l-4 border-cyber-teal">.*?</div>)\s*<!-- Specs Bento -->\s*<div class="grid grid-cols-2 gap-4">\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">Zen 4 / 3D</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">5\.7 GHz</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">16 Cores</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4">.*?<p class="font-label-mono text-on-surface">120W Max</p>\s*</div>)\s*</div>', re.DOTALL)
    
    amd_replacement = r'''\1
    <h4 class="font-label-mono text-[10px] text-cyber-teal uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Gaming Performance</h4>
    \2
    
    <h4 class="font-label-mono text-[10px] text-cyber-teal uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Architecture & Speeds</h4>
    <div class="grid grid-cols-2 gap-4">
        \3
        \4
    </div>
    
    <h4 class="font-label-mono text-[10px] text-cyber-teal uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Cores & Efficiency</h4>
    <div class="grid grid-cols-2 gap-4">
        \5
        \6
    </div>'''
    
    content = amd_spec_pattern.sub(amd_replacement, content)

    # 4. Add min-h-[130px] and flex to all glass-card p-4 (the spec boxes)
    content = content.replace('class="glass-card rounded-2xl p-4"', 'class="glass-card rounded-2xl p-4 flex flex-col justify-between min-h-[130px]"')

    # Also fix the JS function we injected earlier for the 3rd item
    js_pattern = re.compile(r'(<div class="glass-card rounded-2xl p-5 border-l-4 border-primary">.*?</div>)\s*<div class="grid grid-cols-2 gap-4">\s*(<div class="glass-card rounded-2xl p-4[^>]*">.*?<p class="font-label-mono text-on-surface">Zen 4 / 3D</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4[^>]*">.*?<p class="font-label-mono text-on-surface">5\.0 GHz</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4[^>]*">.*?<p class="font-label-mono text-on-surface">8 Cores</p>\s*</div>)\s*(<div class="glass-card rounded-2xl p-4[^>]*">.*?<p class="font-label-mono text-on-surface">120W</p>\s*</div>)\s*</div>', re.DOTALL)
    
    js_replacement = r'''<h4 class="font-label-mono text-[10px] text-primary uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Gaming Performance</h4>
                        \1
                        
                        <h4 class="font-label-mono text-[10px] text-primary uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Architecture & Speeds</h4>
                        <div class="grid grid-cols-2 gap-4">
                            \2
                            \3
                        </div>
                        
                        <h4 class="font-label-mono text-[10px] text-primary uppercase tracking-widest mt-2 border-b border-white/5 pb-2">Cores & Efficiency</h4>
                        <div class="grid grid-cols-2 gap-4">
                            \4
                            \5
                        </div>'''
    
    content = js_pattern.sub(js_replacement, content)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated compare-products.html")
    except Exception as e:
        print(f"Error writing {filepath}: {e}")

if __name__ == "__main__":
    main()
