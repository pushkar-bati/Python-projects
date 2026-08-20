import json
import os
from datetime import datetime


BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"
TRANSACTIONS_FILE = "data/transactions.json"


def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(filename, data):
    os.makedirs("data", exist_ok=True)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def issue_book():
    books = load_data(BOOKS_FILE)
    members = load_data(MEMBERS_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    print("\n========== ISSUE BOOK ==========")

    if not books:
        print("No books available in the library.")
        return

    if not members:
        print("No members registered.")
        return

    try:
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Please enter valid numeric IDs.")
        return

    book = None
    member = None

    for item in books:
        if item["id"] == book_id:
            book = item
            break

    for item in members:
        if item["id"] == member_id:
            member = item
            break

    if book is None:
        print("Book not found.")
        return

    if member is None:
        print("Member not found.")
        return

    if not book["available"]:
        print("This book is already issued.")
        return

    transaction_id = (
        max([t["id"] for t in transactions], default=0) + 1
    )

    issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "id": transaction_id,
        "book_id": book_id,
        "member_id": member_id,
        "issue_date": issue_date,
        "return_date": None
    }

    transactions.append(transaction)

    book["available"] = False

    save_data(BOOKS_FILE, books)
    save_data(TRANSACTIONS_FILE, transactions)

    print("\nBook issued successfully!")
    print(f"Transaction ID: {transaction_id}")
    print(f"Book         : {book['title']}")
    print(f"Member       : {member['name']}")
    print(f"Issue Date   : {issue_date}")


def return_book():
    books = load_data(BOOKS_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    print("\n========== RETURN BOOK ==========")

    try:
        book_id = int(input("Enter book ID: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    active_transaction = None

    for transaction in transactions:
        if (
            transaction["book_id"] == book_id
            and transaction["return_date"] is None
        ):
            active_transaction = transaction
            break

    if active_transaction is None:
        print("This book is not currently issued.")
        return

    book = None

    for item in books:
        if item["id"] == book_id:
            book = item
            break

    if book is None:
        print("Book not found.")
        return

    return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    active_transaction["return_date"] = return_date

    book["available"] = True

    save_data(BOOKS_FILE, books)
    save_data(TRANSACTIONS_FILE, transactions)

    print("\nBook returned successfully!")
    print(f"Book        : {book['title']}")
    print(f"Return Date : {return_date}")


def view_issued_books():
    books = load_data(BOOKS_FILE)
    members = load_data(MEMBERS_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    print("\n========== ISSUED BOOKS ==========")

    issued_transactions = [
        transaction
        for transaction in transactions
        if transaction["return_date"] is None
    ]

    if not issued_transactions:
        print("No books are currently issued.")
        return

    for transaction in issued_transactions:

        book = next(
            (
                book
                for book in books
                if book["id"] == transaction["book_id"]
            ),
            None
        )

        member = next(
            (
                member
                for member in members
                if member["id"] == transaction["member_id"]
            ),
            None
        )

        print("-" * 40)

        if book:
            print(f"Book ID      : {book['id']}")
            print(f"Book Title   : {book['title']}")
            print(f"Author       : {book['author']}")

        if member:
            print(f"Member ID    : {member['id']}")
            print(f"Member Name  : {member['name']}")

        print(f"Issue Date   : {transaction['issue_date']}")

    print("-" * 40)