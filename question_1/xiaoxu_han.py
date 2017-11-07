# -*- coding: UTF-8-*-
def enumerate_fn():
 '''enumerate是python内置函数：获取每个元素的索引和值
 :return:打印每个元素的索引和值
 '''
 list = [10,29,30,41,50]
 for index, value in enumerate(list,0):
     print (index,value)
enumerate_fn()    
