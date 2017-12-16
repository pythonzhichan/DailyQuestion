import random

# 选定随机答案
ans = random.randint(1, 100)


class OverValueException(Exception):
    '''
    猜测的数值超过了100
    '''
    pass


class LessValueException(Exception):
    '''
    猜测的数值小于1
    '''
    pass


# 所有机会
chances = 5
while(chances):
    guessAns = input("请输入猜测的数字：")
    try:
        intAns = int(guessAns, 10)
        if intAns > 100:
            raise OverValueException
        elif intAns < 1:
            raise LessValueException
        if intAns == ans:
            print("恭喜你，猜对了！")
            break
        elif intAns > ans:
            print("太大啦")
            chances -= 1
        else:
            print("太小啦")
            chances -= 1
    except OverValueException as over:
        print("答案在1到100呢，您猜的太大了")
        chances -= 1
    except LessValueException as less:
        print("答案在1到100呢，您猜的太小了")
        chances -= 1
    except Exception as ex:
        print("请输入数字呢")
        chances -= 1
print("答案是" + str(ans))
