"""
Fix: Replace the broken plain <a> Customers nav item with the proper <details> submenu
across all admin HTML pages that are missing it.
"""

import os
import re

PAGES_DIR = r"c:\Projects\MakeMyPC"

# The broken plain-link pattern (no submenu)
BROKEN_CUSTOMERS = '''\
        <a href="#" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary">
            <span class="material-symbols-outlined">group</span>
            <span class="text-body-sm font-medium">Customers</span>
        </a>'''

# The correct <details> submenu (non-active state — used on pages that are NOT in the Customers section)
CORRECT_CUSTOMERS = '''\
        <details class="group" name="sidebar-menu">
            <summary class="flex items-center justify-between px-4 py-3 rounded-xl cursor-pointer transition-all duration-300 text-on-surface-variant hover:bg-white/5 hover:text-primary list-none [&::-webkit-details-marker]:hidden">
                <div class="flex items-center gap-3">
                    <span class="material-symbols-outlined">group</span>
                    <span class="text-body-sm font-medium">Customers</span>
                </div>
                <span class="material-symbols-outlined text-[18px] transition-transform duration-300 group-open:rotate-180">expand_more</span>
            </summary>
            <div class="ml-6 pl-4 border-l border-white/10 flex flex-col space-y-1 mt-1 mb-2">
                <a href="admin-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    All Customers
                </a>
                <a href="admin-customer-groups.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Customer Groups
                </a>
                <a href="admin-saved-builds.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Saved Builds
                </a>
                <a href="admin-addresses.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Addresses
                </a>
                <a href="admin-wishlist.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Wishlist
                </a>
                <a href="admin-order-history.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Order History
                </a>
                <a href="admin-support-tickets.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Support Tickets
                </a>
                <a href="admin-loyalty-rewards.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Loyalty &amp; Rewards
                </a>
                <a href="admin-activity-logs.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Activity Logs
                </a>
                <a href="admin-email-notifications.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Email &amp; Notifications
                </a>
                <a href="admin-blocked-customers.html" class="text-sm text-on-surface-variant hover:text-white px-4 py-2 rounded-lg transition-colors block">
                    Blocked Customers
                </a>
            </div>
        </details>'''

fixed_files = []
skipped_files = []

for fname in os.listdir(PAGES_DIR):
    if not (fname.startswith("admin-") and fname.endswith(".html")):
        continue

    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if BROKEN_CUSTOMERS in content:
        new_content = content.replace(BROKEN_CUSTOMERS, CORRECT_CUSTOMERS, 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_files.append(fname)
        print(f"  [FIXED] {fname}")
    else:
        skipped_files.append(fname)

print(f"\nDone. Fixed {len(fixed_files)} file(s).")
if fixed_files:
    print("Fixed files:")
    for f in fixed_files:
        print(f"  - {f}")
if skipped_files:
    print(f"\nSkipped {len(skipped_files)} file(s) (already correct or no match):")
    for f in skipped_files:
        print(f"  - {f}")
