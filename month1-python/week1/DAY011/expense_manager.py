expenses = []
def create_expense(name, amount):
    expense = {
        "name": name,
        "amount": amount
    }
    return expense

def add_item(name,amount):
    expense = create_expense(name, amount)
    expenses.append(expense) 
    return expenses

def view_expenses():
    for expense in expenses:
        print(f"{expense['name']} : {expense['amount']}")

def calculate_total():
    total = 0
    for expense in expenses:

        total += expense["amount"]
    return total

def largest_expense():
    largest = expenses[0]
    for biggest in expenses:
        if biggest["amount"] > largest["amount"]:
            largest = biggest
    return largest

def get_expense_by_name(name):
    for expense in expenses:
        if expense['name'] == name:
            return expense
        
    return None 






