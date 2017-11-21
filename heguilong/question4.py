#!/usr/bin/env python3
"""
File: heguilong.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:
    斐波那契数列由0和1开始，之后的斐波那契系数就是由之前的两数相加而得出，例如
斐波那契数列的前10个数是 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。
"""
import logging
import sys

import numpy as np


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s \
                    - %(message)s')


# solution 1, O(1.618^n)
class Fibonacci():
    def __init__(self):
        """TODO: Docstring for __init__.

        :arg1: TODO
        :returns: TODO

        """
        self.fib_dict = {}

    def calculate(self, number):
        """TODO: Docstring for calculate.

        :f: TODO
        :number: TODO
        :returns: TODO

        """
        # logging.debug("number: {%d}" % number)
        assert number >= 0
        if number in (0, 1):
            result = number
        else:
            result = self.calculate(number - 1) + self.calculate(number - 2)
        if number > 0 and number not in self.fib_dict:
            self.fib_dict[number] = result
        return result

    def show_fib_values(self):
        print(self.fib_dict.values())


# solution 2, O(n)
def fib_loop(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


# solution 3, O(logn)
def fib_matr(n):
    return (np.matrix([1, 1], [1, 0]) ** (n - 1) * np.matrix([1], [0]))[0, 0]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 heguilong.py number")
        sys.exit()
    number = int(sys.argv[1])
    if number <= 0:
        print("number should be larger than 0")

    # solution 1
    print("Solution 1:")
    fib_obj = Fibonacci()
    fib_obj.calculate(number)
    fib_obj.show_fib_values()

    # solution 2
    print("Solution 2:")
    for i in fib_loop(number):
        print(i, end=" ")

    # solution 3
    print("Solution 3:")
    for n in range(number):
        print(fib_matr(n), end=" ")
