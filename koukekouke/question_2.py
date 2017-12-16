'''
设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，
每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，
如果5次都没猜中，结束游戏并告知正确答案。
'''


import random


num = random.randint(1, 100)
times = 5

for time in range(5, 0, -1):
    if time < 5:
        print('你还有%d次机会' % time)
    while True:
        try:
            guess = int(input('请输入您猜的整数(1~100):'))
            break
        except ValueError:
            print('输入错误')
    if guess > num:
        print('大了！')
        continue
    elif guess < num:
        print('小了！')
        continue
    else:
        print('恭喜你猜对了！')
        break
else:
    print('你没有机会了，正确答案:%d' % num)
