# -*- coding: utf-8 -*-

import random

random_number = random.randrange(1, 100)


def guess():
    status = False
    for i in range(0, 5):
        print('-' * 10)
        print('You have {} shot(s) now'.format(5 - i))
        guess_number = int(input('Input a number between 1 and 100 :'))
        if not isinstance(guess_number, int):
            print('Wrong Input!')
            break

        if random_number == guess_number:
            print('You Win! The number is {}.'.format(random_number))
            status = True
            break
        elif guess_number < random_number:
            print('The number should be BIGGER !')
        else:
            print('The number should be SMALLER !')

    return status


result = guess()

if result == False:
    print('-' * 10)
    print('Sorry, you used all your chances!')
else:
    print('-' * 10)
    print('Congratulation! You got the right answer!')
