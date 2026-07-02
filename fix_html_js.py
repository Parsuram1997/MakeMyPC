import glob

for f in glob.glob(r'c:\Projects\MakeMyPC\*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = content.replace('₹{', '${')
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Fixed ₹{ in', f)
print('Done fixing HTML')
