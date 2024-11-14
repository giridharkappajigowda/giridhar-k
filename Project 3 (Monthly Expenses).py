# Import required modules
import datetime

# Define a dictionary to store expense data
expense_data = {}


# Function to add new expense
def add_expense():
    date = datetime.date.today()
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")

    # Store the expense data
    if date not in expense_data:
        expense_data[date] = []
    expense_data[date].append({"amount": amount, "description": description, "category": category})

    print("Expense added successfully!")


# Function to view monthly summary
def view_monthly_summary():
    month = input("Enter the month (e.g., January, February, ...): ")
    total_amount = 0
    for date, expenses in expense_data.items():
        if date.strftime("%B") == month:
            for expense in expenses:
                total_amount += expense["amount"]
    print(f"Total amount spent in {month}: {total_amount:.2f}")


# Function to view category-wise expenditure
def view_category_wise_expenditure():
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    total_amount = 0
    for date, expenses in expense_data.items():
        for expense in expenses:
            if expense["category"] == category:
                total_amount += expense["amount"]
    print(f"Total amount spent on {category}: {total_amount:.2f}")


# Function to display user interface
def display_ui():
    print("Expense Tracker")
    print("1. Add new expense")
    print("2. View monthly summary")
    print("3. View category-wise expenditure")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_monthly_summary()
    elif choice == "3":
        view_category_wise_expenditure()
    elif choice == "4":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        display_ui()


# Main function
def main():
    while True:
        display_ui()


if __name__ == "__main__":
    main()