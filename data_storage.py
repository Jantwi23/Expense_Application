# data_storage.py

DATA_FILE = "budget_data.txt"
USER_FILE = "user_data.txt"

def load_data():
    """Load expenses and budgets from a text file into a dictionary."""
    data = {"expenses": {}, "budgets": {}}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                key, value = line.strip().split(":", 1)
                data[key] = eval(value)
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
    return data

def save_data(data):
    """Save the dictionary data to a text file."""
    with open(DATA_FILE, "w") as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")

def load_users():
    """Load user login information from a text file into a dictionary."""
    users = {}
    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        print("No user data file found. Starting fresh.")
    return users

def save_users(users):
    """Save the user login information to a text file."""
    with open(USER_FILE, "w") as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")
