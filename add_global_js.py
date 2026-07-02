import os

for filename in [r'c:\Projects\MakeMyPC\login.html', r'c:\Projects\MakeMyPC\signup.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'js/global.js' not in c:
        c = c.replace('<script type="module" src="js/auth.js"></script>', '<script src="js/global.js"></script>\n<script type="module" src="js/auth.js"></script>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(c)
print('Done')
