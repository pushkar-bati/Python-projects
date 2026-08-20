import json
import os


MEMBERS_FILE = "data/members.json"


def load_members():
    if not os.path.exists(MEMBERS_FILE):
        return []

    try:
        with open(MEMBERS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_members(members):
    os.makedirs("data", exist_ok=True)

    with open(MEMBERS_FILE, "w") as file:
        json.dump(members, file, indent=4)


def add_member():
    members = load_members()

    print("\n========== ADD MEMBER ==========")

    name = input("Enter member name: ").strip()
    email = input("Enter member email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    for member in members:
        if member["email"].lower() == email.lower():
            print("A member with this email already exists.")
            return

    if members:
        member_id = max(member["id"] for member in members) + 1
    else:
        member_id = 1

    member = {
        "id": member_id,
        "name": name,
        "email": email
    }

    members.append(member)
    save_members(members)

    print("\nMember added successfully!")
    print(f"Member ID: {member_id}")


def view_members():
    members = load_members()

    print("\n========== ALL MEMBERS ==========")

    if not members:
        print("No members found.")
        return

    for member in members:
        print("-" * 35)
        print(f"ID       : {member['id']}")
        print(f"Name     : {member['name']}")
        print(f"Email    : {member['email']}")

    print("-" * 35)