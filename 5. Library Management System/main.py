from books import (
    add_book,
    view_books,
    search_book
)

from members import (
    add_member,
    view_members
)

from transactions import (
    issue_book,
    return_book,
    view_issued_books
)


def display_menu():
    print("\n" + "=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View Issued Books")
    print("9. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            add_member()

        elif choice == "5":
            view_members()

        elif choice == "6":
            issue_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            view_issued_books()

        elif choice == "9":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()