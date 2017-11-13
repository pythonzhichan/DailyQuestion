"""
File: heguilong.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
"""
import logging
import sys
import re
from collections import Counter


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s \
                    - %(message)s')
class WordCount:
    def __init__(self, file_name):
        self.file_name = file_name

    def count_word(self, most_num):
        """print most counts words

        :most_num: print most counts words

        """
        with open(self.file_name, 'r') as f:
            data = f.read().lower()
            # characters and single quote not split
            words = re.split(r'[^\w\']+', data)
            logging.debug(words)
            most_cnts_words = Counter(words).most_common(most_num)
            print(most_cnts_words)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 heguilong.py file_name')
        sys.exit()
    word_count = WordCount(sys.argv[1])
    word_count.count_word(5)
