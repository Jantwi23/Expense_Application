# login.py
user_database = {}  # Dictionary to store user credentials

def create_login():
    """Create a new user login."""
    print("\n--- Create New Login ---")
    username = input("Enter a new username: ")
    if username in user_database:
        print("Username already exists. Try logging in or use a different username.")
        return
    password = input("Enter a new password: ")
    user_database[username] = password
    print("User created successfully!")

def login():
    """Log in a user."""
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_database and user_database[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False