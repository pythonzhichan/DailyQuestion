# coding=utf-8

# DailyQuestion 2: guess number game

import random

gamestart = 'Y'
while gamestart == 'Y':
    rndnum = random.randint(1,100)
    testnum = 5

    print(u"\n猜数游戏")
    print(u"\n游戏规则：电脑给出一个[1,100]之间的整数，让你来猜数。")
    print(u"提示：电脑会给出数字偏大或偏小的信息。")
    print(u"　　　你最多可以猜 %d 次。" %testnum)
    print(u"\n准备好，按任意键开始猜数……",end="")
    input()
    while testnum>0:
        print('number = ',rndnum)
        testnum = testnum -1
        while 1:
            inputstr = input(u"你猜数字是多少：")
            if inputstr.isdigit():
                usernum = int(inputstr)
                if usernum>=1 and usernum <=100:
                    break
                else:
                    print(u"无效输入！只限整数，范围[1,100]，请重新输入。")
            else:
                print(u"无效输入！只限整数，范围[1,100]，请重新输入。")
                
        if usernum == rndnum:
            print(u"恭喜你，你猜对了！")
            # 重置测试次数
            testnum = 5
            break    
        elif usernum > rndnum:
            print(u"偏大。你还有 %d 次机会。" % testnum)
        else:
            print(u"偏小。你还有 %d 次机会。" % testnum)
    if testnum ==0:
        print(u"游戏失败，正确数字是 %d 。" % rndnum)
    print(u"\n是否再玩一次？按 Q 退出，其它继续。",end="")
    quitstr = input()
    if quitstr.upper() == 'Q':
        gamestart = 'N'
