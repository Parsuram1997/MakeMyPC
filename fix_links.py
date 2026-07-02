import os
import glob
import re

html_files = glob.glob('c:/Projects/MakeMyPC/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Logo link
    content = re.sub(
        r'<div class="text-headline-lg font-headline-lg font-black text-on-surface tracking-tighter">\s*MakeMyPC\s*</div>',
        r'<a href="index.html" class="text-headline-lg font-headline-lg font-black text-on-surface tracking-tighter">MakeMyPC</a>',
        content
    )
    
    # Shop link
    content = re.sub(
        r'<a class="(.*?)href="#">Shop</a>',
        r'<a class="\1href="prebuilt-pcs.html">Shop</a>',
        content
    )
    # Builder link
    content = re.sub(
        r'<a class="(.*?)href="#">Builder</a>',
        r'<a class="\1href="custom-pc-builder.html">Builder</a>',
        content
    )
    # Resources link
    content = re.sub(
        r'<a class="(.*?)href="#">Resources</a>',
        r'<a class="\1href="support-faq.html">Resources</a>',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
