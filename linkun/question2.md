#林坤的作业
import random
answer = random.randint(1,100)
i = 1
while i <= 5:
    guess = int(input("猜一个0到100的整数："))
    if guess == answer:
        print('厉害了，猜对了！')
        break
    else :
        if guess > answer:
            print('猜大了！')
        else :
            print('猜小了！')
        chance = 5 - i
        print('再猜，还有%d次机会！'%chance)
    i += 1
print('游戏结束，正确答案是：%d'%answer)