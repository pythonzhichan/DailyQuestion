#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author  :   {PHQ}
@License :   (C) Copyright 2017, {public}
@Contact :   {puhuaqiang@hotmail.com}
@Software:   {question_2}
@File    :   MrPHQ.py
@Time    :   2017-10-30
@Desc    :

每日一题的第2题：
    系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，
则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案
'''

import random

answer_number = random.randint(1,100)
answer_cnt = 5
while answer_cnt > 0:
    number = input('Answer a number({0} chances): '.format(answer_cnt))
    number = int(number)
    if number == answer_number:
        break
    elif number > answer_number:
        print("The numbers are too big!")
    else:
        print("The numbers are too small!")
    answer_cnt -= 1;

if answer_cnt > 0:
    print("Congratulations, right answer!")
else:
    print("The correct answer is ", answer_number)

        
        
    
    
    
