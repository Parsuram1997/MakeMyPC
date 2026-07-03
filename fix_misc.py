import re
for file in ['builder-landing.html', 'smart-builder.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Update Logo Class
    c = c.replace('class="text-3xl font-black', 'class="text-headline-lg font-headline-lg font-black')
    
    # Add global.js if not present
    if 'global.js' not in c:
        c = c.replace('</body>', '<script src="js/global.js"></script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated {file}')
