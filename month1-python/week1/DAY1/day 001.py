# Ask for a number and print "Even" or "Odd".
n =int(input("enter a number: "))
if n % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

# Largest of Three
# Ask for three numbers and print the largest.
x = ( 2,5,7)
largest = max(x)
print(largest)

#using loops for largest
large = x[0]
for num in x:
    if num > large:
        large = num
print(large)


#Count Vowels
# Count vowels in a sentence.
count = 0
word = "caterpilla"
for vowel in word:
    if vowel in "aeiou".lower(): 
        count += 1
print (f"there are {count} vowels in the word")


# Reverse String
# Reverse a string without using slicing [::-1].
string = "pussycat"
reverse = ""
for ch in string:
    reverse += ch
print(reverse)


# Simple Calculator
# Support + - * / and handle division by zero.
def operate(a,operator,b):


    if operator == "+":
        print (a + b)

    elif operator =="-":
        print(a - b)

    elif operator == "*":
        print(a * b)

    elif operator == "/":
        if b == 0:
            print("not divisible")
        else:
            print ( a / b )
    else:
        print("invalid operator")

operate(10, "+", 9)


