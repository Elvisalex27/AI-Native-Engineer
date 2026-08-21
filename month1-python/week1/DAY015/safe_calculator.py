
try:
    first_number = int(input("Enter first number: "))
    operator = input("Enter operator ( +, -, *, /)")
    second_number = int(input("Enter second number: "))

    if operator == "+":
        print(first_number + second_number)

    elif operator == "-":
        print(first_number - second_number) 

    elif operator == "*":
        print(first_number * second_number)

    elif operator == "/":
        if second_number == 0:
            print("non divisible by zero")
        else:
            print(first_number / second_number) 
    else:
        print("an invalid operator")

except ValueError:
    print("please enter a valid number.")
except ZeroDivisionError:
    print("non divisible by zero, select another value")
finally:
    print("your result is visible")

        
    