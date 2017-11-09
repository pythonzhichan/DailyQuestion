import math
def fibo(index):
   if index >2:
      return fibo(index-1)+fibo(index-2)
    elif index ==2:
      return 1
    elif index ==1:
      return 0
if __name__=="__main__":
   temp = int(input('please input a num(num>2):'))
    print fibo(index)
