路明非的回答

斐波那契数列是常见的递归问题，很多oj题目的规律都是斐波那契，但是使用递归方法会超时，一般在oj遇到这种题目都用递推。

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

num_list = [0, 1]

index = int(input('要取前多少个数？'))
for i in range(2, index):
    num_list.append(num_list[i-1] + num_list[i-2])

print(num_list)
```
