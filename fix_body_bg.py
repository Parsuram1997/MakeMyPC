import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<body class="overflow-x-hidden">' in content:
        new_content = content.replace(
            '<body class="overflow-x-hidden">',
            '<body class="bg-surface-deep text-on-surface font-body-md overflow-x-hidden">'
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed body classes in {file}')

print('Done fixing body backgrounds.')
