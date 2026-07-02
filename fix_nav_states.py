import os
import glob
import re

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')

active_class = 'text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-label-mono'
inactive_class = 'text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-label-mono'

# Map filenames to the link text that should be active
active_map = {
    'index.html': None, # Maybe none active on home, or Shop? 
    'prebuilt-pcs.html': 'Shop',
    'product-details.html': 'Shop',
    'custom-pc-builder.html': 'Builder',
    'support-faq.html': 'Resources',
    'submit-ticket.html': 'Resources',
    'ticket-submitted.html': 'Resources',
    'order-tracking.html': 'Resources',
    'calculators-tools.html': 'Resources'
}

def update_nav_states(content, active_item):
    # First, make all links inactive
    content = re.sub(
        r'<a class="[^"]*?" href="prebuilt-pcs.html">Shop</a>',
        f'<a class="{inactive_class}" href="prebuilt-pcs.html">Shop</a>',
        content
    )
    content = re.sub(
        r'<a class="[^"]*?" href="custom-pc-builder.html">Builder</a>',
        f'<a class="{inactive_class}" href="custom-pc-builder.html">Builder</a>',
        content
    )
    content = re.sub(
        r'<a class="[^"]*?" href="support-faq.html">Resources</a>',
        f'<a class="{inactive_class}" href="support-faq.html">Resources</a>',
        content
    )
    
    # Then, make the target link active if there is one
    if active_item == 'Shop':
        content = content.replace(f'<a class="{inactive_class}" href="prebuilt-pcs.html">Shop</a>', f'<a class="{active_class}" href="prebuilt-pcs.html">Shop</a>')
    elif active_item == 'Builder':
        content = content.replace(f'<a class="{inactive_class}" href="custom-pc-builder.html">Builder</a>', f'<a class="{active_class}" href="custom-pc-builder.html">Builder</a>')
    elif active_item == 'Resources':
        content = content.replace(f'<a class="{inactive_class}" href="support-faq.html">Resources</a>', f'<a class="{active_class}" href="support-faq.html">Resources</a>')
        
    return content

for file in html_files:
    basename = os.path.basename(file)
    active_item = active_map.get(basename)
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = update_nav_states(content, active_item)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
