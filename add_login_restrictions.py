import re

def update_login():
    with open('login.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_logic = """
    <script>
        document.querySelector('form').addEventListener('submit', function(e) {
            const email = document.getElementById('email').value.toLowerCase();
            if (email.includes('admin@') || email.includes('admin.')) {
                e.preventDefault();
                alert('Admin accounts must use the Admin Portal to sign in.');
                window.location.href = 'admin-login.html';
            }
        });
    </script>
</body>
"""
    content = content.replace('</body>', js_logic)
    
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
def update_admin_login():
    with open('admin-login.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_logic = """
    <script>
        document.querySelector('form').addEventListener('submit', function(e) {
            const email = document.getElementById('email').value.toLowerCase();
            if (!email.includes('admin@') && !email.includes('admin.')) {
                e.preventDefault();
                alert('User accounts cannot access the Admin Portal. Please use the standard login.');
                window.location.href = 'login.html';
            }
        });
    </script>
</body>
"""
    content = content.replace('</body>', js_logic)
    
    with open('admin-login.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_login()
update_admin_login()
print("Login restrictions applied successfully!")
