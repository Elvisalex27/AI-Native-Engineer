expenses = []
def get_expense_by_name(name):
    for expense in expenses:
        if expense["name"] == name:
            return expense
    return None


def show_expense(name):
    expense = get_expense_by_name(name)
    if expense:
        print(expense)
    else:
        print("Expense not found")


def Average_expense():
    total = 0
    if expenses:
        for expense in expenses:
            total += expense["amount"]
    else:
        return "cant be divided by zero"

    average = total / len(expenses)
    return average


def expense_summary():
    total = 0
    for expense in expenses:
        total += expense["amount"]

    avarege = Average_expense()

    number_of_expense = len(expenses)


    return f"Total: {total}\n Average: {avarege}\n Number of expenses: {number_of_expense}"

def get_expenses_above(amount):
    matching_expenses = []
    for expense in expenses:
        if expense["amount"] > amount:
            matching_expenses.append(expense)
    return matching_expenses