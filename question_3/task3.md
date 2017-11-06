
#林坤的作业
#统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
import string

def high_frequency_words(path,number):
    #打开文件，并将文档里的单词（去标点、小写化）分离
    with open(path,'r') as text:
        words = [raw_word.strip(string.punctuation).lower()  for raw_word in text.read().split()]
    #单词列表变成集合,去重
    word_index = set(words)
    #用一个词典表示单词及对应的词频
    counts_dict ={word : words.count(word)  for word in word_index}
    #将词汇按照频率从大到小排序，形成一个词汇列表
    counts_dict_sorted = sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True)
    #输出前五个单词
    for i in range(number):
        hf_word = counts_dict_sorted[i]
        print('{} -- {} times'.format(hf_word,counts_dict[hf_word]))


path = 'D:\_programming exercise\每日一题\Zen of Python.txt'
high_frequency_words(path,5)
