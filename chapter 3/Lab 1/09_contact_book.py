contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Display all")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")