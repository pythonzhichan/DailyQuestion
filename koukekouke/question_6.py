'''
设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数。
尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目
'''


import io
import re
import os
import sys
from getopt import getopt, GetoptError


class Args(object):

    def __init__(self):
        self.type_arg = self._args_getopt()

    def _args_getopt(self):         # 解析命令行参数
        try:
            opt, _ = getopt(sys.argv[1:], '', ['type='])
            _, type_arg = opt[0]
        except (GetoptError, IndexError):
            print('e.g. >>> countor.py --type python')
            exit()
        return type_arg

    def get_type(self):
        return self.type_arg


class CodeCountor(object):

    def __init__(self, type):
        self.result_dict = {
            'files': 0,
            'code_lines': 0,
            'comments': 0,
            'blanks': 0
        }
        self.type = type
        self._type_config = self._type_config()
        self._file_num = self._file_num()

    def _type_config(self):
        type_key = self.type.lower().strip()
        config = {
            'python': ['.py', r'#[^\'\"]*', r'\s*(\'\'\')|(\"\"\")', r'.*(\'\'\')|(\"\"\")'],
            'java': ['.java', r'//', r'/\*', r'.*(\*/)'],
            'php': ['.php', r'//', r'/\*', r'.*(\*/)'],
            'c': ['.c', r'//', r'/\*', r'.*(\*/)'],
            'c++': ['.cpp', r'//', r'/\*', r'.*(\*/)']
        }
        try:
            type_config = config[type_key]
        except KeyError:
            print('This type is not supported')
            exit()
        return type_config

    def _file_num(self):        # 遍历当前文件夹下的文件
        all_file = os.listdir('./')
        for filename in all_file:
            if self._type_config[0] in filename:
                self._lines_count(filename)
                self.result_dict['files'] += 1

    def _lines_count(self, file):       # 统计每行的内容
        with io.open(file, 'r', encoding='utf-8') as f:
            multi_comments = 0          # 用来判断多行注释
            for line in f.readlines():
                if re.search(r'\S', line):        # 判断非空行
                    if not multi_comments:
                        if re.match(r'\s*[a-zA-Z]+', line):         # 判断代码行
                            self.result_dict['code_lines'] += 1
                        if re.search(self._type_config[1], line):       # 判断单行注释
                            self.result_dict['comments'] += 1
                            continue
                        if re.search(self._type_config[2], line):        # 判断多行注释开始
                            self.result_dict['comments'] += 1
                            if not re.search(self._type_config[3], re.sub(self._type_config[2], '', line, 1)):
                                multi_comments = 1      # 防止多行注释在本行结束

                    elif multi_comments:
                        self.result_dict['comments'] += 1
                        if re.match(self._type_config[3], line):        # 判断多行注释结束
                            multi_comments = 0

                else:                                    # 空行
                    self.result_dict['blanks'] += 1

    def get_result(self):
        return self.result_dict


if __name__ == '__main__':
    args = Args()
    code_countor = CodeCountor(args.get_type())
    for key, val in code_countor.get_result().items():
        print('%s: %d' % (key, val))
