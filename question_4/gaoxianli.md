# 斐波那契数列
### 斐波那契数列是一组数列，从 0 和 1 开始，之后（第3项开始）的每一项都等于前两项之和。
，例如：斐波那契数列的前10个数是：
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

在数学上，用递归的方法定义斐波纳契数列如下：
> F(0)=0
F(1)=1
F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

## Python Code

```
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
```
执行结果如下：
```
F:\Python>python Fibonacci_sequence.py
您要输出斐波那契数列的多少项？（正整数）：10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ……

您要输出斐波那契数列的多少项？（正整数）：2
0, 1, ……

您要输出斐波那契数列的多少项？（正整数）：1
0, ……

您要输出斐波那契数列的多少项？（正整数）：0
不能输入小于1的数，请您重新输入一个正整数

您要输出斐波那契数列的多少项？（正整数）：-1
不能输入小于1的数，请您重新输入一个正整数

您要输出斐波那契数列的多少项？（正整数）：5.1
不能输入小数，请您重新输入一个正整数

您要输出斐波那契数列的多少项？（正整数）：
结束！

F:\Python>
```
## 代码解读
```
def fibo_num(item):
    if item > 2:
        return fibo_num(item-1) + fibo_num(item-2)
    elif item == 2:
        return 1
    elif item == 1:
        return 0
```
`fibo_num(item)` 函数是利用递归的方式求第 item 项的的斐波那契数
```
def each_item(items):
    for item in range(1,items+1):
        print("%d, " % fibo_num(item), end="")
    print("……\n")
```
而 `each_item(items)` 函数里面定义了从第1项开始迭代输出每一项，直到第 items 项结束
```
while True:
        items_float=float(input("您要输出斐波那契数列的多少项？（正整数）："))
        items_int = int(items_float)
        if items_int < 1:
                print("不能输入小于1的数，请您重新输入一个正整数\n")
        elif items_int != items_float:
                print("不能输入小数，请您重新输入一个正整数\n")
        else:
                each_item(items_int)
```
这段代码让程序不断循环，方便让用户可以不断输入，直到用户按 `Ctrl + C` 快捷键才结束

但一开始上面这段代码不是这样的，程序要求用户输入的是正整数（多少项），如果不符合要求就给出相应的提示
所以用户不能输入比1小的数，也不能输入小数（输出 5.1 项是啥意思？）。
判断是否比1小比较简单 `items < 1` ，那判断是不是小数呢？我注意到 `type(5.1)` 返回的是 `float`，因此可以用 `type(items) == float`
```
items = input("您要输出斐波那契数列的多少项？（正整数）：")
if items < 1:
        print("不能输入小于1的数，请您重新输入一个正整数\n")
elif type(items) == float:
        print("不能输入小数，请您重新输入一个正整数\n")
```
可是万万没想到程序报错，提示 str 不能与 int 作比较，也就是说用户以为输入的是数字，但其实是字符串
如果把输入的转换为 int 类型不就可以比较了吗？
```
items = int(input("您要输出斐波那契数列的多少项？（正整数）："))
if items < 1:
        print("不能输入小于1的数，请您重新输入一个正整数\n")
elif type(items) == float:
        print("不能输入小数，请您重新输入一个正整数\n")
```
可是再观察一下会发现 `type(items) == float` 永远不会成立！因为 items 被 `int()` 转化为整数。
如果把用户输入的字符串用 `float()` 转成浮点型，`type(items) == float` 又永远都成立
后来我又注意到 `int(5.0)` 返回 `5`，而 `int(5.1)` 也返回 `5`，这样就可以根据 `int()` 转换前后的值是否相等来判断是小数还是整数
```
>>> int(5.0) == 5
True
>>> int(5.1) == 5.1
False
```
返回 `True` 表示用户输入的是整数（当然也可能用户本来输入 `5.0`，这种情况也当作整数吧），
返回 `False` 表示用户输入的是小数
修改后代码如下：
```
items_float=float(input("您要输出斐波那契数列的多少项？（正整数）："))
items_int = int(items_float)
if items_int < 1:
        print("不能输入小于1的数，请您重新输入一个正整数\n")
elif items_int != items_float:
        print("不能输入小数，请您重新输入一个正整数\n")
else:
        each_item(items_int)
```
