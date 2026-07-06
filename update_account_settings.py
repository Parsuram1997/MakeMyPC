import sys
import re

with open('account-settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add IDs to inputs
text = text.replace(
    'class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text" value="Alex Vandal"',
    'id="profile-name" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="text"'
)

text = text.replace(
    'class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="email" value="alex.vandal@techforge.io"',
    'id="profile-email" readonly class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm cursor-not-allowed opacity-50" type="email"'
)

text = text.replace(
    'class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="tel" value="+91 98765 43210"',
    'id="profile-phone" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm" type="tel"'
)

text = text.replace(
    '<select class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none appearance-none text-sm text-on-surface">',
    '<select id="profile-location" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none appearance-none text-sm text-on-surface">'
)

text = text.replace(
    '<textarea class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm resize-y" rows="3">PC enthusiast & builder. Love crafting high performance setups!</textarea>',
    '<textarea id="profile-bio" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue/50 transition-colors outline-none text-sm resize-y" rows="3"></textarea>'
)

text = text.replace(
    '<button class="text-electric-blue text-xs font-bold hover:underline">Change Photo</button>',
    '<button id="profile-photo-btn" class="text-electric-blue text-xs font-bold hover:underline">Change Photo</button>\n<input type="file" id="profile-photo-input" accept="image/png, image/jpeg, image/webp" class="hidden" />'
)

text = text.replace(
    '<img class="w-full h-full object-cover rounded-full group-hover:opacity-80 transition-opacity"',
    '<img id="profile-img" class="w-full h-full object-cover rounded-full group-hover:opacity-80 transition-opacity"'
)

text = text.replace(
    '<button class="absolute bottom-1 right-1 bg-electric-blue text-white p-2 rounded-full shadow-lg hover:scale-110 transition-transform">',
    '<button id="profile-photo-btn-icon" class="absolute bottom-1 right-1 bg-electric-blue text-white p-2 rounded-full shadow-lg hover:scale-110 transition-transform">'
)

text = text.replace(
    '<button class="bg-electric-blue text-white px-6 py-2.5 rounded-lg font-bold hover:shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:bg-blue-600 active:scale-95 transition-all text-sm">Save Changes</button>',
    '<button id="profile-save-btn" class="bg-electric-blue text-white px-6 py-2.5 rounded-lg font-bold hover:shadow-[0_0_20px_rgba(0,122,255,0.4)] hover:bg-blue-600 active:scale-95 transition-all text-sm flex items-center justify-center gap-2"><span>Save Changes</span></button>'
)

text = text.replace(
    '<h3 class="font-headline-lg text-headline-lg text-3xl font-bold">Alex Vandal</h3>',
    '<h3 id="profile-display-name" class="font-headline-lg text-headline-lg text-3xl font-bold">Alex Vandal</h3>'
)

# Add profile script at the end
if '<script src="js/profile.js" type="module"></script>' not in text:
    text = text.replace('</body>', '<script src="js/profile.js" type="module"></script>\n</body>')

with open('account-settings.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated account-settings.html")
