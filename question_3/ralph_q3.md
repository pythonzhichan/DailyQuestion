#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


class AnalyzeWords(object):

    def __init__(self, filename, num):
        self.filename = filename
        self.num = num

    def get_word_dict(self):
        with open(self.filename, "r") as f:
            article = f.read()
            words_list = re.split(r'\s*[\s\W]\s*', article)
            result_list = []
            words_count = {}
            for word in words_list:
                word = word.lower()
                if word:
                    if word in result_list:
                        words_count[word] += 1
                    else:
                        words_count[word] = 1
                        result_list.append(word)
        return words_count

    def output_words(self, words_dict):
        sorted_list = sorted(words_dict.items(), key=lambda w: w[1], reverse=True)
        print("文章中出现频率最多的%s个单词是： " % self.num)
        print(sorted_list)
        for i in range(0, self.num):
            try:
                print("第%s" %(i+1), sorted_list[i][0], "%s 次" % sorted_list[i][1])
                i += 1
            except Exception as e:
                print(e)


analyze_words = AnalyzeWords("import_this.txt", 5)
word_dict = analyze_words.get_word_dict()
analyze_words.output_words(word_dict)