import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and ('admin' in f or 'product-' in f or 'orders-' in f)]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def process_details(match):
        details_content = match.group(0)
        
        is_active = False
        if '>inventory_2<' in details_content and file.startswith('product-'):
            is_active = True
        elif '>computer<' in details_content and False:
            is_active = True
        elif '>shopping_cart<' in details_content and file.startswith('orders-'):
            is_active = True
        elif '>group<' in details_content and file in ['admin-customers.html', 'admin-customer-groups.html', 'admin-saved-builds.html']:
            is_active = True
            
        # Fix the details tag
        details_tag = re.match(r'<details[^>]*>', details_content).group(0)
        # remove 'open' attribute
        new_details_tag = re.sub(r'\s*open\b', '', details_tag)
        
        if is_active:
            # add open before the closing bracket
            new_details_tag = new_details_tag.replace('>', ' open>')
            
        # Fix the summary tag classes
        summary_match = re.search(r'<summary[^>]*>', details_content)
        if summary_match:
            summary_tag = summary_match.group(0)
            
            # Remove active classes
            new_summary_tag = summary_tag.replace('text-primary bg-primary/10', 'text-on-surface-variant')
            # Add inactive class if it somehow got lost
            if 'text-on-surface-variant' not in new_summary_tag:
                new_summary_tag = new_summary_tag.replace('text-primary', 'text-on-surface-variant')
                
            # If active, add them back
            if is_active:
                new_summary_tag = new_summary_tag.replace('text-on-surface-variant', 'text-primary bg-primary/10')
            
            # Replace summary in details_content
            details_content = details_content.replace(summary_tag, new_summary_tag, 1)
            
        details_content = details_content.replace(details_tag, new_details_tag, 1)
        return details_content

    # Regex to match details blocks
    new_content = re.sub(r'<details\s*class="group"[^>]*>.*?</details>', process_details, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed sidebar details in {file}")

print("Sidebar details fix complete.")
