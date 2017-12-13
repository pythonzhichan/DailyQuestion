from random import randint
from sys import exit

min_of_target = 0
max_of_target = 100
target = randint(min_of_target,max_of_target)
chances = 7

print("Welcome to guess number game!")
print(f"You have {chances} chances to guess the number, which is range from {min_of_target} to {max_of_target}.")
print("Each time you guessed, you will get a hint about that your number is greater or smaller, until you guesss it or you use up all {chances} chances.")
print("Are you ready? (y or n)")
is_ready = input("> ")
while(True):
    if is_ready == "y":
        print("Let's begin.")
        break
    elif is_ready == "n":
        print("Bye")
        exit(0)
    else:
        print("Are you ready? (y or n)")
        is_ready = input("> ")


for i in range(0, chances):
    print(f"Now, you have {chances-i} chance(s), please input your number.")
    input_number = None
    while(True):
        try:
            input_str = input("> ")
            input_number = int(input_str)
            break
        except ValueError:
            print(f"Please input a NUMBER, {input_str} is not a number.")
    if i == chances-1 and input_number != target:
        print(f"You don't guess it, but you already use up all chances, the target number is {target}.")
        exit(0)
    elif input_number == target:
        print(f"Congratulations! The target number is {input_number}")
        exit(0)
    else:
        if input_number > target:
            print(f"Your number {input_number} is greater than the target, pleas try again.")
        elif input_number < target:
            print(f"Your number {input_number} is less than the target, pleas try again.")
