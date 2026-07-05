import json
import re

# 1. Update builder-data.js
data_file = "c:/Projects/MakeMyPC/js/builder-data.js"
with open(data_file, "r", encoding="utf-8") as f:
    data_content = f.read()

rgb_data = """    rgb: [
        {
            id: 'rgb_corsair_strip',
            brand: 'Corsair',
            model: 'iCUE LS100 Smart Lighting Strip',
            price: 4500,
            image: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'LED Strip',
            length: '450mm',
            features: ['Diffused Lighting', 'Magnetic', 'iCUE Compatible'],
            badge: 'Premium'
        },
        {
            id: 'rgb_deepcool_strip',
            brand: 'DeepCool',
            model: 'RGB200 EX LED Strip',
            price: 1500,
            image: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'LED Strip',
            length: '200mm',
            features: ['Standard RGB', 'Budget Friendly'],
            badge: 'Value'
        }
    ],
"""
if "rgb: [" not in data_content:
    data_content = data_content.replace("    accessories: [", rgb_data + "    accessories: [")
    with open(data_file, "w", encoding="utf-8") as f:
        f.write(data_content)
    print("builder-data.js updated with RGB array.")

# 2. Update builder-app.js
app_file = "c:/Projects/MakeMyPC/js/builder-app.js"
with open(app_file, "r", encoding="utf-8") as f:
    app_content = f.read()

# Update steps array
steps_old = """    { id: 'os', label: 'OS', key: 'os' },
    { id: 'cpu', label: 'CPU', key: 'cpu' },
    { id: 'mobo', label: 'Motherboard', key: 'mobo' },
    { id: 'ram', label: 'RAM', key: 'ram' },
    { id: 'gpu', label: 'GPU', key: 'gpu' },
    { id: 'ssd', label: 'SSD', key: 'ssd' },
    { id: 'hdd', label: 'HDD', key: 'hdd' },
    { id: 'cooler', label: 'Cooler', key: 'cooler' },
    { id: 'psu', label: 'PSU', key: 'psu' },
    { id: 'case', label: 'Cabinet', key: 'case' },
    { id: 'fans', label: 'Fans/RGB', key: 'fans' },
    { id: 'accessories', label: 'Accessories', key: 'accessories' },
    { id: 'review', label: 'Review', key: null }"""

steps_new = """    { id: 'os', label: 'OS', key: 'os' },
    { id: 'cpu', label: 'CPU', key: 'cpu' },
    { id: 'mobo', label: 'Motherboard', key: 'mobo' },
    { id: 'ram', label: 'RAM', key: 'ram' },
    { id: 'ssd', label: 'SSD', key: 'ssd' },
    { id: 'hdd', label: 'HDD', key: 'hdd' },
    { id: 'cooler', label: 'Cooler', key: 'cooler' },
    { id: 'psu', label: 'PSU', key: 'psu' },
    { id: 'case', label: 'Cabinet', key: 'case' },
    { id: 'gpu', label: 'GPU', key: 'gpu' },
    { id: 'fans', label: 'Fans', key: 'fans' },
    { id: 'rgb', label: 'RGB', key: 'rgb' },
    { id: 'accessories', label: 'Accessories', key: 'accessories' },
    { id: 'review', label: 'Review', key: null }"""

if steps_old in app_content:
    app_content = app_content.replace(steps_old, steps_new)

# Add RGB to selections
if "rgb: null" not in app_content:
    app_content = app_content.replace("fans: null,\n        accessories: null", "fans: null,\n        rgb: null,\n        accessories: null")

# Add RGB filter
if "rgb: [\n" not in app_content:
    rgb_filter = """    rgb: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'DeepCool'] },
        { key: 'type', label: 'Type', options: ['LED Strip'] }
    ],"""
    app_content = app_content.replace("fans: [\n", rgb_filter + "\n    fans: [\n")

with open(app_file, "w", encoding="utf-8") as f:
    f.write(app_content)
    
print("builder-app.js updated.")
