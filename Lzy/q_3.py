# _*_coding:utf-8_*_
# author: Lzy
# version: python 2.7
# question: 统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。

# 这是我的回答: ---------  抄作业

import re

class Counter(object):
    def __init__(self,path):
        self.mapping = dict()
        with open(path) as f:
            data = f.read()
            words = [s.lower() for s in re.findall("\w+",data)]
            for word in words:
                #这里这个get(word,0)用的好，需要记住
                self.mapping[word] = self.mapping.get(word,0) + 1

    def most_common(self,n):
        #assert 的用法需要记住，以前只知道assert用来判断一个条件的真假，但知道和会用是2个概念！！
        assert n > 0, "n should be large than 0"
        return sorted(self.mapping.items(),key = lambda item: item[1],reverse=Ture)[:n]


if __name__ == '__main__':
    most_common_5 = Counter("this.txt").most_common(5)
    for item in most_common_5:
        print item


