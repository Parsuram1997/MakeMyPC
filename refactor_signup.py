import re
import os

with open(r'c:\Projects\MakeMyPC\login.html', 'r', encoding='utf-8') as f:
    login_html = f.read()

# Extract the header and footer from login to match exact structures (excluding main content)
login_nav_start = login_html.find('<nav')
login_nav_end = login_html.find('</nav>') + 6
# Actually login doesn't have a <nav>! It's just a blank page with <div class="circuit-bg">.
# Let's check login_html.

with open(r'c:\Projects\MakeMyPC\signup.html', 'r', encoding='utf-8') as f:
    signup_html = f.read()

# We will completely rewrite the <main> block of signup to match login's <main> block style.
new_main = """
    <main class="relative z-10 flex-grow flex items-center justify-center p-margin-mobile md:p-margin-desktop">
        <div class="glass-card w-full max-w-[440px] p-8 md:p-10 rounded-xl">
            <div class="mb-8 text-center">
                <div class="inline-flex items-center justify-center w-16 h-16 rounded-lg bg-primary/10 mb-4 border border-primary/20">
                    <span class="material-symbols-outlined text-electric-blue text-4xl">person_add</span>
                </div>
                <h1 class="text-headline-lg font-bold tracking-tight text-white">MakeMyPC</h1>
                <p class="text-body-sm text-on-surface-variant mt-2">Elite Builder Recruitment Phase</p>
            </div>

            <div id="signup-error" class="hidden bg-error/20 text-error p-3 rounded text-sm mb-4"></div>
            <form class="space-y-6" onsubmit="window.handleSignup(event)">
                <div class="space-y-2">
                    <label class="block text-label-mono uppercase text-outline" for="signup-email">Neural Link (Email)</label>
                    <div class="relative">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-xl">alternate_email</span>
                        <input id="signup-email" type="email" placeholder="identifier@neural.net" required class="input-neural w-full pl-10 pr-4 py-3 rounded text-body-md text-on-surface placeholder:text-outline-variant bg-white/5 border border-white/10 focus:ring-1 focus:ring-electric-blue focus:border-electric-blue">
                    </div>
                </div>

                <div class="space-y-2">
                    <label class="block text-label-mono uppercase text-outline" for="signup-password">Access Key (Password)</label>
                    <div class="relative">
                        <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-xl">vpn_key</span>
                        <input id="signup-password" type="password" placeholder="••••••••••••" required class="input-neural w-full pl-10 pr-4 py-3 rounded text-body-md text-on-surface placeholder:text-outline-variant bg-white/5 border border-white/10 focus:ring-1 focus:ring-electric-blue focus:border-electric-blue">
                    </div>
                </div>

                <button id="signup-btn" type="submit" class="w-full bg-electric-blue hover:bg-electric-blue/90 text-white font-semibold py-4 rounded transition-all duration-200 shadow-lg shadow-electric-blue/20 flex items-center justify-center gap-2 group">
                    <span class="">Create Account</span>
                    <span class="material-symbols-outlined text-xl group-hover:translate-x-1 transition-transform">person_add</span>
                </button>
                
                <div class="flex items-center gap-4 my-6">
                    <div class="flex-grow h-px bg-white/10"></div>
                    <span class="text-label-mono text-outline-variant uppercase">OR SIGN UP WITH</span>
                    <div class="flex-grow h-px bg-white/10"></div>
                </div>
                
                <button id="google-login-btn" type="button" class="w-full bg-white/5 hover:bg-white/10 border border-white/10 text-on-surface font-medium py-3 rounded transition-all duration-200 flex items-center justify-center gap-3 group">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"></path><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"></path><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"></path><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"></path></svg>
                    <span class="text-body-sm">Google Neural ID</span>
                </button>
            </form>

            <div class="mt-8 pt-8 border-t border-white/5 text-center">
                <p class="text-body-sm text-on-surface-variant">
                    Already have clearance? 
                    <a href="login.html" class="text-secondary font-medium hover:underline ml-1">Log In</a>
                </p>
            </div>
        </div>
    </main>
"""

# Extract everything before <main...>
start = signup_html.find('<main')
end = signup_html.find('</main>') + 7

new_signup = signup_html[:start] + new_main + signup_html[end:]

with open(r'c:\Projects\MakeMyPC\signup.html', 'w', encoding='utf-8') as f:
    f.write(new_signup)

print('Done')
