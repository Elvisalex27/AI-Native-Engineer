expenses = []
def Add_Expeses():
    expense_name = input("Enter the name of the product: ")
    expense_amount = int(input("Enter the amount of the product: ")) 
    expense = {
        "name": expense_name,
        "amount": expense_amount
    }
    expenses.append(expense)

def View_expenses():
    for expense in expenses:
        
        print(f"{expense['name']}: ₦{expense['amount']}")

def Calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def lagest_Expenses():
    if expenses == []:
        print("its an empty list")
    else:
        largest = expenses[0]
        for biggest in expenses:
            if biggest["amount"] > largest['amount']:
                largest = biggest
        return largest

def delete():
    deleted_expense = input("Enter the name of the Product: ")
    for expense in expenses:
        if deleted_expense == expense["name"]:
            expenses.remove(expense)6
            print(f"{deleted_expense} has been removed successfully")
            return
                    
    else:
        print("product not found")


while True:
    header = "=" * 20 
    print(header)
    print("1. Add Expense\n2. View Exoenses\n3. Calculate Total\n4. Find Largest Expense\n5. Delete Expense\n6. Exit")
    question = input("Select an option: ")

    if question == '1':
            
        Add_Expeses()

    elif question == '2':
        View_expenses()

    elif question == '3':
        total = Calculate_total()
        print(f" total expenses: N{total}")

    elif question == '4':
        lagest_Expenses()

    elif question == '5':
        delete()

    elif question == '6':
        print("Goodbye, Thanks for participating")
        break
    else:
        print("Invalid input")
        