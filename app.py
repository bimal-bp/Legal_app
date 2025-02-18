import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, auth
import geocoder

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Functions to check Firebase Auth and fetch user data
def get_user_type(user):
    doc_ref = db.collection("users").document(user.uid)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get("Type")
    else:
        return None

# Streamlit UI
def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        try:
            user = auth.get_user_by_email(email)
            # Authenticate with Firebase
            if user:
                user_type = get_user_type(user)
                st.session_state.user = user
                st.session_state.user_type = user_type
                st.success("Logged in successfully")
                return user_type
        except Exception as e:
            st.error(f"Error: {e}")
    
def permission_page():
    st.title("Location Permission")
    st.write("Please grant location access to continue.")
    
    if st.button("Grant Permission"):
        # Use geocoder or Location APIs to request permissions
        location = geocoder.ip('me')
        if location:
            st.success(f"Location granted: {location}")
        else:
            st.error("Permission denied")

def main_app(user_type):
    if user_type == "Lawyer":
        st.title("Lawyer Dashboard")
        # Lawyer-specific functionality here
        st.write("Welcome Lawyer! Here's your dashboard.")
    elif user_type == "Client":
        st.title("Client Dashboard")
        # Client-specific functionality here
        st.write("Welcome Client! Here's your dashboard.")
    else:
        st.write("Error: No user type found")

# Main logic
if 'user' not in st.session_state:
    st.session_state.user = None
    st.session_state.user_type = None

if st.session_state.user is None:
    user_type = login_page()
    if user_type:
        main_app(user_type)
elif st.session_state.user_type == "Lawyer" or st.session_state.user_type == "Client":
    main_app(st.session_state.user_type)
else:
    permission_page()
