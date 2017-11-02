import collections
import re

with open("import_this.txt","r",encoding="utf-8") as file1: #打开文本表

    tmp_str = file1.read().split(' ')  # 将文章按照空格划分开,存础为列
    count = collections.Counter(tmp_str) #以字典的形式存储,每个自符对应的键值就是在文本中出现的次数
    print('每个单词出现的次数：%s'%count)
    print('出现最多的：%s'%count.most_common()[:5])  #取出
