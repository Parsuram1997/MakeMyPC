import os
import re
import shutil

# Copy the base file
shutil.copy('orders-management.html', 'admin-order-tracking.html')

with open('admin-order-tracking.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure the Active Link in Sidebar points to Order Tracking instead of All Orders
content = content.replace(
    '<a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block bg-white/10 text-white font-semibold">',
    '<a href="orders-management.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">'
)
content = content.replace(
    '<a href="admin-order-tracking.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block">',
    '<a href="admin-order-tracking.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-1 rounded-lg transition-colors block bg-white/10 text-white font-semibold">'
)

main_content = """<main class="flex-1 lg:ml-64 px-6 py-8 md:px-8 bg-surface-dim relative text-on-surface">

    <div class="w-full space-y-6">
        
        <!-- Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mt-2">
            <div>
                <h1 class="text-2xl font-bold text-white mb-1">Order Tracking</h1>
                <p class="text-sm text-on-surface-variant">Track and manage the real-time status of customer orders.</p>
            </div>
            <div class="flex items-center gap-3">
                <button class="flex items-center gap-2 bg-surface-container border border-white/5 hover:bg-white/5 text-sm text-white px-4 py-2 rounded-lg transition-colors font-medium">
                    <span class="material-symbols-outlined text-[18px]">download</span> Export Tracking Data
                </button>
            </div>
        </div>

        <!-- Metric Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            <div class="bg-surface-container border border-white/5 rounded-xl p-4 flex flex-col gap-2">
                <div class="flex items-center gap-3 mb-1">
                    <div class="w-8 h-8 rounded-full bg-[#1A73E8]/20 text-[#1A73E8] flex items-center justify-center">
                        <span class="material-symbols-outlined text-[18px]">shopping_cart</span>
                    </div>
                    <span class="text-sm text-on-surface-variant">Total Orders</span>
                </div>
                <div class="text-2xl font-bold text-white">1,254</div>
                <div class="text-[11px] text-[#00D084] font-medium flex items-center gap-1">
                    <span class="material-symbols-outlined text-[12px]">arrow_upward</span> 12.6% vs last month
                </div>
            </div>

            <div class="bg-surface-container border border-white/5 rounded-xl p-4 flex flex-col gap-2">
                <div class="flex items-center gap-3 mb-1">
                    <div class="w-8 h-8 rounded-full bg-[#34A853]/20 text-[#34A853] flex items-center justify-center">
                        <span class="material-symbols-outlined text-[18px]">local_shipping</span>
                    </div>
                    <span class="text-sm text-on-surface-variant">In Transit</span>
                </div>
                <div class="text-2xl font-bold text-white">642</div>
                <div class="text-[11px] text-[#00D084] font-medium flex items-center gap-1">
                    <span class="material-symbols-outlined text-[12px]">arrow_upward</span> 14.2% vs last month
                </div>
            </div>

            <div class="bg-surface-container border border-white/5 rounded-xl p-4 flex flex-col gap-2">
                <div class="flex items-center gap-3 mb-1">
                    <div class="w-8 h-8 rounded-full bg-[#9333EA]/20 text-[#9333EA] flex items-center justify-center">
                        <span class="material-symbols-outlined text-[18px]">inventory_2</span>
                    </div>
                    <span class="text-sm text-on-surface-variant">Out for Delivery</span>
                </div>
                <div class="text-2xl font-bold text-white">218</div>
                <div class="text-[11px] text-[#00D084] font-medium flex items-center gap-1">
                    <span class="material-symbols-outlined text-[12px]">arrow_upward</span> 8.4% vs last month
                </div>
            </div>

            <div class="bg-surface-container border border-white/5 rounded-xl p-4 flex flex-col gap-2">
                <div class="flex items-center gap-3 mb-1">
                    <div class="w-8 h-8 rounded-full bg-[#00D084]/20 text-[#00D084] flex items-center justify-center">
                        <span class="material-symbols-outlined text-[18px]">check_circle</span>
                    </div>
                    <span class="text-sm text-on-surface-variant">Delivered</span>
                </div>
                <div class="text-2xl font-bold text-white">1,024</div>
                <div class="text-[11px] text-[#00D084] font-medium flex items-center gap-1">
                    <span class="material-symbols-outlined text-[12px]">arrow_upward</span> 16.8% vs last month
                </div>
            </div>

            <div class="bg-surface-container border border-white/5 rounded-xl p-4 flex flex-col gap-2">
                <div class="flex items-center gap-3 mb-1">
                    <div class="w-8 h-8 rounded-full bg-[#F87171]/20 text-[#F87171] flex items-center justify-center">
                        <span class="material-symbols-outlined text-[18px]">cancel</span>
                    </div>
                    <span class="text-sm text-on-surface-variant">Exception</span>
                </div>
                <div class="text-2xl font-bold text-white">87</div>
                <div class="text-[11px] text-[#F87171] font-medium flex items-center gap-1">
                    <span class="material-symbols-outlined text-[12px]">arrow_downward</span> 5.2% vs last month
                </div>
            </div>
        </div>

        <!-- Filters Row -->
        <div class="flex flex-wrap items-center gap-3 mt-4">
            <div class="relative flex-1 min-w-[240px]">
                <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                <input type="text" placeholder="Search by Order ID, AWB, Customer, Phone..." class="w-full bg-surface-container border border-white/5 rounded-lg py-2 pl-9 pr-4 text-sm text-white placeholder-on-surface-variant/70 focus:outline-none focus:border-primary/50">
            </div>
            <select class="bg-surface-container border border-white/5 rounded-lg py-2 px-3 text-sm text-white focus:outline-none focus:border-primary/50 appearance-none pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%24%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2010l5%205%205-5%22%20stroke%3D%22%23c1c6d7%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%3C%2Fsvg%3E')] bg-[position:right_0.5rem_center] bg-no-repeat bg-[length:16px]">
                <option>All Status</option>
            </select>
            <select class="bg-surface-container border border-white/5 rounded-lg py-2 px-3 text-sm text-white focus:outline-none focus:border-primary/50 appearance-none pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%24%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2010l5%205%205-5%22%20stroke%3D%22%23c1c6d7%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%3C%2Fsvg%3E')] bg-[position:right_0.5rem_center] bg-no-repeat bg-[length:16px]">
                <option>All Carriers</option>
            </select>
            <select class="bg-surface-container border border-white/5 rounded-lg py-2 px-3 text-sm text-white focus:outline-none focus:border-primary/50 appearance-none pr-8 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%24%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2010l5%205%205-5%22%20stroke%3D%22%23c1c6d7%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%3C%2Fsvg%3E')] bg-[position:right_0.5rem_center] bg-no-repeat bg-[length:16px]">
                <option>All Warehouses</option>
            </select>
            <button class="flex items-center gap-2 bg-transparent border border-white/10 hover:bg-white/5 text-sm text-white px-3 py-2 rounded-lg transition-colors">
                <span class="material-symbols-outlined text-[18px]">filter_alt</span> Filters
            </button>
            <a href="#" class="text-sm text-[#1A73E8] hover:underline font-medium">Reset</a>
        </div>

        <!-- Main Content Area -->
        <div class="grid grid-cols-1 xl:grid-cols-[1fr_320px] gap-6">
            
            <!-- Left Side: Table & Overview Chart -->
            <div class="space-y-6">
                
                <!-- Table Card -->
                <div class="bg-surface-container border border-white/5 rounded-xl flex flex-col overflow-hidden">
                    
                    <!-- Tabs -->
                    <div class="flex border-b border-white/5 overflow-x-auto custom-scrollbar">
                        <button class="px-5 py-3 text-sm font-semibold text-[#1A73E8] border-b-2 border-[#1A73E8] whitespace-nowrap">All (1,254)</button>
                        <button class="px-5 py-3 text-sm font-medium text-on-surface-variant hover:text-white transition-colors whitespace-nowrap">In Transit (642)</button>
                        <button class="px-5 py-3 text-sm font-medium text-on-surface-variant hover:text-white transition-colors whitespace-nowrap">Out for Delivery (218)</button>
                        <button class="px-5 py-3 text-sm font-medium text-on-surface-variant hover:text-white transition-colors whitespace-nowrap">Delivered (1,024)</button>
                        <button class="px-5 py-3 text-sm font-medium text-on-surface-variant hover:text-white transition-colors whitespace-nowrap">Exception (87)</button>
                        <button class="px-5 py-3 text-sm font-medium text-on-surface-variant hover:text-white transition-colors whitespace-nowrap">Cancelled (43)</button>
                    </div>

                    <!-- Table -->
                    <div class="overflow-x-auto flex-1">
                        <table class="w-full text-left text-sm whitespace-nowrap">
                            <thead class="text-xs uppercase text-on-surface-variant bg-white/[0.02] border-b border-white/5">
                                <tr>
                                    <th class="px-5 py-3 font-medium tracking-wider">Order ID</th>
                                    <th class="px-5 py-3 font-medium tracking-wider">Customer</th>
                                    <th class="px-5 py-3 font-medium tracking-wider">Carrier / AWB</th>
                                    <th class="px-5 py-3 font-medium tracking-wider">Current Status</th>
                                    <th class="px-5 py-3 font-medium tracking-wider">Last Update</th>
                                    <th class="px-5 py-3 font-medium tracking-wider text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-white/5">
                                <tr class="hover:bg-white/[0.02] transition-colors group cursor-pointer bg-white/[0.03]">
                                    <td class="px-5 py-3">
                                        <div class="text-[#1A73E8] font-medium">ORD-2024-1254</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">18 May 2024, 10:30 AM</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">Rohit Kumar</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">+91 98765 43210</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white font-bold">DELHIVERY</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5 flex items-center gap-1">1498563214785 <span class="material-symbols-outlined text-[12px] text-[#1A73E8] cursor-pointer">content_copy</span></div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="inline-flex items-center text-[12px] font-medium text-[#1A73E8]">In Transit</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">Arrived at Bhubaneswar Hub</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">18 May 2024</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">09:45 AM</div>
                                    </td>
                                    <td class="px-5 py-3 text-right space-x-1">
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">visibility</span>
                                        </button>
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">location_on</span>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-white/[0.02] transition-colors group">
                                    <td class="px-5 py-3">
                                        <div class="text-[#1A73E8] font-medium">ORD-2024-1253</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">18 May 2024, 09:15 AM</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">Pooja Sharma</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">+91 98711 22334</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-[#1A73E8] font-bold">BLUE<span class="text-[#34A853]">DART</span></div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5 flex items-center gap-1">3126549874123 <span class="material-symbols-outlined text-[12px] text-[#1A73E8] cursor-pointer">content_copy</span></div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="inline-flex items-center text-[12px] font-medium text-[#F59E0B]">Out for Delivery</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">Out for delivery</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">18 May 2024</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">11:20 AM</div>
                                    </td>
                                    <td class="px-5 py-3 text-right space-x-1">
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">visibility</span>
                                        </button>
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">location_on</span>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-white/[0.02] transition-colors group">
                                    <td class="px-5 py-3">
                                        <div class="text-[#1A73E8] font-medium">ORD-2024-1252</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">17 May 2024, 08:45 PM</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">Amit Singh</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">+91 91234 56789</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-[#F59E0B] font-bold">XPRESSBEES</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5 flex items-center gap-1">X1234567890IN <span class="material-symbols-outlined text-[12px] text-[#1A73E8] cursor-pointer">content_copy</span></div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="inline-flex items-center text-[12px] font-medium text-[#00D084]">Delivered</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">Delivered Successfully</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">17 May 2024</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">06:10 PM</div>
                                    </td>
                                    <td class="px-5 py-3 text-right space-x-1">
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">visibility</span>
                                        </button>
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">location_on</span>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-white/[0.02] transition-colors group">
                                    <td class="px-5 py-3">
                                        <div class="text-[#1A73E8] font-medium">ORD-2024-1249</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">16 May 2024, 11:30 AM</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">Sanjay Kumar</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">+91 87654 32109</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-[#F59E0B] font-bold">XPRESSBEES</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5 flex items-center gap-1">X1234567892IN <span class="material-symbols-outlined text-[12px] text-[#1A73E8] cursor-pointer">content_copy</span></div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="inline-flex items-center text-[12px] font-medium text-[#F87171]">Exception</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">Address not found</div>
                                    </td>
                                    <td class="px-5 py-3">
                                        <div class="text-white">16 May 2024</div>
                                        <div class="text-[11px] text-on-surface-variant mt-0.5">10:15 AM</div>
                                    </td>
                                    <td class="px-5 py-3 text-right space-x-1">
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">visibility</span>
                                        </button>
                                        <button class="w-8 h-8 rounded-lg hover:bg-white/10 text-on-surface-variant hover:text-white transition-colors inline-flex items-center justify-center">
                                            <span class="material-symbols-outlined text-[18px]">location_on</span>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Pagination -->
                    <div class="border-t border-white/5 px-5 py-3 flex items-center justify-between">
                        <div class="text-sm text-on-surface-variant">
                            Showing 1 to 8 of 1,254 orders
                        </div>
                        <div class="flex items-center gap-3">
                            <div class="flex bg-white/5 rounded-lg overflow-hidden border border-white/5">
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                </button>
                                <button class="w-8 h-8 flex items-center justify-center text-white bg-[#1A73E8] font-medium text-sm">1</button>
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors font-medium text-sm">2</button>
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors font-medium text-sm">3</button>
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant font-medium text-sm">...</button>
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors font-medium text-sm">157</button>
                                <button class="w-8 h-8 flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">chevron_right</span>
                                </button>
                            </div>
                            <select class="bg-surface-container border border-white/5 rounded-lg py-1.5 px-3 text-sm text-white focus:outline-none focus:border-primary/50 appearance-none pr-7 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%24%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2010l5%205%205-5%22%20stroke%3D%22%23c1c6d7%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%3C%2Fsvg%3E')] bg-[position:right_4px_center] bg-no-repeat bg-[length:14px]">
                                <option>10 / page</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Tracking Overview Graphic Chart -->
                <div class="bg-surface-container border border-white/5 rounded-xl p-6">
                    <h2 class="text-sm font-semibold text-white mb-6">Tracking Overview</h2>
                    <div class="flex items-center gap-10">
                        <div class="relative w-24 h-24 rounded-full border-8 border-white/5 flex items-center justify-center shrink-0">
                            <!-- SVG Donut Chart Mockup -->
                            <svg class="absolute inset-0 w-full h-full -rotate-90" viewBox="0 0 100 100">
                                <circle cx="50" cy="50" r="46" fill="none" stroke="#1A73E8" stroke-width="8" stroke-dasharray="289" stroke-dashoffset="50" class="drop-shadow-[0_0_4px_#1A73E8]"></circle>
                                <circle cx="50" cy="50" r="46" fill="none" stroke="#F59E0B" stroke-width="8" stroke-dasharray="289" stroke-dashoffset="240"></circle>
                                <circle cx="50" cy="50" r="46" fill="none" stroke="#00D084" stroke-width="8" stroke-dasharray="289" stroke-dashoffset="270"></circle>
                            </svg>
                            <div class="text-center">
                                <div class="text-lg font-bold text-white leading-tight">1,254</div>
                                <div class="text-[10px] text-on-surface-variant">Total Orders</div>
                            </div>
                        </div>

                        <div class="flex-1 grid grid-cols-2 md:grid-cols-5 gap-6">
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-2 h-2 rounded-full bg-[#1A73E8]"></div>
                                    <div class="text-[11px] text-on-surface-variant">In Transit</div>
                                </div>
                                <div class="text-lg font-bold text-white mb-2">642 <span class="text-[11px] text-on-surface-variant font-normal">(51.2%)</span></div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-[#1A73E8]" style="width:51.2%"></div></div>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-2 h-2 rounded-full bg-[#F59E0B]"></div>
                                    <div class="text-[11px] text-on-surface-variant">Out for Delivery</div>
                                </div>
                                <div class="text-lg font-bold text-white mb-2">218 <span class="text-[11px] text-on-surface-variant font-normal">(17.4%)</span></div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-[#F59E0B]" style="width:17.4%"></div></div>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-2 h-2 rounded-full bg-[#00D084]"></div>
                                    <div class="text-[11px] text-on-surface-variant">Delivered</div>
                                </div>
                                <div class="text-lg font-bold text-white mb-2">1,024 <span class="text-[11px] text-on-surface-variant font-normal">(81.7%)</span></div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-[#00D084]" style="width:81.7%"></div></div>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-2 h-2 rounded-full bg-[#F87171]"></div>
                                    <div class="text-[11px] text-on-surface-variant">Exception</div>
                                </div>
                                <div class="text-lg font-bold text-white mb-2">87 <span class="text-[11px] text-on-surface-variant font-normal">(6.9%)</span></div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-[#F87171]" style="width:6.9%"></div></div>
                            </div>
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-2 h-2 rounded-full bg-on-surface-variant"></div>
                                    <div class="text-[11px] text-on-surface-variant">Cancelled</div>
                                </div>
                                <div class="text-lg font-bold text-white mb-2">43 <span class="text-[11px] text-on-surface-variant font-normal">(3.4%)</span></div>
                                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden"><div class="h-full bg-on-surface-variant" style="width:3.4%"></div></div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Right Side: Order Details Sidebar Panel -->
            <div class="bg-surface-container border border-white/5 rounded-xl flex flex-col h-[calc(100vh-160px)] sticky top-8">
                
                <!-- Panel Header -->
                <div class="p-4 border-b border-white/5 flex items-center justify-between">
                    <h3 class="text-sm font-semibold text-white">Order Details</h3>
                    <div class="bg-[#00D084]/20 text-[#00D084] px-2 py-0.5 rounded text-[10px] font-bold">Delivered</div>
                </div>

                <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-6">
                    
                    <!-- Product Summary -->
                    <div class="flex gap-4 items-center">
                        <div class="w-12 h-12 rounded-lg bg-surface-deep border border-white/5 overflow-hidden shrink-0">
                            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuA0g3LsM-qtPpHQcILcEuIud2ScowamPvY19mTuDmn46dSgF04e1j6wk_eGP7JXYf7KQHw7wWhnl0XCHl6-y_uq8v64zbG9DpfzbRGG80QaMr4ci5qdMV6WwDHVQw4jIw-hUgpXF_mev8T456Fiy1exifr6a-GIfiqumYpdmgL32jp9MnzgjBRsTiFnY22T1qejIIflTz8IuykB0HW7z7VQSveU-2n9pIvNTuK4M3w-38_aOb_JiUTyOWs4oB7TsnFLLoaocHvkC726" class="w-full h-full object-cover">
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="text-[13px] font-medium text-white truncate">High Performance Gaming PC</div>
                            <div class="text-[11px] text-on-surface-variant mt-0.5">1 x ₹45,320</div>
                        </div>
                    </div>

                    <div class="space-y-2">
                        <div class="flex justify-between text-[12px]">
                            <span class="text-on-surface-variant">Order ID</span>
                            <span class="text-white">ORD-2024-1252</span>
                        </div>
                        <div class="flex justify-between text-[12px]">
                            <span class="text-on-surface-variant">Order Date</span>
                            <span class="text-white">17 May 2024, 08:45 PM</span>
                        </div>
                        <div class="flex justify-between text-[12px]">
                            <span class="text-on-surface-variant">Payment Method</span>
                            <span class="text-white">Online (UPI)</span>
                        </div>
                        <div class="flex justify-between text-[12px] pt-2 border-t border-white/5">
                            <span class="text-on-surface-variant">Total Amount</span>
                            <span class="text-white font-semibold">₹62,999</span>
                        </div>
                    </div>

                    <!-- Customer Details -->
                    <div>
                        <h4 class="text-sm font-medium text-white mb-3">Customer Details</h4>
                        <div class="space-y-2 text-[12px]">
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">person</span>
                                <span class="text-white">Amit Singh</span>
                            </div>
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">call</span>
                                <span class="text-white">+91 91234 56789</span>
                            </div>
                            <div class="flex items-center gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px]">mail</span>
                                <span class="text-white">amit.singh@email.com</span>
                            </div>
                            <div class="flex items-start gap-3 text-on-surface-variant">
                                <span class="material-symbols-outlined text-[16px] mt-0.5">location_on</span>
                                <span class="text-white leading-relaxed text-right flex-1">Mumbai, Maharashtra, 400001</span>
                            </div>
                        </div>
                    </div>

                    <!-- Shipping Details -->
                    <div>
                        <h4 class="text-sm font-medium text-white mb-3">Shipping Details</h4>
                        <div class="space-y-2 text-[12px]">
                            <div class="flex justify-between">
                                <span class="text-on-surface-variant">Carrier</span>
                                <span class="text-white">Xpressbees</span>
                            </div>
                            <div class="flex justify-between">
                                <span class="text-on-surface-variant">AWB / Tracking ID</span>
                                <span class="text-[#1A73E8] font-medium flex items-center gap-1">X1234567890IN <span class="material-symbols-outlined text-[12px] cursor-pointer">content_copy</span></span>
                            </div>
                            <div class="flex justify-between pt-2">
                                <span class="text-on-surface-variant">Shipping Address</span>
                                <span class="text-white text-right max-w-[150px] leading-relaxed">Amit Singh<br>123, Andheri West<br>Mumbai, Maharashtra - 400058<br>India</span>
                            </div>
                        </div>
                    </div>

                    <!-- Tracking Timeline -->
                    <div>
                        <h4 class="text-sm font-medium text-white mb-4">Tracking Timeline</h4>
                        <div class="relative pl-6 space-y-6">
                            <!-- Line -->
                            <div class="absolute top-2 bottom-2 left-[7px] w-0.5 bg-white/10"></div>
                            <div class="absolute top-2 bottom-1/2 left-[7px] w-0.5 bg-[#00D084]"></div>
                            
                            <!-- Step 1 -->
                            <div class="relative">
                                <div class="absolute left-[-24px] top-1 w-3 h-3 rounded-full bg-[#00D084] border-2 border-surface-container ring-2 ring-[#00D084]/20 z-10"></div>
                                <div class="flex justify-between items-start gap-4">
                                    <div>
                                        <div class="text-[12px] font-medium text-white">Delivered</div>
                                        <div class="text-[11px] text-on-surface-variant leading-tight mt-0.5">Delivered Successfully<br>Mumbai, Maharashtra</div>
                                    </div>
                                    <div class="text-[10px] text-on-surface-variant text-right">
                                        <div class="text-white">17 May 2024</div>
                                        06:10 PM
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Step 2 -->
                            <div class="relative">
                                <div class="absolute left-[-24px] top-1 w-3 h-3 rounded-full bg-transparent border-2 border-[#00D084] bg-surface-container z-10"></div>
                                <div class="flex justify-between items-start gap-4">
                                    <div>
                                        <div class="text-[12px] font-medium text-white">Out for Delivery</div>
                                        <div class="text-[11px] text-on-surface-variant leading-tight mt-0.5">Out for delivery<br>Mumbai, Maharashtra</div>
                                    </div>
                                    <div class="text-[10px] text-on-surface-variant text-right">
                                        <div class="text-white">17 May 2024</div>
                                        09:42 AM
                                    </div>
                                </div>
                            </div>

                            <!-- Step 3 -->
                            <div class="relative">
                                <div class="absolute left-[-24px] top-1 w-3 h-3 rounded-full bg-transparent border-2 border-[#1A73E8] bg-surface-container z-10"></div>
                                <div class="flex justify-between items-start gap-4">
                                    <div>
                                        <div class="text-[12px] font-medium text-white">Arrived at Delivery Hub</div>
                                        <div class="text-[11px] text-on-surface-variant leading-tight mt-0.5">Arrived at Mumbai Hub<br>Mumbai, Maharashtra</div>
                                    </div>
                                    <div class="text-[10px] text-on-surface-variant text-right">
                                        <div class="text-white">16 May 2024</div>
                                        11:15 PM
                                    </div>
                                </div>
                            </div>

                            <!-- Step 4 -->
                            <div class="relative">
                                <div class="absolute left-[-24px] top-1 w-3 h-3 rounded-full bg-transparent border-2 border-[#1A73E8] bg-surface-container z-10"></div>
                                <div class="flex justify-between items-start gap-4">
                                    <div>
                                        <div class="text-[12px] font-medium text-white">In Transit</div>
                                        <div class="text-[11px] text-on-surface-variant leading-tight mt-0.5">Departed from Pune Hub<br>Pune, Maharashtra</div>
                                    </div>
                                    <div class="text-[10px] text-on-surface-variant text-right">
                                        <div class="text-white">16 May 2024</div>
                                        06:35 PM
                                    </div>
                                </div>
                            </div>

                            <!-- Step 5 -->
                            <div class="relative">
                                <div class="absolute left-[-24px] top-1 w-3 h-3 rounded-full bg-transparent border-2 border-white/20 bg-surface-container z-10"></div>
                                <div class="flex justify-between items-start gap-4 opacity-70">
                                    <div>
                                        <div class="text-[12px] font-medium text-white">Order Picked Up</div>
                                        <div class="text-[11px] text-on-surface-variant leading-tight mt-0.5">Picked up from seller<br>Pune, Maharashtra</div>
                                    </div>
                                    <div class="text-[10px] text-on-surface-variant text-right">
                                        <div class="text-white">16 May 2024</div>
                                        02:20 PM
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

                <div class="p-4 border-t border-white/5">
                    <button class="w-full py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm text-white font-medium transition-colors flex items-center justify-center gap-2">
                        View Full Tracking Page <span class="material-symbols-outlined text-[16px]">open_in_new</span>
                    </button>
                </div>
            </div>

        </div>

    </div>

</main>"""

content = re.sub(r'<main[^>]*>.*?</main>', main_content, content, flags=re.DOTALL)

with open('admin-order-tracking.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created admin-order-tracking.html successfully.")
