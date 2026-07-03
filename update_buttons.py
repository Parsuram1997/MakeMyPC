import glob

for file in glob.glob('*.html'):
    if file in ['builder-landing.html', 'smart-builder.html', 'custom-pc-builder.html']:
        continue # wait, for smart builder and custom pc builder they already have links back and forth inside, but wait, the main "Builder" button should always point to builder-landing.html
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace("window.location.href='custom-pc-builder.html'", "window.location.href='builder-landing.html'")
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
