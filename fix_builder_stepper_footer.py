import re

def fix_builder():
    with open('custom-pc-builder.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the stepper (replace the ... with steps 9 to 13)
    stepper_target = """<div class="relative z-10 flex flex-col items-center gap-2 opacity-50">
                    <div class="w-8 h-8 rounded-full bg-transparent text-on-surface-variant text-xs font-semibold">...</div>
                </div>"""
                
    stepper_replacement = """<div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">9</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">GPU</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">10</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Case</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">11</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Fans</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">12</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">RGB</span>
                </div>
                <div class="relative z-10 flex flex-col items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-[#0F172A] border border-white/10 flex items-center justify-center text-on-surface-variant text-xs font-semibold">13</div>
                    <span class="text-[10px] text-on-surface-variant font-medium uppercase tracking-wider">Extras</span>
                </div>"""
    
    if stepper_target in content:
        content = content.replace(stepper_target, stepper_replacement)
    
    # 2. Replace the small footer with the full footer from index.html
    # Get footer from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    m_index_footer = re.search(r'<footer.*?</footer>', index_content, re.DOTALL | re.IGNORECASE)
    if not m_index_footer:
        print("Could not find footer in index.html")
        return
        
    full_footer = m_index_footer.group(0)
    
    # Also we need to make sure the footer matches the dark theme (change bg-surface-deep to bg-[#0B1120])
    full_footer = full_footer.replace('bg-surface-deep', 'bg-[#0B1120]')
    
    # Find footer in custom-pc-builder.html and replace it
    m_builder_footer = re.search(r'<footer.*?</footer>', content, re.DOTALL | re.IGNORECASE)
    if m_builder_footer:
        content = content.replace(m_builder_footer.group(0), full_footer)
        
    with open('custom-pc-builder.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_builder()
print("Fixed stepper and restored footer!")
