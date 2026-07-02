import os

with open(r'c:\Projects\MakeMyPC\js\auth.js', 'r', encoding='utf-8') as f:
    content = f.read()

google_code = """
import { GoogleAuthProvider, signInWithPopup } from './firebase-config.js';

const googleProvider = new GoogleAuthProvider();
const googleLoginBtns = document.querySelectorAll('#google-login-btn');

if (googleLoginBtns.length > 0) {
    googleLoginBtns.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const originalHTML = btn.innerHTML;
            btn.innerHTML = '<span class="material-symbols-outlined animate-spin text-xl">progress_activity</span>';
            btn.disabled = true;
            try {
                await signInWithPopup(auth, googleProvider);
                window.showToast('Logged in with Google successfully!', 'success');
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 1500);
            } catch (error) {
                console.error("Google Auth Error:", error);
                window.showToast('Google login failed: ' + error.message, 'error');
                btn.innerHTML = originalHTML;
                btn.disabled = false;
            }
        });
    });
}
"""

if 'GoogleAuthProvider' not in content:
    content = content + '\n' + google_code
    with open(r'c:\Projects\MakeMyPC\js\auth.js', 'w', encoding='utf-8') as f:
        f.write(content)
