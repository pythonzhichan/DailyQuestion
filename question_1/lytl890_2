# -*- encoding:utf-8 -*-
from random import randint
rannumber=randint(1,100)
count=0
print rannumber
while count<5:
    number=input('请输入你要猜的数字:')
    if isinstance(number,int):
        count+=1
        if number==rannumber:
            print ('恭喜你,猜对了')
            break
        elif number<rannumber:
            print ('你猜的数字偏小了,请往大一点的数字猜')
        else:
            print ('你猜的数字偏大了，请往小一点的数字猜')
        print ('你还剩余{0}次机会'.format(5-count))
    else:
        print ('输入的不是数字，重新输入:')
print ('游戏结束,正确答案是:%s'%rannumber)
