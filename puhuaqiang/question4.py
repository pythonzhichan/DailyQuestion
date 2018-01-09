#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author  :   {PHQ}
@License :   (C) Copyright 2017, {public}
@Contact :   {puhuaqiang@hotmail.com}
@Software:   {question_3}
@File    :   question4.py
@Time    :   2017-11-07
@Desc    :

    用Python实现斐波那契数列
'''

class Fibonacci():

    def __init__(self, n):
        # 需要查询的序号
        self.que_serial_number = n
        #当前序号, 0是第0项，不是第1项
        self.current_serial_number = 0
        #当前序号的值
        self.current_serial_number_value = 0
        #保存前2个值的数组 [0]=f(n-2) [1]=f(n-1)
        self.val = [0,0] 

    def calculate(self):
        '''
            得到当前序号的值
        '''
        if self.current_serial_number < 2:
            if self.current_serial_number == 0:
                self.current_serial_number_value = 0
            else:
                self.current_serial_number_value = 1
        else:
            self.current_serial_number_value = self.val[0] + self.val[1]

        self.val[0] = self.val[1]
        self.val[1] = self.current_serial_number_value
        
        if self.current_serial_number == self.que_serial_number:
            return
        # 计算下一个序号
        self.current_serial_number += 1
        self.calculate()
        
    def ans(self):
        if not isinstance(self.que_serial_number, int):
            print("查询序号值错误!")
            return
        self.current_serial_number = 0
        self.calculate()
        return self.current_serial_number_value

if __name__ == '__main__':
    number = 6
    print("第%d序列数:%d" % (number,Fibonacci(number).ans()))
        

        
