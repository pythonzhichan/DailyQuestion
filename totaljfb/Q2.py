#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jason Zhang
#
# Created:     08/12/2017
# Copyright:   (c) Jason Zhang 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Question 2
#a function to validate the input and return the input as an integer
def input_validation():
    input_number = input("Please enter a number to guess: ")
    while(True):
        try:
            given_number = int(input_number)
            return given_number
        except ValueError:
            input_number = input("Please enter an integer: ")
import random
random_number = random.randint(1,100)
the_input = input_validation()
#two conditions make the guess over, guess is correct and under 5 times
guess_correct = False
n = 4
while(not guess_correct and n != 0):
    if the_input > random_number:
        print("Your number is greater, try again, " +str(n)+ " time(s) left to guess.")
        n -= 1
        the_input = input_validation()
    elif the_input < random_number:
        print("Your number is smaller, try again, " +str(n)+ " time(s) left to guess.")
        n -= 1
        the_input = input_validation()
    else:
        print("You got the number! It's", the_input)
        print("You have used " + str(5-n) + " times to get it.")
        guess_correct = True
#when n = 0, while loop quits, check the last guess below:
if guess_correct == False:
    if the_input == random_number:
        print("You got the number! It's", the_input)
        print("You have used " + str(5-n) + " times to get it.")
    else:
        print("Sorry, you need more luck to guess, the number is " + str(random_number))

