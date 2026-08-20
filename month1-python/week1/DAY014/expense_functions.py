from expense_data import expenses

def add_expense():
    product_name = input("Enter your name: ")
    product_price = int(input("Enter the price: "))

    expense = {
        "name": product_name,
        "price": product_price
    }
    expenses.append(expense)

def get_expense_by_name():
    name_of_goods = input("Enter the name of the product: ")
    for expense in expenses:
        if expense["name"] == name_of_goods:
            return expense  
    return

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["price"]
    return total

def average_expense():
    if not expenses:
        return 0
    
    total = calculate_total()
    number_of_expense = len(expenses)
    average = total / number_of_expense
    return average

def get_expense_above():
    amount_of_product = int(input("Enter the price of the product: "))
    above_expense = []
    for expense in expenses:
        if expense["price"] > amount_of_product:
            above_expense.append(expense)
    return above_expense

def get_expense_below():
    amount_of_product = int(input("Enter the price of the product: "))
    below_expense = []
    for expense in expenses:
        if expense["price"] < amount_of_product:
            below_expense.append(expense)
    return below_expense

def sort_expenses():
    sort = sorted(expenses, key=lambda expense:expense["price"])
    return sort

def sort_expnses_descending():
    sort = sorted(expenses, key=lambda expense:expense["price"],
                  reverse=True)
    return sort

def cheapest_expense():
    cheap = min(expenses, key=lambda expense:expense["price"])
    return cheap

def most_expensive():
    cost = max(expenses, key=lambda expense:expense["price"])
    return cost

def expense_report():
    #for getting the total of the list
    total = 0
    for expense in expenses:
        total += expense["price"]
    total_expense = total

    #for getting the average of the list
    if not expenses:
        print("No expeses available")
        return

    else:

        average = total_expense / len(expenses)

    #for getting the number of expense
        num_of_expense = len(expenses)

    cheap = cheapest_expense()
    cost = most_expensive()

    print("="*15 + " " + "EXPENSE REPORT" + " " + "="*15 )
    print(f"Total Expenses: {total_expense}\n Average Expense: {average}\n Number of Expense: {num_of_expense}\n\n\n Cheapest Expense: {cheap['name']} - {cheap['price']}\n\n\n Most Expensive Expense: {cost['name']} - {cost['price']} ")
    print("="*45)

