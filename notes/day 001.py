# Ask for a number and print "Even" or "Odd".
n = 14
if n % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

# Largest of Three

# Ask for three numbers and print the largest.
x = ( 2,5,7)
largest = max(x)
print(largest)
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


