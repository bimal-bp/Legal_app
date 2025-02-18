import os
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

# Load Firebase credentials using an environment variable (or direct file path)
firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-credentials.json")

# Check if the file exists at the specified path
if not os.path.exists(firebase_credentials_path):
    st.error("Firebase credentials file not found. Please ensure the correct path is provided.")
else:
    # Initialize Firebase with the credentials
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)

    # Initialize Firestore DB
    db = firestore.client()

    # Function to add data to Firestore
    def add_sample_data():
        # Define the collection name (e.g., 'users')
        collection_name = "users"  # Change this to your collection name
        
        # Define sample data to insert
        sample_data = [
            {"name": "Alice", "age": 30, "email": "alice@example.com"},
            {"name": "Bob", "age": 25, "email": "bob@example.com"},
            {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
        ]
        
        # Add documents to the collection
        for data in sample_data:
            db.collection(collection_name).add(data)
        st.success("Sample data added successfully!")

    # Call the function to add data
    add_sample_data()

    # Function to get data from Firestore
    @st.cache
    def get_data_from_firestore():
        # Replace 'users' with the actual collection name in your Firestore
        users_ref = db.collection("users")  # Change this to your collection name
        docs = users_ref.stream()

        data = []
        for doc in docs:
            data.append(doc.to_dict())
        
        return data

    # Display data from Firestore in Streamlit
    data = get_data_from_firestore()
    st.write(data)

    # Optionally, add a feature to display the data in a more readable format
    if data:
        st.subheader("User Data")
        for user in data:
            st.write(f"Name: {user.get('name')}, Age: {user.get('age')}, Email: {user.get('email')}")
    else:
        st.warning("No data found in Firestore.")
