#!D:\\Python34
# -*- coding: UTF-8 -*-

'''
@Author  :   {PHQ}
@License :   (C) Copyright 2017, {public}
@Contact :   {puhuaqiang@hotmail.com}
@Software:   {question_3}
@File    :   MrPHQ.py
@Time    :   2017-11-02
@Desc    :
每日一题的第3题：
    统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
'''

import re
try:
    # 打开文件,如果运行请修改文件路径
    with open("f:\import_this.txt",'r') as my_file:
        data = my_file.read()
        #print(data)
        read_len = 0
        words = {}
        # 使用正则表达式读取单个单词
        while 1:
            if read_len > 0:
                data = data[read_len:]
            matchObj = re.search(r'(\S+\b)', data, re.M|re.I)
            if not matchObj:
               print("Nothing found!!")
               break
            read_len = matchObj.end()
            if len(matchObj.group()) <= 0:
                continue
            #print(matchObj.group())

            # 读取的单词放在字典中
            if matchObj.group() in words.keys():
                words[matchObj.group()] += 1
            else:
                words[matchObj.group()] = 1
        print("单词总数:",len(words));

        # 单词按出现次数排序
        sort_words = sorted(words.items(), key=lambda el:el[1], reverse = True)
        '''for word,count in words.items():
            print("单词:{0}\t总数:{1}".format(word,count));'''
        
        for word in sort_words:
            print("单词:{0}\t总数:{1}".format(word[0],word[1]));
except IOError:
    print("File Error!")

'''
    前五的单词：
		
    单词:is	总数:10
    单词:better	总数:8
    单词:than	总数:8
    单词:to	总数:5
    单词:the	总数:5
'''
