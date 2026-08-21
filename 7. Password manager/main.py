import json
import os
import secrets
import string


DATA_FILE = "passwords.json"


def load_passwords():
    """Load saved passwords from the JSON file."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("\n❌ Password file is corrupted.")
        return []

    except Exception as error:
        print(f"\n❌ Error loading passwords: {error}")
        return []


def save_passwords(passwords):
    """Save passwords to the JSON file."""

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(passwords, file, indent=4)

        return True

    except Exception as error:
        print(f"\n❌ Error saving passwords: {error}")
        return False


def generate_password(length=16):
    """Generate a strong random password."""

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def add_password(passwords):
    """Add a new password entry."""

    print("\n========== ADD PASSWORD ==========")

    website = input("Enter website: ").strip()
    username = input("Enter username/email: ").strip()

    if not website or not username:
        print("\n❌ Website and username cannot be empty.")
        return

    print("\n1. Enter password manually")
    print("2. Generate strong password")

    choice = input("Choose an option: ").strip()

    if choice == "1":

        password = input("Enter password: ")

        if not password:
            print("\n❌ Password cannot be empty.")
            return

    elif choice == "2":

        while True:

            try:
                length = int(
                    input("Enter password length (8-64): ")
                )

                if 8 <= length <= 64:
                    break

                print("❌ Length must be between 8 and 64.")

            except ValueError:
                print("❌ Please enter a valid number.")

        password = generate_password(length)

        print(f"\nGenerated password: {password}")

    else:

        print("\n❌ Invalid choice.")
        return

    entry = {
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(entry)

    if save_passwords(passwords):
        print("\n✅ Password saved successfully.")


def view_passwords(passwords):
    """Display all saved passwords."""

    print("\n========== SAVED PASSWORDS ==========")

    if not passwords:
        print("No passwords saved.")
        return

    for index, entry in enumerate(passwords, start=1):

        print(f"\nPassword #{index}")
        print("--------------------------------")
        print(f"Website : {entry['website']}")
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")


def search_password(passwords):
    """Search for a password by website."""

    print("\n========== SEARCH PASSWORD ==========")

    search_term = input(
        "Enter website to search: "
    ).strip().lower()

    found = False

    for entry in passwords:

        if search_term in entry["website"].lower():

            print("\nPassword found:")
            print("--------------------------------")
            print(f"Website : {entry['website']}")
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")

            found = True

    if not found:
        print("\n❌ No matching website found.")


def delete_password(passwords):
    """Delete a saved password."""

    print("\n========== DELETE PASSWORD ==========")

    if not passwords:
        print("No passwords saved.")
        return

    for index, entry in enumerate(passwords, start=1):

        print(
            f"{index}. "
            f"{entry['website']} - "
            f"{entry['username']}"
        )

    try:

        choice = int(
            input("\nEnter password number to delete: ")
        )

        if choice < 1 or choice > len(passwords):
            print("\n❌ Invalid password number.")
            return

        deleted = passwords.pop(choice - 1)

        if save_passwords(passwords):

            print(
                f"\n✅ Deleted password for "
                f"{deleted['website']}."
            )

    except ValueError:

        print("\n❌ Please enter a valid number.")


def password_generator():
    """Generate a password without saving it."""

    print("\n========== PASSWORD GENERATOR ==========")

    while True:

        try:

            length = int(
                input("Enter password length (8-64): ")
            )

            if 8 <= length <= 64:
                break

            print("❌ Length must be between 8 and 64.")

        except ValueError:

            print("❌ Please enter a valid number.")

    password = generate_password(length)

    print("\nGenerated Password:")
    print("--------------------------------")
    print(password)


def main():

    passwords = load_passwords()

    print("========================================")
    print("          PASSWORD MANAGER")
    print("========================================")

    while True:

        print("\nMenu")
        print("--------------------------------")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Generate Password")
        print("6. Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_password(passwords)

        elif choice == "2":

            view_passwords(passwords)

        elif choice == "3":

            search_password(passwords)

        elif choice == "4":

            delete_password(passwords)

        elif choice == "5":

            password_generator()

        elif choice == "6":

            print("\nThank you for using Password Manager!")
            print("Goodbye!")

            break

        else:

            print("\n❌ Invalid choice.")
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()