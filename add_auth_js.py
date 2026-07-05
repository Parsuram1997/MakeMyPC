import os
import glob

# Get all HTML files in current directory
html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'src="js/auth.js"' not in content:
        # We need to insert <script type="module" src="js/auth.js"></script> before </body>
        script_tag = '\n<script type="module" src="js/auth.js"></script>\n'
        
        if '</body>' in content:
            new_content = content.replace('</body>', script_tag + '</body>')
        elif '</html>' in content:
            new_content = content.replace('</html>', script_tag + '</html>')
        else:
            new_content = content + script_tag
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added auth.js to {file_path}")
    else:
        print(f"auth.js already in {file_path}")
