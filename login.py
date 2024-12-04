# login.py
from data_storage import load_users, save_users

# Load user data on module import
users = load_users()

def create_login():
    """Create a new user login."""
    username = input("Enter a new username: ") # user input new username
    if username in users: # check if the entered username exists in users dict
        print("Username already exists. Try logging in or use a different username.")
        return
    password = input("Enter a new password: ") # user input new password
    users[username] = password # adds username and password to users dict (username = key, password = value)
    save_users(users) # calls function to save updated users dict
    print("User created successfully!")

def login():
    """Log in a user."""
    username = input("Enter your username: ") # user input username
    password = input("Enter your password: ") # user input password
    if username in users and users[username] == password: # checks if username and password exists and matches
        print("Login successful!")
        return True # indicate successful login
    else:
        print("Invalid username or password.")
        return False # indicate unsuccessful login