// global.js
// Handles global navigation and interactive elements across all MakeMyPC pages.

document.addEventListener('DOMContentLoaded', () => {
    // 1. Fix Global Navigation
    
    // Make Logo Clickable
    const logo = document.querySelector('header .text-headline-lg');
    if (logo) {
        logo.classList.add('cursor-pointer');
        logo.addEventListener('click', () => {
            window.location.href = 'index.html';
        });
    }

    // Update Nav Links
    const navLinks = document.querySelectorAll('header nav a');
    navLinks.forEach(a => {
        const text = a.textContent.toLowerCase();
        if (text.includes('shop')) a.href = 'prebuilt-pcs.html';
        if (text.includes('builder')) a.href = 'custom-pc-builder.html';
        if (text.includes('resources')) a.href = 'support-faq.html';
    });

    // Update Header Icons
    const cartBtn = document.querySelector('header button[data-icon="shopping_cart"]');
    if (cartBtn) {
        cartBtn.addEventListener('click', () => {
            window.location.href = 'shopping-cart.html';
        });
        
        // Add a badge if there are items in the cart
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        if (cart.length > 0) {
            cartBtn.classList.add('relative');
            const badge = document.createElement('span');
            badge.className = 'absolute -top-1 -right-1 bg-tertiary text-on-tertiary text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold';
            badge.textContent = cart.length;
            cartBtn.appendChild(badge);
        }
    }

    const accountBtn = document.querySelector('header button[data-icon="account_circle"]');
    if (accountBtn) {
        accountBtn.addEventListener('click', () => {
            window.location.href = 'account-settings.html';
        });
    }

    // 2. Mock Form Handling
    
    // Submit Ticket Form Redirect
    const ticketForm = document.querySelector('form');
    if (window.location.pathname.includes('submit-ticket.html') && ticketForm) {
        ticketForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = ticketForm.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = `<span class="material-symbols-outlined animate-spin">refresh</span> Submitting...`;
            btn.classList.add('opacity-50', 'pointer-events-none');
            
            setTimeout(() => {
                window.location.href = 'ticket-submitted.html';
            }, 1000);
        });
    }

    // Order Tracking Form
    const trackForm = document.querySelector('.bg-surface-container form, form');
    if (window.location.pathname.includes('order-tracking.html') && trackForm) {
        trackForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = trackForm.querySelector('button[type="submit"]');
            if (btn) btn.innerHTML = 'Tracking...';
            setTimeout(() => {
                window.showToast('Order #MMYPC-12345 found! Delivery expected tomorrow.', 'success');
                if (btn) btn.innerHTML = 'Track Order';
            }, 1500);
        });
    }

    // Account Settings Save
    const saveBtns = document.querySelectorAll('button');
    if (window.location.pathname.includes('account-settings.html')) {
        saveBtns.forEach(btn => {
            if (btn.textContent.includes('Save')) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.showToast('Settings saved successfully!', 'success');
                });
            }
        });
    }
});

// 3. Global Toast Notification System
window.showToast = function(message, type = 'info') {
    // Create container if not exists
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'fixed bottom-4 right-4 z-[9999] flex flex-col gap-2';
        document.body.appendChild(container);
    }

    // Colors based on type
    const colors = {
        success: 'bg-cyber-teal text-on-secondary-fixed',
        error: 'bg-error text-on-error',
        info: 'bg-electric-blue text-white'
    };

    const icon = {
        success: 'check_circle',
        error: 'error',
        info: 'info'
    };

    const toast = document.createElement('div');
    toast.className = `${colors[type]} px-4 py-3 rounded-lg shadow-lg flex items-center gap-3 transform translate-y-10 opacity-0 transition-all duration-300`;
    toast.innerHTML = `
        <span class="material-symbols-outlined">${icon[type]}</span>
        <span class="font-medium text-sm">${message}</span>
    `;

    container.appendChild(toast);

    // Animate in
    requestAnimationFrame(() => {
        toast.classList.remove('translate-y-10', 'opacity-0');
    });

    // Remove after 3 seconds
    setTimeout(() => {
        toast.classList.add('translate-y-10', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
};
