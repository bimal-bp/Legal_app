import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials, firestore
import requests

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")  # Replace with your Firebase service account JSON file
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to check authentication
def check_auth():
    if "user" not in st.session_state:
        return None
    return st.session_state["user"]

# Function to sign in
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.get_user_by_email(email)
            st.session_state["user"] = user
            st.session_state["email"] = email
            st.success("Login Successful!")
            st.experimental_rerun()
        except Exception as e:
            st.error("Invalid Credentials")

# Function to sign up
def signup():
    st.subheader("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Client", "Lawyer"])
    
    if st.button("Signup"):
        try:
            user = auth.create_user(email=email, password=password)
            db.collection("users").document(user.uid).set({"email": email, "role": role})
            st.success("Signup Successful! Please login.")
        except Exception as e:
            st.error("Error creating user")

# Function to get user role
def get_user_role(email):
    users_ref = db.collection("users").where("email", "==", email).stream()
    for user in users_ref:
        return user.to_dict().get("role")
    return None

# Home Page for Clients
def client_home():
    st.title("Client Dashboard")
    st.write("Welcome to the Client Portal")

# Home Page for Lawyers
def lawyer_home():
    st.title("Lawyer Dashboard")
    st.write("Welcome to the Lawyer Portal")

# Main Streamlit App Logic
def main():
    st.sidebar.title("Navigation")
    user = check_auth()

    if user:
        email = st.session_state["email"]
        role = get_user_role(email)

        if role == "Client":
            client_home()
        elif role == "Lawyer":
            lawyer_home()
        else:
            st.error("Role not found. Please contact support.")

        if st.sidebar.button("Logout"):
            del st.session_state["user"]
            del st.session_state["email"]
            st.success("Logged out successfully!")
            st.experimental_rerun()
    else:
        page = st.sidebar.radio("Login / Signup", ["Login", "Signup"])
        if page == "Login":
            login()
        else:
            signup()

if __name__ == "__main__":
    main()
