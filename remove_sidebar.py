import re

file_path = "c:/Projects/MakeMyPC/smart-builder.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the aside
content = re.sub(r'<!-- Right: SideNavBar \(Build Summary\) -->\s*<aside.*?</aside>', '', content, flags=re.DOTALL)

# Remove the mock steps and state script
mock_script_pattern = r'<script>\s*// Mock steps for builder-sidebar\.js.*?const state = \{.*?\};\s*</script>'
content = re.sub(mock_script_pattern, '', content, flags=re.DOTALL)

# Remove builder-sidebar.js import
content = content.replace('<script src="js/builder-sidebar.js"></script>\n', '')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Removed aside and builder-sidebar.js from smart-builder.html")
