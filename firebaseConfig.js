<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-analytics.js";
  // Add other Firebase products you plan to use (e.g., Auth, Firestore)
  // import { getAuth } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-auth.js";
  // import { getFirestore } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-firestore.js";

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAAMjMXlpIPBof-7ZjQiQypAA9P1X0JhE0",
    authDomain: "legal-aid-44a46.firebaseapp.com",
    databaseURL: "https://legal-aid-44a46-default-rtdb.firebaseio.com",
    projectId: "legal-aid-44a46",
    storageBucket: "legal-aid-44a46.firebasestorage.app",
    messagingSenderId: "384870336246",
    appId: "1:384870336246:web:32fd2faef7bb537ef24ed7",
    measurementId: "G-ET0KJ54Q8K"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  
  // Analytics initialization (optional, depending on your needs)
  const analytics = getAnalytics(app);
  
  // If you're using Firebase Auth or Firestore, initialize those services too
  // const auth = getAuth(app);
  // const db = getFirestore(app);

  // You can now interact with Firebase services
</script>
