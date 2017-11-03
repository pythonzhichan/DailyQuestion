## 第3题 ##

```
import string

# 将文件中的每个单词存储到列表
word_lists = []
content = open('import_this.txt')
lines = content.readlines()
for line in lines:
    line = line.strip("\n")
    line = line.translate(str.maketrans('','',string.punctuation))
    word_list = line.split(" ")
    for word in word_list:
        word_lists.append(word)

# 将每个单词和出现的次数存储到字典
word_count = {}
for word in word_lists:
    word_count[word] = word_lists.count(word)

# 拿到字典中键、值的列表
words = list(word_count.keys())
counts = list(word_count.values())

# 打印频率最高的5个单词(每一次都拿到最大的那个，打印后删除)
count = 5
print("出现频率最多的5个单词是：")
while count > 0:
    index = counts.index(max(counts))
    print("(" + words[index] + ", " + str(max(counts)) + ")")
    del counts[index]
    del words[index]
    count -= 1
```