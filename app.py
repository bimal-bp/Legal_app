import streamlit as st

# Temporary user storage (for demo purposes)
users_db = {
    "client@example.com": {"password": "client123", "role": "Client"},
    "lawyer@example.com": {"password": "lawyer123", "role": "Lawyer"},
}

# Function to check authentication
def check_auth():
    return st.session_state.get("user", None)

# Function to sign in
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = users_db.get(email)
        if user and user["password"] == password:
            st.session_state["user"] = email
            st.session_state["role"] = user["role"]
            st.success("Login Successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid Credentials")

# Function to sign up (store new users in the dictionary)
def signup():
    st.subheader("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Client", "Lawyer"])
    
    if st.button("Signup"):
        if email in users_db:
            st.error("User already exists!")
        else:
            users_db[email] = {"password": password, "role": role}
            st.success("Signup Successful! Please login.")

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
        role = st.session_state["role"]

        if role == "Client":
            client_home()
        elif role == "Lawyer":
            lawyer_home()
        else:
            st.error("Role not found. Please contact support.")

        if st.sidebar.button("Logout"):
            del st.session_state["user"]
            del st.session_state["role"]
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
