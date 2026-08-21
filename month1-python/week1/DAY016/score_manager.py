students = []
def add_function():
    while True:
        
        student_name = input("Enter your name: ")
        if not student_name:
            print("Name cannot be empty")
            continue
        try:
            student_score = int(input("Enter your score: "))
            if student_score < 0:
                print("score can't be a negative number")
            elif student_score > 100:
                print("student score must be between 0 - 100")
            else:
                break
        except ValueError:
            print("Enter a valid number")
            

    student = {
        "name": student_name,
        "score": student_score
    }
    students.append(student)

def view_students():
    if not student:
        print("the list is empty")

    print('=' * 10 + "STUDENTS" + '=' * 10)
    for student in students:
        
        print(f"Name: {student['name']} | Score: {student['score']}")


def average_score():
    total = 0
    if not students:
            print("No students available.")
            return
    for student in students:
        total += student["score"]
    
    average = total / len(students)
    return average

def highest_score():
    if not students:
        return "No students available"
    
    highest = students[0]
    for student in students:
        if student["score"] > highest["score"]:
            highest["score"] = student["score"]
    return f"{student['name']}-  {highest["score"]}"


while True:
    print("\n1. Add Student\n2. View Studnts\n3.Average Score\n4.Highest score\n5.Exit")
    choice = input("Enter a number: ")

    if choice == "1":
        add_function()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print(average_score())

    elif choice == "4":
        print(highest_score())

    elif choice == "5":
        print("Goodbye, Thanks for playing")
        break
    else:
        print("Enter a valid number.")

    



    

        