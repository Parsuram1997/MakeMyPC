import os
import glob

directory = "c:/Projects/MakeMyPC/"
html_files = glob.glob(os.path.join(directory, "*.html"))

target_block = """            <div class="flex gap-3 items-center opacity-60 grayscale hover:grayscale-0 transition-all">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png" alt="VISA" class="h-3 object-contain">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Mastercard_2019_logo.svg" alt="MasterCard" class="h-4 object-contain">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/UPI-Logo-vector.svg" alt="UPI" class="h-4 object-contain">
            </div>"""

replacement_block = """            <div class="flex gap-2 items-center">
                <div class="bg-white px-2 py-1 rounded flex items-center justify-center opacity-80 hover:opacity-100 transition-opacity">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg" alt="VISA" class="h-3 object-contain">
                </div>
                <div class="bg-white px-2 py-1 rounded flex items-center justify-center opacity-80 hover:opacity-100 transition-opacity">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="MasterCard" class="h-3 object-contain">
                </div>
                <div class="bg-white px-2 py-1 rounded flex items-center justify-center opacity-80 hover:opacity-100 transition-opacity">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/UPI-Logo-vector.svg" alt="UPI" class="h-3 object-contain">
                </div>
            </div>"""

count = 0
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if target_block in content:
        new_content = content.replace(target_block, replacement_block)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Successfully fixed payment logos in {count} HTML files.")
