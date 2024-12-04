# main.py
from utility import (
    add_expense, view_expenses, delete_expense, set_budget,
    view_budgets, update_expense, reset_budget,
    generate_monthly_summary, clear_all_expenses
)
from login import create_login, login

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
        print("8. Generate Monthly Summary")
        print("9. Clear All Expenses")
        print("10. Logout")

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
            generate_monthly_summary()
        elif choice == "9":
            clear_all_expenses()
        elif choice == "10":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

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

if __name__ == "__main__":
    start_program()
  