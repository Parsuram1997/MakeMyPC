import os
import glob

directory = "c:/Projects/MakeMyPC/"
html_files = glob.glob(os.path.join(directory, "*.html"))

target_block = """            <div class="flex gap-2 opacity-50 grayscale hover:grayscale-0 transition-all">
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">VISA</div>
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">MasterCard</div>
                <div class="bg-white px-2 py-1 rounded text-black text-[10px] font-bold">UPI</div>
            </div>"""

replacement_block = """            <div class="flex gap-3 items-center opacity-60 grayscale hover:grayscale-0 transition-all">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png" alt="VISA" class="h-3 object-contain">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Mastercard_2019_logo.svg" alt="MasterCard" class="h-4 object-contain">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/UPI-Logo-vector.svg" alt="UPI" class="h-4 object-contain">
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

print(f"Successfully updated payment logos in {count} HTML files.")
