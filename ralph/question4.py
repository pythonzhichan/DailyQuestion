#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
第4题：

用Python实现斐波那契数列，费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出
'''


class Fibo(object):

    def __init__(self):
        pass

    def fib(self, num):
        fibo_list = [0]
        cnt, x, y = 0, 0, 1
        while cnt < num - 1:
            fibo_list.append(y)
            x, y = y, x + y
            cnt += 1
        return fibo_list

fibo = Fibo()
num = int(input("请输入你想得到的斐波那契数列的长度： "))
print("该数列为： ", fibo.fib(num))