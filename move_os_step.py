import re

# 1. Update builder-app.js
app_file = "c:/Projects/MakeMyPC/js/builder-app.js"
with open(app_file, "r", encoding="utf-8") as f:
    app_content = f.read()

# Remove { id: 'os', label: 'OS', key: 'os' }
app_content = app_content.replace("    { id: 'os', label: 'OS', key: 'os' },\n", "")

# Add it to the beginning of steps
app_content = app_content.replace(
    "const steps = [\n",
    "const steps = [\n    { id: 'os', label: 'OS', key: 'os' },\n"
)

with open(app_file, "w", encoding="utf-8") as f:
    f.write(app_content)

# 2. Update builder-sidebar.js
sidebar_file = "c:/Projects/MakeMyPC/js/builder-sidebar.js"
with open(sidebar_file, "r", encoding="utf-8") as f:
    sidebar_content = f.read()

# Replace hardcoded 11 with steps.length - 1
sidebar_content = sidebar_content.replace("state.currentStepIndex === 11", "state.currentStepIndex === steps.length - 1")
sidebar_content = sidebar_content.replace("goToStep(11)", "goToStep(steps.length - 1)")

with open(sidebar_file, "w", encoding="utf-8") as f:
    f.write(sidebar_content)

print("Moved OS step to the beginning and fixed hardcoded review index.")
