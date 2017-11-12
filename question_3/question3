from collections import Counter
import re
from collections import Counter
class Word:
    def __init__(self,a,top_number):
        self.a=a
        self.top_number=top_number
    def getWord(self):
        items=self.a
        list1=[]
        for item1 in items.split(' '):
            for item2 in item1.split('\n'):
                words=item2.strip('-!,.*')
                list1.append(words)
        return list1
    def getnorepeatword(self,words):
        seen=set()
        for word in words:
            if word not in seen:
                seen.add(word)
        return seen
    def start(self):
        words=self.getWord()
        norepeatword=self.getnorepeatword(words)
        list1=[]
        for word in norepeatword:
            print {word:words.count(word)},
        print '\n\n'
        print '出现频率最高的五个单词是:',Counter(words).most_common(self.top_number)

            
        
a='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
top_number=5
word=Word(a,top_number)
word.start()
