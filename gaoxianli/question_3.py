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
except OSError as reason:
	print('出错啦：'+str(reason))

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