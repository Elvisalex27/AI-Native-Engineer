def check_password():
    password = input("Enter your password: ")

    has_alpha = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_alpha = True

        elif char.isdigit():
            has_digit = True

    if len(password) >= 8 and has_digit and has_alpha:
            print(" A Strong  password")
    else:
         print("A weak password")

check_password()