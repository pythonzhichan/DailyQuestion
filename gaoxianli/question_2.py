import random
print("系统已生成了一个1~100之间的整数，请输入系统生成的数字，不过您只有五次机会")
print("游戏开始:\n")
num = random.randint(1,100)
count = 5

while count:
    usernum = int(input("第%d次猜的数字是：" % (6 - count)))
    if usernum == num:
        print("恭喜您猜中了，答案就是",num)
        break
    elif usernum < num:
        if count != 1:#如果已经是最后一次机会就不用输出
            print("真不走运，您猜小了，请猜大点的吧:\n")
    else:
        if count != 1:
            print("真不走运，您猜大了，请猜小点的吧:\n")
    count -= 1

if count == 0:
    print('太倒霉了，您用光了五次机会，而且还没猜中！')
elif count == 1:
    print("太危险了，刚好最后一次机会被您猜中了，不过也挺厉害的了！")
else:
    print('你牛B，五次机会还没用完就猜中了！')
    
print("游戏结束")
