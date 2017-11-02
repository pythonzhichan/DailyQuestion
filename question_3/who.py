'''
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
'''
import re
from collections import Counter

def file_statistic(filename):
    with open(filename, 'r') as f:
        text = f.read()
    
    # 使用非字母做分隔符，提取出所有的单词
    txt = re.split(r'\W+', text)
    words = Counter(txt)
    print(words.most_common(5))

if __name__ == "__main__":
    file_statistic("import_this.txt")