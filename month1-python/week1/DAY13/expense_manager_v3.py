expenses = []


def get_expense_above(amount):
    matching_expenses_higher = []
    for expense in expenses:
        if expense["amount"] > amount:
            matching_expenses_higher.append(expense)
    return matching_expenses_higher 


def get_expense_below(amount):
    matching_expenses_lower = []
    for expense in expenses:
        if expense["amount"] < amount: 
            matching_expenses_lower.append(expense)
    return matching_expenses_lower

def sort_expenses():
    sort = sorted(expenses, key=lambda expense:expense["amount"])
    return sort

def sort_expenses_descending():
    reversed_sort = sorted(expenses, key=lambda expense: expense["amount"],
                           reverse=True)
    return reversed_sort

def cheapest_expense():
    for expense in expenses:
        cheapest_expense = min(expenses,key=lambda expense: expense["amount"])
    return cheapest_expense

def most_expensive():
    for expense in expenses:
        costly_expense = max(expenses,key=lambda expense: expense["amount"])
    return costly_expense

def expense_report():
    #for getting the total of the list
    total = 0
    for expense in expenses:
        total += expense["amount"]
    total_expense = total

    #for getting the average of the list
    if not expenses:
        print("No expeses available")

    else:

        average = total_expense / len(expenses)

    #for getting the number of expense
        num_of_expense = len(expenses)

    cheap = cheapest_expense()
    cost = most_expensive()

    print("="*15 + " " + "EXPENSE REPORT" + " " + "="*15 )
    print(f"Total Expenses: {total_expense}\n Average Expense: {average}\n Number of Expense: {num_of_expense}\n\n\n Cheapest Expense: {cheap['name']} - {cheap['amount']}\n\n\n Most Expensive Expense: {cost['name'] - {cost['amount']}} ")
    print("="*45)


    
