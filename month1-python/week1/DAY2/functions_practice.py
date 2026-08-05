# Task1
def greet(name):
    print(f" hello, {name}")

greet("elvis")


# Task2
# Return the square of the number.
def square(number):
    return number * number

msg = square(3)
print(msg)



# Task3
# check for even numbers or odd numbers
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

num = is_even(7)
print(num)


#Task4
#count vowels
def count_vowels(text):
    count = 0
    vowel = "aeiou"
    for ch in text.lower():
        if ch in vowel:
            count += 1
    return count

count_vowels("animal")
print(count_vowels("amimal")) 


#Task5
#Find the largest number without using max()
def largest_number(numbers):
    large = numbers[0]
    for ch in numbers:
        if ch > large:
            large = ch
    return large
        

print(largest_number([8,16,11,1]))

