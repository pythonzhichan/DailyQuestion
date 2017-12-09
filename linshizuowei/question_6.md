## 第6题

设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数。尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目

```
import os
import argparse
class Summarise(object):
    def __init__(self):
        self.pro_name = None
        self.type = None
        self.file_sum = None
        self.files = 0
        self.code_lines = 0
        self.comments = 0
        self.blanks = 0

    def sum_print(self):
        print 'files:', self.files
        print 'code_lines:', self.code_lines
        print 'comments:', self.comments
        print 'blanks:', self.blanks

    def summarize(self):
        if self.type == None:
            self.type = 'py'
        if self.type == 'py':
            self.file_sum = self.py_file_sum
        elif self.type == 'java':
            self.file_sum = self.java_file_sum
        for entry in os.listdir(self.pro_name):
            entry = os.path.join(self.pro_name, entry)
            if os.path.isfile(entry):
                self.file_sum(entry)
            elif os.path.isdir(entry):
                self.dir_sum(entry)
        self.sum_print()

    def py_file_sum(self, file):
        self.files += 1
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.lstrip('\t ')
                if line == '\n':
                    self.blanks += 1
                elif line.startswith('#'):
                    self.comments += 1
                elif line.startswith('"""'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '"""':
                            break
                elif line.startswith("'''"):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == "'''":
                            break
                else:
                    self.code_lines += 1

    def java_file_sum(self, file):
        self.files += 1
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.lstrip('\t ')
                if line == '\n':
                    self.blanks += 1
                elif line.startswith('//'):
                    self.comments += 1
                elif line.startswith('/**'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '*/':
                            break
                elif line.startswith('/*'):
                    self.comments += 1
                    while True:
                        line = f.readline()
                        self.comments += 1
                        if line == '*/':
                            break
                else:
                    self.code_lines += 1

    def dir_sum(self, dir):
        for entry in os.listdir(dir):
            entry = os.path.join(dir, entry)
            if os.path.isfile(entry):
                self.file_sum(entry)
            elif os.path.isdir(entry):
                self.dir_sum(entry)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a summary program',)
    parser.add_argument('--type', default='py', choices=['py','java'], help='This argument specified the language type')
    parser.add_argument('-i', default=os.getcwd(), help='Project that being summarized')
    args = parser.parse_args()
    summa = Summarise()
    summa.pro_name = args.i
    summa.type = args.type
    summa.summarize()
```