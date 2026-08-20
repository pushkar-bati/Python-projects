import json
import os


BOOKS_FILE = "data/books.json"


def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []

    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_books(books):
    os.makedirs("data", exist_ok=True)

    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()

    print("\n========== ADD BOOK ==========")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    if books:
        book_id = max(book["id"] for book in books) + 1
    else:
        book_id = 1

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    save_books(books)

    print(f"\nBook added successfully!")
    print(f"Book ID: {book_id}")


def view_books():
    books = load_books()

    print("\n========== ALL BOOKS ==========")

    if not books:
        print("No books found.")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print("-" * 35)
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Status   : {status}")

    print("-" * 35)


def search_book():
    books = load_books()

    print("\n========== SEARCH BOOK ==========")

    search = input("Enter title or author to search: ").strip().lower()

    if not search:
        print("Search value cannot be empty.")
        return

    found = False

    for book in books:
        if (
            search in book["title"].lower()
            or search in book["author"].lower()
        ):
            status = "Available" if book["available"] else "Issued"

            print("\nBook Found")
            print("-" * 35)
            print(f"ID       : {book['id']}")
            print(f"Title    : {book['title']}")
            print(f"Author   : {book['author']}")
            print(f"Status   : {status}")

            found = True

    if not found:
        print("\nNo matching book found.")