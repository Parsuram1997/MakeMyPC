import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, collection, addDoc, getDocs, deleteDoc, updateDoc, arrayUnion, arrayRemove } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
import { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyA4m5APkD8zTYn6-usKu8T9tUNRVmSV9vI",
  authDomain: "makemypc.firebaseapp.com",
  projectId: "makemypc",
  storageBucket: "makemypc.firebasestorage.app",
  messagingSenderId: "105096472355",
  appId: "1:105096472355:web:09e751214975ed186b8e96",
  measurementId: "G-6DPZWS0RS5"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

const storage = getStorage(app);

export { auth, db, storage, ref, uploadBytes, getDownloadURL, doc, setDoc, getDoc, collection, addDoc, getDocs, deleteDoc, updateDoc, arrayUnion, arrayRemove, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged, GoogleAuthProvider, signInWithPopup };
