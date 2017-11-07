# 张强的 question_3 答题
# 先用函数实现吧，类的使用还不熟悉......
# re也不够熟练

import re

def words_count(file_name, count_max = 5, punctuation = '!,.*;:?"\-'):
    try:
        file_text = open(file_name)
    except FileNotFoundError:
        return print("文件不存在，请核实文件名及路径后重新开始。")

    # 转换小写，删除标点符号，分割成单词列表
    text = re.sub(r'[{}]+'.format(punctuation),'',file_text.read().lower())
    all_words = text.split()
    file_text.close()
    
    # 遍历单词列表，使计数字典累加
    words_dic = {}
    for the_word in all_words:
        words_dic.setdefault(the_word, 0)
        words_dic[the_word] += 1

    if len(words_dic) == 0:
        print("这篇文章不含英文单词，不能统计。")
    elif len(words_dic) < count_max:
        print("这篇文章只使用了", len(words_dic), "个单词，未达您的预期。")
        count_max = len(words_dic)
    
    # 字典排序
    value_sort = sorted(words_dic.items(), key = lambda item:item[1], reverse = True)
    print("在", file_name,"中出现频率最多的", count_max, "个单词是：")
    i = 0
    while i < count_max:
        print(i + 1, "-", value_sort[i][0], value_sort[i][1], "次")
        i += 1
    print("统计结束。")

words_count("import_this.txt")

