import json

def load_expenses():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    return expenses
def add_expense():    
    expense_name = input("Enter the name of the product: ")
    expense_amount = int(input("Enter the amount: "))

    expense = {
        "name": expense_name,
        "amount": expense_amount
    }
    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


