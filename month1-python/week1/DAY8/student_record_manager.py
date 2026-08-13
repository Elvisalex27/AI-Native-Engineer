students = []

def add_student():
    name = input("What is your name? ")
    score = int(input("What did you score? "))

    new_student = {"name": name, "score": score}
    students.append(new_student)

    print("Student added successfully")


def view_students():
    if not students:
        print("No students available")
        return

    for student in students:
        print(f"Name: {student['name']} | Score: {student['score']}")


def search_student():
    search_name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Found: {student['name']} - {student['score']}")
            return

    print("Student not found")


def remove_student():
    name = input("Enter name of student to remove: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student removed successfully")
            return

    print("Student not found")


def show_average_score():
    if not students:
        print("No students available")
        return

    total = 0

    for student in students:
        total += student["score"]

    average = total / len(students)
    print(f"Average score: {average}")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Show Average Score")
    print("6. Exit")

    choice = input("Choose a number: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        show_average_score()

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid option")