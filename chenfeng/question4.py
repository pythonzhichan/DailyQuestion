#!usr/bin/python3
#-*- coding:utf-8 -*-

'''
@auter:chenfeng
@date:2017-11-7
@remark:简单实现斐波拉契数列
'''

def print_fib(index):
    the_front, the_behind = 0, 1
    
    while the_front < index:
        print(the_front, end=',')
        the_front, the_behind = the_behind, the_front + the_behind

if __name__ == '__main__':
    try:
        index_num = int(input("请输入需要打印的前n位的斐波那契数列："))
        print_fib(index_num)
    except ValueError as e:
        print("输入的数字不合法")
