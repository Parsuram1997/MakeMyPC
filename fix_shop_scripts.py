text = open('shop.html', encoding='utf-8').read()

# Remove wrong scripts block that was added
old_block = '\n<script src="js/global.js" type="module"></script>\n<script type="module" src="js/auth.js"></script>\n'

# Correct scripts block - matching builder-landing.html pattern exactly
correct_block = '\n<script src="js/global.js"></script>\n<script type="module" src="js/auth.js"></script>\n'

result = text.replace(old_block, correct_block)
if result != text:
    open('shop.html', 'w', encoding='utf-8').write(result)
    print('Fixed: global.js no longer type=module in shop.html')
else:
    # Try without leading newline
    old2 = '<script src="js/global.js" type="module"></script>'
    new2 = '<script src="js/global.js"></script>'
    result2 = text.replace(old2, new2)
    if result2 != text:
        open('shop.html', 'w', encoding='utf-8').write(result2)
        print('Fixed: removed type=module from global.js')
    else:
        # Find what's there
        idx = text.find('global.js')
        print('Not found, context:', repr(text[max(0,idx-20):idx+80]))
