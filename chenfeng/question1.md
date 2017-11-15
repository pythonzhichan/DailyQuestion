#### chenfeng
---
##### date:2017-10-27
##### question:在使用`for`循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如：有列表 `numbers = [10, 29, 30, 41]`，要求输出`(0, 10)，(1, 29)，(2, 30)，(3, 41)`
---
> 解题思路：

1) 主要知识点：
1.  内置函数`enumerate()`的使用，可以同时获得索引和值;
2. 字符串`join()`函数的使用.
>代码实现
```python
numbers = [10,29,30,41]
print(",".join(str((i,number)) for (i,number) in enumerate(numbers)))
```
