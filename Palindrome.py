# getting input

def getting_input():
    a = True
    while a:
        user_input = input("Write a word: ")
        if user_input.isalpha():
            a = False
            return user_input
        else:
            print("You should write alphabets")
            continue

# changing order of word

def order_changing(user_input):
    changed_input = user_input[ ::-1]
    return changed_input

# setting valuables

user_input = getting_input()
changed_input = order_changing(user_input)

# running program

if user_input == changed_input:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")