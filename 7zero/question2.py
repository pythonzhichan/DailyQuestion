import random

class GuessGame:
    def __init__(self, min_num, max_num, choice):

        self.max_num = max_num
        self.min_num = min_num
        self.target = random.randint(min_num, max_num)
        self.choice = choice

    def guess(self):
        choice = self.choice

        while choice > 0:
            choice -= 1
            try:
                num = int(input("输入幸运数字："))
            except ValueError as e:
                print("请输入有效数字")
                continue

            if num == self.target:
                print("恭喜你猜中了")
                break
            elif num < self.target:
                print("你猜的数字小了，还有 %d 次机会" % choice)
            else:
                print("你猜的数字大了！，还有 %d 次机会" % choice)
        else:
            print('很遗憾，{} 次机会都用完了,正确答案是 {}'.format(self.choice,self.target))


if __name__ == '__main__':
    game = GuessGame(1, 100, 5)
    game.guess()
