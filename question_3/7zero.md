题目：统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。

```
import collections

filename = 'import_this.txt'
with open(filename) as f:
    list_str = f.read().split()
    data_dict = collections.Counter(list_str)
    new_list = (sorted(data_dict.items(), key=lambda x: x[1], reverse = True))
    for i in new_list[0:5]:
        print(i)

```
