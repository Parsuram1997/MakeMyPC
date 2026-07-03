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
    const navContainer = document.querySelector('nav .hidden.md\\:flex.gap-x-8.items-center');
    if (navContainer) {
        const navLinks = navContainer.querySelectorAll('a');
        const path = window.location.pathname.toLowerCase();
        navLinks.forEach(a => {
            const text = a.textContent.toLowerCase();
            
            // Update hrefs
            if (text.includes('shop')) a.href = 'prebuilt-pcs.html';
            if (text.includes('builder')) a.href = 'builder-landing.html';
            if (text.includes('resources')) a.href = 'support-faq.html';
            
            // Reset styles
            a.className = 'text-on-surface-variant font-medium hover:text-primary transition-colors duration-300 font-label-mono text-xs';
            
            // Apply active style
            if ((path.includes('prebuilt') && text.includes('shop')) ||
                (path.includes('builder') && text.includes('builder')) ||
                (path.includes('support') && text.includes('resources'))) {
                a.className = 'text-primary font-bold border-b-2 border-primary pb-1 font-label-mono text-xs';
            }
        });
    }

    // Update Header Icons
    window.updateCartBadge = function() {
        const badges = document.querySelectorAll('#cart-badge');
        let cart = [];
        try {
            cart = JSON.parse(localStorage.getItem('cart') || '[]');
        } catch(e) {}
        
        badges.forEach(badge => {
            if (cart.length > 0) {
                badge.textContent = cart.length;
                badge.classList.remove('hidden');
            } else {
                badge.classList.add('hidden');
            }
        });
    };
    window.updateCartBadge();
    
    // Setup Cart Button Redirect
    const cartBtn = document.querySelector('header button:has(span[data-icon="shopping_cart"]), header button span[data-icon="shopping_cart"]');
    if (cartBtn) {
        const clickable = cartBtn.tagName === 'SPAN' ? cartBtn.parentElement : cartBtn;
        clickable.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = 'shopping-cart.html';
        });
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
