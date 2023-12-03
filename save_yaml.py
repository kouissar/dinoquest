import streamlit as st
import yaml
import os

# Function to save user data to YAML file
def save_user_data(user_data, filename="users.yaml"):
    # Load existing data
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            existing_data = yaml.safe_load(file) or {}
    else:
        existing_data = {}

    # Add new user
    existing_data[user_data['username']] = user_data

    # Write updated data back to file
    with open(filename, 'w') as file:
        yaml.dump(existing_data, file)

# Streamlit form for user registration
def user_registration_form():
    with st.form("User Registration Form"):
        username = st.text_input("Username")
        full_name = st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        submit_button = st.form_submit_button("Register")

        if submit_button:
            user_data = {
                "username": username,
                "full_name": full_name,
                "password": password,  # For a real app, hash the password!
                "email": email
            }
            save_user_data(user_data)
            st.success(f"User {username} registered successfully!")

# Main function
def main():
    st.title("User Registration")
    user_registration_form()

if __name__ == "__main__":
    main()
