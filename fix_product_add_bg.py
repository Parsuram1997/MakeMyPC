with open('product-add.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace bg-[#0a0f1c] with bg-surface-deep
content = content.replace('bg-[#0a0f1c]', 'bg-surface-deep')

# Remove sticky top-0 from header
content = content.replace('sticky top-0', '')

# Ensure body has bg-surface-deep text-on-surface font-body-md overflow-x-hidden
if '<body class="overflow-x-hidden">' in content:
    content = content.replace('<body class="overflow-x-hidden">', '<body class="bg-surface-deep text-on-surface font-body-md overflow-x-hidden">')

with open('product-add.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed product-add.html")
