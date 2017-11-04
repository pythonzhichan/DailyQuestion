#!usr/bin/python3
#-*- coding:utf-8 -*-

'''
@auter:chenfeng
@date:2017-11-2
@remark:统计python之禅中出现频率最多的5个单词
'''

import collections
import re

def read_file(file_source):
    #读取文件
    with open(file_source,'r') as article_file:
        return article_file.read()

def statistic_words(file_source):
    result_list = re.findall('[a-z\'A-Z]+',read_file(file_source))
    #print(result_list)
    coll_words = collections.Counter(result_list)
    print(coll_words.most_common(5))

if __name__ == '__main__':
    file_source = "import_this.txt"
    statistic_words(file_source)
