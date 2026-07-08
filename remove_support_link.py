import os
import glob
import re

def remove_support_link():
    html_files = glob.glob('*.html')
    
    support_pattern = re.compile(r'\s*<a href="[^"]*" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300[^>]*>\s*<span class="material-symbols-outlined">support_agent</span>\s*<span class="text-body-sm font-medium">Support</span>\s*</a>', re.DOTALL)
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if support_pattern.search(content):
            new_content = support_pattern.sub('', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed from {filepath}")
            count += 1
            
    print(f"Removed Support link from {count} files.")

if __name__ == '__main__':
    remove_support_link()
