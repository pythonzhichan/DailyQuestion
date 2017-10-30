"""
系统随机生成一个1~100之间的整数，玩家有5次机会，
每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，
则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案
"""

import random

def guessNumber(inputNumber, counter, randNumer):   #传入三个位置参数,一个可变参数用于
    if inputNumber > randNumer:
        if counter:  # 最后一次传入的counter为 0 时 不打印你还有 0 次机会
            print('输入的数大了,输个小点的你还有 %d 次机会!' % counter)
    elif inputNumber < randNumer:
        if counter: 
            print('输入的数小了,输个大点的你还有 %d 次机会!' % counter)
    else:
        print('猜对了! 你输入的是 %d 系统生成的是 %d' % (inputNumber, randNumer))
        return True   

if __name__ == "__main__":
    numRange = (1,100)     #生成数范围
    nstart,nend = numRange  # 练习下元组解包用法
    counter = 5   # 输入机会计数
    
    while counter:
        randNumber = random.randint(*numRange)
        print('测试用-->系统生成的数是 %s ' % randNumber)
        print('请输入一个%s~%s之间的数:' % (nstart, nend), end=' ')
        userInput = int(input())  # input不支持字符串格式化
        counter -= 1
        if guessNumber(userInput, counter, randNumber):  # 传入*numRange
            break
    else:
        print('你的机会用光了,没猜对,系统生成的数是 %s ' % randNumber)
