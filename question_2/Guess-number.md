import random
secret=random.randint(1,100)

time=6
guess=0
minNum=0
maxNum=100
print("---------猜数字游戏马上开始---------")
while guess!=secret and time>=0:
    guess=int(input("*数字区间0-100，请输入你猜的数字:"))
    print("你输入数字是：",guess)
    if guess==secret:
        print("猜对了，真厉害")
    else:
        if guess<secret:
            minNum=guess
            print("你的猜数小于正确答案")
            print("现在的数字区间是：",minNum,"-",maxNum)
        else:
            maxNum=guess
            print("你的猜数大于正确答案")
            print("数字区间是：",minNum,"-",maxNum)
        print("太遗憾了，你猜错了，你还有",time,"次机会")
    time-=1
print("游戏结束")