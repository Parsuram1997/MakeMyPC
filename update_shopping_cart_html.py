import re

with open(r'c:\Projects\MakeMyPC\shopping-cart.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything inside <main> ... </main> with an empty container
main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)
new_main = '''<main id="checkout-root" class="w-full min-h-screen pt-24 pb-12">
    <!-- Premium Checkout Rendered via JS -->
</main>'''

new_html = main_pattern.sub(new_main, html)

# Also insert <script src="js/shopping-cart.js"></script> before the closing body tag
if 'js/shopping-cart.js' not in new_html:
    new_html = new_html.replace('</body>', '<script src="js/shopping-cart.js"></script>\n</body>')

# Remove the inline script that was simulating cart updates
inline_script_pattern = re.compile(r'<script>\s*// Micro-interactions.*?// \(Just visual placeholders for now\)\s*</script>', re.DOTALL)
new_html = inline_script_pattern.sub('', new_html)

with open(r'c:\Projects\MakeMyPC\shopping-cart.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Updated shopping-cart.html')
