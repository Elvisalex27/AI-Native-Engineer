try:
    number = int(input("Enter a number: "))
    print("you entered:", number)
except ValueError:
    print("Please enter a valid number.")