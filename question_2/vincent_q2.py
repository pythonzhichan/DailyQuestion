#!/usr/bin/env python3
import random

print("猜测数字，这个数字范围为１－100，你有５次机会．")

target = random.randint(1,100)

i = 0
while i < 5:
    try:
        guess = input("猜测数字为：　")
        guess = int(guess)
        if guess < target:
            print("小了!剩余次数　"+str(4-i)+ "次")
            i += 1
            continue
        elif guess > target:
            print("大了!剩余次数　"+str(4-i)+"次")
            i += 1
            continue
        else:
            print("Bingo!")
            break
    except ValueError as err:
        print(err)
        continue

if i == 5:
    print("游戏结束，这个数字是", target)

