contact = [{
    "name": "Elvis", "phone": "09064063478"},{
    "name": "Maureen", "phone": "07077671162"},{
    "name": "Abraham", "phone": "08055625798"},{
    "name": "nuel", "phone": "07037092134"
}]

def add_contact(name,phone):
    new_contact = {"name": name, "phone": phone}
    contact.append(new_contact)
    print("contact added successfully ")


def view_contacts():
    if not contact:
        print("contact not available")


    for contacts in contact:

        print(f"name: {contacts['name']}, phone: {contacts['phone']}")

def search_contact(name,phone):
    for contacts in contact:           
        if contacts['name'].lower() == name.lower() or contacts['phone'].lower() == phone.lower():
            print(f"name: {contacts['name']}, phone: {contacts['phone']}")
            return
    print("Contact not found")

while True:
    print("\n1. Add contact\n2. View Contacts\n3. Search Contacts\n4. Exit")
    question = input("choose an option: ")
    if question == "Add contact" or question == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_contact(name, phone)
        

    elif question == "View contact" or question == "2":
        view_contacts()

    elif question == "search contact" or question == "3":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        search_contact(name,phone)

    elif question == "Exit" or question == "4":
        print("Goodbye")
        break

    else:
        print("Invalid option")


