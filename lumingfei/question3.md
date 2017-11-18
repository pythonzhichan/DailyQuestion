路明非的回答：

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

word_list = re.sub('[,|.|!|*|-]', ' ', open('import_this.txt').read()).split()
word_dict = {}

for word in word_list:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

new_word_list = sorted(word_dict.items(), key=lambda item:item[1])
print('出现频率最多的五个单词是:')
for index in range(0, 5):
    print('单词:', new_word_list[::-1][index][0], ' 次数:', new_word_list[::-1][index][1])
```
