text = open('shop.html', encoding='utf-8').read()

scripts_block = '''
<script src="js/global.js" type="module"></script>
<script type="module" src="js/auth.js"></script>
'''

if 'auth.js' in text:
    print('Already has auth.js')
else:
    # Inject before </body>
    text = text.replace('</body>', scripts_block + '\n</body>', 1)
    open('shop.html', 'w', encoding='utf-8').write(text)
    print('Done: auth scripts added to shop.html')
    # Verify
    print('auth.js present:', 'auth.js' in open('shop.html').read())
    print('global.js present:', 'global.js' in open('shop.html').read())
