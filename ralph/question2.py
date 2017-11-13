#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，
如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
'''


import random


number = random.randint(1, 100)
print("游戏开始！")
chances = 5
while True:
    try:
        guess = int(input("请输入你的数字： "))
        if guess == number:
            break
        elif guess > number:
            print("大了大了")
        else:
            print("小了小了")
        chances = chances - 1
        if chances == 0:
            print("太遗憾了，正确答案是%s，你没有猜对。"% number)
            break
        else:
            print("你还有%d次机会，再猜一次吧！" % chances)
    except Exception as e:
        print("请输入正确的数字格式！！")