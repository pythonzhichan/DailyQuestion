#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
第6题

设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数。尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目
is
例如执行：
```
# type用于指定文件类型
python counter.py --type python
```

输出：

```
files:10
code_lines:200
comments:100
blanks:20
'''


import os
import sys


lang_dict = {
    'python': ['py', '#', "'''", "'''\n"],
    'javascript': ['js', '//', '/*', '*/\n'],
    'java': ['java', '//', '/*', '*/\n'],
    'c': ['c', '//', '/*', '*/\n'],
}


class PromCounter(object):

    def __init__(self, dirpath, lang):
        '''

        '''
        self.files = 0
        self.code_lines = 0
        self.comments = 0
        self.blanks = 0
        self.dirpath = dirpath
        self.file_type = lang_dict[lang][0]
        self.single_line_comment = lang_dict[lang][1]
        self.multi_start_comment = lang_dict[lang][2]
        self.multi_end_comment = lang_dict[lang][3]

    def count(self):
        end_comment = True
        for dirpath, dirnames, filenames in os.walk(self.dirpath):
            for filename in filenames:
                if filename.endswith(self.file_type):
                    self.files += 1
                    with open(filename, encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            line = line.replace(r'\r\n', r'\n').strip(' ')
                            if line == '' or line == '\n':
                                self.blanks += 1
                            elif line.startswith(self.single_line_comment):
                                self.comments += 1
                            elif line.startswith(self.multi_start_comment or self.multi_end_comment):
                                self.comments += 1
                                end_comment = not end_comment
                            elif not end_comment:
                                self.comments += 1
                            else:
                                self.code_lines += 1
        count_result = {
            'files': self.files,
            'code_lines': self.code_lines,
            'comments': self.comments,
            'blanks': self.blanks,
        }
        return count_result


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 question6.py --propath [path] --type [language]")
        sys.exit()
    elif sys.argv[1] != '--propath':
        print("this argument should be --propath")
        sys.exit()
    elif not os.path.isdir(sys.argv[2]):
        print("the path is not a folder")
        sys.exit()
    elif sys.argv[3] != '--type':
        print("should start with --")
        sys.exit()
    elif sys.argv[4] not in lang_dict:
        print("language can be python, javascript, java and c. You should input with lowercase.")
        sys.exit()

    counter = PromCounter(sys.argv[2], sys.argv[4])
    result = counter.count()
    print('files' + ':' + str(result['files']) + '\n' +
          'code_lines' + ':' + str(result['code_lines']) + '\n' + 'comments' + ':' + str(result['comments']) +
          '\n' + 'blanks' + ':' + str(result['blanks']))
