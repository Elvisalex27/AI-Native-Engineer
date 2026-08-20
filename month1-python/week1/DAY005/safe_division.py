try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

    print("The result is:", result)
except ValueError:
    print("Please enter valid numbers.")
    
except ZeroDivisionError:
    print("The second number cannot be zero.")