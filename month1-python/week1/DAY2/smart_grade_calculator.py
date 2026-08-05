def get_score(subject_name):
    score = float(input(f"what did you score in {subject_name}? "))
    return score

score1 = get_score("maths")
score2 = get_score("furthermaths")
score3 = get_score("english")

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):

    if average >= 70:
        return "A"

    elif  average >= 60:
        return "B"

    elif average >= 50:
        return "C" 

    elif average >= 45:
        return "D"

    else:
        return "F"
       


def get_status(average):

    if average >= 50:
        return "PASS"
    else:
        return "FAIL"

def display_report(name, average, grade, status):
    print("--- SMART REPORT CARD ---")
    print(f"Name: {name}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

scores = [score1, score2, score3]
average = calculate_average(scores)
grade = get_grade(average)
status = get_status(average)

display_report(name, average, grade, status)


    

