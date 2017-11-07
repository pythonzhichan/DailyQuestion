# -*- coding: utf-8 -*-

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield a
        a, b = b, a + b
        n = n + 1

def output(num):
    res = []
    for i in fib(num):
        res.append(i)
    print(res)

output(10)