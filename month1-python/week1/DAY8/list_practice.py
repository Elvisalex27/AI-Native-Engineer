numbers = [10,20,30,40]
add_numbers = numbers.insert(4, 50)
remove_numbers = numbers.remove(20)
    
def first_number():
    print(numbers[0])

def last_number():
    print(numbers[-1])


def all_numbers():
    
    for all in numbers:
        print(all, end=" ")

first_number()
last_number()
all_numbers()
