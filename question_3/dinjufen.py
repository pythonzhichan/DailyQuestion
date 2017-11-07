'''
# 每日一题 # 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
'''
def countWords(File):
    try:
        f = open(File, 'r')
        words = {}
        for line in f.readlines():
            begin = 0
            end = 0
            length = len(line)
            while end < length:
                while line[end].isalpha():
                    end += 1
                word = line[begin:end]
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
                begin = end
                while begin < length and not line[begin].isalpha():
                    begin += 1
                end = begin
    except:
        print("Open File failed.")
    finally:
        f.close()
        sortedWords = sorted(words.items(), key=lambda d:d[1], reverse=True)
        print("The 5 words with highest frequency:",sortedWords[:5])

File = "import_this.txt"
countWords(File)
