import csv
import os

def add_student():

    student_name = input("Enter your name: ")
    student_score = int(input("Enter your score: "))

    with open("students.csv", "a", newline="") as file:

        fieldnames = ["name", "score"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.path.getsize("students.csv") == 0: 
        
            writer.writeheader()
        
        writer.writerow({
            "name": student_name ,
            "score": student_score
        })

def view_student():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            print(student)

def cal_Avarage():
    total = 0
    count = 0
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            total = total + int(student["score"])
            count += 1
    if count == 0:
        return "No Studen Available"
    average = total / count
    return average

def highest_score():
    highest = None

    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            score = int(student["score"])

            if highest is None or score > highest["score"]:
                highest = {
                    "name": student["name"],
                    "score": score
                }

    if highest is None:
        return "No students available"

    return f"{highest['name']} - {highest['score']}"

while True:
    print("=" * 5 + "STUDENT CSV MANAGER" + "=" * 5 )
    print("\n1. Add Student.\n2. View Students. \n3. Average Score. \n4. Highest Student.\n5. Exit")
    choice = input("Enter an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        print(cal_Avarage())
    elif choice == "4":
        print(highest_score())
    elif choice == "5":
        print("Thank you for participating")
        break
    else:
        print("Enter a valid number.")

    
    



    