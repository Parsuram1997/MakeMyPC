import os
import glob
import re

def update_headers():
    project_dir = 'c:/Projects/MakeMyPC'
    
    # Extract the nav block from custom-pc-builder.html
    with open(os.path.join(project_dir, 'custom-pc-builder.html'), 'r', encoding='utf-8') as f:
        custom_content = f.read()
        
    m_nav = re.search(r'<nav.*?</nav>', custom_content, re.DOTALL | re.IGNORECASE)
    if not m_nav:
        print("Could not find nav in custom-pc-builder.html")
        return
        
    new_nav = m_nav.group(0)
    
    # 1. Convert the hexagon CSS to inline styling
    hexagon_div = '<div class="hexagon">'
    hexagon_inline = '<div style="width: 28px; height: 32px; background-color: #2563EB; position: relative; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); display: flex; align-items: center; justify-content: center;">'
    new_nav = new_nav.replace(hexagon_div, hexagon_inline)
    
    # 2. Remove the hardcoded active state on 'Builder'
    active_class_str = 'text-primary font-medium border-b-2 border-primary pb-1'
    inactive_class_str = 'text-on-surface-variant hover:text-white transition-colors'
    new_nav = new_nav.replace(active_class_str, inactive_class_str)
    
    # Add a marker so we know it's the new nav
    new_nav = f"<!-- ═══ NEW PREMIUM NAVBAR START ═══ -->\n{new_nav}\n<!-- ═══ NEW PREMIUM NAVBAR END ═══ -->"
    
    # Process all html files
    html_files = glob.glob(os.path.join(project_dir, '*.html'))
    
    skip_files = ['login.html', 'signup.html', 'custom-pc-builder.html']
    
    updated_count = 0
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        
        # Skip admin pages and specific files
        if filename.startswith('admin') or filename in skip_files:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to find existing nav
        m_existing_nav = re.search(r'<nav.*?</nav>', content, re.DOTALL | re.IGNORECASE)
        if m_existing_nav:
            # Replace old nav with new nav
            content = content.replace(m_existing_nav.group(0), new_nav)
            
            # Optionally, let's try to remove the old mobile menu block if it exists
            # The old mobile menu usually has id="mobile-menu"
            # Since we can't easily parse matching divs with regex, we'll just leave it. 
            # It starts with display:none so it shouldn't cause visual issues.
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated {filename}")
            
    print(f"Successfully updated {updated_count} files!")

update_headers()
