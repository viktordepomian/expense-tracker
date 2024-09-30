import csv
from datetime import datetime

# First off we need to store all the expenses.
expenses = []

# View all expenses with total calculation
def view_expenses():
    if not expenses:
        print("No expenses to show.")
    else:
        print("\n### All Expenses ###")
        total_amount = 0
        # This loops through all the expenses with their given index, so we can reference them easier
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['name']} - ${expense['amount']} ({expense['category']})")
            total_amount += expense['amount']
        
        # This will display the total of all expenses at the bottom
        print(f"\n### Total Expenses: ${total_amount:.2f} ###")

# Add a new expense
def add_expense():
    # These user inputs are for the details
    name = input("Enter product name: ")
    amount = float(input("Enter the products amount: "))
    category = input("Enter product category: ")
    date = input("Enter product date (YYYY-MM-DD) or press Enter for today: ")
    # If the user does not provide a date, we use today's date
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    # This uses a dictionary to store the expenses
    expense = {"name": name, "amount": amount, "category": category, "date": date}
    expenses.append(expense)  # Save the new expense dictionary to the list at the top called "expenses"
    print("Expense added successfully!")

# Remove an expense
def remove_expense():
    view_expenses()
    if expenses:
        try:
            expense_num = int(input("\nEnter the number of the product you wish to remove: "))
            # Check if the given number is valid
            if 1 <= expense_num <= len(expenses):
                removed_expense = expenses.pop(expense_num - 1)
                print(f"Removed product: {removed_expense['name']} - ${removed_expense['amount']}")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Edit an expense
def edit_expense():
    view_expenses()
    if expenses:
        try:
            expense_num = int(input("\nEnter the number of the product to edit: "))
            # It first needs to check if the chosen expense exists
            if 1 <= expense_num <= len(expenses):
                expense = expenses[expense_num - 1]
                print(f"Editing product: {expense['name']} - ${expense['amount']} ({expense['category']})")
                
                # Asks the user for the new value(s). Enter will skip the value change
                new_name = input(f"Enter new name (or press Enter to keep '{expense['name']}'): ")
                new_amount = input(f"Enter new amount (or press Enter to keep '{expense['amount']}'): ")
                new_category = input(f"Enter new category (or press Enter to keep '{expense['category']}'): ")
                
                # If given a new value it will update it
                if new_name:
                    expense['name'] = new_name
                if new_amount:
                    expense['amount'] = float(new_amount)
                if new_category:
                    expense['category'] = new_category
                
                print("Product updated successfully!")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Export expenses to a CSV file
def export_expenses_to_file():
    filename = input("Enter the filename to export to (e.g., products.csv): ")
    if not filename.endswith('.csv'):
        filename += '.csv'

    # Open the file in write mode and use csv.DictWriter to write the data
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount", "category", "date"])
        writer.writeheader()  # Write CSV header
        writer.writerows(expenses)  # Write all expenses
    print(f"Expenses exported to {filename} successfully!")

# Show options
while True:
    print("\n## EXPENSE TRACKER ##")
    print("1. VIEW")
    print("2. ADD")
    print("3. REMOVE")
    print("4. EDIT")
    print("5. EXPORT TO FILE")
    print("6. EXIT")

    choice = input("Choose an option: ")

    if choice == "1":
        view_expenses()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        remove_expense()
    elif choice == "4":
        edit_expense()
    elif choice == "5":
        export_expenses_to_file()
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
