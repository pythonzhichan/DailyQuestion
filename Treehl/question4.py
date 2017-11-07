# _*_ coding:utf-8 _*_

'''
用Python实现斐波那契数列(Fibonacci sequence)
除第一个和第二个数外，任意一个数都可由前两个数相加得到:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def fib(max):
    #n=0, a=0, b=1
    n, a, b = 0, 0, 1
    #条件满足 n < max 就循环,n > max 就停止
    while n < max:
        print(b)
        #不等于a=b, b=a + b
        a, b = b, a + b
        n = n + 1
    return 'done'
#调用函数
f= fib(9)
print(f)
