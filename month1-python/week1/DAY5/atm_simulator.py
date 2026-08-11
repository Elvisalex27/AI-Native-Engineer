balance = 10000

def check_balance():
    print(f"your current balance is {balance}")

def withdraw(amount):
    try:
        
        if amount <= 0:
            print("amount should be a positive number")

        elif amount > balance:
            print("insufficient funds")
        else:
            balance = balance - amount
            print(f"the transaction was successful, your new balance is {balance}")
    except ValueError:
        print("Enter a valid number")

def deposit(amount):
    try:
        
        if amount <= 0:
            print("amount should be a positive number")
        else:
            balance = balance + amount
            print(f"the transaction was successful, your new balance is {balance}")
    except ValueError:
        print("Enter a valid number")

while True:
    try:
        print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")

        question = int(input("Enter your choice: "))

        if question == 1:
            check_balance()

        elif question == 2:
            amount = int(input("Enter the amount you want to withdraw"))
            withdraw(amount)

        elif question == 3:
            amount = int(input("Enter the amount you want to deposit"))
            deposit(amount)
            
        elif question == 4:
            print("thank you for your time, GOODBYE")
            break
        else:
            print("Invalid option, please try again")

    except ValueError:
        print("Please enter a valid number")
