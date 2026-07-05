import os
import glob

directory = "c:/Projects/MakeMyPC/"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_url = "https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg"
new_url = "https://cdn.simpleicons.org/visa/1434CB"

count = 0
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_url in content:
        new_content = content.replace(old_url, new_url)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Successfully fixed Visa logo URL in {count} HTML files.")
