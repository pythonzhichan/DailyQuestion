#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys


param_dict = {
    "Python": 'py',
    "Java": 'java',
    "JS": 'js',
    "C": ["c", "h"]
}

filetype = {
    'py': [r"^\s*#", r'^\s*"""', r'"""\r?\n'],
    'java': [r"^\s*//", r"^\s*/*", r"*/\r?\n"],
    'js': [r"^\s*//", r"^\s*/*", r"*/\r?\n"],
    'c':  [r"^\s*//", r"^\s*/*", r"*/\r?\n"],
    'h':  [r"^\s*//", r"^\s*/*", r"*/\r?\n"]
}


class Stats:
    def __init__(self, basedir=os.getcwd(), file_type="auto"):
        self.basedir = basedir
        self.file_type = file_type
        self.type_list = []
        self.file_num = 0
        self.code_line_num = 0
        self.comment_num = 0
        self.blank_num = 0
        self.flag = 0

    def calc(self):
        if self.file_type == "auto":
            self.type_list = filetype.keys()
        else:
            self.type_list = param_dict[self.file_type]

        for dirpath, dirnames, filenames in os.walk(self.basedir):
            for filename in filenames:
                ext = filename.split('.')[-1]
                if ext in self.type_list:
                    self.file_num += 1
                    with open(os.path.join(dirpath, filename)) as f:
                        for line in f.readlines():
                            line = line.strip(' \t')
                            line = line.replace(r'\r\n', r'\n')
                            if self.flag and ~line.endswith(filetype[ext][2]):
                                self.comment_num += 1
                                self.flag = 0
                            elif line.startswith(filetype[ext][1]):
                                self.comment_num += 1
                                self.flag = 1
                            elif line == '\n':
                                self.blank_num += 1
                            elif line.startswith(filetype[ext][0]):
                                self.comment_num += 1
                            else:
                                self.code_line_num += 1

    def __str__(self):
        return "Number of files:{}\n Number of code lines:{}\n Number of comment lines:{}\n " \
               "Number of blank line{}".format(self.file_num, self.code_line_num, self.comment_num, self.blank_num)


# python3 question6.py [-d directory --type project_type]
if __name__ == "__main__":
    if len(sys.argv) == 5:
        counter = Stats(basedir=sys.argv[2], file_type=sys.argv[4])
    elif len(sys.argv) == 3 and sys.argv[1] == "-d":
        counter = Stats(basedir=sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == "--type":
        counter = Stats(file_type=sys.argv[2])
    else:
        counter = Stats()
    counter.calc()
    print(counter)
