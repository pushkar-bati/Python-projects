expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(f"Expense {index}")
        print(f"Name: {expense['name']}")
        print(f"Amount: ₹{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print("--------------------")


def calculate_total():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ₹{total:.2f}")


def view_by_category():
    category = input("Enter category: ")

    found = False
    total = 0

    print(f"\n--- Expenses in {category} ---")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"Name: {expense['name']}")
            print(f"Amount: ₹{expense['amount']:.2f}")
            print("--------------------")

            total += expense["amount"]
            found = True

    if found:
        print(f"Category total: ₹{total:.2f}")
    else:
        print("No expenses found in this category.")


def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted_expense = expenses.pop(choice - 1)
            print(
                f"Expense '{deleted_expense['name']}' "
                "deleted successfully!"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n========================")
        print("     EXPENSE TRACKER")
        print("========================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. View By Category")
        print("5. Delete Expense")
        print("6. Exit")
        print("========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            view_by_category()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()