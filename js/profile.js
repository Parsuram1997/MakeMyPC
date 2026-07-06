import { auth, db, storage, doc, getDoc, setDoc, onAuthStateChanged, ref, uploadBytes, getDownloadURL } from './firebase-config.js';

document.addEventListener('DOMContentLoaded', () => {
    const profileName = document.getElementById('profile-name');
    const profileEmail = document.getElementById('profile-email');
    const profilePhone = document.getElementById('profile-phone');
    const profileLocation = document.getElementById('profile-location');
    const profileBio = document.getElementById('profile-bio');
    const profileDisplayName = document.getElementById('profile-display-name');
    const profileRoleBadge = document.getElementById('profile-role-badge');
    const adminDashboardLink = document.getElementById('admin-dashboard-link');
    const profileImg = document.getElementById('profile-img');
    const photoBtn = document.getElementById('profile-photo-btn');
    const photoBtnIcon = document.getElementById('profile-photo-btn-icon');
    const photoInput = document.getElementById('profile-photo-input');
    const saveBtn = document.getElementById('profile-save-btn');
    
    let currentUser = null;

    // Load Data
    onAuthStateChanged(auth, async (user) => {
        if (user) {
            currentUser = user;
            profileEmail.value = user.email || '';
            
            try {
                const docRef = doc(db, 'users', user.uid);
                const docSnap = await getDoc(docRef);
                
                if (docSnap.exists()) {
                    const data = docSnap.data();
                    if (profileRoleBadge && data.role) {
                        if (data.role === 'admin') {
                            profileRoleBadge.innerHTML = '<span class="material-symbols-outlined text-[14px]">admin_panel_settings</span> SYSTEM ADMIN';
                            profileRoleBadge.className = 'bg-red-500/20 border border-red-500 text-red-500 px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';
                            if (adminDashboardLink) adminDashboardLink.style.display = 'flex';
                        } else if (data.role === 'customer') {
                            profileRoleBadge.innerHTML = '<span class="material-symbols-outlined text-[14px]">workspace_premium</span> ELITE BUILDER';
                            profileRoleBadge.className = 'bg-electric-blue/20 border border-electric-blue text-electric-blue px-3 py-1 rounded-full text-label-mono font-label-mono text-[10px] uppercase font-bold flex items-center gap-1';
                        }
                    }
                    if (data.name) {
                        profileName.value = data.name;
                        if (profileDisplayName) profileDisplayName.textContent = data.name;
                    }
                    if (data.phone) profilePhone.value = data.phone;
                    if (data.location) profileLocation.value = data.location;
                    if (data.bio) profileBio.value = data.bio;
                    if (data.photoURL) {
                        if (profileImg) profileImg.src = data.photoURL;
                    }
                }
            } catch (err) {
                console.error("Error loading profile:", err);
            }
        }
    });

    // Handle Photo Click
    const triggerUpload = (e) => {
        e.preventDefault();
        if (photoInput) photoInput.click();
    };
    if (photoBtn) photoBtn.addEventListener('click', triggerUpload);
    if (photoBtnIcon) photoBtnIcon.addEventListener('click', triggerUpload);

    // Handle Photo Selection and Upload
    if (photoInput) {
        photoInput.addEventListener('change', async (e) => {
            const file = e.target.files[0];
            if (!file || !currentUser) return;
            
            if (file.size > 2 * 1024 * 1024) {
                if (window.showToast) window.showToast('File too large (Max 2MB)', 'error');
                return;
            }

            try {
                if (window.showToast) window.showToast('Uploading photo...', 'info');
                
                const storageRef = ref(storage, `users/${currentUser.uid}/profile_${Date.now()}`);
                await uploadBytes(storageRef, file);
                const downloadURL = await getDownloadURL(storageRef);
                
                // Update Firestore
                await setDoc(doc(db, 'users', currentUser.uid), { photoURL: downloadURL }, { merge: true });
                
                // Update UI
                if (profileImg) profileImg.src = downloadURL;
                if (window.showToast) window.showToast('Profile photo updated!', 'success');
                
                // Update avatar in navbar if it exists
                const navAvatar = document.getElementById('auth-avatar-btn');
                if (navAvatar) {
                    navAvatar.innerHTML = `<img src="${downloadURL}" class="w-full h-full rounded-full object-cover">`;
                }

            } catch (err) {
                console.error("Error uploading photo:", err);
                if (window.showToast) window.showToast('Failed to upload photo', 'error');
            }
        });
    }

    // Handle Save Changes
    if (saveBtn) {
        saveBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            if (!currentUser) return;

            const originalHTML = saveBtn.innerHTML;
            saveBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">progress_activity</span> <span>Saving...</span>';
            saveBtn.disabled = true;

            try {
                await setDoc(doc(db, 'users', currentUser.uid), {
                    name: profileName.value.trim(),
                    phone: profilePhone.value.trim(),
                    location: profileLocation.value,
                    bio: profileBio.value.trim(),
                    updatedAt: new Date()
                }, { merge: true });

                if (profileDisplayName) profileDisplayName.textContent = profileName.value.trim();
                
                if (window.showToast) window.showToast('Profile saved successfully!', 'success');
            } catch (err) {
                console.error("Error saving profile:", err);
                if (window.showToast) window.showToast('Failed to save profile', 'error');
            } finally {
                saveBtn.innerHTML = originalHTML;
                saveBtn.disabled = false;
            }
        });
    }
});
