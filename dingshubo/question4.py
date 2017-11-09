#!/user/bin/env python
#_*_coding:utf-8_*_
try:
  num_input=int(raw_input('请输入你想获得n+2位的斐波那契数列）：'))  #输出斐波那契数列个数,2为初始位
  num_feb=[0,1]    #初始位
  while num_input<=0:
      print('你所输入的不是一个有效整数！')
      break
  for i in range(0,num_input):
     num_feb.append(num_feb[-2]+num_feb[-1])
     print('所想获得的斐波那契数列为%r')%num_feb
except ValueError:
    print('\n你输入的不是一个整数！')
