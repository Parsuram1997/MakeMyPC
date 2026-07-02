import os
import glob
import re

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')

# Extract full tailwind script from index.html
with open('c:/Projects/MakeMyPC/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# We look for <script> tailwind.config = ... </script>
start = index_content.find('<script id="tailwind-config">')
if start == -1:
    start = index_content.find('<script>\n        tailwind.config =')
if start == -1:
    start = index_content.find('<script>tailwind.config')
if start == -1:
    start = index_content.find('<script>\ntailwind.config')

end = index_content.find('</script>', start) + 9
tailwind_script = index_content[start:end]

for file in html_files:
    if file.endswith('index.html'):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace existing tailwind script if it exists
    start_cur = content.find('tailwind.config =')
    if start_cur != -1:
        # Find the <script> before it and </script> after it
        script_start = content.rfind('<script', 0, start_cur)
        script_end = content.find('</script>', start_cur) + 9
        content = content[:script_start] + tailwind_script + content[script_end:]
    else:
        # If no tailwind config exists, inject it before </head>
        content = content.replace('</head>', '\n' + tailwind_script + '\n</head>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Synchronized Tailwind Config!")
