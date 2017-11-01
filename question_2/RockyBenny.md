import random

scode = random.randint(1,100)
guess = 0
times = 0

print("现在，我生成了一个秘密数字，0到100，你有五次机会，请猜对我的秘密数字，加油哦～")

while guess != scode and times < 5 :
    guess = int(input("输入你的猜的数字吧"))
    if guess < scode :
        print("偏小咯，请继续猜")
    elif guess > scode :
        print("偏大咯，请继续猜")

    times = times +1

if guess == scode:
    print ("厉害啦我的歌！你猜对了！游戏结束。")

else:
    print ("你的次数用完了，真遗憾。")
    print ("正确的秘密数字是", scode)
