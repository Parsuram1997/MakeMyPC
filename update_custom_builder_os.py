import re
import json

# 1. Update builder-data.js
data_file = "c:/Projects/MakeMyPC/js/builder-data.js"
with open(data_file, "r", encoding="utf-8") as f:
    data_content = f.read()

os_data = """    os: [
        {
            id: 'os_windows_11_home',
            brand: 'Microsoft',
            model: 'Windows 11 Home',
            price: 9500,
            image: 'https://images.unsplash.com/photo-1633419461186-7d40a38105ec?auto=format&fit=crop&w=400&q=80',
            stock: 'Digital License',
            type: 'Operating System',
            features: ['DirectX 12 Ultimate', 'Auto HDR', 'Seamless Gaming'],
            badge: 'Standard'
        },
        {
            id: 'os_windows_11_pro',
            brand: 'Microsoft',
            model: 'Windows 11 Pro',
            price: 14500,
            image: 'https://images.unsplash.com/photo-1633419461186-7d40a38105ec?auto=format&fit=crop&w=400&q=80',
            stock: 'Digital License',
            type: 'Operating System',
            features: ['BitLocker', 'Remote Desktop', 'Hyper-V'],
            badge: 'Professional'
        },
        {
            id: 'os_ubuntu_linux',
            brand: 'Canonical',
            model: 'Ubuntu 24.04 LTS',
            price: 0,
            image: 'https://images.unsplash.com/photo-1629654297299-c8506221ca97?auto=format&fit=crop&w=400&q=80',
            stock: 'Pre-installed',
            type: 'Operating System',
            features: ['Open Source', 'Developer Friendly', 'Free'],
            badge: 'Free'
        },
        {
            id: 'os_none',
            brand: 'Custom',
            model: 'No Operating System',
            price: 0,
            image: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80',
            stock: 'N/A',
            type: 'Operating System',
            features: ['Install your own OS', 'Blank Drive'],
            badge: ''
        }
    ]"""

if "os: [" not in data_content:
    # Find the last closing brace of the db object
    # It ends with 'accessories: [\n...\n    ]\n};'
    data_content = data_content.replace('    ]\n};\n', '    ],\n' + os_data + '\n};\n')
    with open(data_file, "w", encoding="utf-8") as f:
        f.write(data_content)
    print("builder-data.js updated!")
else:
    print("builder-data.js already has OS data")

# 2. Update builder-app.js
app_file = "c:/Projects/MakeMyPC/js/builder-app.js"
with open(app_file, "r", encoding="utf-8") as f:
    app_content = f.read()

# Add to steps array
if "{ id: 'os', label: 'OS'" not in app_content:
    app_content = app_content.replace(
        "{ id: 'review', label: 'Review', key: null }",
        "{ id: 'os', label: 'OS', key: 'os' },\n    { id: 'review', label: 'Review', key: null }"
    )

# Add to state.selections
if "os: null" not in app_content:
    app_content = app_content.replace(
        "accessories: null\n    }",
        "accessories: null,\n        os: null\n    }"
    )

# Add to requiredParts in review step logic
if "'psu', 'case', 'os']" not in app_content:
    app_content = app_content.replace(
        "['cpu', 'mobo', 'ram', 'ssd', 'psu', 'case']",
        "['cpu', 'mobo', 'ram', 'ssd', 'psu', 'case', 'os']"
    )

# Add to filterDefinitions
if "os: [\n" not in app_content:
    os_filter = """    os: [
        { key: 'brand', label: 'Brand', options: ['Microsoft', 'Canonical', 'Custom'] }
    ],"""
    app_content = app_content.replace(
        "fans: [",
        os_filter + "\n    fans: ["
    )

with open(app_file, "w", encoding="utf-8") as f:
    f.write(app_content)
print("builder-app.js updated!")
