import re
text = open('builder-landing.html', encoding='utf-8').read()
scripts = re.findall(r'<script[^>]+src="([^"]+)"', text)
print('Scripts in builder-landing.html:')
for s in scripts:
    print(' ', s)

# Also get the exact script block near </body>
idx = text.rfind('</body>')
print('\nLast 1000 chars before </body>:')
print(text[max(0,idx-1000):idx])
