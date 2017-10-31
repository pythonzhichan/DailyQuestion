# author: Lzy
# version: python 2.7
# question: 设计一个猜数字的游戏
系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统会提示玩家该数字是偏大
还是偏小，如果猜中了，则告诉玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知
正确答案

# 这是我的回答:
# _*_coding:utf-8_*_

import random

def main():
    correct_number= random.randint(1, 100)

    print u"猜数字游戏："
    print u"游戏规则：请输入1-100之间的数字."
    print u"你有5次机会，看看你的运气如何吧！"

    for i in range(1, 6):
        print u'第 %s 次请输入你猜的数字：' %i
        guess_number = raw_input('->')
        #判断guess_number是否为数字用 isdigit()
        if guess_number.isdigit():
            if correct_number == int(guess_number):
                print u"恭喜你答对了！游戏结束！"
                break
            elif correct_number < int(guess_number):
                print u"你猜的太大了！"
            else:
                print u"你猜的太小了！"
        else:
            print u"输入错误，请重新输入1-100之间的数字！"
    if i == 5 and guess_number != correct_number:
        print u"游戏结束，要猜的数字是：%s" % correct_number

if __name__== '__main__':
    main()