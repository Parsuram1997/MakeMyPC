import re
with open(r'c:\Projects\MakeMyPC\builder-landing.html', 'r', encoding='utf-8') as f:
    c = f.read()
    m = re.search(r'<div class="flex gap-x-4">.*?</nav>', c, re.DOTALL)
    if m:
        print(m.group(0))
