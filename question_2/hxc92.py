from random import randrange


def f(truth, times):
    while times:
        guess = int(input('剩余游戏次数：%s\n请输入您的答案：' % times))
        '''while not isinstance(guess, int):
            print('您输入的不是整数，请重新输入')
            '''
        if guess == truth:
            print('回答正确，游戏结束')
            break
        else:
            if guess > truth:
                print('您的结果偏大')
            else:
                print('您的结果偏小')
        times -= 1
    else:
        print('游戏结束，失败\n答案为%s' % truth)


right_answer = randrange(1, 100)
f(right_answer, 5)
