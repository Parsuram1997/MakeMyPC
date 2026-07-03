db_content = """// builder-data.js
// Enterprise Mock Database for MakeMyPC Custom Builder

const db = {
    cpu: [
        {
            id: 'cpu_intel_i9_14900k',
            brand: 'Intel',
            model: 'Core i9-14900K',
            price: 52000,
            image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC6gB37IcBzIowOffL84lrfBf7ZSC3ceQH6HPwbjiobQFsrgVey7uDpJoFhljunliPLEAlYVp8N-NJkqijAKD-ZPGwmIDjXg0W9gIL2GLfRV31aS0eA4be2CI8_UaK7SRTN83BLq8KBjwZbEfmBxLSsBWB5o_d8U4aUHezDTBZej6yN1Kuv5G61sLuBXAbpqFwqoTNm_iOlxV4CAMJlDCxtuptb6z2eGRFJwEzTPLlYXcnPjwSK3sWX2lOZ97BlHNv6psMX2UOx0T7k',
            stock: 'In Stock',
            socket: 'LGA1700',
            ram_support: ['DDR4', 'DDR5'],
            power: 253,
            integrated_graphics: 'Yes',
            unlocked: 'Yes',
            core_count: '24',
            thread_count: '32',
            base_clock: '3.2 GHz',
            boost_clock: '6.0 GHz',
            features: ['24 Cores (8P+16E)', '6.0 GHz Max Turbo', 'LGA1700 Socket'],
            badge: 'Top Choice'
        },
        {
            id: 'cpu_amd_r9_7950x3d',
            brand: 'AMD',
            model: 'Ryzen 9 7950X3D',
            price: 58000,
            image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC75KlJmDw5UCh-7xIzTAo4yij42i-6fyOBEu--LvjssEFJkQaNvtR2_zHaDXDd_MrveHUfKqjqDAd32Tq0cYofDWcZP9Ch2b_Qv1jlR7wTG31IZC-0NWMwVKn4scX_T6-hxvZl2vF8yZ1CaTyZs-Y91ldA_9T3ncjZNE8IT6f3648KM1_tBZVe5BCekbfA-4zWqoK-uF_INCqmJ4dhyF521VEldhEYorqzo1MZNI_kRVLGcpVmGrXiyp5ESo-s1p_5LYypuysK5gPd',
            stock: 'Low Stock',
            socket: 'AM5',
            ram_support: ['DDR5'],
            power: 120,
            integrated_graphics: 'Yes',
            unlocked: 'Yes',
            core_count: '16',
            thread_count: '32',
            base_clock: '4.2 GHz',
            boost_clock: '5.7 GHz',
            features: ['16 Cores / 32 Threads', '3D V-Cache', 'AM5 Socket'],
            badge: 'Best for Gaming'
        },
        {
            id: 'cpu_amd_r5_7600x',
            brand: 'AMD',
            model: 'Ryzen 5 7600X',
            price: 21000,
            image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC75KlJmDw5UCh-7xIzTAo4yij42i-6fyOBEu--LvjssEFJkQaNvtR2_zHaDXDd_MrveHUfKqjqDAd32Tq0cYofDWcZP9Ch2b_Qv1jlR7wTG31IZC-0NWMwVKn4scX_T6-hxvZl2vF8yZ1CaTyZs-Y91ldA_9T3ncjZNE8IT6f3648KM1_tBZVe5BCekbfA-4zWqoK-uF_INCqmJ4dhyF521VEldhEYorqzo1MZNI_kRVLGcpVmGrXiyp5ESo-s1p_5LYypuysK5gPd',
            stock: 'In Stock',
            socket: 'AM5',
            ram_support: ['DDR5'],
            power: 105,
            integrated_graphics: 'Yes',
            unlocked: 'Yes',
            core_count: '6',
            thread_count: '12',
            base_clock: '4.7 GHz',
            boost_clock: '5.3 GHz',
            features: ['6 Cores / 12 Threads', '5.3 GHz Max Boost', 'AM5 Socket'],
            badge: 'Value King'
        }
    ],
    mobo: [
        {
            id: 'mobo_asus_z790',
            brand: 'ASUS',
            model: 'ROG Strix Z790-E Gaming WiFi',
            price: 42000,
            image: 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            socket: 'LGA1700',
            chipset: 'Z790',
            ram_support: 'DDR5',
            form_factor: 'ATX',
            ram_slots: '4',
            m2_slots: 4,
            wifi: 'Yes',
            bluetooth: 'Yes',
            pcie_version: 'PCIe 5.0',
            features: ['Z790 Chipset', 'DDR5 Support', 'PCIe 5.0'],
            badge: 'Premium'
        },
        {
            id: 'mobo_msi_b650',
            brand: 'MSI',
            model: 'MAG B650 TOMAHAWK WIFI',
            price: 22000,
            image: 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            socket: 'AM5',
            chipset: 'B650',
            ram_support: 'DDR5',
            form_factor: 'ATX',
            ram_slots: '4',
            m2_slots: 3,
            wifi: 'Yes',
            bluetooth: 'Yes',
            pcie_version: 'PCIe 4.0',
            features: ['B650 Chipset', 'Robust VRM', 'Wi-Fi 6E'],
            badge: ''
        }
    ],
    ram: [
        {
            id: 'ram_corsair_vengeance_32gb_ddr5',
            brand: 'Corsair',
            model: 'Vengeance RGB 32GB',
            price: 10500,
            image: 'https://images.unsplash.com/photo-1541029071515-84cc54f84dc5?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'DDR5',
            capacity: '32GB',
            speed: '6000MHz',
            latency: 'CL30',
            rgb: 'Yes',
            features: ['2x16GB Kit', '6000MHz CL30', 'RGB Ready'],
            badge: 'Sweet Spot'
        },
        {
            id: 'ram_gskill_trident_64gb_ddr5',
            brand: 'G.Skill',
            model: 'Trident Z5 Neo RGB 64GB',
            price: 22000,
            image: 'https://images.unsplash.com/photo-1541029071515-84cc54f84dc5?auto=format&fit=crop&w=400&q=80',
            stock: 'Low Stock',
            type: 'DDR5',
            capacity: '64GB',
            speed: '6000MHz',
            latency: 'CL30',
            rgb: 'Yes',
            features: ['2x32GB Kit', 'EXPO Tuned', 'High Capacity'],
            badge: ''
        }
    ],
    gpu: [
        {
            id: 'gpu_nvidia_rtx_4090',
            brand: 'NVIDIA',
            model: 'GeForce RTX 4090 24GB',
            price: 185000,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            vram: '24GB',
            memory_type: 'GDDR6X',
            ray_tracing: 'Yes',
            dlss: 'Yes',
            fsr: 'No',
            power_consumption: '450W',
            recommended_psu: '1000W',
            features: ['24GB GDDR6X', 'DLSS 3.0', 'Ada Lovelace'],
            badge: 'Ultimate'
        },
        {
            id: 'gpu_amd_rx_7900xtx',
            brand: 'AMD',
            model: 'Radeon RX 7900 XTX 24GB',
            price: 95000,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            vram: '24GB',
            memory_type: 'GDDR6',
            ray_tracing: 'Yes',
            dlss: 'No',
            fsr: 'Yes',
            power_consumption: '355W',
            recommended_psu: '850W',
            features: ['24GB GDDR6', 'RDNA 3', 'FSR 3.0'],
            badge: 'Value Flagship'
        }
    ],
    ssd: [
        {
            id: 'ssd_samsung_990_2tb',
            brand: 'Samsung',
            model: '990 PRO 2TB',
            price: 16500,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            interface: 'NVMe',
            capacity: '2TB',
            pcie_gen: 'Gen4',
            read_speed: '7450 MB/s',
            dram_cache: 'Yes',
            features: ['PCIe 4.0 NVMe', 'Read: 7450MB/s', 'Write: 6900MB/s'],
            badge: 'Ultra Fast'
        },
        {
            id: 'ssd_wd_blue_1tb',
            brand: 'Western Digital',
            model: 'Blue SN580 1TB',
            price: 5800,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            interface: 'NVMe',
            capacity: '1TB',
            pcie_gen: 'Gen4',
            read_speed: '4150 MB/s',
            dram_cache: 'No',
            features: ['PCIe 4.0 NVMe', 'Read: 4150MB/s', 'Budget Friendly'],
            badge: 'Budget'
        }
    ],
    hdd: [
        {
            id: 'hdd_seagate_barracuda_2tb',
            brand: 'Seagate',
            model: 'Barracuda 2TB',
            price: 4500,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            interface: 'SATA',
            capacity: '2TB',
            rpm: '7200',
            cache: '256MB',
            nas_support: 'No',
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
            interface: 'SATA',
            capacity: '4TB',
            rpm: '7200',
            cache: '128MB',
            nas_support: 'Yes',
            features: ['7200 RPM', 'Gaming Grade', '128MB Cache'],
            badge: 'Pro'
        }
    ],
    cooler: [
        {
            id: 'cooler_nzxt_kraken_360',
            brand: 'NZXT',
            model: 'Kraken Elite 360 RGB',
            price: 24000,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'Liquid Cooler',
            radiator_size: '360mm',
            rgb: 'Yes',
            noise_level: '27 dBA',
            features: ['360mm AIO', 'LCD Display', 'F120 RGB Fans'],
            badge: 'Aesthetics'
        },
        {
            id: 'cooler_noctua_d15',
            brand: 'Noctua',
            model: 'NH-D15 chromax.black',
            price: 10500,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'Air Cooler',
            height: '165mm',
            rgb: 'No',
            noise_level: '24 dBA',
            features: ['Dual Tower', '140mm Fans', 'Ultra Quiet'],
            badge: 'Silence'
        }
    ],
    psu: [
        {
            id: 'psu_corsair_rm1000x',
            brand: 'Corsair',
            model: 'RM1000x Shift',
            price: 18000,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            wattage: '1000W',
            efficiency: 'Gold',
            modular: 'Fully Modular',
            pcie5: 'Yes',
            features: ['1000W 80+ Gold', 'ATX 3.0', 'Side Cables'],
            badge: 'Top Tier'
        }
    ],
    case: [
        {
            id: 'case_lianli_o11',
            brand: 'Lian Li',
            model: 'O11 Dynamic EVO',
            price: 14500,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            form_factor: 'ATX',
            front_panel: 'USB Type-C',
            rgb: 'Yes',
            tempered_glass: 'Yes',
            color: 'Black',
            features: ['Dual Chamber', 'Reversible', 'Type-C'],
            badge: 'Popular'
        }
    ],
    fans: [
        {
            id: 'fan_lianli_uni_sl120',
            brand: 'Lian Li',
            model: 'UNI FAN SL120 V2 (3-Pack)',
            price: 8500,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            size: '120mm',
            rgb: 'ARGB',
            pwm: 'Yes',
            pack_size: '3',
            features: ['Daisy Chain', 'ARGB', 'L-Connect 3'],
            badge: 'Best RGB'
        }
    ],
    accessories: []
};
"""

with open('c:/Projects/MakeMyPC/js/builder-data.js', 'w', encoding='utf-8') as f:
    f.write(db_content)
print("Database updated.")
