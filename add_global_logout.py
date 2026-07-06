import sys

with open('js/auth.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Add global logout function
fn_code = """
// Global Logout Function
window.logoutUser = async function(e) {
    if (e) e.preventDefault();
    try {
        await signOut(auth);
        window.showToast('Logged out successfully', 'success');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1000);
    } catch (error) {
        console.error('Logout error', error);
        if (window.showToast) window.showToast('Error logging out', 'error');
    }
};

// Also attach to any existing #logout-btn for backward compatibility
const logoutBtn = document.getElementById('logout-btn');
"""

old_code = """// Logout
if (logoutBtn) {"""

if old_code in text:
    text = text.replace(old_code, fn_code + "if (logoutBtn) {")
    with open('js/auth.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("auth.js updated with window.logoutUser.")
else:
    print("Could not find the logout section in auth.js.")
