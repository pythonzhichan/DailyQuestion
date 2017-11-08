from random import randrange


class GuessGame(object):
    def __init__(self, min_int, max_int, times ):
        self.truth = randrange(min_int, max_int)
        self.min_int = min_int
        self.max_int = max_int
        self.times = times

    def guessing(self):
        times = self.times
        truth = self.truth
        while times:
            try:
                guess = int(input('剩余游戏次数：%s\n请输入您的答案：' % times))
            except ValueError as e:
                print('输入的不是数字，请重新输入')
                continue
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


if __name__ == '__main__':
    game = GuessGame(1, 100, 5)
    game.guessing()

