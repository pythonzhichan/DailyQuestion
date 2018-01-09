'''
## 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
文件在DailyQuestion/huangguolong/resource/import_this.txt
'''
import re
from collections import Counter


class MyCounter():
    def __init__(self,file_path,top_num):
        '''

        :param file_path: 文件路径
        :param top_num: 显示出现次数最多几个单词
        '''

        self.file_path = file_path
        self.top_num = top_num

    def iCounter(self):
        '''

        列出出现次数最多的几个单词
        '''
        try:
            with open(self.file_path) as f:
                text = f.read()
                words = re.findall(r'[a-zA-Z\']+',text)
                c= Counter(words)
                topData = c.most_common(self.top_num)
                print('出现次数最多的前{0}个单词是:'.format(self.top_num)+str(topData))

        except FileNotFoundError as e:
            print('文件不存在')


if __name__ == '__main__':
    mycounter = MyCounter('../huangguolong/resource/import_this.txt',5)
    mycounter.iCounter()

