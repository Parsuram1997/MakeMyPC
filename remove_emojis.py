import glob

def remove_emojis():
    html_files = glob.glob('*.html')
    
    replacements = {
        'Saved Builds ⭐': 'Saved Builds',
        'Wishlist ❤️': 'Wishlist',
        'Order History 📦': 'Order History',
        'Support Tickets 🎫': 'Support Tickets',
        'Loyalty & Rewards 🎁': 'Loyalty & Rewards',
        'Activity Logs 📊': 'Activity Logs',
        'Email & Notifications ✉️': 'Email & Notifications',
        'Blocked Customers 🚫': 'Blocked Customers'
    }
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new)
                changed = True
                
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Removed emojis from {filepath}")

if __name__ == '__main__':
    remove_emojis()
