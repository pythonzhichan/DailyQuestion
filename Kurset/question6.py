import argparse
import re
import os
import io

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='file name:java c python')
parser.add_argument('-p', '--project', help='project path')
args = parser.parse_args()


class CountFile():
    def __init__(self, file_path = '', file_project = ''):
        self.all_files = []
        self.code_lines = 0
        self.blanks_lines = 0
        self.comment_lines = 0
        if file_path:
            self.__count_line_data(file_path)
            self.__count_comment_data(file_path)
            self.all_files.append(file_path)
        if file_project:
            path_dir = os.listdir(file_project)
            for i in path_dir:
                self.__count_line_data(file_project + '/' + i)
                self.__count_comment_data(file_project + '/' + i)
                self.all_files.append(i)
        print('文件目录:', self.all_files)
        print('文件注释:', self.comment_lines)
        print('文件空行:', self.blanks_lines)
        print('文件代码数:', self.code_lines)

    def judge_file_type(self, file_name):
        if '.' in file_name:
            return file_name.split('.')[-1]
        else:
            raise '文件未识别'

    def __count_line_data(self, file_name):
        file_type = self.judge_file_type(file_name)
        with io.open(file_name, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line == '\n':
                    self.blanks_lines += 1
                if file_type == 'py' and line.startswith('#'):
                    #python 单行注释
                    self.comment_lines += 1
                self.code_lines += 1

    def __count_comment_data(self, file_name):
        file_type = self.judge_file_type(file_name)
        with io.open(file_name, encoding='utf-8') as f:
            if file_type == 'java' or file_type == 'c':
                mult_comment_re = re.compile(r'/\*((?:.|\n)*?)\*/')
                data = f.read()
                for i in mult_comment_re.findall(data):
                    nums = i.count('\n')
                    if nums == 0:
                        #单行注释
                        self.comment_lines += 1
                    else:
                        #多行注释
                        self.comment_lines += nums + 1
            if file_type == 'py':
                mult_comment_re = re.compile(r"'''((?:.|\n)*?)'''")
                data = f.read()
                for i in mult_comment_re.findall(data):
                    nums = i.count('\n')
                    #多行注释
                    self.comment_lines += nums + 1

#python3 question6.py -p demo     
#python3 question6.py -f question5.py 
CountFile(args.file, args.project)