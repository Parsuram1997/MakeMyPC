import re

def print_steps(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Try to match the steps in the top nav of the builder
            steps = re.findall(r'<div class="[^"]*w-8 h-8 rounded-full[^"]*">\s*<span>([^<]+)</span>\s*</div>\s*<span class="[^"]*">([^<]+)</span>', content)
            if not steps:
                # Try another pattern
                steps = re.findall(r'<div class="[^"]*rounded-full[^"]*">\s*<span>([^<]+)</span>\s*</div>\s*<span class="[^"]*">([^<]+)</span>', content)
            if not steps:
                steps = re.findall(r'<div class="[^"]*rounded-full[^"]*">\s*(\d+)\s*</div>\s*<span class="[^"]*">([^<]+)</span>', content)
            
            print(f'{file_path} steps:', steps)
    except Exception as e:
        print(e)

print_steps('smart-builder.html')
print_steps('custom-pc-builder.html')
