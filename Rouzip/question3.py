import re
import string
from collections import OrderedDict, Counter

with open('import_this.txt', 'r') as fp:
    files = fp.read()
    line = files.translate(str.maketrans('', '', string.punctuation))
    line = re.sub('\n', ' ', line)
    line = re.sub(' +', ' ', line)
    lists = line.split()
    order_dict = Counter(lists).most_common(5)
    # 打印最频繁的五个单词
    print(order_dict)
