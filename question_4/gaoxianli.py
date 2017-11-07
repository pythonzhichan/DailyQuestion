def fibo_num(item):
        if item > 2:
                return fibo_num(item-1) + fibo_num(item-2)
        elif item == 2:
                return 1
        elif item == 1:
                return 0

def each_item(items):
        for item in range(1,items+1):
                print("%d, " % fibo_num(item), end="")
        print("……\n")

if __name__ == "__main__":
        try:
                while True:
                        items_float=float(input("您要输出斐波那契数列的多少项？（正整数）："))
                        items_int = int(items_float)
                        if items_int < 1:
                                print("不能输入小于1的数，请您重新输入一个正整数\n")
                        elif items_int != items_float:
                                print("不能输入小数，请您重新输入一个正整数\n")
                        else:
                                each_item(items_int)
        except KeyboardInterrupt:
                print('\n结束！')