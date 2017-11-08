
## 每日一题 # 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
<pre>
from collections import Counter
import re

filesource = 'c:\ces\\test.txt'

def getword(source):

    pattern = r'[a-zA-z]+'

    with open(source) as f:
        r = re.findall(pattern, f.read())
        return Counter(r).most_common(5)

if __name__ == '__main__':
    print(getword(filesource))
</pre>

