sentence = input("Enter a sentence: ").lower()
reverse = sentence[::-1]
if sentence == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")