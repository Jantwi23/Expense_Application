# File names for storing budget data and user login information.
DATA_FILE = "budget_data.txt"
USER_FILE = "user_data.txt"

def load_data():
    """Load expenses and budgets from a text file into a dictionary."""
    # Initialize an empty dictionary with keys for expenses and budgets.
    data = {"expenses": {}, "budgets": {}}
    try:
        # Attempt to open the budget data file in read mode.
        with open(DATA_FILE, "r") as file:
            # Read each line, split it into a key and value, and update the dictionary.
            for line in file:
                key, value = line.strip().split(":", 1)
                # Convert the value back to its original data type using `eval`.
                data[key] = eval(value)
    except FileNotFoundError:
        # If the file does not exist, inform the user and start with an empty dictionary.
        print("No data file found. Starting fresh.")
    # Return the loaded data as a dictionary.
    return data

def save_data(data):
    """Save the dictionary data to a text file."""
    # Open the budget data file in write mode.
    with open(DATA_FILE, "w") as file:
        # Write each key-value pair to the file in "key:value" format.
        for key, value in data.items():
            file.write(f"{key}:{value}\n")

def load_users():
    """Load user login information from a text file into a dictionary."""
    # Initialize an empty dictionary to store user login data.
    users = {}
    try:
        # Attempt to open the user data file in read mode.
        with open(USER_FILE, "r") as file:
            # Read each line, split it into username and password, and update the dictionary.
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        # If the file does not exist, inform the user and start with an empty dictionary.
        print("No user data file found. Starting fresh.")
    # Return the loaded user data as a dictionary.
    return users

def save_users(users):
    """Save the user login information to a text file."""
    # Open the user data file in write mode.
    with open(USER_FILE, "w") as file:
        # Write each username-password pair to the file in "username:password" format.
        for username, password in users.items():
            file.write(f"{username}:{password}\n")
