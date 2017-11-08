# -*- coding: utf-8 -*-


# ----------------Ver 1.0----------------
# path = 'd:/import_this.txt'
# with open(path, 'r') as text:
#     words = text.read().split()
#     result = {}
#     for word in words:
#         print('{} - {} times'.format(word, words.count(word)))
#         result[word] = words.count(word)
#     sort = sorted(result.items(), key=lambda kv: (-kv[1], kv[0]))
#     print(sort[0:5])


# ----------------Ver 2.0 ----------------  
path = 'd:/import_this.txt'
with open(path, 'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    for i in words:
        if i == '':
            words.remove(i)
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}
    sort = sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True)
    
    for word in sort:
        print('{} - {} times'.format(word, counts_dict[word]))
    print(sort[0:5])
