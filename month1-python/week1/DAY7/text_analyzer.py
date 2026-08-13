sentence = input("Enter a sentence for me: ")

def total_characters():
    characters = len(sentence)

    print(f"Characters: {characters}" )

def total_vowel():
    count = 0
    for vowel in sentence.lower():
        if vowel in "aeiou":
            count += 1

    print(f"vowels: {count}")
            

def total_spaces():
    spaces = sentence.count(" ")
    print(f"sentence: {spaces}")

def total_words():
    words = len(sentence.split())
    print(f"words: {words}")
    

total_characters()
total_spaces()
total_vowel()
total_words()