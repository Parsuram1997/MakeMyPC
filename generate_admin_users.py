import os
import glob
import re

def update_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add USER MANAGEMENT section if it doesn't exist
    user_management_check = r'User Management'
    if not re.search(user_management_check, content):
        admin_users_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-[^>]*>\s*<span class="material-symbols-outlined">admin_panel_settings</span>\s*<span class="text-body-sm font-medium">Admin Users</span>\s*</a>'
        new_user_management = """
        <div class="px-4 mt-6 mb-2">
            <p class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">User Management</p>
        </div>
        <a href="admin-users.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">manage_accounts</span>
            <span class="text-body-sm font-medium">Admin Users</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">shield_person</span>
            <span class="text-body-sm font-medium">Roles & Permissions</span>
        </a>
"""
        content = re.sub(admin_users_pattern, new_user_management, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_admin_users_page():
    base_file = 'admin-dashboard.html'
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()

    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    users_content = """
        <div class="flex flex-col relative w-full">
            
            <!-- Header -->
            <div class="flex justify-between items-end mb-8 relative z-10">
                <div>
                    <h2 class="text-2xl font-bold text-white mb-1">Admin Users</h2>
                    <p class="text-on-surface-variant text-sm">Manage admin users, roles, and permissions.</p>
                </div>
                <div>
                    <button class="bg-primary hover:bg-primary-hover text-on-primary px-4 py-2 rounded-lg text-sm font-medium transition-colors flex items-center gap-2">
                        <span class="material-symbols-outlined text-[18px]">add</span>
                        Add Admin User
                    </button>
                </div>
            </div>

            <!-- Stats Row -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8 relative z-10">
                <!-- Total Users -->
                <div class="glass-card p-6 rounded-xl border border-white/5 bg-surface-container/30 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#0066FF]/10 text-[#0066FF] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">group</span>
                    </div>
                    <div>
                        <p class="text-xs text-on-surface-variant font-medium mb-1">Total Admin Users</p>
                        <p class="text-xl font-bold text-white mb-0.5">24</p>
                        <p class="text-[10px] text-on-surface-variant">All admin accounts</p>
                    </div>
                </div>

                <!-- Active Users -->
                <div class="glass-card p-6 rounded-xl border border-white/5 bg-surface-container/30 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#00D084]/10 text-[#00D084] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">verified_user</span>
                    </div>
                    <div>
                        <p class="text-xs text-on-surface-variant font-medium mb-1">Active Users</p>
                        <p class="text-xl font-bold text-white mb-0.5">21</p>
                        <p class="text-[10px] text-on-surface-variant">Currently active</p>
                    </div>
                </div>

                <!-- Inactive Users -->
                <div class="glass-card p-6 rounded-xl border border-white/5 bg-surface-container/30 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#FF9800]/10 text-[#FF9800] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">person_off</span>
                    </div>
                    <div>
                        <p class="text-xs text-on-surface-variant font-medium mb-1">Inactive Users</p>
                        <p class="text-xl font-bold text-white mb-0.5">3</p>
                        <p class="text-[10px] text-on-surface-variant">Currently inactive</p>
                    </div>
                </div>

                <!-- Super Admins -->
                <div class="glass-card p-6 rounded-xl border border-white/5 bg-surface-container/30 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-lg bg-[#9C27B0]/10 text-[#9C27B0] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[24px]">lock_person</span>
                    </div>
                    <div>
                        <p class="text-xs text-on-surface-variant font-medium mb-1">Super Admins</p>
                        <p class="text-xl font-bold text-white mb-0.5">2</p>
                        <p class="text-[10px] text-on-surface-variant">Full access users</p>
                    </div>
                </div>
            </div>

            <!-- Table Section -->
            <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col relative z-10 overflow-hidden mb-8">
                <!-- Filters -->
                <div class="p-4 border-b border-white/5 flex items-center gap-4">
                    <div class="relative flex-1 max-w-[280px]">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]">search</span>
                        <input type="text" placeholder="Search by name, email or phone..." class="w-full bg-surface-deep/50 border border-white/5 rounded-lg pl-10 pr-4 py-2 text-[12px] text-white focus:outline-none focus:border-primary/50 transition-colors placeholder:text-on-surface-variant">
                    </div>
                    
                    <div class="relative w-40">
                        <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-3 py-2 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                            <option>All Roles</option>
                            <option>Super Admin</option>
                            <option>Inventory Admin</option>
                            <option>Order Admin</option>
                        </select>
                        <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[16px] text-on-surface-variant pointer-events-none">expand_more</span>
                    </div>
                    
                    <div class="relative w-40">
                        <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-3 py-2 text-[12px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                            <option>All Status</option>
                            <option>Active</option>
                            <option>Inactive</option>
                        </select>
                        <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[16px] text-on-surface-variant pointer-events-none">expand_more</span>
                    </div>

                    <button class="bg-surface-deep/50 border border-white/5 hover:bg-white/5 text-white px-3 py-2 rounded-lg text-[12px] font-medium transition-colors flex items-center gap-2">
                        <span class="material-symbols-outlined text-[16px]">filter_list</span>
                        Filters
                    </button>
                    
                    <button class="text-primary hover:text-primary-hover text-[12px] font-medium transition-colors">Reset</button>
                </div>

                <!-- Table -->
                <div class="overflow-x-auto flex-1">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-white/5 bg-white/[0.02]">
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">User</th>
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">Email</th>
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">Role</th>
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">Status</th>
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">Last Login</th>
                                <th class="px-4 py-3 text-[10px] font-bold text-on-surface-variant uppercase tracking-wider text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-white/5">
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#0066FF] text-white flex items-center justify-center font-bold text-xs shrink-0">AD</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Admin User</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">admin@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#0066FF]/10 text-[#0066FF]">Super Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                        <span class="text-[11px] text-[#00D084]">Active</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">20 May 2024, 10:30 AM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#00D084]/20 text-[#00D084] flex items-center justify-center font-bold text-xs shrink-0">RK</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Rohit Kumar</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">rohit.kumar@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#03A9F4]/10 text-[#03A9F4]">Inventory Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                        <span class="text-[11px] text-[#00D084]">Active</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">19 May 2024, 04:15 PM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#FF9800]/20 text-[#FF9800] flex items-center justify-center font-bold text-xs shrink-0">PS</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Pooja Sharma</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">pooja.sharma@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#00D084]/10 text-[#00D084]">Order Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                        <span class="text-[11px] text-[#00D084]">Active</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">18 May 2024, 09:20 AM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#9C27B0]/20 text-[#9C27B0] flex items-center justify-center font-bold text-xs shrink-0">AS</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Amit Singh</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">amit.singh@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#E91E63]/10 text-[#E91E63]">Customer Support</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                        <span class="text-[11px] text-[#00D084]">Active</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">17 May 2024, 03:45 PM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#00D084]/20 text-[#00D084] flex items-center justify-center font-bold text-xs shrink-0">NV</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Neha Verma</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">neha.verma@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#FF9800]/10 text-[#FF9800]">Marketing Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#F44336]"></span>
                                        <span class="text-[11px] text-[#F44336]">Inactive</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">10 May 2024, 11:20 AM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#0066FF]/20 text-[#0066FF] flex items-center justify-center font-bold text-xs shrink-0">MJ</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Manoj Jha</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">manoj.jha@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#9C27B0]/10 text-[#9C27B0]">Finance Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span>
                                        <span class="text-[11px] text-[#00D084]">Active</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">16 May 2024, 02:10 PM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            
                            <tr class="hover:bg-white/[0.02] transition-colors group">
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-[#FF9800]/20 text-[#FF9800] flex items-center justify-center font-bold text-xs shrink-0">SK</div>
                                        <div>
                                            <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Sanjay Kumar</p>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[12px] text-on-surface-variant">sanjay.kumar@makemypc.com</td>
                                <td class="px-4 py-3">
                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium bg-[#E91E63]/10 text-[#E91E63]">Warehouse Admin</span>
                                </td>
                                <td class="px-4 py-3">
                                    <div class="flex items-center gap-1.5">
                                        <span class="w-1.5 h-1.5 rounded-full bg-[#F44336]"></span>
                                        <span class="text-[11px] text-[#F44336]">Inactive</span>
                                    </div>
                                </td>
                                <td class="px-4 py-3 text-[11px] text-on-surface-variant">08 May 2024, 06:30 PM</td>
                                <td class="px-4 py-3 text-right">
                                    <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">edit</span>
                                        </button>
                                        <button class="w-7 h-7 rounded bg-white/5 hover:bg-white/10 text-on-surface-variant flex items-center justify-center transition-colors">
                                            <span class="material-symbols-outlined text-[14px]">more_horiz</span>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Pagination -->
                <div class="p-4 border-t border-white/5 flex items-center justify-between">
                    <p class="text-[11px] text-on-surface-variant">Showing 1 to 7 of 24 users</p>
                    <div class="flex items-center gap-2">
                        <button class="w-8 h-8 rounded flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors disabled:opacity-50">
                            <span class="material-symbols-outlined text-[18px]">chevron_left</span>
                        </button>
                        <button class="w-8 h-8 rounded flex items-center justify-center bg-primary text-white text-[12px] font-medium transition-colors">1</button>
                        <button class="w-8 h-8 rounded flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-[12px] font-medium transition-colors">2</button>
                        <button class="w-8 h-8 rounded flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-[12px] font-medium transition-colors">3</button>
                        <span class="text-on-surface-variant px-1">...</span>
                        <button class="w-8 h-8 rounded flex items-center justify-center text-on-surface-variant hover:bg-white/5 hover:text-white text-[12px] font-medium transition-colors">4</button>
                        <button class="w-8 h-8 rounded flex items-center justify-center text-on-surface-variant hover:bg-white/5 transition-colors">
                            <span class="material-symbols-outlined text-[18px]">chevron_right</span>
                        </button>
                        
                        <div class="relative ml-2 w-24">
                            <select class="w-full bg-surface-deep/50 border border-white/5 rounded-lg px-2 py-1.5 text-[11px] text-white appearance-none focus:outline-none focus:border-primary/50 cursor-pointer">
                                <option>10 / page</option>
                                <option>25 / page</option>
                                <option>50 / page</option>
                            </select>
                            <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[14px] text-on-surface-variant pointer-events-none">expand_more</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Bottom Section (3 Columns) -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 relative z-10">
                <!-- Role Distribution -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col">
                    <div class="p-6 border-b border-white/5">
                        <h3 class="text-sm font-medium text-white">Role Distribution</h3>
                    </div>
                    <div class="p-6 flex items-center gap-6 flex-1">
                        <!-- Donut Chart Approximation -->
                        <div class="relative w-32 h-32 shrink-0 flex items-center justify-center">
                            <!-- SVG Donut Chart -->
                            <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                                <!-- Background Circle -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(255,255,255,0.05)" stroke-width="12"></circle>
                                
                                <!-- Segments (Approximation) -->
                                <!-- Warehouse Admin (8.3%) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#E91E63" stroke-width="12" stroke-dasharray="25.1 251.2" stroke-dashoffset="0"></circle>
                                <!-- Finance Admin (8.3%) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#9C27B0" stroke-width="12" stroke-dasharray="25.1 251.2" stroke-dashoffset="-25.1"></circle>
                                <!-- Marketing Admin (12.5%) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#FF9800" stroke-width="12" stroke-dasharray="37.7 251.2" stroke-dashoffset="-50.2"></circle>
                                <!-- Customer Support (16.7%) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#00D084" stroke-width="12" stroke-dasharray="50.2 251.2" stroke-dashoffset="-87.9"></circle>
                                <!-- Order Admin (20.8%) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#03A9F4" stroke-width="12" stroke-dasharray="62.8 251.2" stroke-dashoffset="-138.1"></circle>
                                <!-- Super Admin (8.3%) (Actually 2 users is 8.3%, but screenshot shows it as the blue segment, wait. Let's just draw some segments) -->
                                <circle cx="50" cy="50" r="40" fill="transparent" stroke="#0066FF" stroke-width="12" stroke-dasharray="50.2 251.2" stroke-dashoffset="-200.9"></circle>
                            </svg>
                            <div class="absolute inset-0 flex flex-col items-center justify-center">
                                <span class="text-xl font-bold text-white">24</span>
                                <span class="text-[10px] text-on-surface-variant">Total</span>
                            </div>
                        </div>
                        
                        <!-- Legend -->
                        <div class="flex-1 flex flex-col gap-2">
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#0066FF]"></span><span class="text-white">Super Admin</span></div>
                                <span class="text-on-surface-variant">2 (8.3%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#03A9F4]"></span><span class="text-white">Inventory Admin</span></div>
                                <span class="text-on-surface-variant">6 (25%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#00D084]"></span><span class="text-white">Order Admin</span></div>
                                <span class="text-on-surface-variant">5 (20.8%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#FFC107]"></span><span class="text-white">Customer Support</span></div>
                                <span class="text-on-surface-variant">4 (16.7%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#FF9800]"></span><span class="text-white">Marketing Admin</span></div>
                                <span class="text-on-surface-variant">3 (12.5%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#9C27B0]"></span><span class="text-white">Finance Admin</span></div>
                                <span class="text-on-surface-variant">2 (8.3%)</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px]">
                                <div class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-[#E91E63]"></span><span class="text-white">Warehouse Admin</span></div>
                                <span class="text-on-surface-variant">2 (8.3%)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Recent Activity -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col">
                    <div class="p-6 border-b border-white/5 flex items-center justify-between">
                        <h3 class="text-sm font-medium text-white">Recent Activity</h3>
                        <a href="#" class="text-[11px] text-primary hover:text-primary-hover font-medium transition-colors">View All</a>
                    </div>
                    <div class="p-4 flex flex-col gap-1 flex-1">
                        <!-- Activity 1 -->
                        <div class="flex items-start gap-3 p-3 rounded-lg hover:bg-white/[0.02] transition-colors">
                            <div class="w-7 h-7 rounded bg-white/5 text-on-surface-variant flex items-center justify-center mt-0.5 shrink-0">
                                <span class="material-symbols-outlined text-[16px]">manage_accounts</span>
                            </div>
                            <div class="flex-1">
                                <div class="flex items-start justify-between gap-2 mb-0.5">
                                    <p class="text-[12px] font-medium text-white">Rohit Kumar</p>
                                    <span class="text-[10px] text-on-surface-variant shrink-0">20 May 2024, 10:30 AM</span>
                                </div>
                                <p class="text-[11px] text-on-surface-variant">Updated product permissions</p>
                            </div>
                        </div>
                        
                        <!-- Activity 2 -->
                        <div class="flex items-start gap-3 p-3 rounded-lg hover:bg-white/[0.02] transition-colors">
                            <div class="w-7 h-7 rounded bg-white/5 text-on-surface-variant flex items-center justify-center mt-0.5 shrink-0">
                                <span class="material-symbols-outlined text-[16px]">person_add</span>
                            </div>
                            <div class="flex-1">
                                <div class="flex items-start justify-between gap-2 mb-0.5">
                                    <p class="text-[12px] font-medium text-white">Pooja Sharma</p>
                                    <span class="text-[10px] text-on-surface-variant shrink-0">19 May 2024, 04:15 PM</span>
                                </div>
                                <p class="text-[11px] text-on-surface-variant">Added new admin user</p>
                            </div>
                        </div>
                        
                        <!-- Activity 3 -->
                        <div class="flex items-start gap-3 p-3 rounded-lg hover:bg-white/[0.02] transition-colors">
                            <div class="w-7 h-7 rounded bg-white/5 text-on-surface-variant flex items-center justify-center mt-0.5 shrink-0">
                                <span class="material-symbols-outlined text-[16px]">manage_accounts</span>
                            </div>
                            <div class="flex-1">
                                <div class="flex items-start justify-between gap-2 mb-0.5">
                                    <p class="text-[12px] font-medium text-white">Amit Singh</p>
                                    <span class="text-[10px] text-on-surface-variant shrink-0">18 May 2024, 11:20 AM</span>
                                </div>
                                <p class="text-[11px] text-on-surface-variant">Updated role permissions</p>
                            </div>
                        </div>
                        
                        <!-- Activity 4 -->
                        <div class="flex items-start gap-3 p-3 rounded-lg hover:bg-white/[0.02] transition-colors">
                            <div class="w-7 h-7 rounded bg-[#F44336]/10 text-[#F44336] flex items-center justify-center mt-0.5 shrink-0">
                                <span class="material-symbols-outlined text-[16px]">person_remove</span>
                            </div>
                            <div class="flex-1">
                                <div class="flex items-start justify-between gap-2 mb-0.5">
                                    <p class="text-[12px] font-medium text-white">Admin User</p>
                                    <span class="text-[10px] text-on-surface-variant shrink-0">17 May 2024, 09:10 PM</span>
                                </div>
                                <p class="text-[11px] text-on-surface-variant">Deleted admin user account</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Quick Actions -->
                <div class="glass-card rounded-xl border border-white/5 bg-surface-container/30 flex flex-col">
                    <div class="p-6 border-b border-white/5">
                        <h3 class="text-sm font-medium text-white">Quick Actions</h3>
                    </div>
                    <div class="p-4 flex flex-col gap-1 flex-1">
                        <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded bg-white/5 text-on-surface-variant flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-[18px]">person_add</span>
                                </div>
                                <div>
                                    <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Add New Admin User</p>
                                    <p class="text-[10px] text-on-surface-variant">Create a new admin account</p>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-primary transition-colors">chevron_right</span>
                        </a>
                        
                        <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded bg-white/5 text-on-surface-variant flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-[18px]">shield_person</span>
                                </div>
                                <div>
                                    <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Roles & Permissions</p>
                                    <p class="text-[10px] text-on-surface-variant">Manage roles and access</p>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-primary transition-colors">chevron_right</span>
                        </a>
                        
                        <a href="admin-activity-logs.html" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded bg-white/5 text-on-surface-variant flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-[18px]">history</span>
                                </div>
                                <div>
                                    <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Admin Activity Logs</p>
                                    <p class="text-[10px] text-on-surface-variant">View admin activity history</p>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-primary transition-colors">chevron_right</span>
                        </a>
                        
                        <a href="#" class="flex items-center justify-between p-3 rounded-lg hover:bg-white/5 transition-colors group">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded bg-white/5 text-on-surface-variant flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-[18px]">download</span>
                                </div>
                                <div>
                                    <p class="text-[12px] font-medium text-white group-hover:text-primary transition-colors">Export Admin List</p>
                                    <p class="text-[10px] text-on-surface-variant">Download admin users list</p>
                                </div>
                            </div>
                            <span class="material-symbols-outlined text-[16px] text-on-surface-variant group-hover:text-primary transition-colors">chevron_right</span>
                        </a>
                    </div>
                </div>
            </div>

        </div>
"""
    
    new_html = main_pattern.sub(f'<main class="ml-64 flex-1 p-6 h-screen overflow-y-auto custom-scrollbar bg-surface-deep flex flex-col pb-24">{users_content}</main>', base_html)
    
    # Let's ensure the sidebar has the updated "USER MANAGEMENT" active link for this specific page
    # Since we updated all files to have the new user management links, we will find it in this new_html
    # and mark "Admin Users" as active.
    
    # We first replace the old Admin Users if it's there
    old_admin_users_pattern = r'<a href="[^"]*" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-[^>]*>\s*<span class="material-symbols-outlined">admin_panel_settings</span>\s*<span class="text-body-sm font-medium">Admin Users</span>\s*</a>'
    new_user_management = """
        <div class="px-4 mt-6 mb-2">
            <p class="text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">User Management</p>
        </div>
        <a href="admin-users.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-white bg-primary">
            <span class="material-symbols-outlined">manage_accounts</span>
            <span class="text-body-sm font-medium">Admin Users</span>
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">shield_person</span>
            <span class="text-body-sm font-medium">Roles & Permissions</span>
        </a>
"""
    
    if re.search(old_admin_users_pattern, new_html):
        new_html = re.sub(old_admin_users_pattern, new_user_management, new_html)
    else:
        # If it was already updated by update_sidebar, let's just make it active
        user_management_inactive = r'<a href="admin-users.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">\s*<span class="material-symbols-outlined">manage_accounts</span>\s*<span class="text-body-sm font-medium">Admin Users</span>\s*</a>'
        user_management_active = """<a href="admin-users.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-white bg-primary">
            <span class="material-symbols-outlined">manage_accounts</span>
            <span class="text-body-sm font-medium">Admin Users</span>
        </a>"""
        if re.search(user_management_inactive, new_html):
            new_html = re.sub(user_management_inactive, user_management_active, new_html)

    # Deactivate dashboard
    dashboard_active = r'<a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-white bg-primary">'
    dashboard_inactive = '<a href="admin-dashboard.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">'
    
    if re.search(dashboard_active, new_html):
        new_html = re.sub(dashboard_active, dashboard_inactive, new_html)

    with open('admin-users.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Created admin-users.html")

def main():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        if filepath != 'admin-users.html':
            update_sidebar(filepath)
            print(f"Updated sidebar in {filepath}")
            
    generate_admin_users_page()

if __name__ == '__main__':
    main()
