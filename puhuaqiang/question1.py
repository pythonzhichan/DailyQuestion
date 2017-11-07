#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author  :   {PHQ}
@License :   (C) Copyright 2017, {public}
@Contact :   {puhuaqiang@hotmail.com}
@Software:   {question_1}
@File    :   question1.py
@Time    :   2017-10-28
@Desc    :

每日一题的第1题：
    在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，
例如 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
'''

'''
@analysis:
    1.构造列表
    2.枚举列表
    3.格式化字符串
    4.字符串拼接
    涉及知识点:列表、字符串、内建函数
@result:
    代码执行输出结果:(0,10),(1,29),(2,30),(3,41)
'''

numbers = [10, 29, 30, 41]
str_ret = ''
index = 0
for item in numbers:
    if len(str_ret) > 0:
        str_ret += ','
    str_ret += '({1},{0})'.format(item,index)
    index += 1
print(str_ret);

