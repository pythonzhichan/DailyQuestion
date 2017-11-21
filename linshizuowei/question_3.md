# 每日一题 # 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。

```
def count_words():
    words = {}
    with open('import_this.txt','r') as file:
        for line in file:
            for word in line.split():
                for i in range(len(word)):
                    if (ord(word[i]) > 64 and ord(word[i]) < 91 ) or ( ord(word[i]) > 96 and ord(word[i]) < 123 ):
                        word = word[i:]
                        break
                else:
                    continue
                for j in range(len(word)-1, -1, -1):
                    if (ord(word[j]) > 64 and ord(word[j]) < 91 ) or ( ord(word[j]) > 96 and ord(word[j]) < 123 ):
                        word = word[:j+1]
                        break
                words.setdefault(word, 0)
                words[word] += 1
    
    for out in sorted(words.values(), key=lambda x:x[0],reverse=True)[:5]:
        print out[1]

```