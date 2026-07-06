import sys

with open('js/auth.js', 'r', encoding='utf-8') as f:
    text = f.read()

auto_attach = """
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
"""

if "Auto-attach logout handler" not in text:
    text = text + "\n" + auto_attach
    with open('js/auth.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Auto-attach logic added to auth.js.")
else:
    print("Logic already exists.")

