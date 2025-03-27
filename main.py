import json
import os

FileName = "contactBook.json"

# Function to load the data
def load_contacts():
    if os.path.exists(FileName):
        with open(FileName, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []  
            except json.JSONDecodeError:
                return []  
    return []  

# Function to save contacts
def save_contacts(contacts):
    with open(FileName, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact():
    name = input("Enter name: ").strip()
    contact_no = input("Enter contact number: ").strip()

    contacts = load_contacts()

 
    if not isinstance(contacts, list):
        contacts = []

    for contact in contacts:
        if contact["Contact_no"] == contact_no:
            print("Contact number already exists!")
            return


    contacts.append({"Name": name, "Contact_no": contact_no})  
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to delete a contact
def delete_contact():
    contact_no = input("Enter the contact number to delete: ").strip()

    contacts = load_contacts()
    new_contacts = [contact for contact in contacts if contact["Contact_no"] != contact_no]

    if len(new_contacts) == len(contacts):
        print("Contact not found!")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully!")


# Edit a contact 
def edit_contact():
    contact_no = input("Enter contact number to edit: ").strip()

    contacts = load_contacts()

    for contact in contacts:
        if contact["Contact_no"] == contact_no:
            new_name = input("Enter new name: ").strip()
            new_contact_no = input("Enter new contact number: ").strip()

            # Update only if new values are provided
            if new_name:
                contact["Name"] = new_name
                print("Name updated successfully!")
            if new_contact_no:
                contact["Contact_no"] = new_contact_no
                print("Number updated successfully!")

            save_contacts(contacts)
         
            return

    print("Contact not found!")


# Function to search for a contact
def search_contact():
    contact_no = input("Enter contact number to search: ").strip()

    contacts = load_contacts()

    for contact in contacts:
        if contact["Contact_no"] == contact_no:
            print(f"\nContact Found:\nName: {contact['Name']}\nNumber: {contact['Contact_no']}")
            return

    print("Contact not found!")


def main():
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. Search Contact by Number")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
