#coding:UTF-8
import collections
import re
patt = re.compile("\w+")
counter = collections.Counter(patt.findall(open('import_this.txt','r').read()))
for word, times in counter.most_common(5):
    print (word, times)

