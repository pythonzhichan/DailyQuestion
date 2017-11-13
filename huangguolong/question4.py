

def fib(nums):
    '''
    :param nums: 一个整数，相当于数列的下标
    :return: 返回该下标的值
    '''
    if nums == 0 or nums == 1:
        return nums
    else:
        return fib(nums-2) + fib(nums-1)


def createFib(n):
    '''
    :param n: 需要展示前面n个数
    :return: 返回一个列表，费波那契数列
    '''
    list1 = []
    for i in range(n):

        list1.append(fib(i))

    print(list1)

#调用生成费波那契数列函数，指定展示的前面n个数
createFib(20)
