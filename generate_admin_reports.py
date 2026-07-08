import os
import re

def generate_admin_reports():
    # Read the base template from an existing admin file (like admin-dashboard.html)
    with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
        base_html = f.read()

    # Find the main content area
    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    reports_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div>
                    <h1 class="text-3xl font-bold text-white mb-2 tracking-tight">Reports</h1>
                    <p class="text-on-surface-variant">Detailed reports and insights about your business performance.</p>
                </div>
                <div class="flex items-center gap-4">
                    <button class="px-5 py-2.5 rounded-xl border border-white/10 hover:border-white/20 bg-surface-container/50 text-white font-medium transition-all duration-300 flex items-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">calendar_today</span>
                        Schedule Reports
                    </button>
                    <button class="px-5 py-2.5 rounded-xl bg-primary hover:bg-primary/90 text-on-primary font-medium transition-all duration-300 flex items-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">download</span>
                        Export Reports
                    </button>
                </div>
            </div>

            <!-- Stats Grid (5 Cards) -->
            <div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-8 relative z-10">
                <!-- Total Revenue -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-[#3b82f6]/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-12 h-12 rounded-xl bg-[#3b82f6]/10 border border-[#3b82f6]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#3b82f6]">currency_rupee</span>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-on-surface-variant mb-1">Total Revenue</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">₹24,58,750</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-4">
                        <span class="material-symbols-outlined text-[16px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">18.6%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Total Orders -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-[#10b981]/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-12 h-12 rounded-xl bg-[#10b981]/10 border border-[#10b981]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#10b981]">shopping_bag</span>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-on-surface-variant mb-1">Total Orders</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">1,254</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-4">
                        <span class="material-symbols-outlined text-[16px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">12.4%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Average Order Value -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-[#8b5cf6]/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-12 h-12 rounded-xl bg-[#8b5cf6]/10 border border-[#8b5cf6]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#8b5cf6]">trending_up</span>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-on-surface-variant mb-1">Average Order Value</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">₹19,590</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-4">
                        <span class="material-symbols-outlined text-[16px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">8.3%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Total Customers -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-[#f59e0b]/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-12 h-12 rounded-xl bg-[#f59e0b]/10 border border-[#f59e0b]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#f59e0b]">group</span>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-on-surface-variant mb-1">Total Customers</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">3,245</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-4">
                        <span class="material-symbols-outlined text-[16px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">14.8%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>

                <!-- Total Profit -->
                <div class="glass-card rounded-2xl border border-white/5 bg-surface-container/30 p-6 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-[#14b8a6]/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="flex items-start gap-4 mb-2">
                        <div class="w-12 h-12 rounded-xl bg-[#14b8a6]/10 border border-[#14b8a6]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#14b8a6]">account_balance_wallet</span>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-on-surface-variant mb-1">Total Profit</p>
                            <h3 class="text-2xl font-bold text-white tracking-tight">₹4,56,320</h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 mt-4">
                        <span class="material-symbols-outlined text-[16px] text-green-400">arrow_upward</span>
                        <span class="text-xs font-medium text-green-400">16.2%</span>
                        <span class="text-xs text-on-surface-variant ml-1">vs last month</span>
                    </div>
                </div>
            </div>

            <!-- Filters Bar -->
            <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-4 mb-8 relative z-10 flex items-center gap-4">
                <!-- Date Picker -->
                <div class="relative flex-1 max-w-[280px]">
                    <span class="material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px] pointer-events-none">calendar_month</span>
                    <input type="text" value="12 May 2024 - 18 May 2024" readonly class="w-full h-11 bg-black/20 border border-white/10 rounded-lg pr-11 pl-4 text-sm text-white focus:outline-none focus:border-primary/50 transition-colors cursor-pointer" />
                </div>

                <!-- Dropdown Filters -->
                <div class="relative flex-1 max-w-[180px]">
                    <select class="w-full h-11 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Channels</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none">expand_more</span>
                </div>
                
                <div class="relative flex-1 max-w-[180px]">
                    <select class="w-full h-11 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Categories</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none">expand_more</span>
                </div>

                <div class="relative flex-1 max-w-[180px]">
                    <select class="w-full h-11 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                        <option value="all">All Payment Methods</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none">expand_more</span>
                </div>

                <div class="flex items-center gap-4 ml-auto">
                    <button class="px-5 py-2.5 rounded-lg border border-white/10 hover:border-white/20 bg-surface-container/50 text-white font-medium transition-all duration-300 flex items-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">filter_list</span>
                        Filters
                    </button>
                    <a href="#" class="text-primary hover:text-primary/80 text-sm font-medium transition-colors">Reset</a>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="flex gap-6 relative z-10">
                
                <!-- Left Column (approx 2/3) -->
                <div class="w-2/3 flex flex-col gap-6">
                    
                    <!-- Revenue Overview Chart -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-6 flex flex-col">
                        <div class="flex justify-between items-center mb-6">
                            <div>
                                <h3 class="text-lg font-bold text-white">Revenue Overview</h3>
                            </div>
                            <div class="relative w-[120px]">
                                <select class="w-full h-9 bg-black/20 border border-white/10 rounded-lg px-4 text-sm text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                                    <option value="daily">Daily</option>
                                    <option value="weekly">Weekly</option>
                                    <option value="monthly">Monthly</option>
                                </select>
                                <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px] pointer-events-none">expand_more</span>
                            </div>
                        </div>
                        
                        <!-- Chart Legend -->
                        <div class="flex items-center gap-6 mb-4">
                            <div class="flex items-center gap-2">
                                <div class="w-3 h-1 bg-[#3b82f6] rounded-full"></div>
                                <span class="text-xs text-on-surface-variant">Revenue</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="w-3 h-1 bg-[#10b981] rounded-full"></div>
                                <span class="text-xs text-on-surface-variant">Orders</span>
                            </div>
                        </div>

                        <!-- Chart Placeholder (Simulating the SVG lines) -->
                        <div class="flex-1 w-full relative min-h-[300px]">
                            <!-- Y-axis labels Left (Revenue) -->
                            <div class="absolute left-0 top-0 bottom-6 flex flex-col justify-between text-[10px] text-on-surface-variant">
                                <span>₹2.5L</span>
                                <span>₹2.0L</span>
                                <span>₹1.5L</span>
                                <span>₹1.0L</span>
                                <span>₹0.5L</span>
                                <span>₹0</span>
                            </div>
                            <!-- Y-axis labels Right (Orders) -->
                            <div class="absolute right-0 top-0 bottom-6 flex flex-col justify-between text-[10px] text-on-surface-variant text-right">
                                <span>250</span>
                                <span>200</span>
                                <span>150</span>
                                <span>100</span>
                                <span>50</span>
                                <span>0</span>
                            </div>
                            <!-- Grid Lines -->
                            <div class="absolute left-10 right-8 top-1 bottom-8 flex flex-col justify-between pointer-events-none">
                                <div class="w-full border-t border-white/5"></div>
                                <div class="w-full border-t border-white/5"></div>
                                <div class="w-full border-t border-white/5"></div>
                                <div class="w-full border-t border-white/5"></div>
                                <div class="w-full border-t border-white/5"></div>
                                <div class="w-full border-t border-white/5"></div>
                            </div>
                            
                            <!-- X-axis labels -->
                            <div class="absolute left-10 right-8 bottom-0 flex justify-between text-[10px] text-on-surface-variant mt-2">
                                <span>12 May</span>
                                <span>13 May</span>
                                <span>14 May</span>
                                <span>15 May</span>
                                <span>16 May</span>
                                <span>17 May</span>
                                <span>18 May</span>
                            </div>

                            <!-- Lines (SVG approximation) -->
                            <div class="absolute left-10 right-8 top-1 bottom-8 pointer-events-none">
                                <svg class="w-full h-full" preserveAspectRatio="none" viewBox="0 0 100 100">
                                    <!-- Revenue Line (Blue) -->
                                    <polyline points="0,50 16.6,40 33.3,35 50,20 66.6,35 83.3,35 100,55" fill="none" stroke="#3b82f6" stroke-width="2" vector-effect="non-scaling-stroke"></polyline>
                                    <circle cx="0" cy="50" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="16.6" cy="40" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="33.3" cy="35" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="50" cy="20" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="66.6" cy="35" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="83.3" cy="35" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="100" cy="55" r="3" fill="#3b82f6" vector-effect="non-scaling-stroke"></circle>
                                    
                                    <!-- Orders Line (Green) -->
                                    <polyline points="0,70 16.6,60 33.3,55 50,45 66.6,55 83.3,55 100,75" fill="none" stroke="#10b981" stroke-width="2" vector-effect="non-scaling-stroke"></polyline>
                                    <circle cx="0" cy="70" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="16.6" cy="60" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="33.3" cy="55" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="50" cy="45" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="66.6" cy="55" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="83.3" cy="55" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                    <circle cx="100" cy="75" r="3" fill="#10b981" vector-effect="non-scaling-stroke"></circle>
                                </svg>
                            </div>
                        </div>
                    </div>

                    <!-- Top Performing Categories -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-6 border-b border-white/5">
                            <h3 class="text-lg font-bold text-white">Top Performing Categories</h3>
                        </div>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="border-b border-white/5 bg-black/20">
                                        <th class="py-3 px-6 text-xs font-semibold text-on-surface-variant uppercase tracking-wider">Category</th>
                                        <th class="py-3 px-6 text-xs font-semibold text-on-surface-variant uppercase tracking-wider">Orders</th>
                                        <th class="py-3 px-6 text-xs font-semibold text-on-surface-variant uppercase tracking-wider">Revenue</th>
                                        <th class="py-3 px-6 text-xs font-semibold text-on-surface-variant uppercase tracking-wider">Profit</th>
                                        <th class="py-3 px-6 text-xs font-semibold text-on-surface-variant uppercase tracking-wider">Conversion Rate</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-white/5">
                                    <tr class="hover:bg-white/5 transition-colors">
                                        <td class="py-4 px-6 text-sm text-white font-medium">Processors</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">245</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹6,45,230</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹1,28,450</td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <span class="text-sm text-on-surface-variant min-w-[36px]">4.62%</span>
                                                <div class="w-24 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 85%"></div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors">
                                        <td class="py-4 px-6 text-sm text-white font-medium">Graphics Cards</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">198</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹5,65,890</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹1,12,380</td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <span class="text-sm text-on-surface-variant min-w-[36px]">3.98%</span>
                                                <div class="w-24 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 70%"></div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors">
                                        <td class="py-4 px-6 text-sm text-white font-medium">Motherboards</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">176</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹3,45,670</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹72,450</td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <span class="text-sm text-on-surface-variant min-w-[36px]">3.21%</span>
                                                <div class="w-24 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 55%"></div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors">
                                        <td class="py-4 px-6 text-sm text-white font-medium">RAM</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">164</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹2,34,560</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹54,320</td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <span class="text-sm text-on-surface-variant min-w-[36px]">2.98%</span>
                                                <div class="w-24 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 45%"></div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-white/5 transition-colors">
                                        <td class="py-4 px-6 text-sm text-white font-medium">Storage (SSD/HDD)</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">152</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹2,12,450</td>
                                        <td class="py-4 px-6 text-sm text-on-surface-variant">₹48,620</td>
                                        <td class="py-4 px-6">
                                            <div class="flex items-center gap-3">
                                                <span class="text-sm text-on-surface-variant min-w-[36px]">2.45%</span>
                                                <div class="w-24 h-1.5 bg-white/10 rounded-full overflow-hidden">
                                                    <div class="h-full bg-[#3b82f6] rounded-full" style="width: 35%"></div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="p-4 border-t border-white/5 bg-black/10 text-left">
                            <a href="#" class="text-primary hover:text-primary/80 text-sm font-medium transition-colors inline-flex items-center gap-1">
                                View all categories report <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Right Column (approx 1/3) -->
                <div class="w-1/3 flex flex-col gap-6">
                    
                    <!-- Quick Reports -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-6 border-b border-white/5">
                            <h3 class="text-lg font-bold text-white">Quick Reports</h3>
                        </div>
                        <div class="flex flex-col">
                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">bar_chart</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Sales Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Detailed sales and revenue report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>
                            
                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">calendar_today</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Order Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Order status and performance report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">group</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Customer Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Customer growth and activity report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">shopping_bag</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Product Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Product performance and stock report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">inventory_2</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Inventory Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Stock movement and inventory report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>

                            <a href="#" class="flex items-center gap-4 p-4 hover:bg-white/5 transition-colors border-b border-white/5 group">
                                <div class="w-10 h-10 rounded-lg bg-surface-container border border-white/10 flex items-center justify-center shrink-0 text-on-surface-variant group-hover:text-primary transition-colors">
                                    <span class="material-symbols-outlined text-[20px]">request_quote</span>
                                </div>
                                <div class="flex-1">
                                    <p class="text-sm font-medium text-white group-hover:text-primary transition-colors">Profit & Loss Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Profitability and loss analysis report</p>
                                </div>
                                <span class="material-symbols-outlined text-on-surface-variant text-[16px]">chevron_right</span>
                            </a>
                        </div>
                        <div class="p-4 bg-black/10">
                            <a href="#" class="text-primary hover:text-primary/80 text-sm font-medium transition-colors inline-flex items-center gap-1">
                                View All Reports <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                            </a>
                        </div>
                    </div>

                    <!-- Report Insights -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-6 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-lg font-bold text-white flex items-center gap-2">
                                <span class="material-symbols-outlined text-[#10b981] text-[20px]">trending_up</span> Report Insights
                            </h3>
                            <a href="#" class="text-primary hover:text-primary/80 text-xs font-medium transition-colors inline-flex items-center gap-1">
                                View Analytics <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                            </a>
                        </div>
                        <div class="p-6 flex flex-col gap-5">
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-[#3b82f6]/10 flex items-center justify-center shrink-0 mt-0.5">
                                    <span class="material-symbols-outlined text-[#3b82f6] text-[16px]">thumb_up</span>
                                </div>
                                <div>
                                    <p class="text-sm text-white font-medium mb-1">Revenue is up 18.6% compared to last month.</p>
                                    <p class="text-xs text-on-surface-variant">You earned ₹3,85,230 more than last month.</p>
                                </div>
                            </div>
                            
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-[#14b8a6]/10 flex items-center justify-center shrink-0 mt-0.5">
                                    <span class="material-symbols-outlined text-[#14b8a6] text-[16px]">devices</span>
                                </div>
                                <div>
                                    <p class="text-sm text-white font-medium mb-1">Graphics Cards category has highest revenue.</p>
                                    <p class="text-xs text-on-surface-variant">₹5,65,890 earned from 198 orders.</p>
                                </div>
                            </div>

                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-[#10b981]/10 flex items-center justify-center shrink-0 mt-0.5">
                                    <span class="material-symbols-outlined text-[#10b981] text-[16px]">payments</span>
                                </div>
                                <div>
                                    <p class="text-sm text-white font-medium mb-1">COD orders decreased by 8.4%.</p>
                                    <p class="text-xs text-on-surface-variant">Online payments are increasing.</p>
                                </div>
                            </div>

                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-[#f59e0b]/10 flex items-center justify-center shrink-0 mt-0.5">
                                    <span class="material-symbols-outlined text-[#f59e0b] text-[16px]">person_add</span>
                                </div>
                                <div>
                                    <p class="text-sm text-white font-medium mb-1">New customers increased by 15.3%.</p>
                                    <p class="text-xs text-on-surface-variant">You gained 429 new customers this month.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Scheduled Reports -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-6 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-lg font-bold text-white flex items-center gap-2">
                                <span class="material-symbols-outlined text-on-surface-variant text-[20px]">schedule</span> Scheduled Reports
                            </h3>
                            <a href="#" class="text-primary hover:text-primary/80 text-xs font-medium transition-colors inline-flex items-center gap-1">
                                View All <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                            </a>
                        </div>
                        <div class="p-4 flex flex-col gap-2">
                            <div class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors">
                                <div>
                                    <p class="text-sm font-medium text-white mb-0.5">Daily Sales Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Every day at 09:00 AM</p>
                                </div>
                                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/10 text-[#10b981] uppercase tracking-wider">Active</span>
                            </div>
                            <div class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors">
                                <div>
                                    <p class="text-sm font-medium text-white mb-0.5">Weekly Order Report</p>
                                    <p class="text-[11px] text-on-surface-variant">Every Monday at 10:00 AM</p>
                                </div>
                                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/10 text-[#10b981] uppercase tracking-wider">Active</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{reports_content}</main>', base_html)
    
    # Update active state in sidebar
    new_html = new_html.replace('href="admin-reports.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary"', 
                                'href="admin-reports.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 bg-primary/10 text-primary"')
    
    # Just to be safe, if we use "#" for Reports in base html, replace that too.
    # We should search for the exact block from `update_admin_nav.py`.
    reports_link_pattern = re.compile(r'<a href="[^"]*" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\s*<span class="material-symbols-outlined">summarize</span>\s*<span class="text-body-sm font-medium">Reports</span>\s*</a>')
    
    reports_active_link = """<a href="admin-reports.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 bg-primary/10 text-primary">
            <span class="material-symbols-outlined">summarize</span>
            <span class="text-body-sm font-medium">Reports</span>
        </a>"""
        
    new_html = reports_link_pattern.sub(reports_active_link, new_html)

    with open('admin-reports.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Successfully generated admin-reports.html")

if __name__ == '__main__':
    generate_admin_reports()
