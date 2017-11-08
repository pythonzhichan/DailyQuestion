# 每日一题  第2题：

设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

```python
import random
secret = random.randint(1, 100)  # 生成随机数

time = 5  # 猜数字的次数
guess = 0  # 输入的数字
minNum = 0  # 最小随机数
maxNum = 100  # 最大随机数
print("---------欢迎来到猜数字的地方，请开始---------")
while guess!=secret and time>=0:#条件
    guess = int(input("*数字区间0-100，请输入你猜的数字:"))
    print("你输入数字是：", guess)
    if guess == secret:
        print("猜对了，真厉害")
    else:
        # 当不等于的时候，还需要打印出相应的区间，让用户更容易使用
        if guess < secret:
            minNum = guess
            print("你的猜数小于正确答案")
            print("现在的数字区间是：", minNum, "-", maxNum)
        else:
            maxNum = guess
            print("你的猜数大于正确答案")
            print("数字区间是：", minNum, "-", maxNum)
        print("太遗憾了，你猜错了，你还有", time, "次机会")
    time -= 1
print("游戏结束！正确数字是:" + str(secret))
```
