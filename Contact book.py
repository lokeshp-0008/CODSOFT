import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"- {name}: {details['phone']}")
    print()

def search_contact(contacts):
    search = input("Enter Name or Phone Number to Search: ").strip()
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details["phone"]:
            print(f"\nContact Found:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            return
    print("Contact not found.")

def update_contact(contacts):
    name = input("Enter Name of the Contact to Update: ").strip()
    if name in contacts:
        print(f"Current Details: {contacts[name]}")
        phone = input("Enter New Phone Number: ").strip()
        email = input("Enter New Email: ").strip()
        address = input("Enter New Address: ").strip()
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter Name of the Contact to Delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def contact_book():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

contact_book()
