import re

def update_builder_app():
    filepath = 'c:/Projects/MakeMyPC/js/builder-app.js'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading app file: {e}")
        return

    content = content.replace("{ id: 'storage', label: 'Storage/SSD', key: 'storage' },", 
                              "{ id: 'ssd', label: 'Primary (SSD)', key: 'ssd' },\n    { id: 'hdd', label: 'Secondary (HDD)', key: 'hdd' },")
    content = content.replace("storage: null,", "ssd: null,\n        hdd: null,")

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated builder-app.js")
    except Exception as e:
        print(f"Error writing app file: {e}")

def update_builder_data():
    filepath = 'c:/Projects/MakeMyPC/js/builder-data.js'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading data file: {e}")
        return

    content = content.replace("storage: [", "ssd: [")
    content = content.replace("'storage_", "'ssd_")
    
    # insert hdd array before cooler: [
    hdd_str = """hdd: [
        {
            id: 'hdd_seagate_barracuda_2tb',
            brand: 'Seagate',
            model: 'Barracuda 2TB',
            price: 4500,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'HDD',
            capacity: '2TB',
            speed: '7200 RPM',
            features: ['7200 RPM', 'SATA 6Gb/s', '256MB Cache'],
            badge: 'Value'
        },
        {
            id: 'hdd_wd_black_4tb',
            brand: 'Western Digital',
            model: 'WD Black 4TB',
            price: 12500,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'HDD',
            capacity: '4TB',
            speed: '7200 RPM',
            features: ['7200 RPM', 'Gaming Grade', '128MB Cache'],
            badge: 'Pro'
        }
    ],
    cooler: ["""
    content = content.replace("cooler: [", hdd_str)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated builder-data.js")
    except Exception as e:
        print(f"Error writing data file: {e}")

def update_builder_sidebar():
    filepath = 'c:/Projects/MakeMyPC/js/builder-sidebar.js'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading sidebar file: {e}")
        return

    content = content.replace("storage: 'hard_drive'", "ssd: 'storage', hdd: 'hard_drive'")

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated builder-sidebar.js")
    except Exception as e:
        print(f"Error writing sidebar file: {e}")

if __name__ == "__main__":
    update_builder_app()
    update_builder_data()
    update_builder_sidebar()
