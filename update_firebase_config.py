import sys

with open('js/firebase-config.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Check if already has getStorage
if "getStorage" not in text:
    new_import = 'import { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";'
    # Insert right after the third import
    text = text.replace('from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";', 'from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";\n' + new_import)
    
    # Export it
    text = text.replace('export { auth, db', 'const storage = getStorage(app);\n\nexport { auth, db, storage, ref, uploadBytes, getDownloadURL')
    
    with open('js/firebase-config.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("firebase-config.js updated successfully with Storage.")
else:
    print("Storage is already in firebase-config.js")
