import { auth, db, doc, setDoc, getDoc, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from './firebase-config.js';

// Elements
const authAvatarBtn = document.getElementById('auth-avatar-btn');
const authLoginBtn = document.getElementById('auth-login-btn');
const avatarInitial = document.getElementById('avatar-initial');
const logoutBtn = document.getElementById('logout-btn');

// Sign up
window.handleSignup = async function(e) {
    e.preventDefault();
    const nameEl = document.getElementById('signup-name') || document.getElementById('name');
    const emailEl = document.getElementById('signup-email') || document.getElementById('email');
    const passwordEl = document.getElementById('signup-password') || document.getElementById('password');
    
    const name = nameEl ? nameEl.value : 'New User';
    const email = emailEl ? emailEl.value : '';
    const password = passwordEl ? passwordEl.value : '';
    
    const errorEl = document.getElementById('signup-error');
    const submitBtn = document.getElementById('signup-btn');
    
    errorEl.classList.add('hidden');
    
    // Add loading state
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-xl">progress_activity</span>';
    submitBtn.disabled = true;

    try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        
        // Define role (admin if admin email, else customer)
        const role = (email.toLowerCase() === 'admin@makemypc.com') ? 'admin' : 'customer';
        
        // Save user to Firestore
        await setDoc(doc(db, 'users', user.uid), {
            name: name,
            email: email,
            role: role,
            createdAt: new Date()
        });

        // Firebase automatically logs in the user after signup.
        // If we want them to log in manually, we must sign them out immediately.
        await signOut(auth);

        window.showToast('Account created successfully! Please log in.', 'success');
        
        setTimeout(() => {
            window.location.href = 'login.html';
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
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-xl">progress_activity</span>';
    submitBtn.disabled = true;

    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        
        // Check role
        const userDoc = await getDoc(doc(db, 'users', user.uid));
        let role = 'customer';
        if (userDoc.exists()) {
            role = userDoc.data().role || 'customer';
        }

        window.showToast('Logged in successfully!', 'success');
        
        setTimeout(() => {
            if (role === 'admin') {
                window.location.href = 'admin-dashboard.html';
            } else {
                window.location.href = 'index.html';
            }
        }, 1500);
    } catch (error) {
        errorEl.textContent = error.message;
        errorEl.classList.remove('hidden');
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    }
};


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
onAuthStateChanged(auth, async (user) => {
    const isProtected = window.location.pathname.includes('account-settings.html') || window.location.pathname.includes('my-builds.html');
    
    if (user) {
        // Logged in — show avatar, hide login link
        if (authLoginBtn) authLoginBtn.style.display = 'none';
        if (authAvatarBtn) {
            authAvatarBtn.style.display = 'flex';
            if (avatarInitial) avatarInitial.textContent = user.email ? user.email.charAt(0).toUpperCase() : 'U';
        }
        // Also update mobile auth
        const mobileLogin = document.getElementById('mobile-auth-login');
        const mobileAccount = document.getElementById('mobile-auth-account');
        if (mobileLogin)  mobileLogin.style.display  = 'none';
        if (mobileAccount) mobileAccount.style.display = 'flex';
        
        // Optional: redirect from login page if already logged in
        if (window.location.pathname.includes('login.html') || window.location.pathname.includes('signup.html')) {
             try {
                const docSnap = await getDoc(doc(db, 'users', user.uid));
                if (docSnap.exists() && docSnap.data().role === 'admin') {
                    window.location.href = 'admin-dashboard.html';
                } else {
                    window.location.href = 'index.html';
                }
             } catch(e){}
        }
    } else {
        // Not logged in — show login link, hide avatar
        if (authLoginBtn) authLoginBtn.style.display = 'flex';
        if (authAvatarBtn) authAvatarBtn.style.display = 'none';
        // Mobile auth
        const mobileLogin = document.getElementById('mobile-auth-login');
        const mobileAccount = document.getElementById('mobile-auth-account');
        if (mobileLogin)  mobileLogin.style.display  = 'flex';
        if (mobileAccount) mobileAccount.style.display = 'none';
        
        // Guard protected routes
        if (isProtected) {
            window.location.href = 'login.html';
        }
    }
});


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
                const userCredential = await signInWithPopup(auth, googleProvider);
                const user = userCredential.user;
                
                // Define role
                const role = (user.email && user.email.toLowerCase() === 'admin@makemypc.com') ? 'admin' : 'customer';
                
                // Save user to Firestore (merge true so we don't overwrite if existing)
                await setDoc(doc(db, 'users', user.uid), {
                    name: user.displayName || 'Google User',
                    email: user.email,
                    role: role,
                    lastLogin: new Date()
                }, { merge: true });

                window.showToast('Logged in with Google successfully!', 'success');
                
                setTimeout(() => {
                    if (role === 'admin') {
                        window.location.href = 'admin-dashboard.html';
                    } else {
                        window.location.href = 'index.html';
                    }
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


// Auto-attach logout handler to any element containing 'Logout' text or logout icon
document.addEventListener('DOMContentLoaded', () => {
    // Find all links or buttons in the document
    const elements = document.querySelectorAll('a, button, [role="button"]');
    elements.forEach(el => {
        // If the element has text "Logout" (case insensitive) and is not already wired
        if (el.textContent.trim().toLowerCase() === 'logout' || 
            el.innerHTML.includes('>Logout<') || 
            el.innerHTML.includes('>logout<')) {
            el.addEventListener('click', window.logoutUser);
            el.style.cursor = 'pointer';
        }
    });
});
