def safe_number():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        return "invalid input"

def validate_positive(number):
   
    if number <= 0:
        raise ValueError("Number must be Positive")
    
    return "Valid number"

def safe_divide(a,b):
    try:
       if b == 0 :
           raise ValueError("Cannot divide by Zero")
       
       divide = a / b 
       
    except ValueError:

        return "Invalid division"
    else:
        return  divide
    
        
def validate_expense(amount):
   
    if amount <= 0:
        raise ValueError ("Expense amount must be positive")

    return True


#print(safe_number())
#print(validate_positive(-4))
print(safe_divide(4,0))

