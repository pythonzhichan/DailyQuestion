from collections import Counter
import re
def Counter_number(path,top_number):
    with open(path,'rb') as f:
        words=f.read()
        words=[word for word in re.findall('\w+',words)]
        word_number=Counter(words)
        top_num=word_number.most_common(top_number)
        print top_num
path='import this.txt'
top_number=5
Counter_number(path,top_number)
