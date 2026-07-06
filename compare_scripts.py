import re

for f in ['shop.html', 'builder-landing.html', 'index.html']:
    text = open(f, encoding='utf-8').read()
    tags = re.findall(r'<script[^>]+src="js/[^"]+"[^>]*>', text)
    print(f + ':')
    for t in tags:
        print(' ', t)
    print()
