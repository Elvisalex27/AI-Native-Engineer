import json
def add():
    
    with open ("students.json", "r") as file:
        students = json.load( file)

    
    
   
    student_name = input("Enter your name: ")
    student_score = int(input("Enter your score: "))

    student = {"name": student_name, 
               "score": student_score}

    students.append(student)
    
    with open ("students.json", "w") as file:
        json.dump(students, file, indent=4)
   
def view():
    with open("students.json", "r") as file:
        students = json.load(file)

        for student in students:
            print (student["name"], student["score"])

def average_score():
    with open("students.json", "r")as file:
        students = json.load(file)

    total = 0
    no_of_students = 0

    for student in students:
        total =+ student["score"] 
        no_of_students +=  1

    average = total / no_of_students

    return average

def highest_score():
    with open("students.json", "r")as file:
        students = json.load(file)

    if not students:
        return "No Students available"

    highest = students[0]
    for student in students:
        if student["score"] > highest["score"]:
            highest = student

    return f"{highest['name']} - {highest['score']}"

def lowest_score():
    with open("students.json", "r")as file:
        students = json.load(file)

    if not students:
        return "No Students available"

    lowest = students[0]
    for student in students:
        if student["score"] < lowest["score"]:
           lowest = student

    return f"{lowest['name']} - {lowest['score']}"


#add()
# view()
# print(average_score())
# print(highest_score())
# print(lowest_score())
while True:
    print("=" * 5 + "STUDENT JSON MANAGER" + "=" * 5)
    print("\n1. Add Student\n2. View Students\n3. Avearge Score\n4. Highest Score\n5. Lowest Score\n6. Exit")
    question = input("Enter an option: ")
    if question == "1":
        add()
    elif question == "2":
        view()
    elif question == "3":
        print(average_score())
    elif question == "4":
        print(highest_score())
    elif question == "5":
        print(lowest_score())
    elif question == "6":
        print("Thanks for participating, see you next time.")
        break
    else:
        print("input the correct number")






