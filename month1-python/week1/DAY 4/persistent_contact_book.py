def add_contact():
    name = input("ehat is your name? ")
    phone = input("what is your phone number? ")

    with open("contacts.txt","a") as files:
        files.write(f"{name}, {phone}\n")

    print("Contact Saved")

def view_contacts():
    with open("contacts.txt", "r") as files:
        for line in files:
            name, phone = line.strip().split(",")
            print(f"name: {name}, phone: {phone}")

    

while True:
    print("1. Add Contact\n2. View Contact\n3. Exit")

    question = input("choose an option? ")

    if question == "1" :
        add_contact()

    elif question == "2" :
        view_contacts()

    elif question == "3" :
        print("Goodbye")
        break

    else:
        print("Invalid option")

    


