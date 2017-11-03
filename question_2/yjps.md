#每日一题 第2题：
设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

#代码:
```python
from random import randint
number = randint(1,100)
times = 5
print('猜一个1~100之间的数字,退出请输入:0')
while times >= 0:
    if times == 0:
        print('次数用完,正确答案:' + str(number))
        break
    answer = input('还有' + str(times) + '机会:')
    try:
        answer = int(answer)
        if answer == 0:
            break
        times -= 1
        # print(type(answer))
        if answer < number:
            print('猜小了')
        elif answer > number:
            print('猜大了')
        else:
            print('恭喜你猜对了!')
            break
    except ValueError:
        print('--------请输入数字--------')
```