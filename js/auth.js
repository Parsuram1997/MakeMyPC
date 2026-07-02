import { auth, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged } from './firebase-config.js';

// Elements
const authAvatarBtn = document.getElementById('auth-avatar-btn');
const authLoginBtn = document.getElementById('auth-login-btn');
const avatarInitial = document.getElementById('avatar-initial');
const logoutBtn = document.getElementById('logout-btn');

// Sign up
window.handleSignup = async function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorEl = document.getElementById('signup-error');
    const submitBtn = document.getElementById('signup-btn');
    
    errorEl.classList.add('hidden');
    
    // Add loading state
    const originalText = submitBtn.innerText;
    submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-xl">progress_activity</span>';
    submitBtn.disabled = true;

    try {
        await createUserWithEmailAndPassword(auth, email, password);
        window.showToast('Account created successfully!', 'success');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1500);
    } catch (error) {
        errorEl.textContent = error.message;
        errorEl.classList.remove('hidden');
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    }
};

// Login
window.handleLogin = async function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorEl = document.getElementById('login-error');
    const submitBtn = document.getElementById('login-btn');
    
    errorEl.classList.add('hidden');
    
    // Add loading state
    const originalText = submitBtn.innerText;
    submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-xl">progress_activity</span>';
    submitBtn.disabled = true;

    try {
        await signInWithEmailAndPassword(auth, email, password);
        window.showToast('Logged in successfully!', 'success');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1500);
    } catch (error) {
        errorEl.textContent = error.message;
        errorEl.classList.remove('hidden');
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    }
};

// Logout
if (logoutBtn) {
    logoutBtn.addEventListener('click', async (e) => {
        e.preventDefault();
        try {
            await signOut(auth);
            window.showToast('Logged out', 'success');
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 1000);
        } catch (error) {
            console.error('Logout error', error);
        }
    });
}

// Global Auth State Observer
onAuthStateChanged(auth, (user) => {
    const isProtected = window.location.pathname.includes('account-settings.html') || window.location.pathname.includes('my-builds.html');
    
    if (user) {
        // Logged in
        if (authLoginBtn) authLoginBtn.classList.add('hidden');
        if (authAvatarBtn) {
            authAvatarBtn.classList.remove('hidden');
            if (avatarInitial) avatarInitial.textContent = user.email.charAt(0).toUpperCase();
        }
    } else {
        // Not logged in
        if (authLoginBtn) authLoginBtn.classList.remove('hidden');
        if (authAvatarBtn) authAvatarBtn.classList.add('hidden');
        
        // Guard protected routes
        if (isProtected) {
            window.location.href = 'login.html';
        }
    }
});


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
