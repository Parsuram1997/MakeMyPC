import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <aside> tag and its closing tag to only replace inside sidebar
    aside_pattern = r'(<aside[^>]*>.*?)</aside>'
    aside_match = re.search(aside_pattern, content, flags=re.DOTALL)
    
    if aside_match:
        aside_content = aside_match.group(1)
        
        # We want to add name="sidebar-menu" to all <details class="group" ...>
        # Check if it's already there
        if 'name="sidebar-menu"' not in aside_content:
            new_aside_content = aside_content.replace('<details class="group"', '<details class="group" name="sidebar-menu"')
            
            content = content.replace(aside_content, new_aside_content)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added accordion effect to {file}")
        else:
            print(f"Accordion already present in {file}")

print("Accordion update complete.")
