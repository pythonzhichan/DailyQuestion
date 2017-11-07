# 例如斐波那契数列的前10个数是 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。用数学方法可定义为如图所示：
#if n=0 f(n)=0;if n=1 f(n)=1 if (n>1) f(n)=f(n-1)+f(n-2)
#思路: 一、确定变量 num_input （我要输出多少个数列）、f(n-1)、f(n-2)、num_feb
#      二、由列表次序排列和斐波那契定义可以使用num_feb[-2]和num_feb[-1]表示最后两位
#      三、列表个数可以通过range进行循环
#      四、关于输入量的判断
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
