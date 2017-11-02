## 思路
* 将所有单词转换为小写，提取所有的单词（我使用了正则）到一个列表中
* 计算每个单词出现的次数（频率）
* 创建一个字典，存放：{单词频率 : [单词列表]}（同一频率的单词放在同一列表，并且该列表中没有重复单词）
* 将字典按频率从高到低排序
* 先输出高频中的单词列表（最多五个单词，即使列表中有超过五个的同频率单词）
## 面向过程源代码
```
import re
word_dict = {}
with open("import_this.txt") as f:
	words = re.findall(r'[A-Za-z]+\'?[A-Za-z]',f.read().lower())
	word_join = []
	for word in words:
	 	# 单词的频率
	 	count = words.count(word)
	 	# 频率次数相同 且 单词不重复
	 	if count in word_dict and word not in word_dict[count]:
	 		word_join = word_dict[count]+[word]
	 		count_word = {count : word_join}
	 	else:
	 		# {频率 : 同频率单词列表}
	 		count_word = {count : [word]}
	 	word_dict.update(count_word)

# 从大到小排序
count_list = sorted(word_dict, reverse=True)
# 输出个数
out_num = 5
# 从频率最高的开始输出
for count in count_list:
                # 输出相同频率的单词（有些单词可能频率相同
                # 但由于只能输出5个，所以位置靠后单词没机会输出）
	for word in word_dict[count]:
		if out_num:
			print(word)
			out_num -=1
```
## 半面向对象
```
import re

word_dict = {}
try:
	with open("import_this.txt") as f:
		words = re.findall(r'[A-Za-z]+\'?[A-Za-z]',f.read().lower())
		word_join = []
		for word in words:
		 	# 单词的频率
		 	count = words.count(word)
		 	# 频率次数相同 且 单词不重复
		 	if count in word_dict and word not in word_dict[count]:
		 		word_join = word_dict[count]+[word]
		 		count_word = {count : word_join}
		 	else:
		 		# {频率 : 同频率单词列表}
		 		count_word = {count : [word]}
		 	word_dict.update(count_word)
except:
	print('出错啦')

def before(out_num, rsort = False):
	# 从大到小排序
	count_list = sorted(word_dict, reverse=rsort)
	# 输出个数
	out_num = 5
	# 从频率最高的开始输出
	for count in count_list:
		# 输出相同频率的单词（有些单词可能频率相同
		# 但由于只能输出5个，所以位置靠后单词没机会输出）
		for word in word_dict[count]:
			if out_num:
				print(word)
				out_num -=1

if __name__ == '__main__':
	before(5, True)
```
## 进一步面向对象
* 本想进一步把代码抽象化，但由于对面向对象编程还不太熟练，具体错在什么地方，如何修改都不知道
```
import re
def __init__(self, filename, out_num, rsort=False):
	self.filename = filename
	self.out_num = out_num
	self.rsort = rsort
	self.word_dict = {}

def organize(filename, word_dict={}):
	try:
		with open(self.filename) as f:
			words = re.findall(r'[A-Za-z]+\'?[A-Za-z]',f.read().lower())
			word_join = []
			for word in words:
			 	# 单词的频率
			 	count = words.count(word)
			 	# 频率次数相同 且 单词不重复
			 	if count in self.word_dict and word not in self.word_dict[count]:
			 		word_join = self.word_dict[count]+[word]
			 		count_word = {count : word_join}
			 	else:
			 		# {频率 : 同频率单词列表}
			 		count_word = {count : [word]}
			 	self.word_dict.update(count_word)
	except OSError as reason:
		print('出错啦：'+str(reason))

def before(out_num, rsort = False):
	# 从大到小排序
	count_list = sorted(self.word_dict, reverse=self.rsort)
	# 从频率最高的开始输出
	for count in count_list:
		# 输出相同频率的单词（有些单词可能频率相同
		# 但由于只能输出5个，所以位置靠后单词没机会输出）
		for word in self.word_dict[count]:
			if self.out_num:
				print(word)
				self.out_num -=1

if __name__ == '__main__':
	organize("import_this.txt")
	before(5, True)
```
## 遇到的问题：
* 代码中的 word_join = word_dict[count]+[word]，是向单词列表中添加新单词。但原先是用这种方法的： word_join = word_dict[count].append([word])，但不知道为什么老是返回 None，不知道是哪里的问题。
