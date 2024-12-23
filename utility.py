from data_storage import load_data, save_data

# Load data on module import
data = load_data()

def add_expense():
    """Add a new expense and save it to the data file."""
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    if category not in data["expenses"]:
        data["expenses"][category] = amount
    else:
        data["expenses"][category] += amount
    if category in data["budgets"]:
        data["budgets"][category][1] += amount  # Update spent value
    save_data(data)
    print("Expense added successfully!")

def view_expenses():
    """View all expenses."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        for category, amount in data["expenses"].items():
            print(f"Category: {category}, Amount: ${amount}")

def delete_expense():
    """Delete an expense by its category and save the change."""
    category = input("Enter category to delete: ")
    if category in data["expenses"]:
        del data["expenses"][category]
        save_data(data)
        print("Expense deleted successfully!")
    else:
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

def clear_all_expenses():
    """Clear all expense records and save the change."""
    confirmation = input("Are you sure you want to clear all expenses? (yes/no): ").lower()
    if confirmation == "yes":
        data["expenses"].clear()
        save_data(data)
        print("All expenses cleared.")
    else:
        print("Operation canceled.")

def check_budget_status():
    """Check whether any category is over budget and display the status."""
    if not data["budgets"]:
        print("No budgets set. Please set budgets first.")
    else:
        print("\n--- Budget Status ---")
        for category, details in data["budgets"].items():
            limit, spent = details
            status = "Over Budget" if spent > limit else "Within Budget"
            print(f"Category: {category}, Limit: ${limit}, Spent: ${spent}, Status: {status}")
