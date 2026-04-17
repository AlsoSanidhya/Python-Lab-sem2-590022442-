contacts = {}

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add contact
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    # 2. Search contact
    elif choice == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    # 3. Update contact
    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    # 4. Delete contact
    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # 5. Display all contacts
    elif choice == 5:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    # 6. Exit
    elif choice == 6:
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice.")