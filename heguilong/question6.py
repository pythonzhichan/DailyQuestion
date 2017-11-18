#!/usr/bin/env python3
"""
File: question6.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle

今天来第六题，设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数

尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目

例如：python counter.py --type python  用于统计python代码，type是java就用于统计java代码

输出：

files:10
code_lines:200
comments:100
blanks:20
"""
import os
import sys


prog_lang_dict = {
    "python": [["py"], '#', '"""', '"""\n'],
    "java": [["java"], "//", "/*", "*/\n"],
    "C": [["c", "h"], "//", "/*", "*/\n"],
    "C++": [["cpp", "h"], "//", "/*", "*/\n"]
}


class Project():
    """
    count code lines in the project
    """
    def __init__(self, cwd, prog_lang):
        """TODO: Docstring for __init__.

        :cwd: TODO
        :returns: TODO

        """
        self.files = 0
        self.code_lines = 0
        self.comments = 0
        self.blanks = 0
        self.cwd = cwd
        self.file_types = prog_lang_dict[prog_lang][0]
        self.single_comment_sign = prog_lang_dict[prog_lang][1]
        self.multi_start_comment_sign = prog_lang_dict[prog_lang][2]
        self.multi_end_comment_sign = prog_lang_dict[prog_lang][3]

    def count(self):
        """count files, blanks, code_lines, comments in the project
        """
        is_end = True
        self.files = self.code_lines = self.comments = self.blanks = 0
        for foldername, subfolders, filenames in os.walk(self.cwd):
            for filename in filenames:
                for filetype in self.file_types:
                    if filename.endswith(filetype):
                        self.files += 1
                        with open(filename) as f:
                            lines = f.readlines()
                            for line in lines:
                                # delete left space
                                line = line.lstrip(' ')
                                # converted to unix
                                line = line.replace(r'\r\n', r'\n')
                                if line == '\n':
                                    self.blanks += 1
                                elif line.startswith(self.multi_start_comment_sign):
                                    self.comments += 1
                                    is_end = not is_end
                                elif line.endswith(self.multi_end_comment_sign):
                                    self.comments += 1
                                    is_end = not is_end
                                elif not is_end:
                                    self.comments += 1
                                elif line.startswith(self.single_comment_sign):
                                    self.comments += 1
                                else:
                                    self.code_lines += 1

    def __str__(self):
        return "file: %d\ncode_lines: %d\ncomments: %d\nblanks: %d" % (
            self.files, self.code_lines, self.comments, self.blanks)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 question6.py --type [language]")
        sys.exit()
    elif sys.argv[1] != '--type':
        print("should start with --")
        sys.exit()
    elif sys.argv[2] not in prog_lang_dict:
        print("language can be python, C, C++, java")
        sys.exit()

    project = Project(os.getcwd(), sys.argv[2])
    project.count()
    print(project)
