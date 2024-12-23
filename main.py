from utility import (
    add_expense, view_expenses, delete_expense, set_budget,
    view_budgets, update_expense, reset_budget,
    generate_summary, clear_all_expenses, check_budget_status
)
from login import create_login, login

# Main menu - handles user choices
def main_menu():
    """Main menu for the Smart Budget Tracker."""
    while True:
        print("\n--- Smart Budget Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Set Budget")
        print("5. View Budgets")
        print("6. Update an Expense")
        print("7. Reset Budget for a Category")
        print("8. Generate Summary")
        print("9. Clear All Expenses")
        print("10. Check Budget Status")
        print("11. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            view_budgets()
        elif choice == "6":
            update_expense()
        elif choice == "7":
            reset_budget()
        elif choice == "8":
            generate_summary()
        elif choice == "9":
            clear_all_expenses()
        elif choice == "10":
            check_budget_status()
        elif choice == "11":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Start program - login or create an account
def start_program():
    """Start the program with login or account creation."""
    while True:
        print("\n--- Welcome to Smart Budget Tracker ---")
        print("1. Create Login")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_login()
        elif choice == "2":
            if login():
                main_menu()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Directly call start_program()
start_program()
