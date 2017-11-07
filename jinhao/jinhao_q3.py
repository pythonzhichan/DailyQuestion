# 每日一题 # 第3题：
# 统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。

python 3 
-*- coding:utf-8 -*-

import re
import collections

class wordsCounter(object):

	def __init__(self, file, top):
		
		self.file = file
		self.top = top

	def count(self):

		with open(self.file, 'r') as f:
			text = f.read()

		words = re.findall(r'[\w\']+', text.lower())

		result = collections.Counter(words)

		total_words = sum(result.values())

		top = result.most_common(self.top)
		#print(top)

		print('The file has {0} words totally, the top {1} Words are:'.format(total_words, self.top))
		for word in top:
			print(word[0], '-', word[1])


if __name__ == '__main__':
	file = 'import_this.txt'
	top = 5
	c = wordsCounter(file, top)
	c.count()