> ## 现在是通过Git的方式向GitHub远程仓库提现的结果
```
numbers = [10, 29, 30, 41]
for i in range(len(numbers)):
    print("(%d, %d)" % (i,numbers[i]),end="")
    if i < len(numbers) - 1:
        print(end="，")
```
## 但我希望可以跟简洁点
```
numbers = [10, 29, 30, 41]
for i in range(len(numbers)):
    print("(%d, %d)" % (i,numbers[i]),end="，")
print(end="\b")
```
## 可惜输出的结果是
> (0, 10)，(1, 29)，(2, 30)，(3, 41)，
### 最后一个逗号不但没删掉，反而多了一个乱码
