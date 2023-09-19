contacts = {}  # Create dictonary

while True:
    print("Please choose a number:")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. View contacts")
    print("4. Exit")
    #Get user input
    choice = input("Please input a number 1 - 4")
    # Adding a contact
    if choice == '1':
        name = input("Enter the contact name: ")
        phone = input("Enter the contact's phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    # Deleting a contact
    if choice == '2':
        deleteName = input("Enter the contact name to delete: ")
        if deleteName in contacts:
            del contacts[deleteName]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Viewing contacts
    if choice == '3':
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    #Exit the program
    if choice == '4':
        print("Exiting Program")
        break

    # Make sure program continues to run when invalid input
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
