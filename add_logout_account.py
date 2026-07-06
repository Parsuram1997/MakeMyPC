import sys

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = """                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('saved')">
                        <span class="material-symbols-outlined">favorite</span>
                        <span class="font-headline-sm text-headline-sm">Saved Items</span>
                    </button>
                </nav>"""

new_block = """                    <button class="tab-btn w-full flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick="switchTab('saved')">
                        <span class="material-symbols-outlined">favorite</span>
                        <span class="font-headline-sm text-headline-sm">Saved Items</span>
                    </button>
                    
                    <button class="w-full flex items-center gap-3 px-4 py-3 mt-4 rounded-lg text-error hover:bg-error/10 transition-all border border-error/20" onclick="window.logoutUser(event)">
                        <span class="material-symbols-outlined">logout</span>
                        <span class="font-headline-sm text-headline-sm">Logout</span>
                    </button>
                </nav>"""

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('account-settings.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Logout button added to account-settings.html")
else:
    print("Could not find the target block in account-settings.html.")
