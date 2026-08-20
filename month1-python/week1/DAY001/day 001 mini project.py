def classroom():
        
    student_name = input("what is your name? ")
    student_scores1 = float(input("what is your score in the first sublect? "))
    student_scores2 = float(input("what is your score in the second subject? "))
    student_scores3 = float(input("what is your score in the third subject? "))
    student_AVG = (student_scores1 + student_scores2 + student_scores3)/3
    student_average = round(student_AVG, 2) 
    print("---REPORT CARD---")
    print(f"Name: {student_name}")
    print(F"Average: {student_average}")
    if student_average > 69:
        print("Grade: A")
        print ("Status: PASS")
    elif 69 > student_average > 59:
        print("Grade: B")
        print("Status: PASS")
    elif 59 > student_average > 49:
        print("Grade: C")
        print("Status: SIDE PASS")
    elif 49 > student_average > 44:
        print("Grade: D")
        print("Status: PHAROH LET MY PEOPLE GO")
    else:
        print("Grade: F")
        print("Status: FAIL")


classroom1 = classroom()
classroom1
