#_*_ coding:utf-8 _*_

#!/user/bin/python

import random

number_random = random.randint(1,100)



for chance in range(5):     #玩家有5次机会

   number_player=input('请输入一个1-100之间的整数：')

   if(number_player>number_random):

       print('这个数字偏大')

   elif (number_player<number_random):

       print('这个数字偏小')

   print('你还有%d次机会')%(4-chance)

   while (chance == 4):  #当for遍历到第最后一次的时候

       if (number_player == number_random):

           print('恭喜你答对了')

           break

       else:

           print('正确答案是：%s') % number_random

           break

