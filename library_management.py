# Library Management System

print("===== Library Management System =====")

# Dictionary to store books and availability
library = {}

# Set to store unique categories
categories = set()

while True:

    print("\nMenu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Categories")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        book = input("Enter book name: ")
        category = input("Enter book category: ")

        library[book] = "Available"
        categories.add(category)

        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if len(library) == 0:
            print("No books in library.")
        else:
            print("\nBooks List:")
            for book in library:
                print(book, "-", library[book])

    # Borrow Book
    elif choice == "3":
        book = input("Enter book name to borrow: ")

        if book in library:
            if library[book] == "Available":
                library[book] = "Borrowed"
                print("Book borrowed successfully!")
            else:
                print("Book already borrowed.")
        else:
            print("Book not found.")

    # Return Book
    elif choice == "4":
        book = input("Enter book name to return: ")

        if book in library:
            library[book] = "Available"
            print("Book returned successfully!")
        else:
            print("Book not found.")

    # Show Categories using SET
    elif choice == "5":
        print("\nUnique Book Categories:")
        for cat in categories:
            print(cat)

    # Exit
    elif choice == "6":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Try again.")
