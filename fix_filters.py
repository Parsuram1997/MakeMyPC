import re

def main():
    filepath = 'c:/Projects/MakeMyPC/js/builder-app.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_defs = """const filterDefinitions = {
    cpu: [
        { key: 'brand', label: 'Brand', options: ['Intel', 'AMD'] },
        { key: 'socket', label: 'Socket', options: ['LGA1700', 'AM4', 'AM5'] },
        { key: 'core_count', label: 'Cores', options: ['6', '8', '12', '16', '24'] }
    ],
    mobo: [
        { key: 'brand', label: 'Brand', options: ['ASUS', 'MSI', 'Gigabyte', 'ASRock'] },
        { key: 'socket', label: 'Socket', options: ['LGA1700', 'AM4', 'AM5'] },
        { key: 'form_factor', label: 'Size', options: ['ATX', 'Micro ATX', 'Mini ITX'] }
    ],
    ram: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'G.Skill', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['16GB', '32GB', '64GB'] },
        { key: 'type', label: 'Type', options: ['DDR4', 'DDR5'] }
    ],
    gpu: [
        { key: 'brand', label: 'Brand', options: ['NVIDIA', 'AMD', 'Intel'] },
        { key: 'vram', label: 'VRAM', options: ['8GB', '12GB', '16GB', '24GB'] },
        { key: 'memory_type', label: 'Mem Type', options: ['GDDR6', 'GDDR6X'] }
    ],
    ssd: [
        { key: 'brand', label: 'Brand', options: ['Samsung', 'Western Digital', 'Crucial'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB'] },
        { key: 'pcie_gen', label: 'Generation', options: ['Gen3', 'Gen4', 'Gen5'] }
    ],
    hdd: [
        { key: 'brand', label: 'Brand', options: ['Seagate', 'Western Digital'] },
        { key: 'capacity', label: 'Capacity', options: ['1TB', '2TB', '4TB', '8TB'] },
        { key: 'rpm', label: 'Speed', options: ['5400', '7200'] }
    ],
    cooler: [
        { key: 'brand', label: 'Brand', options: ['NZXT', 'Corsair', 'Noctua', 'Deepcool'] },
        { key: 'type', label: 'Type', options: ['Air Cooler', 'Liquid Cooler'] },
        { key: 'radiator_size', label: 'Rad Size', options: ['120mm', '240mm', '360mm'] }
    ],
    psu: [
        { key: 'brand', label: 'Brand', options: ['Corsair', 'EVGA', 'Seasonic'] },
        { key: 'wattage', label: 'Wattage', options: ['650W', '750W', '850W', '1000W'] },
        { key: 'efficiency', label: 'Rating', options: ['Bronze', 'Gold', 'Platinum'] }
    ],
    case: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'NZXT', 'Corsair'] },
        { key: 'form_factor', label: 'Size', options: ['ATX', 'Micro ATX', 'Mini ITX'] },
        { key: 'color', label: 'Color', options: ['Black', 'White'] }
    ],
    fans: [
        { key: 'brand', label: 'Brand', options: ['Lian Li', 'Corsair', 'Noctua'] },
        { key: 'size', label: 'Size', options: ['120mm', '140mm'] },
        { key: 'rgb', label: 'RGB', options: ['Yes', 'No', 'ARGB'] }
    ]
};"""

    # Replace the filterDefinitions block
    pattern = re.compile(r'const filterDefinitions = \{.*?\};', re.DOTALL)
    content = pattern.sub(new_defs, content)

    # Make the filter buttons consistent in width
    button_html_old = """<button class="bg-surface-container-low border border-white/10 rounded-lg px-3 py-1.5 text-xs flex items-center gap-2 hover:bg-white/5 transition-all">"""
    button_html_new = """<button class="bg-surface-container-low border border-white/10 rounded-lg px-3 py-1.5 text-xs flex items-center justify-between w-28 hover:bg-white/5 transition-all">"""
    content = content.replace(button_html_old, button_html_new)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

if __name__ == '__main__':
    main()
