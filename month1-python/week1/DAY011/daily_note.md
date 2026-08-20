# Day 011 Daily Note

## Date
August 18, 2026

## What I Learned

Today I learned how functions can work together in a Python program.

I learned that one function can call another function and use the value it returns.

For example:

```python
def create_expense(name, amount):
    return {
        "name": name,
        "amount": amount
    }


def add_item(name, amount):
    expense = create_expense(name, amount)
    expenses.append(expense)