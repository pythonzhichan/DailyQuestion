#!/usr/bin/python3
# -*- coding: UTF-8 -*-


def gen_fibonacci(n=10):
    if n == 1:
        print([0])
    elif n == 2:
        print([0, 1])
    else:
        i = 2
        lis = [0, 1]
        while i < n:
            lis.append(lis[-1] + lis[-2])
            i += 1
        print(lis)


try:
    num = int(input('Please input the number of objects you want to generate:'))
except Exception as e:
    print('Invalid input! Out first 10 objects by default.')
    exit(1)
else:
    if num <= 0:
        print("Must be greater than 0.")
    else:
        gen_fibonacci(num)
