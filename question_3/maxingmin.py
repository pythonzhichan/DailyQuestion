'''
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词.
'''
import re
from collections import Counter


def version1():
    words = re.findall(r'\w+', open('import_this.txt').read().lower())
    print(Counter(words).most_common(5))


def version2():
    def read_data(path):
        with open(path, encoding='utf-8') as f:
            data = f.read().lower()

        words = re.findall(r'\w+', data)
        mapping = dict()
        for word in words:
            mapping[word] = mapping.get(word, 0) + 1
        return mapping

    def count_common(path, n):
        assert n > 0
        mapping = read_data(path)
        return sorted(mapping.items(), key=lambda item: item[1], reverse=True)[:n]
        a = str()

    print(count_common('import_this.txt', 5))


version1()
version2()
