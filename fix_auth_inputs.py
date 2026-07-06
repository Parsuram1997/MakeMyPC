import sys

def fix_inputs(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Replace the class strings in inputs
        old_class = 'class="input-neural w-full pl-10 pr-4 py-3 rounded text-body-md text-on-surface placeholder:text-outline-variant"'
        new_class = 'class="w-full bg-white/5 border border-white/10 focus:border-electric-blue focus:bg-white/10 outline-none pl-10 pr-4 py-3 rounded text-body-md text-on-surface placeholder:text-outline-variant transition-all"'
        
        if old_class in text:
            text = text.replace(old_class, new_class)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Fixed inputs in {filename}")
        else:
            print(f"No match found in {filename}")
    except Exception as e:
        print(f"Error on {filename}: {e}")

fix_inputs('login.html')
fix_inputs('signup.html')
