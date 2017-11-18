'''
Python之禅第六题
设计一个程序，用于统计一个项目中的代码数，包括文件个数，
代码行数，注释行数，空行行数
尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目
例如：python counter.py --type python  用于统计python代码，type是java就用于统计java代码
输出：
files:10
code_lines:200
comments:100
blanks:20
调用方法：在终端输入:python3 本文件名 路径 要查找的语言
目前只统计了两种语言的（python和c），因为只了解这两个，其他的类似
'''
import sys
import os

fpath = sys.argv[1]
language = sys.argv[2]

class CodeCounter:
    '''
    统计一个项目中某种文件的代码数
    包括文件个数、代码行数、注释行数、空行行数
    '''
    def __init__(self, fpath, langType):
        self.fpath = fpath
        self.type = langType
        self.__langDict = {'c':'c','c++':'cpp',
                'python':'py','java':'java',
                'php':'php'}
        self.allfiles = []

    def __findFiles(self, path):
        try:
            parents = os.listdir(path)
        except:
            parents = ''
        for parent in parents:
            child = os.path.join(path, parent)
            if os.path.isfile(child):
                if child.split('.')[-1] == self.__langDict[self.type]:
                    self.allfiles.append(child)
            else:
                self.__findFiles(child)
    
    def counter(self):
        code_lines = 0
        blanks = 0
        comments = 0
        self.__findFiles(self.fpath)
        for file_ in self.allfiles:
            with open(file_) as f:
                for line in f.readlines():
                    if line == '\n':
                        blanks += 1
                    if self.type == 'python':
                        if line.startswith('#'):
                            comments += 1
                        else:
                            code_lines += 1
                    elif self.type == 'c':
                        if line.startswith('//'):
                            comments += 1
                        else:
                            code_lines += 1
        return (len(self.allfiles), blanks, code_lines, comments)

if __name__ == '__main__':
    code = CodeCounter(fpath, language)
    files, blanks, code_lines, comments = code.counter()
    print("files:", files)
    print("blanks:", blanks)
    print("code_lines:", code_lines)
    print("comments:", comments)
