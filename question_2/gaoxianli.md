## 源代码
```
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

# 评价玩家的游戏结果
if count == 0:
    print('太倒霉了，您用光了五次机会，而且还没猜中！')
elif count == 1:
    print("太危险了，刚好最后一次机会被您猜中了，不过也挺厉害的了！")
else:
    print('你牛B，五次机会还没用完就猜中了！')
    
print("游戏结束")
```
## 需要注意的细节
* 用户每次输入后，系统给用户一个提示，并能再次输入
* 最多输入五次，如果提前猜对了就退出循环
* 如果最后一次机会也猜错了，就不用输出 玩家下次输入的提示了
* 在提示“游戏结束”前，根据剩下的机会次数，给玩家一段评价
