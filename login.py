# login.py
from data_storage import load_users, save_users

# Load user data on module import
users = load_users()

def create_login():
    """Create a new user login."""
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try logging in or use a different username.")
        return
    password = input("Enter a new password: ")
    users[username] = password
    save_users(users)
    print("User created successfully!")

def login():
    """Log in a user."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False