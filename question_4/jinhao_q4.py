# python 3
# -*- Coding:utf-8 -*-

class Fibo(object):
    def __init__(self):
        self.fibo_0 = 0
        self.fibo_1 = 1

    def fibo_top(self, n):
        '''
        获取前n个斐波那契数
        ''' 
        fibo = [self.fibo_0, self.fibo_1]
        for i in range(2, n):
            # print(i)
            fibo.append(fibo[i-2] + fibo[i-1])
        return fibo


    def fibo_before(self, n):
        '''
        获取小于数字n的所有斐波那契数
        ''' 
        fibo = [self.fibo_0, self.fibo_1]
        i = 2
        while True:
            fibo.append(fibo[i-2] + fibo[i-1])
            # print(i, fibo)
            if fibo[i] > n:
                return fibo[:-1]
            else:
                i += 1
            

if __name__ == '__main__':
    f= Fibo()
    top_n = 20    
    print('前{0}个斐波那契数：\n{1}'.format(top_n, f.fibo_top(top_n)))
    
    before_n = 20000
    print('小于数字{0}的所有斐波那契数：\n{1}'.format(before_n,f.fibo_before(before_n)))
