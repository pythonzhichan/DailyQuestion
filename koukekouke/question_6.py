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

    def get_extension(self):        # 判断语言类型，返回后缀名
        type_arg = self.type_arg.lower().strip()
        if 'py' in type_arg:
            return '.py'
        elif 'java' in type_arg:
            return '.java'
        elif 'php' in type_arg:
            return '.php'
        elif 'html' in type_arg:
            return '.html'
        else:
            print('e.g. >>> countor.py --type python')
            exit()


class CodeCountor(object):

    def __init__(self, type):
        self.result_dict = {
            'files': 0,
            'code_lines': 0,
            'comments': 0,
            'blanks': 0
        }
        self.type = type
        self._file_num = self._file_num()

    def _file_num(self):        # 遍历当前文件夹下的文件
        all_file = os.listdir('./')
        for filename in all_file:
            if str(self.type) in filename:
                self._lines_count(filename)
                self.result_dict['files'] += 1

    def _lines_count(self, file):       # 统计每行的内容
        with io.open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if re.match(r'\s*[a-zA-Z]+', line):
                    self.result_dict['code_lines'] += 1
                if re.search(r'#', line):
                    self.result_dict['comments'] += 1
                if not re.search(r'\S', line):
                    self.result_dict['blanks'] += 1

    def get_result(self):
        return self.result_dict


if __name__ == '__main__':
    args = Args()
    code_countor = CodeCountor(args.get_extension())
    for key, val in code_countor.get_result().items():
        print('%s: %d' % (key, val))
