# 张强的question_4作业
# 从题目图片上看，军哥好像是希望用递归解题
# 我脑筋绕不过弯，不会做。先用循环写个，递归的坐等讲解

def fib(end = 10000, f0 = 0, f1 = 1):
    fib_list = [f0, f1]
    while True:
        if f0 + f1 > end:
            break
        fib_list.append(f0 + f1)
        f0, f1 = f1, f0 + f1

    return print(fib_list)

fib(200)
