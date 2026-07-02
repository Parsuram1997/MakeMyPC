import os
import glob
import re

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')
logo_html = '<a href="index.html" class="text-headline-lg font-headline-lg font-black text-on-surface tracking-tighter">MakeMyPC</a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav block
    start_nav = content.find('<nav')
    if start_nav != -1:
        end_nav = content.find('</nav>', start_nav)
        nav_content = content[start_nav:end_nav]
        
        # Replace the MakeMyPC logo link in the nav section regardless of its current class or tag
        # It could be <div class="...">MakeMyPC</div> or <a class="...">MakeMyPC</a>
        
        # We will use regex to find anything that looks like <tag ...>MakeMyPC</tag> inside the nav
        # But we only want to replace the first occurrence (which should be the logo)
        
        new_nav_content = re.sub(r'<([a-z]+)[^>]*>\s*MakeMyPC\s*</\1>', logo_html, nav_content, count=1)
        
        content = content[:start_nav] + new_nav_content + content[end_nav:]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated logos")
