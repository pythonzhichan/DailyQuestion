# python 3
# -*- coding:utf8 -*-

'''
每日一题#  第六题，设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数
尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目
例如：python counter.py --type python  用于统计python代码，type是java就用于统计java代码
'''

import re, os, sys

class CodeCounter():
	'''用于统计一个文件或目录中的代码数，包括文件个数，代码行数，注释行数空行数。'''
	def __init__(self, path, language):		
		self.path = path
		self.language = language

		self.total_files = 0
		self.total_code_lines = 0
		self.total_blanks = 0
		self.total_comments = 0

		# 统计常见的13种程序语言,以及对应的源码文件扩展名和注释符号（分单行注释和多行注释）
		self.languages = {
			'javascript': {'ext':['.js'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'java': {'ext':['.java'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'go': {'ext':['.go'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'php': {'ext':['.php'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'c++': {'ext':['.cpp'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'c': {'ext':['.c'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'typescript': {'ext':['.ts'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'c#': {'ext':['.cs'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'swift': {'ext':['.swift'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"/*", 'end':"*/"}},	
			'python': {'ext':['.py'], 'single_line_comment':'#', 'multi_lines_comment':{'start':"'''", 'end':"'''"}},
			'ruby': {'ext':['.rb'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"=begin", 'end':"=end"}},
			'rust': {'ext':['.rs'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"=begin", 'end':"=end"}},
			'html': {'ext':['.html','.htm'], 'single_line_comment':'//', 'multi_lines_comment':{'start':"<!--", 'end':"-->"}},
		}


	def count_file(self, path, language):
		'''统计单个文件'''
		code_lines = 0
		blanks = 0
		comments = 0
		# 标记注释块（多行注释）的开始和结束
		block_comments = False

		try:
			with open(path, 'r', encoding='utf-8') as f:
				lines = f.readlines()

				for line in lines:
					line = line.strip()

					if not block_comments:
						# 当注释块标记为False时，先判断当前行是否为注释块的第一行
						# 如果是则将注释块标记设为True
						if line.startswith(self.languages[language]['multi_lines_comment']['start']):
							block_comments = True
							comments += 1
						#当前行不在注释块中时，如果以'#'开头,注释行数+1
						elif line.startswith(self.languages[language]['single_line_comment']):
							comments += 1
						elif line == '' or line == '\n':
							blanks += 1
						else:
							code_lines += 1
					else:
						# 如果当前行在注释块中，注释行数+1，然后判断是否为注释块最后一行
						# 如果是，则将注释块标记设为False
						comments += 1
						if line.endswith(self.languages[language]['multi_lines_comment']['end']):
							block_comments = False
		# 读文件过程中发生错误，则抛出异常，打印报错内容
		except Exception as e:
			print('Read file error: ', e)

		self.total_code_lines += code_lines
		self.total_comments += comments
		self.total_blanks += blanks

		# 打印单个文件的统计结果
		print('File', path, 'has:')
		print(code_lines, 'code lines')
		print(comments, 'comment lines')
		print(blanks, 'blank lines\n')

		return (code_lines, comments, blanks)

	def count_folder(self, path, language):
		'''统计指定文件夹内所有文件'''

		try:
			# 确保指定的目录能正常打开，并获取内容列表
			folder_list = os.listdir(path)
		except:
			print('Open folder failed, check and try again.')
			return

		# 遍历目录下所有内容
		for item in folder_list:
			item_path = os.path.join(path, item)

			# 如果当前项为文件，且为指定语言对应的源码文件，则进行统计
			if os.path.isfile(item_path):
				if item.endswith(tuple(self.languages[language]['ext'])):
					self.count_file(item_path, language)
					self.total_files += 1
				else:
					continue
			# 如果当前项为目录，则递归调用函数自身，继续遍历
			elif os.path.isdir(item_path):
				self.count_folder(item_path + '/', language)

	def count(self):
		#如果指定的path为单个文件，且扩展名与指定的语言相符，则调用count_file(),否则调用count_folder()
		if re.match('^.*\.\w+$', self.path):
			if self.path.endswith(tuple(self.languages[language]['ext'])):
				self.count_file(self.path, self.language)
			else:
				# 扩展名与指定的语言不相符则报错
				print('Input error, check and try again.')
		else:
			self.count_folder(self.path, self.language)


if __name__ == '__main__':
	# 获取程序执行时给定的参数
	args = sys.argv
	path = args[1]
	language = args[2]

	# 创建CodeCounter实例，并执行统计
	counter = CodeCounter(path, language)
	counter.count()

	#打印总的统计结果
	print('=====Total result=====')
	print('language:', language)
	print(counter.total_files, 'files')
	print(counter.total_code_lines, 'code lines')
	print(counter.total_comments, 'comment lines')
	print(counter.total_blanks, 'blank lines')	