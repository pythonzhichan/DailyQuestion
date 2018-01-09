#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import random

true_int = random.randint(1, 100)
times = 5

while times > 0:
    times -= 1
    try:
        guess = int(input('Please input the number you guess:'))
    except Exception as e:
        print('Invalid input! You have %s chances left.' % times)
        continue

    if guess > true_int:
        print('Sorry, it\'s too BIG! You have %s chances left.' % times)
    elif guess < true_int:
        print('Sorry, it\'s too SMALL! You have %s chances left.' % times)
    else:
        print('Bingo! You got the right answer.')
        break
else:
    print('Sorry, GAME OVER!\n')
    print('The true answer is: %s' % true_int)
