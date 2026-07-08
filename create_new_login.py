import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MakeMyPC - Admin Login</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Material Symbols -->
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
            colors: {
                primary: {
                    DEFAULT: '#2563EB',
                    light: '#60A5FA',
                    dark: '#1D4ED8'
                },
                surface: {
                    DEFAULT: '#0B1120',
                    alt: '#060B14'
                },
                'on-surface': '#F8FAFC',
                'on-surface-variant': '#94A3B8'
            }
          },
        },
      }
    </script>
    <style>
        body {
            background-color: #060B14;
            color: #F8FAFC;
            overflow-x: hidden;
            font-family: 'Inter', sans-serif;
        }
        .tech-bg {
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 100% 100%, rgba(37, 99, 235, 0.05) 0%, transparent 50%);
            background-size: 100% 100%;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        .btn-gradient {
            background: linear-gradient(90deg, #2563EB 0%, #3B82F6 100%);
        }
        .btn-gradient:hover {
            background: linear-gradient(90deg, #1D4ED8 0%, #2563EB 100%);
        }
        
        /* Hexagon Logo */
        .hexagon {
            width: 48px;
            height: 54px;
            background-color: #2563EB;
            position: relative;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto;
        }
        
        /* Input autofill styling fix */
        input:-webkit-autofill,
        input:-webkit-autofill:hover, 
        input:-webkit-autofill:focus, 
        input:-webkit-autofill:active{
            -webkit-box-shadow: 0 0 0 30px #0F172A inset !important;
            -webkit-text-fill-color: white !important;
            transition: background-color 5000s ease-in-out 0s;
        }
    </style>
</head>
<body class="min-h-screen flex text-on-surface">

    <!-- Left Column: Promotional -->
    <div class="hidden lg:flex w-[55%] bg-surface flex-col justify-between p-12 lg:p-16 relative overflow-hidden tech-bg border-r border-white/5">
        
        <!-- Top Section -->
        <div class="z-10 mt-8 max-w-xl">
            <h1 class="text-5xl font-bold mb-2">
                <span class="text-white">Build Better.</span><br>
                <span class="text-white">Build </span><span class="text-primary">Smarter.</span>
            </h1>
            <p class="text-on-surface-variant text-lg mt-6 mb-10 leading-relaxed">
                MakeMyPC is your one-stop platform to customize, build and buy the perfect PC.
            </p>
            
            <div class="space-y-5">
                <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/5 w-max pr-8">
                    <div class="w-10 h-10 rounded-lg bg-primary/20 flex items-center justify-center text-primary shrink-0">
                        <span class="material-symbols-outlined">view_in_ar</span>
                    </div>
                    <div>
                        <h3 class="font-semibold text-white">Custom PC Builder</h3>
                        <p class="text-sm text-on-surface-variant mt-1">Choose components that fit your needs.</p>
                    </div>
                </div>
                
                <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/5 w-max pr-8">
                    <div class="w-10 h-10 rounded-lg bg-primary/20 flex items-center justify-center text-primary shrink-0">
                        <span class="material-symbols-outlined">verified_user</span>
                    </div>
                    <div>
                        <h3 class="font-semibold text-white">100% Compatibility</h3>
                        <p class="text-sm text-on-surface-variant mt-1">Smart checks to ensure perfect match.</p>
                    </div>
                </div>
                
                <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/5 w-max pr-8">
                    <div class="w-10 h-10 rounded-lg bg-primary/20 flex items-center justify-center text-primary shrink-0">
                        <span class="material-symbols-outlined">security</span>
                    </div>
                    <div>
                        <h3 class="font-semibold text-white">Trusted by Thousands</h3>
                        <p class="text-sm text-on-surface-variant mt-1">Secure payments. Genuine products.</p>
                    </div>
                </div>
                
                <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/5 w-max pr-8">
                    <div class="w-10 h-10 rounded-lg bg-primary/20 flex items-center justify-center text-primary shrink-0">
                        <span class="material-symbols-outlined">support_agent</span>
                    </div>
                    <div>
                        <h3 class="font-semibold text-white">Expert Support</h3>
                        <p class="text-sm text-on-surface-variant mt-1">We're here to help you build right.</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- PC Image - Positioned absolute to blend with the background -->
        <div class="absolute right-[-10%] bottom-[10%] w-[55%] z-0 pointer-events-none opacity-80 mix-blend-screen">
            <img src="https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&q=80&w=800" alt="Gaming PC" class="w-full h-auto object-contain drop-shadow-[0_0_30px_rgba(37,99,235,0.4)] mask-image: linear-gradient(to bottom, black 50%, transparent 100%); -webkit-mask-image: -webkit-linear-gradient(top, black 50%, transparent 100%);">
        </div>
        
        <!-- Bottom Features -->
        <div class="z-10 flex items-center gap-8 mt-16 pt-8 border-t border-white/10">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-on-surface-variant">gpp_good</span>
                <div>
                    <h4 class="text-sm font-semibold text-white">Secure Payments</h4>
                    <p class="text-xs text-on-surface-variant">100% secure checkout</p>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-on-surface-variant">replay</span>
                <div>
                    <h4 class="text-sm font-semibold text-white">Easy Returns</h4>
                    <p class="text-xs text-on-surface-variant">Hassle free returns</p>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-on-surface-variant">local_shipping</span>
                <div>
                    <h4 class="text-sm font-semibold text-white">Fast Delivery</h4>
                    <p class="text-xs text-on-surface-variant">Pan India delivery</p>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Right Column: Login Form -->
    <div class="w-full lg:w-[45%] flex flex-col items-center justify-center p-6 relative">
        <!-- Abstract Background dots for right side -->
        <div class="absolute inset-0 z-0 opacity-20 pointer-events-none" style="background-image: radial-gradient(circle, #2563EB 1px, transparent 1px); background-size: 32px 32px;"></div>
        
        <div class="w-full max-w-md z-10">
            <div class="glass-card rounded-3xl p-10 w-full mb-8">
                
                <div class="text-center mb-10">
                    <div class="hexagon mb-6">
                        <span class="text-white font-bold text-2xl">M</span>
                    </div>
                    <h2 class="text-2xl font-bold text-white mb-2">Welcome Back! 👋</h2>
                    <p class="text-sm text-on-surface-variant">Sign in to your MakeMyPC admin account</p>
                </div>
                
                <form action="admin-dashboard.html" method="GET" class="space-y-6">
                    <!-- Email Field -->
                    <div class="space-y-2">
                        <label for="email" class="block text-xs font-semibold text-white">Email Address</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <span class="material-symbols-outlined text-on-surface-variant text-[20px]">mail</span>
                            </div>
                            <input type="email" id="email" name="email" value="admin@makemypc.com" required
                                class="w-full bg-[#0F172A] border border-white/10 rounded-xl py-3 pl-11 pr-4 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                        </div>
                    </div>
                    
                    <!-- Password Field -->
                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <label for="password" class="block text-xs font-semibold text-white">Password</label>
                            <a href="#" class="text-xs text-primary hover:text-primary-light transition-colors">Forgot Password?</a>
                        </div>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <span class="material-symbols-outlined text-on-surface-variant text-[20px]">lock</span>
                            </div>
                            <input type="password" id="password" name="password" value="password123" required
                                class="w-full bg-[#0F172A] border border-white/10 rounded-xl py-3 pl-11 pr-4 text-sm text-white placeholder-on-surface-variant focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                        </div>
                    </div>
                    
                    <!-- Remember Me -->
                    <div class="flex items-center">
                        <input id="remember-me" name="remember-me" type="checkbox"
                            class="h-4 w-4 rounded border-white/10 bg-[#0F172A] text-primary focus:ring-primary focus:ring-offset-[#060B14]">
                        <label for="remember-me" class="ml-2 block text-sm text-on-surface-variant">
                            Remember me
                        </label>
                    </div>
                    
                    <!-- Sign In Button -->
                    <button type="submit"
                        class="w-full flex items-center justify-center gap-2 btn-gradient text-white rounded-xl py-3.5 px-4 text-sm font-semibold transition-all shadow-[0_0_15px_rgba(37,99,235,0.3)] hover:shadow-[0_0_25px_rgba(37,99,235,0.5)]">
                        Sign In
                        <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
                    </button>
                    
                    <!-- Divider -->
                    <div class="relative flex items-center py-2">
                        <div class="flex-grow border-t border-white/10"></div>
                        <span class="flex-shrink-0 mx-4 text-xs text-on-surface-variant">or continue with</span>
                        <div class="flex-grow border-t border-white/10"></div>
                    </div>
                    
                    <!-- Google Button -->
                    <button type="button"
                        class="w-full flex items-center justify-center gap-3 bg-transparent border border-white/10 hover:bg-white/5 text-white rounded-xl py-3 px-4 text-sm font-medium transition-all">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"></path>
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"></path>
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"></path>
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"></path>
                        </svg>
                        Continue with Google
                    </button>
                    
                    <div class="text-center pt-2">
                        <p class="text-xs text-on-surface-variant">New to MakeMyPC? <a href="#" class="text-primary hover:text-primary-light transition-colors">Contact Administrator</a></p>
                    </div>
                </form>
            </div>
            
            <div class="flex items-center justify-center gap-2 text-on-surface-variant">
                <span class="material-symbols-outlined text-[18px] text-green-500">verified_user</span>
                <span class="text-xs">Your data is protected with enterprise-grade security</span>
            </div>
        </div>
    </div>

</body>
</html>
"""

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("login.html updated successfully!")
