numbers = [10,29,30,41]

#方法一，用了不太理解enumerate函数

for idx,val in enumerate(numbers):     #内建函数enumerate

    print ("("+str(idx)+","+str(val)+")"

#方法二，最直接的做法
for a in numbers:
    print("("+str(numbers.index(a))+","+str(a)+")")dddddd
