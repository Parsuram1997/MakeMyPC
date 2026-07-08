import os
import re

def generate_admin_payments():
    with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    payments_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined text-3xl text-on-surface-variant">payments</span>
                    <div>
                        <h1 class="text-3xl font-bold text-white mb-2 tracking-tight">Payments</h1>
                        <p class="text-on-surface-variant text-sm">Monitor transactions, refunds, and payment gateways.</p>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <div class="relative">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px] pointer-events-none">calendar_month</span>
                        <input type="text" value="12 May 2024 - 18 May 2024" readonly class="h-10 bg-black/20 border border-white/10 rounded-lg pl-10 pr-10 text-sm text-white focus:outline-none focus:border-primary/50 transition-colors cursor-pointer min-w-[220px]" />
                        <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px] pointer-events-none">expand_more</span>
                    </div>
                    <button class="px-5 py-2.5 rounded-xl border border-white/10 hover:border-white/20 bg-surface-container/50 text-white font-medium transition-all duration-300 flex items-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">download</span>
                        Export Report
                    </button>
                </div>
            </div>

            <!-- Stats Grid (4 Cards) -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8 relative z-10">
                <!-- Total Revenue -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-5 relative overflow-hidden group">
                    <div class="flex items-start justify-between mb-4">
                        <div class="w-10 h-10 rounded-xl bg-[#2563eb]/10 border border-[#2563eb]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#2563eb] text-[20px]">account_balance_wallet</span>
                        </div>
                        <div class="flex items-center gap-1 bg-[#10b981]/10 border border-[#10b981]/20 px-2 py-1 rounded text-[#10b981]">
                            <span class="material-symbols-outlined text-[12px]">arrow_upward</span>
                            <span class="text-[10px] font-bold">12.5%</span>
                        </div>
                    </div>
                    <div>
                        <p class="text-[11px] font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Total Revenue</p>
                        <h3 class="text-2xl font-bold text-white tracking-tight">₹14,50,000</h3>
                    </div>
                </div>

                <!-- Successful Transactions -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-5 relative overflow-hidden group">
                    <div class="flex items-start justify-between mb-4">
                        <div class="w-10 h-10 rounded-xl bg-[#10b981]/10 border border-[#10b981]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#10b981] text-[20px]">check_circle</span>
                        </div>
                        <div class="flex items-center gap-1 bg-[#10b981]/10 border border-[#10b981]/20 px-2 py-1 rounded text-[#10b981]">
                            <span class="material-symbols-outlined text-[12px]">arrow_upward</span>
                            <span class="text-[10px] font-bold">8.2%</span>
                        </div>
                    </div>
                    <div>
                        <p class="text-[11px] font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Successful Txns</p>
                        <h3 class="text-2xl font-bold text-white tracking-tight">1,245</h3>
                    </div>
                </div>

                <!-- Pending Payments -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-5 relative overflow-hidden group">
                    <div class="flex items-start justify-between mb-4">
                        <div class="w-10 h-10 rounded-xl bg-[#f59e0b]/10 border border-[#f59e0b]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#f59e0b] text-[20px]">pending_actions</span>
                        </div>
                        <div class="flex items-center gap-1 bg-[#ef4444]/10 border border-[#ef4444]/20 px-2 py-1 rounded text-[#ef4444]">
                            <span class="material-symbols-outlined text-[12px]">arrow_upward</span>
                            <span class="text-[10px] font-bold">2.1%</span>
                        </div>
                    </div>
                    <div>
                        <p class="text-[11px] font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Pending</p>
                        <h3 class="text-2xl font-bold text-white tracking-tight">₹45,200</h3>
                    </div>
                </div>

                <!-- Refunds / Failed -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 p-5 relative overflow-hidden group">
                    <div class="flex items-start justify-between mb-4">
                        <div class="w-10 h-10 rounded-xl bg-[#ef4444]/10 border border-[#ef4444]/20 flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#ef4444] text-[20px]">error</span>
                        </div>
                        <div class="flex items-center gap-1 bg-[#10b981]/10 border border-[#10b981]/20 px-2 py-1 rounded text-[#10b981]">
                            <span class="material-symbols-outlined text-[12px]">arrow_downward</span>
                            <span class="text-[10px] font-bold">4.5%</span>
                        </div>
                    </div>
                    <div>
                        <p class="text-[11px] font-medium text-on-surface-variant mb-1 uppercase tracking-wider">Refunds / Failed</p>
                        <h3 class="text-2xl font-bold text-white tracking-tight">₹12,500</h3>
                    </div>
                </div>
            </div>

            <!-- Two Column Layout -->
            <div class="flex gap-6 relative z-10">
                
                <!-- Left Column (Table) -->
                <div class="flex-[3] flex flex-col gap-6">
                    
                    <!-- Filters Bar -->
                    <div class="flex items-center gap-4">
                        <!-- Search -->
                        <div class="relative flex-1 max-w-[280px]">
                            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px] pointer-events-none">search</span>
                            <input type="text" placeholder="Search by Txn ID or Customer..." class="w-full h-10 bg-black/20 border border-white/10 rounded-lg pl-10 pr-4 text-[13px] text-white placeholder-on-surface-variant focus:outline-none focus:border-primary/50 transition-colors" />
                        </div>

                        <!-- Dropdowns -->
                        <div class="relative flex-1 max-w-[140px]">
                            <select class="w-full h-10 bg-black/20 border border-white/10 rounded-lg px-3 pr-8 text-[13px] text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                                <option value="all">All Methods</option>
                            </select>
                            <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[18px]">expand_more</span>
                        </div>
                        
                        <div class="relative flex-1 max-w-[140px]">
                            <select class="w-full h-10 bg-black/20 border border-white/10 rounded-lg px-3 pr-8 text-[13px] text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                                <option value="all">All Statuses</option>
                            </select>
                            <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[18px]">expand_more</span>
                        </div>

                        <button class="px-3 py-2 rounded-lg border border-white/10 hover:border-white/20 bg-surface-container/50 text-white font-medium transition-all duration-300 flex items-center gap-1.5 text-[13px]">
                            <span class="material-symbols-outlined text-[16px]">filter_list</span>
                            Filters
                        </button>
                        <a href="#" class="text-[#2563eb] hover:text-[#2563eb]/80 text-[13px] font-medium transition-colors">Reset</a>
                    </div>
                    
                    <!-- Table -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="border-b border-white/5 bg-black/20">
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Txn ID</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Order ID</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Customer</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Amount</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Method</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider text-center">Status</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider">Date</th>
                                        <th class="py-3 px-4 text-[10px] font-semibold text-on-surface-variant uppercase tracking-wider text-center">Actions</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-white/5">
                                    <!-- Row 1 -->
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <span class="font-medium text-white text-[12px] group-hover:text-primary transition-colors cursor-pointer">TXN-847291</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <a href="#" class="text-[12px] text-[#3b82f6] hover:underline">#ORD-9021</a>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-3">
                                                <img src="https://i.pravatar.cc/150?img=11" alt="Avatar" class="w-7 h-7 rounded-full object-cover">
                                                <div>
                                                    <p class="text-[12px] font-medium text-white">Rahul Sharma</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">rahul@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <span class="text-[13px] font-bold text-white">₹1,45,000</span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-4 bg-white rounded flex items-center justify-center shrink-0">
                                                    <span class="text-[#0f172a] text-[8px] font-bold">UPI</span>
                                                </div>
                                                <span class="text-[11px] text-on-surface-variant">PhonePe</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4 text-center">
                                            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-[#10b981]/10 border border-[#10b981]/20 text-[10px] font-medium text-[#10b981]">
                                                <span class="w-1 h-1 rounded-full bg-[#10b981]"></span>
                                                Success
                                            </span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <p class="text-[11px] text-white">Today</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">10:45 AM</p>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-7 h-7 rounded bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 2 -->
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <span class="font-medium text-white text-[12px] group-hover:text-primary transition-colors cursor-pointer">TXN-847290</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <a href="#" class="text-[12px] text-[#3b82f6] hover:underline">#ORD-9020</a>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-3">
                                                <div class="w-7 h-7 rounded-full bg-purple-500/20 text-purple-400 flex items-center justify-center text-[12px] font-bold shrink-0">AK</div>
                                                <div>
                                                    <p class="text-[12px] font-medium text-white">Ananya Kumar</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">ananya.k@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <span class="text-[13px] font-bold text-white">₹85,500</span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-4 bg-white rounded flex items-center justify-center shrink-0">
                                                    <span class="text-[#ea580c] text-[8px] font-bold italic">MC</span>
                                                </div>
                                                <span class="text-[11px] text-on-surface-variant">**** 4242</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4 text-center">
                                            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-[#f59e0b]/10 border border-[#f59e0b]/20 text-[10px] font-medium text-[#f59e0b]">
                                                <span class="w-1 h-1 rounded-full bg-[#f59e0b]"></span>
                                                Pending
                                            </span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <p class="text-[11px] text-white">Today</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">09:12 AM</p>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-7 h-7 rounded bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 3 -->
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <span class="font-medium text-white text-[12px] group-hover:text-primary transition-colors cursor-pointer">TXN-847289</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <a href="#" class="text-[12px] text-[#3b82f6] hover:underline">#ORD-9018</a>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-3">
                                                <img src="https://i.pravatar.cc/150?img=33" alt="Avatar" class="w-7 h-7 rounded-full object-cover">
                                                <div>
                                                    <p class="text-[12px] font-medium text-white">Vikram Singh</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">v.singh@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <span class="text-[13px] font-bold text-white">₹1,12,000</span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-4 bg-white rounded flex items-center justify-center shrink-0">
                                                    <span class="text-[#0f172a] text-[8px] font-bold">NET</span>
                                                </div>
                                                <span class="text-[11px] text-on-surface-variant">HDFC Bank</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4 text-center">
                                            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-[#10b981]/10 border border-[#10b981]/20 text-[10px] font-medium text-[#10b981]">
                                                <span class="w-1 h-1 rounded-full bg-[#10b981]"></span>
                                                Success
                                            </span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <p class="text-[11px] text-white">Yesterday</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">18:30 PM</p>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-7 h-7 rounded bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 4 -->
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <span class="font-medium text-white text-[12px] group-hover:text-primary transition-colors cursor-pointer">TXN-847288</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <a href="#" class="text-[12px] text-[#3b82f6] hover:underline">#ORD-9015</a>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-3">
                                                <div class="w-7 h-7 rounded-full bg-blue-500/20 text-blue-400 flex items-center justify-center text-[12px] font-bold shrink-0">ND</div>
                                                <div>
                                                    <p class="text-[12px] font-medium text-white">Neha Desai</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">neha.d@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <span class="text-[13px] font-bold text-white line-through opacity-50">₹45,000</span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-4 bg-white rounded flex items-center justify-center shrink-0">
                                                    <span class="text-[#0f172a] text-[8px] font-bold">UPI</span>
                                                </div>
                                                <span class="text-[11px] text-on-surface-variant">GPay</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4 text-center">
                                            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-[#ef4444]/10 border border-[#ef4444]/20 text-[10px] font-medium text-[#ef4444]">
                                                <span class="w-1 h-1 rounded-full bg-[#ef4444]"></span>
                                                Failed
                                            </span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <p class="text-[11px] text-white">Yesterday</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">14:20 PM</p>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-7 h-7 rounded bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                    <!-- Row 5 -->
                                    <tr class="hover:bg-white/5 transition-colors group">
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <span class="font-medium text-white text-[12px] group-hover:text-primary transition-colors cursor-pointer">TXN-847287</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <a href="#" class="text-[12px] text-[#3b82f6] hover:underline">#ORD-9010</a>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-3">
                                                <img src="https://i.pravatar.cc/150?img=59" alt="Avatar" class="w-7 h-7 rounded-full object-cover">
                                                <div>
                                                    <p class="text-[12px] font-medium text-white">Priya Patel</p>
                                                    <p class="text-[10px] text-on-surface-variant mt-0.5">p.patel@example.com</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4">
                                            <span class="text-[13px] font-bold text-[#f59e0b]">-₹12,500</span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center gap-2">
                                                <div class="w-6 h-4 bg-white rounded flex items-center justify-center shrink-0">
                                                    <span class="text-[#0f172a] text-[8px] font-bold italic">VISA</span>
                                                </div>
                                                <span class="text-[11px] text-on-surface-variant">**** 9091</span>
                                            </div>
                                        </td>
                                        <td class="py-4 px-4 text-center">
                                            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-[#f59e0b]/10 border border-[#f59e0b]/20 text-[10px] font-medium text-[#f59e0b]">
                                                <span class="material-symbols-outlined text-[12px]">replay</span>
                                                Refunded
                                            </span>
                                        </td>
                                        <td class="py-4 px-4">
                                            <p class="text-[11px] text-white">16 May 2024</p>
                                            <p class="text-[10px] text-on-surface-variant mt-0.5">11:05 AM</p>
                                        </td>
                                        <td class="py-4 px-4">
                                            <div class="flex items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                                <button class="w-7 h-7 rounded bg-surface-container hover:bg-white/10 flex items-center justify-center text-on-surface-variant hover:text-white transition-colors">
                                                    <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>

                                </tbody>
                            </table>
                        </div>
                        
                        <!-- Pagination -->
                        <div class="p-3 border-t border-white/5 flex items-center justify-between">
                            <p class="text-[12px] text-on-surface-variant">Showing 1 to 5 of 12,450 transactions</p>
                            <div class="flex items-center gap-1">
                                <button class="w-7 h-7 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors disabled:opacity-50">
                                    <span class="material-symbols-outlined text-[16px]">chevron_left</span>
                                </button>
                                <button class="w-7 h-7 rounded bg-[#2563eb] text-white flex items-center justify-center text-[12px] font-medium">1</button>
                                <button class="w-7 h-7 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-[12px] font-medium">2</button>
                                <button class="w-7 h-7 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-[12px] font-medium">3</button>
                                <span class="text-on-surface-variant px-1 text-[12px]">...</span>
                                <button class="w-7 h-7 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors text-[12px] font-medium">9</button>
                                <button class="w-7 h-7 rounded border border-white/10 bg-transparent flex items-center justify-center text-on-surface-variant hover:text-white hover:bg-white/5 transition-colors">
                                    <span class="material-symbols-outlined text-[16px]">chevron_right</span>
                                </button>
                                
                                <div class="relative ml-2">
                                    <select class="h-7 bg-transparent border border-white/10 rounded px-2 pr-5 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 transition-colors cursor-pointer">
                                        <option value="10">10 / page</option>
                                    </select>
                                    <span class="material-symbols-outlined absolute right-1 top-1/2 -translate-y-1/2 text-on-surface-variant pointer-events-none text-[14px]">expand_more</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="flex-1 flex flex-col gap-6">
                    
                    <!-- Payment Methods Summary -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-4 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white tracking-wider">Payment Methods</h3>
                            <button class="text-on-surface-variant hover:text-white transition-colors">
                                <span class="material-symbols-outlined text-[18px]">more_vert</span>
                            </button>
                        </div>
                        <div class="p-4 flex flex-col items-center">
                            <!-- Donut Chart -->
                            <div class="relative w-[140px] h-[140px] shrink-0 mb-6">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                                    <!-- Base Circle -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="12"></circle>
                                    <!-- UPI (Blue) ~55% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#2563eb" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="113"></circle>
                                    <!-- CC (Purple) ~30% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#8b5cf6" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="175.8" transform="rotate(198 50 50)"></circle>
                                    <!-- Net Banking (Yellow) ~15% -->
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#f59e0b" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="213.5" transform="rotate(306 50 50)"></circle>
                                </svg>
                                <div class="absolute inset-0 flex flex-col items-center justify-center">
                                    <span class="text-xs text-on-surface-variant uppercase tracking-wider mb-0.5">UPI</span>
                                    <span class="text-2xl font-bold text-white leading-tight">55%</span>
                                </div>
                            </div>
                            
                            <!-- Legend -->
                            <div class="w-full flex flex-col gap-3 text-[12px]">
                                <div class="flex items-center justify-between p-2 rounded hover:bg-white/5 transition-colors">
                                    <div class="flex items-center gap-3">
                                        <div class="w-2.5 h-2.5 rounded bg-[#2563eb]"></div>
                                        <span class="text-white font-medium">UPI</span>
                                    </div>
                                    <div class="text-right">
                                        <span class="text-white font-medium">₹7.9L</span>
                                    </div>
                                </div>
                                <div class="flex items-center justify-between p-2 rounded hover:bg-white/5 transition-colors">
                                    <div class="flex items-center gap-3">
                                        <div class="w-2.5 h-2.5 rounded bg-[#8b5cf6]"></div>
                                        <span class="text-white font-medium">Credit / Debit Card</span>
                                    </div>
                                    <div class="text-right">
                                        <span class="text-white font-medium">₹4.3L</span>
                                    </div>
                                </div>
                                <div class="flex items-center justify-between p-2 rounded hover:bg-white/5 transition-colors">
                                    <div class="flex items-center gap-3">
                                        <div class="w-2.5 h-2.5 rounded bg-[#f59e0b]"></div>
                                        <span class="text-white font-medium">Net Banking</span>
                                    </div>
                                    <div class="text-right">
                                        <span class="text-white font-medium">₹2.3L</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Revenue Trend Mini Chart -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-4 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white tracking-wider">Revenue Trend</h3>
                            <span class="text-[10px] text-on-surface-variant">Last 7 Days</span>
                        </div>
                        <div class="p-4 flex flex-col h-[140px] relative">
                            <!-- SVG Line Graph -->
                            <svg class="absolute inset-0 w-full h-full pt-4 px-2 overflow-visible" preserveAspectRatio="none">
                                <defs>
                                    <linearGradient id="gradient-blue" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="0%" stop-color="#2563eb" stop-opacity="0.3"></stop>
                                        <stop offset="100%" stop-color="#2563eb" stop-opacity="0"></stop>
                                    </linearGradient>
                                </defs>
                                <path d="M 0,80 L 40,75 L 80,40 L 120,60 L 160,20 L 200,30 L 240,10 L 280,35 L 280,100 L 0,100 Z" fill="url(#gradient-blue)" stroke="none"></path>
                                <path d="M 0,80 L 40,75 L 80,40 L 120,60 L 160,20 L 200,30 L 240,10 L 280,35" fill="none" stroke="#2563eb" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="drop-shadow-[0_2px_4px_rgba(37,99,235,0.4)]"></path>
                            </svg>
                        </div>
                    </div>
                    
                    <!-- Recent Refunds -->
                    <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 overflow-hidden flex flex-col">
                        <div class="p-4 border-b border-white/5 flex justify-between items-center">
                            <h3 class="text-sm font-bold text-white tracking-wider">Recent Refunds</h3>
                        </div>
                        <div class="p-2 flex flex-col gap-1 text-[12px]">
                            <a href="#" class="flex items-center justify-between p-2 rounded hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-[#f59e0b]/10 text-[#f59e0b] flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-[16px]">replay</span>
                                    </div>
                                    <div>
                                        <p class="font-medium text-white group-hover:text-primary transition-colors">#ORD-9010</p>
                                        <p class="text-[10px] text-on-surface-variant">Priya Patel</p>
                                    </div>
                                </div>
                                <span class="font-bold text-[#f59e0b]">-₹12,500</span>
                            </a>
                            <a href="#" class="flex items-center justify-between p-2 rounded hover:bg-white/5 transition-colors group">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-[#f59e0b]/10 text-[#f59e0b] flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-[16px]">replay</span>
                                    </div>
                                    <div>
                                        <p class="font-medium text-white group-hover:text-primary transition-colors">#ORD-8942</p>
                                        <p class="text-[10px] text-on-surface-variant">Arjun Reddy</p>
                                    </div>
                                </div>
                                <span class="font-bold text-[#f59e0b]">-₹5,200</span>
                            </a>
                        </div>
                        <a href="#" class="p-3 text-center border-t border-white/5 text-[11px] font-medium text-primary hover:bg-white/5 transition-colors">
                            View All Refunds
                        </a>
                    </div>

                </div>
            </div>
        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{payments_content}</main>', base_html)
    
    # Update active state in sidebar
    new_html = new_html.replace('href="admin-payments.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary"', 
                                'href="admin-payments.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 bg-primary/10 text-primary"')
    

    with open('admin-payments.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Successfully generated admin-payments.html")

if __name__ == '__main__':
    generate_admin_payments()
