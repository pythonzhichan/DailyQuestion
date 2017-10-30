## 第2题 ##

> 题目描述：系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

```
import random
import datetime

random.seed(datetime.datetime.now())
number = random.randint(1, 100)
count = 0
while count <= 5:
    guess = int(input("请输入数字："))
    count += 1
    if count == 5:
        if guess != number:
            print("回答结束！正确答案应该是是{0}".format(number))
            break

    if guess > number:
        print("数字偏大！请重新回答")
        continue
    elif guess < number:
        print("数字偏小！请重新回答")
        continue
    else:
        print("恭喜你回答正确！")
        break
```
