#-*-coding:utf-8-*-
import random

for i in range(5):
	right_number = random.randint(1,100)
	guess_number = int(input("please enter a number:"))
	if right_number == guess_number:
		print("you win!!!")
		break
	elif guess_number > right_number:
		print('your guess_number is bigger')
		continue
	elif guess_number < right_number:
		print('your guess_number is smaller')
		continue
