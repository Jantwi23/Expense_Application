# utility.py
from data_storage import load_data, save_data

# Load data on module import
data = load_data()


#CHRIS
def add_expense():
    """Add a new expense and save it to the data file."""
    category = input("Enter category: ") # user input category
    amount = float(input("Enter amount: ")) # user input amount and converts to float
    if category not in data["expenses"]: # check if the category doesnt already exist in expenses
        data["expenses"][category] = amount # add new category with amount
    else: # if category exists
        data["expenses"][category] += amount # add amount to existing value for that category
    save_data(data) # call function to save updated data
    print("Expense added successfully!")


#NABIL
def view_expenses():
    """View all expenses."""
    # Check if there are any expenses recorded in the "expenses" dictionary.
    if not data["expenses"]:
        # If the dictionary is empty, inform the user that no expenses are recorded.
        print("No expenses recorded yet.")
    else:
        # If there are expenses, iterate through each category and amount in the "expenses" dictionary.
        for category, amount in data["expenses"].items():
            # Print each category and its corresponding amount in a formatted string.
            print(f"Category: {category}, Amount: ${amount}")



#CHRIS
def delete_expense():
    """Delete an expense by its category and save the change."""
    category = input("Enter category to delete: ") # user input category to delete
    if category in data["expenses"]: # check if the category exists in the expenses
        del data["expenses"][category] # remove category from the expenses dict
        save_data(data) # call function to save updated data
        print("Expense deleted successfully!")
    else: # if category not found
        print("Expense not found.")
#CHRIS
def set_budget():
    """Set a budget for a category and save it to the data file."""
    category = input("Enter category: ") # user input category for budget
    if category not in data["budgets"]: # check if category doesnt already exists in budget
        limit = float(input("Enter budget limit: ")) # user input budget limit and convert to float
        data["budgets"][category] = [limit, 0]  # sets the budget limit and makes default spent = 0
        save_data(data) # call function to save updated data
        print(f"Budget set for {category}.")
    else: # if budget category already exists
        print("Budget for this category already exists.")


#CHRIS
def view_budgets():
    """View all budgets."""
    if not data["budgets"]: # check if budget dict is empty
        print("No budgets set yet.")
    else: # if there are budgets
        for category, details in data["budgets"].items(): # iterates through each category and its details (limit and spent)
            print(f"Category: {category}, Limit: ${details[0]}, Spent: ${details[1]}") # displays the budget details


#CHRIS
def update_expense():
    """Update an existing expense and save the change."""
    category = input("Enter the category of the expense to update: ") # user input category to update
    if category in data["expenses"]: # check if category exists in expense
        new_amount = float(input("Enter the new amount: ")) # user input new amount and convert to float
        data["expenses"][category] = new_amount # updates the amount for specified category
        save_data(data) # call function to save updated data
        print("Expense updated successfully!")
    else: # if category not found
        print("Expense not found.")


#NABIL
def reset_budget():
    """Reset the budget for a category and save the change."""
    # Ask user to input category to reset.
    category = input("Enter category to reset: ")
    # Checks to see if category exists in budget.
    if category in data["budgets"]:
        # Reset the spent value for the category to 0.
        data["budgets"][category][1] = 0 
        # Save the updated data and inform that budget has been reset.
        save_data(data) 
        print(f"Budget for {category} has been reset.")
    else: 
        # If the category is not found, cancel and notify them.
        print("Category not found.")


#CHRIS
def generate_summary():
    """Generate a summary of total expenses for each category."""
    if not data["expenses"]: # check if expense dict is empty
        print("No expenses recorded yet.")
    else: # if there are expenses:
        print("\n--- Expense Summary ---")
        for category, amount in data["expenses"].items(): # iterates through each category and amount
            print(f"Category: {category}, Total Spent: ${amount}") # display category and total spent


#NABIL
def clear_all_expenses():
    """Clear all expense records and save the change."""
    # Ask the user for confirmation to clear all expenses.
    # Convert the input to lowercase to handle case-insensitive responses.
    confirmation = input("Are you sure you want to clear all expenses? (yes/no): ").lower()

    # Check if the user confirmed by typing "yes".
    if confirmation == "yes":
        # Clear all entries from the "expenses" dictionary.
        data["expenses"].clear()

        # Save the updated data (after clearing) to ensure persistence.
        save_data(data)

        # Inform the user that all expenses have been cleared.
        print("All expenses cleared.")
    else:
        # If the user did not confirm, cancel the operation and notify them.
        print("Operation canceled.")

        
        
        
         