import glob
import re

nav_replacement = """<a class="text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-xs" href="prebuilt-pcs.html">Shop</a>
<a class="text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-xs" href="builder-landing.html">Builder</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-xs" href="#">Resources</a>"""

for file in glob.glob('*.html'):
    if file == 'builder-landing.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find the <div class="hidden md:flex gap-x-8 items-center"> and replace its contents up to </div>
    pattern = r'(<div class="hidden md:flex gap-x-8 items-center">)(.*?)(</div>\s*<div class="flex items-center gap-x-6">)'
    
    def repl(m):
        return m.group(1) + '\n' + nav_replacement + '\n' + m.group(3)
        
    new_content = re.sub(pattern, repl, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
