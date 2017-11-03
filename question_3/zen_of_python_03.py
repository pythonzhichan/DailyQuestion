# -*- coding: utf-8 -*-

path = 'd:/import_this.txt'
with open(path, 'r') as text:
    words = text.read().split()
    result = {}
    for word in words:
        print('{} - {} times'.format(word, words.count(word)))
        result[word] = words.count(word)
    sort = sorted(result.items(), key=lambda kv: (-kv[1], kv[0]))
    print(sort[0:5])
