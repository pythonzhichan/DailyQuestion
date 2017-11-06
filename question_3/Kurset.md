Kurset第三天的答案:

```python

test_str = '''
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

import re

def find_front_words(test_str):
    p = re.compile('[^a-zA-Z]')
    all_words = {}
    for i in test_str.split():
        word = p.sub('', i)
        if (word in all_words):
            all_words[word] += 1
        else:
            all_words[word] = 0

    sorted_words_list = sorted(all_words.items(), key=lambda d: d[1], reverse=True)

    print(sorted_words_list[:5])
    return sorted_words_list[:5]

find_front_words(test_str)

```