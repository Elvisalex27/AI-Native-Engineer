from expense_functions import (
    add_expense,
    get_expense_by_name,
    calculate_total,
    average_expense,
    get_expense_above,
    get_expense_below,
    sort_expenses,
    sort_expnses_descending,
    cheapest_expense,
    most_expensive,
    expense_report
)


while True:
    print("\n===== EXPENSE MANAGER =====")
    print("1. Add Expense")
    print("2. Get Expense By Name")
    print("3. Calculate Total")
    print("4. Average Expense")
    print("5. Get Expenses Above")
    print("6. Get Expenses Below")
    print("7. Sort Expenses")
    print("8. Sort Expenses Descending")
    print("9. Cheapest Expense")
    print("10. Most Expensive")
    print("11. Expense Report")
    print("12. Exit")

    choice = input("Choose a number: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        print(get_expense_by_name())

    elif choice == "3":
        print(calculate_total())

    elif choice == "4":
        print(average_expense())

    elif choice == "5":
        print(get_expense_above())

    elif choice == "6":
        print(get_expense_below())

    elif choice == "7":
        print(sort_expenses())

    elif choice == "8":
        print(sort_expnses_descending())

    elif choice == "9":
        print(cheapest_expense())

    elif choice == "10":
        print(most_expensive())

    elif choice == "11":
        expense_report()

    elif choice == "12":
        print("Goodbye")
        break

    else:
        print("Invalid option")