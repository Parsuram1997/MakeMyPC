import os

def update_file(filepath, is_login):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if is_login:
        content = content.replace('<form class="space-y-6" onsubmit="event.preventDefault()">', '<form class="space-y-6" onsubmit="window.handleLogin(event)">')
        content = content.replace('<button type="submit" class="w-full bg-electric-blue', '<button id="login-btn" type="submit" class="w-full bg-electric-blue')
        if 'id="login-error"' not in content:
            content = content.replace('<form class="space-y-6" onsubmit="window.handleLogin(event)">', '<div id="login-error" class="hidden bg-error/20 text-error p-3 rounded text-sm mb-4"></div>\n<form class="space-y-6" onsubmit="window.handleLogin(event)">')
    else:
        content = content.replace('<form class="space-y-6" onsubmit="event.preventDefault()">', '<form class="space-y-6" onsubmit="window.handleSignup(event)">')
        content = content.replace('<button type="submit" class="w-full bg-electric-blue', '<button id="signup-btn" type="submit" class="w-full bg-electric-blue')
        if 'id="signup-error"' not in content:
            content = content.replace('<form class="space-y-6" onsubmit="window.handleSignup(event)">', '<div id="signup-error" class="hidden bg-error/20 text-error p-3 rounded text-sm mb-4"></div>\n<form class="space-y-6" onsubmit="window.handleSignup(event)">')
        
        # also update input IDs for signup if needed. In signup they might not have the correct ids for name, email, password.
        content = content.replace('placeholder="First & Last Name"', 'id="name" placeholder="First & Last Name"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(r'c:\Projects\MakeMyPC\login.html', True)
update_file(r'c:\Projects\MakeMyPC\signup.html', False)
