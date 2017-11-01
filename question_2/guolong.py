import random

ranNum = random.randint(1,100)
nums = 5



for i in range(5):
    userInput = int(input('请猜一个1-100之间的整数：'))
    nums = nums - 1
    if ranNum == userInput:
        print('随机数是{0}，游戏结束，恭喜你！猜中了'.format(ranNum))
        break

    elif userInput < ranNum :
        if nums == 0 :
            print('随机数是{0}，很遗憾，猜少了！游戏结束，你没有机会了'.format(ranNum))
        else :
            print('很遗憾，猜少了！你还有{0}次机会'.format(nums))

    elif userInput > ranNum:
        if nums == 0 :
            print('随机数是{0}，很遗憾，猜多了！游戏结束，你没有机会了'.format(ranNum))
        else :
            print('很遗憾，猜多了！你还有{0}次机会'.format(nums))
