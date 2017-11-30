'''
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
'''


import io
import re
from collections import defaultdict


def countor(file):
    word_dict = defaultdict(int)
    with io.open(file, 'r', encoding='utf-8') as f:
        word_list = re.compile('[a-zA-Z]+').findall(f.read())
    for word in word_list:
        word_dict[word] += 1
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:5]


for word, times in countor('test.txt'):
    print(word, times)
