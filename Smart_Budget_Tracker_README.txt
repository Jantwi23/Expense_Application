Expense Application
Smart Budget Tracker Project

Description
The Smart Budget Tracker is a Python-based terminal application designed to help users manage their personal finances effectively. It provides a simple, text-based interface to track expenses, set budgets, view summaries, and manage user accounts. The application ensures that each user’s budget data is securely saved and associated with their unique account through a login system.

The Smart Budget Tracker is an intuitive tool for gaining insights into spending habits and improving financial planning.

Specifications
a. Tentative I/O
- The application presents users with a menu-driven interface listing all available functionalities.
- Users input values such as expense amounts, categories, and budget limits.
- The application provides outputs like expense summaries, budget information, and confirmation messages for actions taken.

b. Structure
- The project is modular, containing the following main components:
  - Data Storage Module: Handles saving and loading expenses, budgets, and user accounts in text files.
  - Login Module: Manages user authentication and ensures data integrity for individual users.
  - Expense Management Module: Allows users to add, view, update, and delete expenses.
  - Budget Management Module: Enables users to set, view, and reset budget limits for categories.
  - Report Generation Module: Provides a summary of total expenses for each category.

Functionalities
1. Add Expense
   - Allows users to record expenses by entering a category and amount.
   - Automatically adds the amount to the total for that category.

2. Delete Expense
   - Enables users to remove an expense record by specifying the category.

3. View All Expenses
   - Displays all recorded expenses, grouped by category.

4. Set Budget for Category
   - Users can set a spending limit for specific categories (e.g., Food, Transport).

5. Update Expense
   - Allows users to update the total spending for a category.

6. View All Budgets
   - Displays all budget categories, their spending limits, and the total amount spent so far.

7. Generate Summary
   - Provides a summary of total expenses for each category, offering insights into spending patterns.

8. Reset Budget
   - Resets the spent amount for a specific category to zero.

9. Clear All Expenses
   - Clears all recorded expense data.

10. Login and User Accounts
    - Users can create unique accounts with a username and password.
    - Each user’s budget data is saved separately and securely.

Module Details
Main Menu and Input Handling
- Displays a clear menu listing all functionalities.
- Accepts user input to navigate to the appropriate module.

Expense Management
- Add Expense: Users can input a category and amount to record an expense.
- Delete Expense: Removes an expense for a specific category.
- View All Expenses: Lists all expenses, organized by category.

Budget Management
- Set Budget for Category: Allows setting spending limits for categories.
- Update Expense: Modifies the total spending for a specific category.
- View All Budgets: Displays all categories with their respective limits and amounts spent.

Report Generation
- Generate Summary: Provides a summary of total expenses, grouped by category.

Data Integrity
- User accounts and budget data are securely saved in text files, ensuring persistence across sessions.

Technical Details
- Programming Language: Python
- Persistence: Uses text files (budget_data.txt and user_data.txt) to save and load data.
- User Accounts: Managed via a login system, ensuring unique data for each user.

Future Enhancements
- Adding notifications or alerts for budgets nearing their limits.
- Exporting data to CSV for external analysis.
- Improved visualization of budget summaries.

Getting Started
1. Run the main.py file to start the application.
2. Create a user account or log in with an existing account.
3. Use the menu to add expenses, set budgets, and view reports.
