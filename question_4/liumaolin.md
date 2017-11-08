# 第四题
### 用Python实现斐波那契数列，费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出，例如斐波那契数列 前10个数分别为：0, 1, 1, 2, 3, 5, 8, 13, 21, 34。



``` python
# Solution1 递归实现
def Fibonacci(n):
    assert n >= 0, "n should be large than 0"
    if n < 2:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)


# Solution2 循环实现
def Fibonacci(n):
    assert n >= 0, "n should be large than 0"
    if n < 2:
        return n
    x, y = 0, 1
    for i in range(2, n + 1):
        x, y = y, x + y
    return y
```