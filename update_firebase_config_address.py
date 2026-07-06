import sys

with open('js/firebase-config.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Add missing Firestore functions if they don't exist
if "collection" not in text:
    text = text.replace(
        'import { getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";',
        'import { getFirestore, doc, setDoc, getDoc, collection, addDoc, getDocs, deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";'
    )
    
    text = text.replace(
        'export { auth, db, storage, ref, uploadBytes, getDownloadURL, doc, setDoc, getDoc,',
        'export { auth, db, storage, ref, uploadBytes, getDownloadURL, doc, setDoc, getDoc, collection, addDoc, getDocs, deleteDoc,'
    )
    
    with open('js/firebase-config.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated firebase-config.js with Firestore subcollection functions.")
else:
    print("firebase-config.js already has subcollection functions.")
