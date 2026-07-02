import os

with open(r'c:\Projects\MakeMyPC\js\global.js', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("function showToast(message, type = 'info') {", "window.showToast = function(message, type = 'info') {")
c = c.replace("showToast(", "window.showToast(")
c = c.replace("window.window.showToast(", "window.showToast(")

with open(r'c:\Projects\MakeMyPC\js\global.js', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated global.js')
