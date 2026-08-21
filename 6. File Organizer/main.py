import os
import shutil


# File categories
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".ico"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt"
    ],
    "Spreadsheets": [
        ".xls", ".xlsx", ".csv", ".ods"
    ],
    "Presentations": [
        ".ppt", ".pptx", ".odp"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm"
    ],
    "Music": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg",
        ".m4a"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Python": [
        ".py", ".pyw"
    ],
    "Code": [
        ".html", ".htm", ".css", ".js", ".jsx",
        ".ts", ".tsx", ".java", ".c", ".cpp",
        ".h", ".hpp", ".json", ".xml"
    ],
    "Executables": [
        ".exe", ".msi"
    ]
}


def get_category(extension):
    """
    Find the category for a file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_filename(destination_folder, filename):
    """
    Prevent overwriting files with the same name.
    """

    name, extension = os.path.splitext(filename)

    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}_{counter}{extension}"
        counter += 1

    return new_filename


def organize_files(folder_path):
    """
    Organize files inside the selected folder.
    """

    if not os.path.exists(folder_path):
        print("\n❌ Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("\n❌ The provided path is not a folder.")
        return

    moved_files = 0

    try:
        files = os.listdir(folder_path)

        for filename in files:

            source_path = os.path.join(folder_path, filename)

            # Ignore directories
            if os.path.isdir(source_path):
                continue

            # Get file extension
            _, extension = os.path.splitext(filename)

            # Determine category
            category = get_category(extension)

            # Create category folder
            destination_folder = os.path.join(
                folder_path,
                category
            )

            os.makedirs(destination_folder, exist_ok=True)

            # Prevent duplicate filenames
            unique_filename = get_unique_filename(
                destination_folder,
                filename
            )

            destination_path = os.path.join(
                destination_folder,
                unique_filename
            )

            # Move file
            shutil.move(source_path, destination_path)

            print(
                f"Moved: {filename} → {category}/{unique_filename}"
            )

            moved_files += 1

        print("\n================================")
        print("      ORGANIZATION COMPLETE")
        print("================================")
        print(f"Files moved: {moved_files}")

    except PermissionError:
        print("\n❌ Permission denied.")
        print("Try running the program with the required permissions.")

    except Exception as error:
        print(f"\n❌ An error occurred: {error}")


def show_categories():
    """
    Display supported file categories.
    """

    print("\nSupported File Categories:")
    print("--------------------------------")

    for category, extensions in FILE_CATEGORIES.items():
        extensions_text = ", ".join(extensions)
        print(f"{category}: {extensions_text}")

    print("Others: Files with unsupported extensions")


def main():
    print("========================================")
    print("        FILE ORGANIZER")
    print("========================================")

    while True:

        print("\nMenu")
        print("--------------------------------")
        print("1. Organize Files")
        print("2. Show Supported Categories")
        print("3. Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            folder_path = input(
                "\nEnter the folder path to organize: "
            ).strip()

            # Remove quotes if user pastes a quoted path
            folder_path = folder_path.strip('"')

            organize_files(folder_path)

        elif choice == "2":

            show_categories()

        elif choice == "3":

            print("\nThank you for using File Organizer!")
            print("Goodbye!")
            break

        else:

            print("\n❌ Invalid choice.")
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()