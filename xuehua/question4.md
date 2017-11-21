# -*- coding : UTF-8 -*-

nums = int(input("你需要几项(1~50)？"))
 
# 第一和第二项
Fibo_1 = 0
Fibo_2 = 1
count = 2
 
# 判断输入的值是否合法
if nums <= 0 or nums >= 51 :
   print("请输入一个不大于50的正整数。")
elif nums == 1:
   print("斐波那契数列：")
   print(Fibo_1)
else:
   print("斐波那契数列：")
   print(Fibo_1,",",Fibo_2,end=" , ")
   while count < nums:
       Fibo = Fibo_1 + Fibo_2
       print(Fibo,end=" , ")
       # 更新值
       Fibo_1 = Fibo_2
       Fibo_2 = Fibo
       count += 1