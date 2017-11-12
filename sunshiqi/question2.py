# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/10/31 0031'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import random

class GuessValue():
    def __init__(self, min_num, max_num, choice):
        self.min_num = min_num
        self.max_num = max_num
        self.choice = choice
        self.target = random.randint(min_num, max_num)

    def guess(self):
        choice = self.choice

        while choice > 0:
            choice -= 1
            try:
                num = int(input('请输入幸运数字：'))
            except ValueError:
                print('请输入整数')
                continue

            if num == self.target:
                print('恭喜你猜中了！')
                break
            elif num < self.target:
                print('猜小了，你还有%d次机会' % choice)
            else:
                print('猜小了，你还有%d次机会' % choice)
        else:
            print('很遗憾，%d次机会都用光了，正确的数字是%d' % (self.choice, self.target))

if __name__ == '__main__':
    game = GuessValue(1, 100, 5)
    game.guess()