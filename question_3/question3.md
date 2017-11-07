import jieba

def word_frequency(text):
    from collections import Counter
    words = [word for word in jieba.cut(text, cut_all=True) if word!='']
    c = Counter(words)

    for word_freq in c.most_common(5):
        word, freq = word_freq
        print(word, freq)

with open('import_this.txt') as file_object:
    text = file_object.read()
    word_frequency(text)
