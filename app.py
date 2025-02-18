import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase Admin SDK
# Ensure that you provide the correct path to your Firebase credentials JSON file
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Streamlit UI
st.title("Firebase Streamlit App")

# Firebase Authentication Example
def sign_up_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        st.success(f"User {user.uid} created successfully!")
    except Exception as e:
        st.error(f"Error: {e}")

def login_user(email, password):
    try:
        # Firebase Authentication doesn't provide a simple login method in Admin SDK
        # This is a simulated example, as Firebase Admin doesn't support client-side login.
        user = auth.get_user_by_email(email)
        st.success(f"Logged in as {user.email}")
    except Exception as e:
        st.error(f"Error: {e}")

# Firestore operations (Example: Adding a document)
def add_document_to_firestore(name, age, city):
    try:
        doc_ref = db.collection('users').add({
            'name': name,
            'age': age,
            'city': city
        })
        st.success(f"Document added with ID: {doc_ref.id}")
    except Exception as e:
        st.error(f"Error: {e}")

# Form for user input
with st.form(key="auth_form"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Sign Up or Login")
    
    if submit_button:
        sign_up_user(email, password)  # Simulated Sign-Up (Admin SDK doesn't support direct login)
        login_user(email, password)  # Simulated Login

# Form for adding data to Firestore
with st.form(key="firestore_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    city = st.text_input("City")
    add_button = st.form_submit_button("Add to Firestore")

    if add_button:
        add_document_to_firestore(name, age, city)

# Displaying Firestore Data
if st.button("Show Firestore Data"):
    try:
        users_ref = db.collection('users').stream()
        for doc in users_ref:
            st.write(f"{doc.id} => {doc.to_dict()}")
    except Exception as e:
        st.error(f"Error: {e}")
