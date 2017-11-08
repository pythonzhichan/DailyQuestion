# _*_coding:utf-8 _*_

# author: Lzy
# version: python 2.7
# question:
在使用for循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少?
例如：有列表 numbers = [10, 29, 30, 41]，
要求输出(0, 10)，(1, 29)，(2, 30)，(3, 41)
# 这是我的回答:

numbers= [10, 29, 30, 41]
for key, value in enumerate(numbers):
    print "(%s,%s)" %(key,value)
