# -*- coding: UTF-8-*-
"""
设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，
玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，
如果猜中了，则告知玩家并提前结束游戏，
如果5次都没猜中，结束游戏并告知正确答案。
"""
import random
secret = random.randint(1,100)
count=1
while count<=5:
    temp=int(input("不妨猜一下小甲鱼现在心里想的是哪个数字："))
    result=cmp(temp,secret)
    if result==0:
        print("恭喜你，猜对了")
        count=6         
    elif result>0:
        print("猜大了")
        count=count+1
    else:
        print("猜小了")
        count=count+1
print("游戏结束，正确答案是：%d" % (int(secret)))
