"""
Fix remaining pages with unique sidebar structures.
Each page has different sidebar HTML, so we fix each precisely.
"""

import os, re

PAGES_DIR = r"c:\Projects\MakeMyPC"

def fix_file(fname, fixes):
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    for old, new in fixes:
        content = content.replace(old, new)
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [FIXED] {fname}")
    else:
        print(f"  [NO CHANGE] {fname}")
    return content

# ── 1. compatibility-manager.html
# Only issue: mb-8 in logo div (py-3 is in a search input, not nav item - leave it)
fix_file("compatibility-manager.html", [
    ('<div class="px-6 mb-8">', '<div class="px-6 mb-4">'),
])

# ── 2. account-settings.html
# Has a tab-button sidebar (not admin nav), gap-2 -> gap-0.5, py-3 on buttons -> py-2
fix_file("account-settings.html", [
    # nav gap
    ('class="flex flex-col gap-2"', 'class="flex flex-col gap-0.5"'),
    # tab buttons py-3 -> py-2
    ('gap-3 px-4 py-3 rounded-lg text-electric-blue bg-white/5 border-l-2 border-electric-blue font-bold',
     'gap-3 px-4 py-2 rounded-lg text-electric-blue bg-white/5 border-l-2 border-electric-blue font-bold'),
    ('gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick',
     'gap-3 px-4 py-2 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" onclick'),
    # admin link and logout button
    ('gap-3 px-4 py-3 mt-2 rounded-lg text-green-500',
     'gap-3 px-4 py-2 mt-1 rounded-lg text-green-500'),
    ('gap-3 px-4 py-3 mt-2 rounded-lg text-error',
     'gap-3 px-4 py-2 mt-1 rounded-lg text-error'),
])

# ── 3. compare-products.html
# Has a right-panel aside (not nav sidebar), gap-2 is in nav inside it
fix_file("compare-products.html", [
    ('class="flex flex-col gap-2">', 'class="flex flex-col gap-0.5">'),
])

# ── 4. my-builds.html
# Has its own aside with gap-2, py-6, py-3
fix_file("my-builds.html", [
    # aside gap-2 -> gap-1
    ('h-screen w-64 fixed left-0 top-0 pt-20 bg-surface-container-low border-r border-white/5 flex flex-col gap-2 p-4',
     'h-screen w-64 fixed left-0 top-0 pt-20 bg-surface-container-low border-r border-white/5 flex flex-col gap-0.5 p-4'),
    # py-6 in header div
    ('class="px-4 py-6 mb-4"', 'class="px-4 py-3 mb-2"'),
    # nav links py-3 -> py-1.5
    ('gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all active:translate-x-1',
     'gap-3 px-4 py-1.5 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all active:translate-x-1'),
    # active link py-3
    ('gap-3 px-4 py-3 rounded-lg bg-electric-blue/10 text-electric-blue border-r-4',
     'gap-3 px-4 py-1.5 rounded-lg bg-electric-blue/10 text-electric-blue border-r-4'),
    # bottom links
    ('gap-3 px-4 py-3 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" href',
     'gap-3 px-4 py-1.5 rounded-lg text-on-surface-variant hover:bg-white/5 transition-all" href'),
    ('gap-3 px-4 py-3 rounded-lg text-error',
     'gap-3 px-4 py-1.5 rounded-lg text-error'),
    # bottom button
    ('class="mt-auto flex flex-col gap-2 border-t',
     'class="mt-auto flex flex-col gap-1 border-t'),
])

# ── 5. submit-ticket.html
fix_file("submit-ticket.html", [
    ('<div class="mb-8 px-2">', '<div class="mb-4 px-2">'),
    # nav links py-2 -> py-1.5 (space-y-2 -> space-y-1)
    ('class="flex-1 space-y-2"', 'class="flex-1 space-y-1"'),
    ('space-x-3 px-3 py-2 rounded-lg text-on-surface-variant hover:text-primary-fixed-dim',
     'space-x-3 px-3 py-1.5 rounded-lg text-on-surface-variant hover:text-primary-fixed-dim'),
])

print("\nAll remaining pages processed.")
