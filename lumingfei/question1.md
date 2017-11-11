路明非的回答

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

numbers = [10, 29, 30, 41]

# 第一种方法，使用一个变量记录列表的索引
index = 0
for i in numbers:
    print(index, i)
    index += 1

print('---------\n')

# 第二种方法，通过索引获取值
for i in range(0, len(numbers)):
    print(i, numbers[i])

print('---------\n')

# 第三种方法，使用list的index()方法获取元素的索引值
for i in numbers:
    print(numbers.index(i), i)

print('---------\n')

# 第四种方法，使用enumerate(枚举)
i = 0
for i, element in enumerate(numbers):
    print(i, element)
```
