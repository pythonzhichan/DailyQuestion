
#每日一题# 第4题：
终身学习是一本万利的投资，又是新的一周，行动起来
今天来做一道算法题，用Python实现斐波那契数列
斐波那契数列由0和1开始，之后的斐波那契系数就是由之前的两数相加而得出，
例如斐波那契数列的前10个数是 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。用数学方法可定义为如图所示：
<pre>
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def print_fibo(each):
    for i in range(0,each):
        print("%d," % fibo(i),end='')

if __name__ == '__main__':
        while True:
            number = int(input('\n请输入需要输出的斐波那契数列的项数:'))
            print_fibo(number)
</pre>