import sys

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_address_section = """<!-- Address Section (Placeholder) -->
<div class="section-content hidden animate-in fade-in slide-in-from-bottom-4 duration-500" id="section-address">
<h1 class="font-headline-lg text-headline-lg mb-6">Address Book</h1>
<div class="glass-card rounded-xl p-8 text-center text-outline">
    <span class="material-symbols-outlined text-4xl mb-4 opacity-50">location_on</span>
    <p>No addresses saved yet.</p>
</div>
</div>"""

new_address_section = """<!-- Address Section -->
<div class="section-content hidden animate-in fade-in slide-in-from-bottom-4 duration-500" id="section-address">
<div class="flex justify-between items-center mb-6">
    <h1 class="font-headline-lg text-headline-lg">Address Book</h1>
    <button id="add-address-btn" class="bg-electric-blue text-white px-4 py-2 rounded-lg font-bold hover:shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:bg-blue-600 active:scale-95 transition-all text-sm flex items-center gap-2">
        <span class="material-symbols-outlined text-sm">add</span> Add New Address
    </button>
</div>

<!-- Address List Container -->
<div id="address-list-container" class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <!-- Rendered addresses will go here -->
    <div id="no-address-state" class="col-span-1 md:col-span-2 glass-card rounded-xl p-8 text-center text-outline">
        <span class="material-symbols-outlined text-4xl mb-4 opacity-50">location_on</span>
        <p>No addresses saved yet.</p>
    </div>
</div>

<!-- Add Address Form (Hidden by default) -->
<div id="add-address-form-container" class="glass-card rounded-xl p-6 mt-6 hidden">
    <h2 class="font-headline-md text-headline-md mb-6">Add New Address</h2>
    <form id="address-form" class="space-y-6">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Full Name</label>
                <input id="addr-name" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder="John Doe"/>
            </div>
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Phone Number</label>
                <input id="addr-phone" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="tel" placeholder="10-digit mobile number"/>
            </div>
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Pincode</label>
                <input id="addr-pincode" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder="6 digits [0-9] PIN code"/>
            </div>
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">State</label>
                <input id="addr-state" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder="e.g. Maharashtra"/>
            </div>
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">City</label>
                <input id="addr-city" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder="e.g. Mumbai"/>
            </div>
            <div class="space-y-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Address Type</label>
                <div class="relative">
                    <select id="addr-type" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none appearance-none text-sm text-on-surface">
                        <option value="Home" class="bg-surface-deep text-on-surface">Home (All day delivery)</option>
                        <option value="Work" class="bg-surface-deep text-on-surface">Work (Delivery between 10 AM - 5 PM)</option>
                    </select>
                    <span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-outline">expand_more</span>
                </div>
            </div>
            <div class="space-y-2 sm:col-span-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">House No., Building Name</label>
                <input id="addr-house" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder=""/>
            </div>
            <div class="space-y-2 sm:col-span-2">
                <label class="text-label-mono font-label-mono text-outline uppercase tracking-widest text-[10px]">Road name, Area, Colony</label>
                <input id="addr-area" required class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" placeholder=""/>
            </div>
        </div>
        <div class="flex gap-4 border-t border-white/10 pt-6">
            <button type="submit" id="save-address-btn" class="bg-electric-blue text-white px-6 py-2.5 rounded-lg font-bold hover:shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:bg-blue-600 active:scale-95 transition-all text-sm flex items-center justify-center gap-2"><span>Save Address</span></button>
            <button type="button" id="cancel-address-btn" class="bg-white/5 border border-white/10 text-white px-6 py-2.5 rounded-lg font-bold hover:bg-white/10 active:scale-95 transition-all text-sm">Cancel</button>
        </div>
    </form>
</div>
</div>"""

if "<!-- Address Section (Placeholder) -->" in text:
    text = text.replace(old_address_section, new_address_section)

# Inject address.js script if not present
if '<script src="js/address.js" type="module"></script>' not in text:
    text = text.replace('</body>', '<script src="js/address.js" type="module"></script>\n</body>')

with open('account-settings.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("account-settings.html updated with Address Book UI.")
