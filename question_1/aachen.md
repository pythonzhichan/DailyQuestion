#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 17/10/27 7:06 PM
# Author : CA

"""
在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
"""

"""
使用内置函数 enumerate 函数输出值
"""
numbers = [10, 29, 30, 41]

for index, value in enumerate(numbers):
    print(index, value)
