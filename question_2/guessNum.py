#!usr/bin/python3
#-*- coding:utf-8 -*-

import random

def startGame():
    print("<<< 游戏开始 >>>")
    print("请输入1~100之间任意一个数字，一共有5次猜中的机会。")

def endGame(number,isGuess=False):
    if isGuess:
        print("恭喜你，答对了，就是它：{0}".format(number))
    else:
        print("很遗憾，机会已用完，正确答案是：{0}".format(number))        
    print("<<< 游戏结束 >>>")

def guessNum():
    number = random.randint(1,100)
    totalCount = 5

    startGame()
    while totalCount > 0:
        choiseNum = input("请输入：")
        if choiseNum.isdigit():
            totalCount -= 1
            choiseNum = int(choiseNum)
            if choiseNum == number:
                endGame(number,True)
                break
            elif choiseNum > number and totalCount > 0:
                print("数字大了,还有{0}次机会".format(totalCount))
            elif choiseNum < number and totalCount > 0:
                print("数字小了,还有{0}次机会".format(totalCount))
            
            if(totalCount == 0):
                endGame(number)
        else:
            print("输入有误")
if __name__ == '__main__':
    guessNum()
