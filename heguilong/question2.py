#!/usr/bin/python3
import random
"""
系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
"""
gen_num = random.randint(1, 100)
times = 5
while times > 0:
    times -= 1
    print("Please input your guess number:")
    try:
        guess = int(input())
    except ValueError as e:
        print("Please input valid number.")
        continue
    if guess > gen_num:
        print("Sorry, larger than generated number.")
    elif guess == gen_num:
        print("Bingo, you got it!")
        break
    else:
        print("Sorry, smaller than generated number")
else:
    print("Sorry, you run out of times. Game over!")
