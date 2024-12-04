# utility.py
from data_storage import load_data, save_data

# Load data on module import
data = load_data()

def add_expense():
    """Add a new expense and save it to the data file."""
    category = input("Enter category: ") # user input category
    amount = float(input("Enter amount: ")) # user input amount
    if category not in data["expenses"]: # check if the category doesnt already exist in expenses
        data["expenses"][category] = amount # add new category with amount
    else:
        data["expenses"][category] += amount # add amount to existing value for that category
    save_data(data) # call function to save updated data
    print("Expense added successfully!")
#NABIL
def view_expenses():
    """View all expenses."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        for category, amount in data["expenses"].items():
            print(f"Category: {category}, Amount: ${amount}")

def delete_expense():
    """Delete an expense by its category and save the change."""
    category = input("Enter category to delete: ") # user input category to delete
    if category in data["expenses"]: # check if the category exists in the expenses
        del data["expenses"][category] # remove category from the expenses dict
        save_data(data) # call function to save updated data
        print("Expense deleted successfully!")
    else: # if category not found
        print("Expense not found.")

def set_budget():
    """Set a budget for a category and save it to the data file."""
    category = input("Enter category: ")
    if category not in data["budgets"]:
        limit = float(input("Enter budget limit: "))
        data["budgets"][category] = [limit, 0]  # Default spent = 0
        save_data(data)
        print(f"Budget set for {category}.")
    else:
        print("Budget for this category already exists.")

def view_budgets():
    """View all budgets."""
    if not data["budgets"]:
        print("No budgets set yet.")
    else:
        for category, details in data["budgets"].items():
            print(f"Category: {category}, Limit: ${details[0]}, Spent: ${details[1]}")

def update_expense():
    """Update an existing expense and save the change."""
    category = input("Enter the category of the expense to update: ")
    if category in data["expenses"]:
        new_amount = float(input("Enter the new amount: "))
        data["expenses"][category] = new_amount
        save_data(data)
        print("Expense updated successfully!")
    else:
        print("Expense not found.")

def reset_budget():
    """Reset the budget for a category and save the change."""
    category = input("Enter category to reset: ")
    if category in data["budgets"]:
        data["budgets"][category][1] = 0
        save_data(data)
        print(f"Budget for {category} has been reset.")
    else:
        print("Category not found.")

def generate_summary():
    """Generate a summary of total expenses for each category."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        print("\n--- Expense Summary ---")
        for category, amount in data["expenses"].items():
            print(f"Category: {category}, Total Spent: ${amount}")
#NABIL
def clear_all_expenses(): 
    """Clear all expense records and save the change."""
    confirmation = input("Are you sure you want to clear all expenses? (yes/no): ").lower()
    if confirmation == "yes":
        data["expenses"].clear()
        save_data(data)
        print("All expenses cleared.")
    else:
        print("Operation canceled.")