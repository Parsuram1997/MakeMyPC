import os
import re

FOOTER_HTML = """<!-- Footer -->
<footer class="bg-surface-deep border-t border-white/5 w-full">
    <div class="max-w-container-max mx-auto px-margin-desktop py-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-gutter">
        <!-- 1. Company Details -->
        <div class="lg:col-span-2">
            <div class="font-headline-sm text-headline-sm text-on-surface mb-6">MakeMyPC</div>
            <p class="text-on-surface-variant font-body-sm text-body-sm leading-relaxed mb-6">
                India's most trusted Custom PC Builder. We don't just sell parts; we build your dream setup with surgical precision, premium quality, and 100% compatibility guarantee.
            </p>
            <div class="flex items-center gap-4 mb-8">
                <!-- Trust Badges (Images or Icons) -->
                <div class="flex items-center gap-2 bg-white/5 px-3 py-2 rounded-lg border border-white/10">
                    <span class="material-symbols-outlined text-electric-blue">verified</span>
                    <span class="text-label-mono text-xs text-on-surface">100% Genuine</span>
                </div>
                <div class="flex items-center gap-2 bg-white/5 px-3 py-2 rounded-lg border border-white/10">
                    <span class="material-symbols-outlined text-cyber-teal">shield</span>
                    <span class="text-label-mono text-xs text-on-surface">Secure Checkout</span>
                </div>
            </div>
        </div>

        <!-- 2. Explore / Quick Links -->
        <div>
            <h5 class="font-label-mono text-label-mono text-on-surface uppercase tracking-widest mb-6">Explore</h5>
            <ul class="space-y-4">
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all flex items-center gap-2" href="builder-landing.html"><span class="material-symbols-outlined text-[16px]">build</span> Custom PC Builder</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all flex items-center gap-2" href="prebuilt-pcs.html"><span class="material-symbols-outlined text-[16px]">desktop_windows</span> Prebuilt PCs</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all flex items-center gap-2" href="order-tracking.html"><span class="material-symbols-outlined text-[16px]">local_shipping</span> Track Order</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all flex items-center gap-2" href="#"><span class="material-symbols-outlined text-[16px]">info</span> About Us</a></li>
            </ul>
        </div>

        <!-- 3. Policies & Support -->
        <div>
            <h5 class="font-label-mono text-label-mono text-on-surface uppercase tracking-widest mb-6">Policies & Support</h5>
            <ul class="space-y-4">
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all" href="support-faq.html">FAQ & Support</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all" href="#">Return & Cancellation</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all" href="#">Shipping Policy</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all" href="#">Privacy Policy</a></li>
                <li><a class="text-on-surface-variant font-body-sm text-body-sm hover:text-primary transition-all" href="#">Terms of Service</a></li>
            </ul>
        </div>

        <!-- 4. Contact -->
        <div>
            <h5 class="font-label-mono text-label-mono text-on-surface uppercase tracking-widest mb-6">Contact Us</h5>
            <ul class="space-y-4 mb-6">
                <li class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-on-surface-variant mt-0.5">call</span>
                    <div>
                        <p class="text-on-surface font-body-sm text-body-sm">+91 1800-123-4567</p>
                        <p class="text-on-surface-variant text-xs mt-1">Mon - Sat, 10 AM - 7 PM</p>
                    </div>
                </li>
                <li class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-on-surface-variant mt-0.5">mail</span>
                    <div>
                        <p class="text-on-surface font-body-sm text-body-sm">support@makemypc.in</p>
                        <p class="text-on-surface-variant text-xs mt-1">We reply within 24 hours</p>
                    </div>
                </li>
            </ul>
            <!-- Social Links -->
            <div class="flex gap-4">
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="text-lg font-bold">f</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="material-symbols-outlined text-lg">photo_camera</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-lg glass-card flex items-center justify-center text-on-surface-variant hover:text-primary hover:bg-white/10 transition-all">
                    <span class="text-lg font-bold">X</span>
                </a>
            </div>
        </div>
    </div>
    <div class="max-w-container-max mx-auto px-margin-desktop py-6 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-on-surface-variant font-label-mono text-label-mono text-xs">© 2024 MakeMyPC. All Rights Reserved. GSTIN: 27AAAAA0000A1Z5</p>
        <div class="flex gap-x-6 items-center">
            <!-- Payment Badges placeholder -->
            <div class="flex gap-2 opacity-50 grayscale hover:grayscale-0 transition-all">
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">VISA</div>
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">MasterCard</div>
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">UPI</div>
            </div>
            <span class="text-on-surface-variant font-label-mono text-label-mono text-xs hover:text-on-surface cursor-pointer flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-cyber-teal animate-pulse"></span>
                System Status: <span class="text-cyber-teal">ONLINE</span>
            </span>
        </div>
    </div>
</footer>\n"""

def main():
    directory = "c:/Projects/MakeMyPC"
    
    # Regex to find existing footer
    footer_pattern = re.compile(r'(?:<!--\s*Footer\s*-->\s*)?<footer.*?</footer>', re.DOTALL | re.IGNORECASE)

    count_replaced = 0
    count_added = 0
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if footer_pattern.search(content):
                new_content = footer_pattern.sub(FOOTER_HTML, content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Replaced footer in {filename}")
                    count_replaced += 1
            else:
                # Add footer before </body>
                if "</body>" in content:
                    new_content = content.replace("</body>", FOOTER_HTML + "</body>")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added footer to {filename}")
                    count_added += 1
                else:
                    print(f"Could not add footer to {filename} (no </body> tag)")

    print(f"Replaced: {count_replaced}, Added: {count_added}")

if __name__ == "__main__":
    main()
