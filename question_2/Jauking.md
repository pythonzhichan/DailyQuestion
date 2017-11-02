# 张强的question_2作业

import random
guess = random.randint(1, 100)

print("猜1-100的整数，共5次机会。")

i = 0
while i < 5:
    i += 1
    answer = int(input("请输入："))
    if answer == guess:
        print("恭喜！猜对了。")
        break
    elif answer < guess:
        print("小了，猜大些吧。")
    else:
        print("大了，猜小些吧。")
print("游戏结束。正确答案" , guess)
