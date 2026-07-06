import { auth, db, getDoc, setDoc, doc, arrayUnion, onAuthStateChanged } from './firebase-config.js';

const listContainer = document.getElementById('address-list-container');
const noAddressState = document.getElementById('no-address-state');
const addAddressBtn = document.getElementById('add-address-btn');
const formContainer = document.getElementById('add-address-form-container');
const addressForm = document.getElementById('address-form');
const cancelAddressBtn = document.getElementById('cancel-address-btn');
const saveAddressBtn = document.getElementById('save-address-btn');

// Form inputs
const addrName = document.getElementById('addr-name');
const addrPhone = document.getElementById('addr-phone');
const addrPincode = document.getElementById('addr-pincode');
const addrState = document.getElementById('addr-state');
const addrCity = document.getElementById('addr-city');
const addrType = document.getElementById('addr-type');
const addrHouse = document.getElementById('addr-house');
const addrArea = document.getElementById('addr-area');

let currentUser = null;
let userAddresses = [];

// Toggle Form
const toggleForm = (show) => {
    if (show) {
        if (formContainer) formContainer.classList.remove('hidden');
        if (addAddressBtn) addAddressBtn.classList.add('hidden');
    } else {
        if (formContainer) formContainer.classList.add('hidden');
        if (addAddressBtn) addAddressBtn.classList.remove('hidden');
        if (addressForm) addressForm.reset();
    }
};

if (addAddressBtn) addAddressBtn.addEventListener('click', () => toggleForm(true));
if (cancelAddressBtn) cancelAddressBtn.addEventListener('click', () => toggleForm(false));

// Render Addresses
const renderAddresses = () => {
    if (!listContainer) return;
    
    // Clear all existing address cards
    const cards = listContainer.querySelectorAll('.address-card');
    cards.forEach(card => card.remove());

    if (!userAddresses || userAddresses.length === 0) {
        if (noAddressState) noAddressState.style.display = 'block';
    } else {
        if (noAddressState) noAddressState.style.display = 'none';

        userAddresses.forEach(addr => {
            const card = document.createElement('div');
            card.className = 'address-card glass-card rounded-xl p-6 relative border border-white/10 hover:border-electric-blue/50 transition-colors flex flex-col justify-between';
            
            const typeIcon = addr.type === 'Home' ? 'home' : 'work';
            
            card.innerHTML = `
                <div>
                    <div class="flex justify-between items-start mb-4">
                        <span class="bg-white/10 text-white px-2 py-1 rounded text-[10px] font-bold uppercase tracking-wider flex items-center gap-1">
                            <span class="material-symbols-outlined text-[12px]">${typeIcon}</span> ${addr.type || 'Home'}
                        </span>
                    </div>
                    <h3 class="font-bold text-lg mb-1">${addr.name}</h3>
                    <p class="text-sm text-outline mb-4">${addr.phone}</p>
                    
                    <p class="text-sm text-on-surface-variant leading-relaxed">
                        ${addr.house}, ${addr.area}<br/>
                        ${addr.city}, ${addr.state} - <span class="font-bold text-white">${addr.pincode}</span>
                    </p>
                </div>
                <div class="mt-6 pt-4 border-t border-white/5 flex gap-4">
                    <button class="delete-btn text-error hover:text-red-400 text-sm font-medium transition-colors" data-id="${addr.id}">Delete</button>
                </div>
            `;
            listContainer.appendChild(card);
        });

        // Bind delete events
        const deleteBtns = listContainer.querySelectorAll('.delete-btn');
        deleteBtns.forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const id = e.target.getAttribute('data-id');
                await deleteAddress(id);
            });
        });
    }
};

// Load Addresses from Firestore user document
const loadAddresses = async () => {
    if (!currentUser) return;
    try {
        const userDoc = await getDoc(doc(db, 'users', currentUser.uid));
        if (userDoc.exists()) {
            userAddresses = userDoc.data().addresses || [];
            renderAddresses();
        }
    } catch (err) {
        console.error("Error loading addresses:", err);
    }
};

// Save New Address
if (addressForm) {
    addressForm.addEventListener('submit', async (e) => {
        try {
            e.preventDefault();
            
            if (!currentUser) {
                alert('Error: You are not logged in!');
                return;
            }

            const originalHTML = saveAddressBtn.innerHTML;
            saveAddressBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">progress_activity</span> <span>Saving...</span>';
            saveAddressBtn.disabled = true;

            const newAddr = {
                id: 'addr_' + Date.now() + Math.floor(Math.random() * 1000),
                name: addrName.value.trim(),
                phone: addrPhone.value.trim(),
                pincode: addrPincode.value.trim(),
                state: addrState.value.trim(),
                city: addrCity.value.trim(),
                house: addrHouse.value.trim(),
                area: addrArea.value.trim(),
                type: addrType.value,
                createdAt: Date.now()
            };

            const userRef = doc(db, 'users', currentUser.uid);
            await setDoc(userRef, {
                addresses: arrayUnion(newAddr)
            }, { merge: true });
            
            if (window.showToast) window.showToast('Address saved successfully!', 'success');
            toggleForm(false);
            await loadAddresses();
            
            saveAddressBtn.innerHTML = originalHTML;
            saveAddressBtn.disabled = false;
        } catch (err) {
            alert("Error in JS Submit: " + err.message);
            console.error("JS Error:", err);
            saveAddressBtn.innerHTML = "Save Address";
            saveAddressBtn.disabled = false;
        }
    });
} else {
    alert("CRITICAL ERROR: addressForm not found on the page!");
}

// Delete Address
const deleteAddress = async (id) => {
    if (!currentUser) return;
    if (!confirm('Are you sure you want to delete this address?')) return;

    try {
        const addrToRemove = userAddresses.find(a => a.id === id);
        if (!addrToRemove) return;

        const userRef = doc(db, 'users', currentUser.uid);
        const updatedAddresses = userAddresses.filter(a => a.id !== id);
        await setDoc(userRef, {
            addresses: updatedAddresses
        }, { merge: true });
        
        if (window.showToast) window.showToast('Address deleted', 'success');
        await loadAddresses();
    } catch (err) {
        alert("Error deleting: " + err.message);
    }
};

// Initialize
onAuthStateChanged(auth, (user) => {
    if (user) {
        currentUser = user;
        loadAddresses();
    } else {
        currentUser = null;
        userAddresses = [];
        renderAddresses();
    }
});
