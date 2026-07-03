import os
import glob

def add_global_js():
    html_files = glob.glob('c:/Projects/MakeMyPC/*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'js/global.js' not in content:
            # find the last <script> or </body>
            # let's just replace </body> with <script src="js/global.js"></script>\n</body>
            if '</body>' in content:
                content = content.replace('</body>', '<script src="js/global.js"></script>\n</body>')
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {file}")

if __name__ == '__main__':
    add_global_js()
