# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/11/6 0006'
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
class Fibonacci():
    def __init__(self, number):
        self.number = number

    def check_for_Fib(self):
        if not isinstance(self.number,int):
            print('please input the integer')
            return False
        self.number = int(self.number)
        if self.number < 0:
            print('Your input should be greater than zero')
            return False
        return True

    def count_for_Fib(self):
        if not self.check_for_Fib():
            return
        n, a, b = 0, 0, 1
        while n < self.number:
            yield a
            a, b = b, a+b
            n = n + 1

    def display_for_Fib(self):
        if self.number == 0:
            print(self.number)
        elif self.number == 1:
            print(self.number)
        else:
            for num in self.count_for_Fib():
                print(num)

if __name__ == "__main__":
    fib = Fibonacci(10)
    fib.display_for_Fib()