#coding=utf-8
__author__ = 'vimiix'

'''
usage: question6.py [-h] [-p PATH] [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The project filepath
  -t TYPE, --type TYPE  State the aim file's language
'''

import os
import argparse
import logging


class Counter(object):
    '''By specifying the programming language and filepath, 
       the class will count the number of files in a path, 
       the number of lines of code in the file, 
       the number of comment lines, 
       the number of blank lines
    '''

    def __init__(self, path, language):
        self.path = path
        self.lang = language
        self.total_files = 0
        self.code_lines = 0
        self.comment_lines = 0
        self.blank_lines = 0
        self.langMap = {
            'python':{
                'ext':'.py',
                'line_comment':'#',
                'block_comment':[
                    ('"""','"""'),
                    ("'''","'''")
                ]
            },
            'c':{
                'ext':'.c',
                'line_comment':'//',
                'block_comment':[
                    ('/*','*/')
                ]
            },
            'html':{
                'ext':'.html',
                'line_comment':'//',
                'block_comment':[
                    ('<!--','-->')
                ]
            },
            'perl':{
                'ext':'.pl',
                'line_comment':'#',
                'block_comment':[
                    ('==pod','==cut')
                ]
            }
        }

    def count_dir(self, path, lang_cfg):
        '''Folder counter'''

        path_list = []
        total_files = 0
        for root, _, files in os.walk(path):
            if files:
                for filename in files:
                    total_files += 1
                    _, ext = os.path.splitext(filename)
                    if ext == lang_cfg['ext']:
                        filepath = '/'.join([root, filename])
                        path_list.append(filepath)
        self.total_files = total_files
        for filepath in path_list:
            self.count_file(filepath, lang_cfg)
    
    def count_file(self, path, lang_cfg):
        '''Single file counter'''

        _, ext = os.path.splitext(path)
        if ext != lang_cfg['ext']:
            return None
        code_lines = 0
        blank_lines = 0
        comment_lines = 0
        is_comment_end = True
        try:
            with open(path, 'r') as fp:
                lines = fp.readlines()
        except Exception as e:
            logging.debug("Open file error. Error:%s" % str(e))
        code_lines = len(lines)
        for line in lines:
            line = line.strip()
            if is_comment_end:
                # Check if it is blank at first.
                if line == '\n' or line == '':
                    blank_lines += 1
                    continue
                # Then check if it is single line comment.
                if line.startswith(lang_cfg['line_comment']):
                    comment_lines += 1
                    continue
                # Third check if it is block comment.
                for flag in lang_cfg['block_comment']:
                    if line.startswith(flag[0]):
                        comment_lines += 1
                        is_comment_end = False
                    # check if block comment in one line
                    if line.endswith(flag[1]):
                        is_comment_end = True
                        continue
            else:
                comment_lines += 1
                for flag in lang_cfg['block_comment']:
                    if line.endswith(flag[1]):
                        is_comment_end = True

        self.blank_lines += blank_lines
        self.comment_lines += comment_lines
        self.code_lines += (code_lines - blank_lines - comment_lines)


    def count(self):
        '''dispatcher'''

        if not os.path.exists(self.path):
            raise NameError("Wrong path.Path(%s) doesn't exsit." % self.path)
        lang_cfg = self.langMap[self.lang]
        if os.path.isdir(self.path):
            self.count_dir(self.path, lang_cfg)
        else:
            self.total_files = 1
            self.count_file(self.path, lang_cfg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="The project filepath")
    parser.add_argument("-t", "--type", help="State the aim file's language")
    args = parser.parse_args()
    counter = Counter(args.path, args.type.lower())
    counter.count()

    # output
    print "files:",counter.total_files
    print "code_lines:", counter.code_lines
    print "comments:", counter.comment_lines
    print "blanks:", counter.blank_lines

