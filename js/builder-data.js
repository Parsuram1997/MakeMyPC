// builder-data.js
// Mock Database for MakeMyPC Custom Builder

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
            power: 253, // Max Turbo Power
            integrated_graphics: true,
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
            integrated_graphics: true,
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
            integrated_graphics: true,
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
            ram_support: 'DDR5',
            form_factor: 'ATX',
            m2_slots: 4,
            sata_slots: 4,
            features: ['DDR5 Support', 'PCIe 5.0', 'WiFi 6E'],
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
            ram_support: 'DDR5',
            form_factor: 'ATX',
            m2_slots: 3,
            sata_slots: 6,
            features: ['AM5 Socket', 'DDR5 Support', 'WiFi 6E'],
            badge: 'Recommended'
        }
    ],
    ram: [
        {
            id: 'ram_corsair_ddr5_32',
            brand: 'Corsair',
            model: 'Vengeance RGB 32GB (2x16GB)',
            price: 11500,
            image: 'https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            ram_support: 'DDR5',
            speed: '6000MHz',
            capacity: '32GB',
            features: ['6000MHz CL30', 'DDR5', 'RGB Lighting'],
            badge: 'Sweet Spot'
        },
        {
            id: 'ram_gskill_ddr4_16',
            brand: 'G.Skill',
            model: 'Ripjaws V 16GB (2x8GB)',
            price: 4500,
            image: 'https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            ram_support: 'DDR4',
            speed: '3200MHz',
            capacity: '16GB',
            features: ['3200MHz CL16', 'DDR4', 'Low Profile'],
            badge: ''
        }
    ],
    gpu: [
        {
            id: 'gpu_nvidia_4090',
            brand: 'NVIDIA',
            model: 'GeForce RTX 4090 Founders Edition',
            price: 185000,
            image: 'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=400&q=80',
            stock: 'Low Stock',
            length: 304, // mm
            power: 450,
            recommended_psu: 850,
            features: ['24GB GDDR6X', 'DLSS 3', 'Ray Tracing Ultimate'],
            badge: 'Enthusiast'
        },
        {
            id: 'gpu_nvidia_4070_super',
            brand: 'ASUS',
            model: 'TUF Gaming RTX 4070 SUPER OC',
            price: 62000,
            image: 'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            length: 301, // mm
            power: 220,
            recommended_psu: 650,
            features: ['12GB GDDR6X', 'DLSS 3', 'Great 1440p'],
            badge: 'Best Value'
        },
        {
            id: 'gpu_none',
            brand: '',
            model: 'No Dedicated GPU (Use Integrated)',
            price: 0,
            image: '',
            stock: 'In Stock',
            length: 0,
            power: 0,
            recommended_psu: 0,
            features: ['For office use', 'Requires CPU with iGPU'],
            badge: ''
        }
    ],
    storage: [
        {
            id: 'storage_samsung_990_2tb',
            brand: 'Samsung',
            model: '990 PRO 2TB',
            price: 16500,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'NVMe',
            capacity: '2TB',
            speed: '7450 MB/s',
            features: ['PCIe 4.0 NVMe', 'Read: 7450MB/s', 'Write: 6900MB/s'],
            badge: 'Ultra Fast'
        },
        {
            id: 'storage_wd_blue_1tb',
            brand: 'Western Digital',
            model: 'Blue SN580 1TB',
            price: 5800,
            image: 'https://images.unsplash.com/photo-1597849683907-8b010c7104b2?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'NVMe',
            capacity: '1TB',
            speed: '4150 MB/s',
            features: ['PCIe 4.0 NVMe', 'Read: 4150MB/s', 'Budget Friendly'],
            badge: 'Budget'
        }
    ],
    cooler: [
        {
            id: 'cooler_nzxt_kraken_360',
            brand: 'NZXT',
            model: 'Kraken Elite 360 RGB',
            price: 24000,
            image: 'https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            sockets: ['LGA1700', 'AM5', 'AM4'],
            height: 53, // block height
            radiator: 360, // mm
            power: 15,
            features: ['360mm AIO', 'LCD Display', 'RGB Fans'],
            badge: 'Aesthetics'
        },
        {
            id: 'cooler_thermalright_pa120',
            brand: 'Thermalright',
            model: 'Peerless Assassin 120 SE',
            price: 3500,
            image: 'https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            sockets: ['LGA1700', 'AM5', 'AM4'],
            height: 155, // mm
            radiator: 0,
            power: 5,
            features: ['Dual Tower Air Cooler', '155mm Height', 'Excellent Value'],
            badge: 'Best Air Cooler'
        }
    ],
    psu: [
        {
            id: 'psu_corsair_rm850x',
            brand: 'Corsair',
            model: 'RM850x (2021)',
            price: 12500,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            wattage: 850,
            efficiency: '80+ Gold',
            features: ['850W', '80+ Gold', 'Fully Modular'],
            badge: 'Popular'
        },
        {
            id: 'psu_seasonic_focus_1000',
            brand: 'Seasonic',
            model: 'FOCUS GX-1000',
            price: 16000,
            image: 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            wattage: 1000,
            efficiency: '80+ Gold',
            features: ['1000W', '80+ Gold', 'ATX 3.0 Ready'],
            badge: 'High End'
        }
    ],
    case: [
        {
            id: 'case_lianli_o11_dynamic',
            brand: 'Lian Li',
            model: 'O11 Dynamic EVO',
            price: 14000,
            image: 'https://images.unsplash.com/photo-1547941126-3d5322b218b0?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            max_gpu_length: 422, // mm
            max_cooler_height: 167, // mm
            form_factors: ['ATX', 'mATX', 'ITX', 'E-ATX'],
            features: ['Dual Chamber', 'Tempered Glass', 'Great Airflow'],
            badge: 'Showcase'
        },
        {
            id: 'case_corsair_4000d',
            brand: 'Corsair',
            model: '4000D Airflow',
            price: 7500,
            image: 'https://images.unsplash.com/photo-1547941126-3d5322b218b0?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            max_gpu_length: 360,
            max_cooler_height: 170,
            form_factors: ['ATX', 'mATX', 'ITX'],
            features: ['High Airflow Front Panel', 'Included Fans', 'Cable Management'],
            badge: 'Airflow King'
        }
    ],
    fans: [
        {
            id: 'fans_lianli_sl120_3pack',
            brand: 'Lian Li',
            model: 'UNI FAN SL-INF 120 (3-Pack)',
            price: 8500,
            image: 'https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: '120mm',
            features: ['Infinity Mirror RGB', 'Daisy-chain', 'Controller Included'],
            badge: 'Premium RGB'
        },
        {
            id: 'fans_none',
            brand: '',
            model: 'No Additional Fans',
            price: 0,
            image: '',
            stock: 'In Stock',
            type: '',
            features: ['Use stock case fans'],
            badge: ''
        }
    ],
    accessories: [
        {
            id: 'acc_windows_11',
            brand: 'Microsoft',
            model: 'Windows 11 Home',
            price: 10500,
            image: 'https://images.unsplash.com/photo-1633419461186-7d40a38105ec?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'OS',
            features: ['64-bit', 'USB Flash Drive'],
            badge: ''
        },
        {
            id: 'acc_wifi_card',
            brand: 'TP-Link',
            model: 'Archer TX3000E WiFi 6',
            price: 3500,
            image: 'https://images.unsplash.com/photo-1544144433-d50aff500b91?auto=format&fit=crop&w=400&q=80',
            stock: 'In Stock',
            type: 'Network',
            features: ['WiFi 6', 'Bluetooth 5.0', 'PCIe'],
            badge: ''
        },
        {
            id: 'acc_none',
            brand: '',
            model: 'No Accessories Needed',
            price: 0,
            image: '',
            stock: 'In Stock',
            type: '',
            features: ['Just the PC'],
            badge: ''
        }
    ]
};
