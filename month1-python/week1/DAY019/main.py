import json

def load_expenses():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    return expenses

def validate_expense(amount):
   
    if amount <= 0:
        raise ValueError ("Expense amount must be positive")

    return True

def add_expense():  
    expenses = load_expenses()
    
    expense_name = input("Enter the name of the product: ")
    try:
        expense_amount = int(input("Enter the amount: "))

        validate_expense(expense_amount)


        expense = {
                "name": expense_name,
                "amount": expense_amount
            }
        
            
            
        expenses.append(expense)
    
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added Successfully")
        
    except ValueError as error:
        print(f"Invalid expense: {error}")


def view_expenses():
    expenses = load_expenses()
    print("----Your Expenses----")

    if not expenses:
        print("No expenses recorded yet")
        return 

    for expense in expenses:
        print(f"{expense['name']} : ₦{expense['amount']:,}")


    
def total_expenses():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total 


def average_expenses():
    total = total_expenses()
    expenses = load_expenses()
    number_expense = len(expenses)

    if not expenses:
        print("No expenses available to calculate an average")
        return
    
   

    average = total / number_expense

    return average 

def delete_expense():
    expenses = load_expenses()
    
    if not expenses:
        print("No expense to delete.")
        return

    print("---- Your Expenses ----")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']}: {expense['amount']:,}  ")

    try:

        choice = int(input("Enter the number of the expense to delete: "))

        if choice > len(expenses) or choice < 1 :
            raise ValueError ("Invalid input, Choose a number from the list.")

        deleted_expense = expenses.pop(choice -1)

        with open("expenses.json", "w") as file:
           json.dump(expenses, file, indent=4)

    except ValueError as error:
        print(f"Error: {error}")
    
    else:
        print(f"{deleted_expense['name']} deleted successfully")



        

