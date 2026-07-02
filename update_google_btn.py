import os

for filename in [r'c:\Projects\MakeMyPC\login.html', r'c:\Projects\MakeMyPC\signup.html']:
    try:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = c.replace('<button type="button" class="w-full bg-white/5', '<button id="google-login-btn" type="button" class="w-full bg-white/5')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(c)
    except Exception as e:
        print(e)
