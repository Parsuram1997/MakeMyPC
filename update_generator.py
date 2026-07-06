text = open('generate_shop.py', encoding='utf-8').read()

# Find </script>\n</body> near end of file and add auth scripts before </body>
# The closing </body> is in the HTML string
old = '</script>\n</body>\n</html>'
new = '''</script>
<script src="js/global.js"></script>
<script type="module" src="js/auth.js"></script>
</body>
</html>'''

if old in text:
    open('generate_shop.py', 'w', encoding='utf-8').write(text.replace(old, new, 1))
    print('generate_shop.py updated with auth scripts')
else:
    idx = text.rfind('</body>')
    print('Pattern not found. Context near </body>:', repr(text[max(0,idx-100):idx+20]))
