#day1
#question1
#在使用for循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，
#例如numbers = [10,29,30,41],要求输出（0，10），（1，29），（2，30），（3，41）

numbers = [10, 29, 30, 41]
for index, value in enumerate(nummbers):
    print(index, value)
