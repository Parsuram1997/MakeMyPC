import os
import re

html_content = '''<main class="flex-1 lg:ml-64 px-6 py-8 md:px-8 bg-surface-dim relative">
    <div class="w-full space-y-gutter">
        
        <!-- Top KPI Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-gutter">
            <!-- 1. Revenue -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Total Revenue</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">₹248k</h4>
                    </div>
                    <span class="material-symbols-outlined text-cyber-teal p-2 bg-cyber-teal/10 rounded-lg">payments</span>
                </div>
                <div class="mt-4 text-cyber-teal font-label-mono text-xs">+12.5% this month</div>
            </div>
            
            <!-- 2. Today's Orders -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Today's Orders</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">12</h4>
                    </div>
                    <span class="material-symbols-outlined text-electric-blue p-2 bg-electric-blue/10 rounded-lg">shopping_cart</span>
                </div>
                <div class="mt-4 text-electric-blue font-label-mono text-xs">4 already shipped</div>
            </div>
            
            <!-- 3. Pending Orders -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Pending Orders</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">18</h4>
                    </div>
                    <span class="material-symbols-outlined text-tertiary-container p-2 bg-tertiary-container/10 rounded-lg">pending_actions</span>
                </div>
                <div class="mt-4 text-outline font-label-mono text-xs">Needs attention</div>
            </div>
            
            <!-- 4. Active Custom Builds -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Active Builds</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">42</h4>
                    </div>
                    <span class="material-symbols-outlined text-primary p-2 bg-primary/10 rounded-lg">build</span>
                </div>
                <div class="mt-4 text-primary font-label-mono text-xs">In assembly line</div>
            </div>
            
            <!-- 5. New Customers -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">New Customers</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">156</h4>
                    </div>
                    <span class="material-symbols-outlined text-secondary p-2 bg-secondary/10 rounded-lg">group_add</span>
                </div>
                <div class="mt-4 text-secondary font-label-mono text-xs">+8% this week</div>
            </div>
            
            <!-- 6. Website Visitors -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Web Visitors</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">12.4K</h4>
                    </div>
                    <span class="material-symbols-outlined text-surface-tint p-2 bg-surface-tint/10 rounded-lg">language</span>
                </div>
                <div class="mt-4 text-surface-tint font-label-mono text-xs">Live traffic: 45</div>
            </div>
            
            <!-- 7. Conversion Rate -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Conversion Rate</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">3.8%</h4>
                    </div>
                    <span class="material-symbols-outlined text-cyber-teal p-2 bg-cyber-teal/10 rounded-lg">trending_up</span>
                </div>
                <div class="mt-4 text-cyber-teal font-label-mono text-xs">Target: 4.5%</div>
            </div>
            
            <!-- 8. Support Tickets -->
            <div class="glass-card p-6 rounded-2xl flex flex-col justify-between group">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="font-label-mono text-label-mono text-outline uppercase">Support Tickets</p>
                        <h4 class="font-headline-lg text-headline-lg mt-2 font-bold text-on-surface">9</h4>
                    </div>
                    <span class="material-symbols-outlined text-error p-2 bg-error/10 rounded-lg">support_agent</span>
                </div>
                <div class="mt-4 text-error font-label-mono text-xs">2 High Priority</div>
            </div>
        </div>

        <!-- Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-gutter">
            <!-- Sales Graph -->
            <div class="glass-card rounded-2xl p-6">
                <h3 class="font-headline-sm text-headline-sm font-bold mb-6">Sales Overview</h3>
                <div class="h-64 flex items-end justify-between gap-2 relative">
                    <!-- Bar Chart Mockup -->
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[40%] hover:bg-electric-blue transition-all"></div>
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[60%] hover:bg-electric-blue transition-all"></div>
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[30%] hover:bg-electric-blue transition-all"></div>
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[80%] hover:bg-electric-blue transition-all"></div>
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[50%] hover:bg-electric-blue transition-all"></div>
                    <div class="flex-1 bg-electric-blue rounded-t-lg h-[90%] shadow-[0_0_15px_rgba(0,122,255,0.4)] transition-all"></div>
                    <div class="flex-1 bg-electric-blue/20 rounded-t-lg h-[70%] hover:bg-electric-blue transition-all"></div>
                </div>
                <div class="flex justify-between mt-2 font-label-mono text-[10px] text-outline">
                    <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
                </div>
            </div>
            
            <!-- Profit Graph -->
            <div class="glass-card rounded-2xl p-6">
                <h3 class="font-headline-sm text-headline-sm font-bold mb-6">Profit Margin</h3>
                <div class="h-64 flex items-end justify-between gap-2 relative">
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[30%] hover:bg-cyber-teal transition-all"></div>
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[45%] hover:bg-cyber-teal transition-all"></div>
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[25%] hover:bg-cyber-teal transition-all"></div>
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[70%] hover:bg-cyber-teal transition-all"></div>
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[40%] hover:bg-cyber-teal transition-all"></div>
                    <div class="flex-1 bg-cyber-teal rounded-t-lg h-[85%] shadow-[0_0_15px_rgba(0,164,166,0.4)] transition-all"></div>
                    <div class="flex-1 bg-cyber-teal/20 rounded-t-lg h-[60%] hover:bg-cyber-teal transition-all"></div>
                </div>
                <div class="flex justify-between mt-2 font-label-mono text-[10px] text-outline">
                    <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
                </div>
            </div>
        </div>

        <!-- Inventory & Reviews Section -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
            <!-- Inventory Alerts -->
            <div class="glass-card rounded-2xl p-6 flex flex-col h-80">
                <h3 class="font-headline-sm text-headline-sm font-bold mb-4 flex items-center justify-between">
                    Inventory Alerts <span class="material-symbols-outlined text-tertiary-container animate-pulse text-sm">warning</span>
                </h3>
                <div class="overflow-y-auto custom-scrollbar flex-1 space-y-3 pr-2">
                    <div class="p-3 bg-error/10 border border-error/20 rounded-lg flex items-center justify-between">
                        <div class="min-w-0 pr-2">
                            <p class="font-body-sm font-bold text-on-surface truncate">RTX 5090 FE</p>
                            <p class="text-[10px] text-error">Out of Stock</p>
                        </div>
                        <button class="text-[10px] font-bold text-error whitespace-nowrap">REORDER</button>
                    </div>
                    <div class="p-3 bg-tertiary-container/10 border border-tertiary-container/20 rounded-lg flex items-center justify-between">
                        <div class="min-w-0 pr-2">
                            <p class="font-body-sm font-bold text-on-surface truncate">i9-14900K</p>
                            <p class="text-[10px] text-tertiary-container">Low Inventory (5)</p>
                        </div>
                        <button class="text-[10px] font-bold text-tertiary-container whitespace-nowrap">RESTOCK</button>
                    </div>
                    <div class="p-3 bg-white/5 border border-white/10 rounded-lg flex items-center justify-between">
                        <div class="min-w-0 pr-2">
                            <p class="font-body-sm font-bold text-on-surface truncate">Trident Z5 64GB</p>
                            <p class="text-[10px] text-outline">Stock Alert (12)</p>
                        </div>
                        <button class="text-[10px] font-bold text-outline hover:text-white whitespace-nowrap">VIEW</button>
                    </div>
                </div>
            </div>

            <!-- Top Selling Products -->
            <div class="glass-card rounded-2xl p-6 flex flex-col h-80">
                <h3 class="font-headline-sm text-headline-sm font-bold mb-4">Top Sellers</h3>
                <div class="overflow-y-auto custom-scrollbar flex-1 space-y-3 pr-2">
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 bg-surface-container rounded-lg flex items-center justify-center text-electric-blue font-bold text-xs">1</div>
                        <div class="flex-1 min-w-0">
                            <p class="font-body-sm font-bold text-on-surface truncate">Corsair RM1000x</p>
                            <p class="text-[10px] text-outline">42 Units Sold</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 bg-surface-container rounded-lg flex items-center justify-center text-cyber-teal font-bold text-xs">2</div>
                        <div class="flex-1 min-w-0">
                            <p class="font-body-sm font-bold text-on-surface truncate">Ryzen 7 7800X3D</p>
                            <p class="text-[10px] text-outline">38 Units Sold</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 bg-surface-container rounded-lg flex items-center justify-center text-primary font-bold text-xs">3</div>
                        <div class="flex-1 min-w-0">
                            <p class="font-body-sm font-bold text-on-surface truncate">NZXT Kraken Elite</p>
                            <p class="text-[10px] text-outline">31 Units Sold</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 bg-surface-container rounded-lg flex items-center justify-center text-outline font-bold text-xs">4</div>
                        <div class="flex-1 min-w-0">
                            <p class="font-body-sm font-bold text-on-surface truncate">Samsung 990 Pro 2TB</p>
                            <p class="text-[10px] text-outline">29 Units Sold</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Latest Reviews -->
            <div class="glass-card rounded-2xl p-6 flex flex-col h-80">
                <h3 class="font-headline-sm text-headline-sm font-bold mb-4">Latest Reviews</h3>
                <div class="overflow-y-auto custom-scrollbar flex-1 space-y-4 pr-2">
                    <div class="border-b border-white/10 pb-3">
                        <div class="flex items-center justify-between mb-1">
                            <p class="font-body-sm font-bold text-on-surface">Alex R.</p>
                            <div class="flex text-tertiary text-xs">★★★★★</div>
                        </div>
                        <p class="text-[10px] text-on-surface-variant line-clamp-2">"Amazing custom loop build! The cable management is flawless and temperatures are great."</p>
                    </div>
                    <div class="border-b border-white/10 pb-3">
                        <div class="flex items-center justify-between mb-1">
                            <p class="font-body-sm font-bold text-on-surface">Sarah C.</p>
                            <div class="flex text-tertiary text-xs">★★★★☆</div>
                        </div>
                        <p class="text-[10px] text-on-surface-variant line-clamp-2">"Great PC, but delivery was delayed by a day. Support was helpful though."</p>
                    </div>
                    <div>
                        <div class="flex items-center justify-between mb-1">
                            <p class="font-body-sm font-bold text-on-surface">Marcus T.</p>
                            <div class="flex text-tertiary text-xs">★★★★★</div>
                        </div>
                        <p class="text-[10px] text-on-surface-variant line-clamp-2">"The packaging was incredibly secure. Booted up right out of the box with zero issues."</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Recent Orders Table -->
        <div class="glass-card rounded-2xl p-6 overflow-hidden">
            <div class="flex justify-between items-center mb-6">
                <h3 class="font-headline-sm text-headline-sm font-bold">Recent Orders</h3>
                <button class="text-electric-blue font-label-mono text-xs flex items-center gap-1 hover:gap-2 transition-all">
                    VIEW ALL <span class="material-symbols-outlined text-sm">arrow_forward</span>
                </button>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left">
                    <thead class="border-b border-white/10">
                        <tr class="font-label-mono text-outline text-xs">
                            <th class="pb-4 px-2">ORDER ID</th>
                            <th class="pb-4">CLIENT</th>
                            <th class="pb-4">CONFIGURATION</th>
                            <th class="pb-4">PRICE</th>
                            <th class="pb-4">STATUS</th>
                            <th class="pb-4">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-white/5">
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="py-4 px-2 font-label-mono text-electric-blue">#MP-1024</td>
                            <td class="py-4">
                                <div class="font-body-sm text-on-surface">Alex Rivera</div>
                                <div class="font-label-mono text-[10px] text-outline">alex.r@example.com</div>
                            </td>
                            <td class="py-4 text-on-surface-variant font-body-sm">Custom Loop | RTX 4090</td>
                            <td class="py-4 font-label-mono">₹4,299.00</td>
                            <td class="py-4"><span class="status-badge bg-electric-blue/10 text-electric-blue border border-electric-blue/20">Processing</span></td>
                            <td class="py-4"><button class="material-symbols-outlined text-outline hover:text-on-surface text-sm">more_vert</button></td>
                        </tr>
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="py-4 px-2 font-label-mono text-electric-blue">#MP-1023</td>
                            <td class="py-4">
                                <div class="font-body-sm text-on-surface">Sarah Chen</div>
                                <div class="font-label-mono text-[10px] text-outline">schen@example.com</div>
                            </td>
                            <td class="py-4 text-on-surface-variant font-body-sm">Pre-built Stealth | RTX 4080</td>
                            <td class="py-4 font-label-mono">₹2,850.00</td>
                            <td class="py-4"><span class="status-badge bg-cyber-teal/10 text-cyber-teal border border-cyber-teal/20">Shipped</span></td>
                            <td class="py-4"><button class="material-symbols-outlined text-outline hover:text-on-surface text-sm">more_vert</button></td>
                        </tr>
                        <tr class="hover:bg-white/[0.02] transition-colors group">
                            <td class="py-4 px-2 font-label-mono text-electric-blue">#MP-1022</td>
                            <td class="py-4">
                                <div class="font-body-sm text-on-surface">Marcus Thorne</div>
                                <div class="font-label-mono text-[10px] text-outline">mthorne@example.com</div>
                            </td>
                            <td class="py-4 text-on-surface-variant font-body-sm">Creator Pro | RTX 5090</td>
                            <td class="py-4 font-label-mono">₹5,499.00</td>
                            <td class="py-4"><span class="status-badge bg-outline/10 text-on-surface-variant border border-outline/20">Delivered</span></td>
                            <td class="py-4"><button class="material-symbols-outlined text-outline hover:text-on-surface text-sm">more_vert</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>
</main>'''

with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <main ...>...</main>
content = re.sub(r'<main class="flex-1 lg:ml-64 px-6 py-8 md:px-8 bg-surface-dim relative">.*?</main>', html_content, content, flags=re.DOTALL)

with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Main content updated.")
