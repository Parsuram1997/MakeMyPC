text = open('prebuilt-pcs.html', encoding='utf-8').read()

# Add meta redirect right after <head> tag
redirect_tag = '<meta http-equiv="refresh" content="0; url=shop.html"/>\n'

if 'http-equiv="refresh"' in text:
    print('Redirect already exists')
else:
    # Insert after <head> opening tag
    text = text.replace('<head>', '<head>\n' + redirect_tag, 1)
    # Also add JS redirect as backup (faster)
    js_redirect = '<script>window.location.replace("shop.html");</script>\n'
    text = text.replace('<head>', '<head>\n' + js_redirect, 1)
    open('prebuilt-pcs.html', 'w', encoding='utf-8').write(text)
    print('Done: redirect added to prebuilt-pcs.html')
