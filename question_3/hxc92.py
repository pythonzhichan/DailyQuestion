import nltk
from nltk.corpus import stopwords
import fileinput
from nltk.tokenize import word_tokenize
import re
import collections


class WordsFrequency:
    def __init__(self, path):
        self.path = path

    def get_text(self):
        with fileinput.input(files=self.path) as f:
            words = []
            for line in f:
                words.append(line)
        return words

    def clean_text(self):
        sr = stopwords.words('english')  # 包含了英语中的一些诸如is、a之类无意义的词
        clean_texts = list()
        pattern = re.compile('\W')
        for sentence in self.get_text():
            tokens = word_tokenize(sentence)  # 用word_tokenize将句子分成了单词，但是句点等符号还在
            for token in tokens:
                if token not in sr:
                    match = re.search(pattern,token)
                    if not match:  # 去除标点符号
                        clean_texts.append(token)
        return clean_texts

    def freq_dist(self):
        freq = collections.Counter(self.clean_text())
        return freq

    def most_common(self, number):  # 统计频率最高的n个
        return self.freq_dist().most_common(number)

    def nltk_method(self):
        clean_tokens = self.clean_text()
        freq = nltk.FreqDist(clean_tokens)  # nltk库提供的词频统计
        freq.plot(30, cumulative=False)  # ‘10’用于说明要统计的是词频数前10的


words = WordsFrequency('import_this.txt')
