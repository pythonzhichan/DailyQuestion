# _*_ coding=utf-8 _*_
# # author: Lzy
# # version: python 2.7
# # question:
# '''
# 用Python实现斐波那契数列，费波那契数列由0和1开始，
# 之后的费波那契系数就是由之前的两数相加而得出，
# 例如前 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# '''
# # 这是我的回答:

#方法1：正常处理

def feibo1(n):
#此处可以写成 a,b,i=0,1,0
    a = 0
    b = 1
    i = 0
#while 处也可以用for
    while i < n:
        a, b = b, a + b
        i += 1
    return a

if __name__ == '__main__':
    for i in range(10):
        print feibo1(i),

#方法2：用列表
def feibo2(n):
    list_a = [0,1]
    while n-2:
        list_a.append(list_a[-1]+list_a[-2])
        n -= 1
    return list_a

if __name__ == '__main__':
    print feibo2(10)

#方法3：递归函数
def feibo3(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feibo3(n-2) + feibo3(n-1)

if __name__ == '__main__':
   for i in range(10):
        print feibo3(i),

#方法4：迭代---有空补上




