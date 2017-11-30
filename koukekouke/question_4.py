'''
用Python实现斐波那契数列，费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出，
例如前 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。
'''


def fibonacci(n):
    num_list = []
    a, b = 0, 1
    for i in range(n):
        num_list.append(a)
        a, b = b, a+b
    return num_list


print(fibonacci(10))
