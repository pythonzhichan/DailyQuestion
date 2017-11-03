'''
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词.
'''

import re
from collections import Counter

words = re.findall(r'\w+', open('import_this.txt').read().lower())
print(Counter(words).most_common(5))
