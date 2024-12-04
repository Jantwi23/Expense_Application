# utility.py
from data_storage import data, save_data

def add_expense():
    """Add an expense to the tracker."""
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    data["expenses"].append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")
    save_data()

def view_expenses():
    """View all expenses."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        for expense in data["expenses"]:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")

def delete_expense():
    """Delete an expense."""
    date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    initial_length = len(data["expenses"])
    data["expenses"] = [expense for expense in data["expenses"] if expense["date"] != date]
    print("Expense deleted successfully." if len(data["expenses"]) < initial_length else "No expense found.")
    save_data()

def set_budget():
    """Set a budget for a category."""
    category = input("Enter category: ")
    limit = float(input("Enter budget limit: "))
    data["budgets"][category] = {"limit": limit, "spent": 0}
    print(f"Budget set for {category}: ${limit}")
    save_data()

def view_budgets():
    """View all budgets."""
    if not data["budgets"]:
        print("No budgets set yet.")
    else:
        for category, details in data["budgets"].items():
            print(f"Category: {category}, Limit: ${details['limit']}, Spent: ${details['spent']}")

# New Functions
def update_expense():
    """Update an existing expense."""
    date = input("Enter the date of the expense to update (YYYY-MM-DD): ")
    for expense in data["expenses"]:
        if expense["date"] == date:
            print(f"Existing Record: {expense}")
            new_category = input("Enter new category (leave blank to keep current): ") or expense["category"]
            new_amount = input("Enter new amount (leave blank to keep current): ") or expense["amount"]
            expense["category"] = new_category
            expense["amount"] = float(new_amount)
            print("Expense updated successfully!")
            save_data()
            return
    print("No expense found with the given date.")

def reset_budget():
    """Reset the budget for a category."""
    category = input("Enter category to reset: ")
    if category in data["budgets"]:
        data["budgets"][category]["spent"] = 0
        print(f"Budget for {category} has been reset.")
        save_data()
    else:
        print("Category not found.")

def generate_monthly_summary():
    """Generate a monthly summary of expenses."""
    month = input("Enter the month (YYYY-MM): ")
    monthly_expenses = [expense for expense in data["expenses"] if expense["date"].startswith(month)]
    if not monthly_expenses:
        print("No expenses recorded for this month.")
    else:
        print(f"Summary for {month}:")
        total = 0
        for expense in monthly_expenses:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")
            total += expense["amount"]
        print(f"Total spent in {month}: ${total}")

def clear_all_expenses():
    """Clear all recorded expenses."""
    confirmation = input("Are you sure you want to delete all expenses? (yes/no): ").lower()
    if confirmation == "yes":
        data["expenses"].clear()
        print("All expenses cleared successfully!")
        save_data()
    else:
        print("Operation canceled.")
#