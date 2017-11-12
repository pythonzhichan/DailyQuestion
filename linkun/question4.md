'''
 斐波那契数列由0和1开始，之后的斐波那契系数就是由之前的两数相加而得出，例如
斐波那契数列的前10个数是 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。
'''
def f(n):
    if n > 1:
        return f(n-1)+f(n-2)
    elif n == 1:
        return 1
    else:
        return 0
try:
    n = int(input('How many sequence numbers do you want ?'))
    if isinstance(n,int) and n >= 0:
        for i in range (0,n):
            print(f(i),end=' ')
    else:
        print("Please input an integer not less than 0")
except ValueError as e:
    print(e)

