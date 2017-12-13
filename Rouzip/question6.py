import os
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor

from termcolor import cprint, colored

root = os.getcwd()


def statistic_code_file(file):
    with open(file) as fp:
        files = fp.read()


def statistics_file(root=root):
    parser = argparse.ArgumentParser(
        prog='have fun',
        description='personal script to statistic code and files')
    parser.add_argument('-p', '--path', nargs='?',
                        help='dir location', default=os.getcwd())
    parser.add_argument('-t', '--type', nargs='?', help='file type',
                        choices=['python', 'java'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.01')
    kargs = parser.parse_args()
    # 默认无参数情况
    if len(sys.argv[1:]) == 0:
        file_num = 0
        dir_num = 0
        for _, dirs, files in os.walk(kargs.path):
            file_num = file_num + len(files)
            dir_num += len(dirs)
        cprint('文件个数为：' + str(file_num), 'blue', attrs=['bold'])
        cprint('文件夹个数为：' + str(dir_num), 'blue', attrs=['bold'])
    # 指定了文件夹地址，没有选择解析文件
    elif kargs.path and kargs.type == None:
        if os.path.exists(kargs.path):
            file_num = 0
            dir_num = 0
            for _, dirs, files in os.walk(kargs.path):
                file_num += len(files)
                dir_num += len(dirs)
            cprint('文件个数为：' + str(file_num), 'blue', attrs=['bold'])
            cprint('文件夹个数为：' + str(dir_num), 'blue', attrs=['bold'])
        else:
            cprint('不存在该文件夹！', 'red', attrs=['bold'], file=sys.stderr)
    # 没有指定，使用当前路径
    elif kargs.type != None:
        file_num = 0
        # 注释数量
        comment_num = 0
        # 代码数量
        code_num = 0
        # 空格数量
        blank_num = 0
        # 作为标记，判断是不是在多行注释之中
        in_muti_comment = False
        for _, _, files in os.walk(kargs.path):
            # 遍历所有的python文件，统计
            if kargs.type == 'python':
                for file in files:
                    # 不是python，直接跳过
                    if file.split('.')[-1] != 'py':
                        continue
                    file_num += 1
                    with open(file) as f:
                        for line in f.readlines():
                            line = line.strip()
                            # 如果不处于多行注释阶段
                            if not in_muti_comment:
                                # 三种可能，代码，单行注释，空行
                                if len(line) == 0:
                                    blank_num += 1
                                elif line.startswith("#"):
                                    comment_num += 1
                                elif line.startswith("'''") or \
                                        line.startswith('"""'):
                                    in_muti_comment = True
                                    comment_num += 1
                                else:
                                    code_num += 1
                            else:
                                if line.endswith("'''") or \
                                        line.endswith('"""'):
                                    comment_num += 1
                                    in_muti_comment = False
                                else:
                                    comment_num += 1
            else:
                # 遍历所有的java，统计
                for file in files:
                    if file.split('.')[-1] != 'java':
                        continue
                    file_num += 1
                    with open(file) as f:
                        for line in f.readlines():
                            line = line.strip()
                            line = f.readline().strip()
                            # 如果不处于多行注释阶段
                            if not in_muti_comment:
                                # 三种可能，代码，单行注释，空行
                                if len(line) == 0:
                                    blank_num += 1
                                elif line.startswith("//"):
                                    comment_num += 1
                                elif line.startswith("/*"):
                                    in_muti_comment = True
                                    comment_num += 1
                                else:
                                    code_num += 1
                            else:
                                if line.endswith("*/"):
                                    comment_num += 1
                                    in_muti_comment = False
                                else:
                                    comment_num += 1
        cprint('文件个数为：' + str(file_num), 'blue', attrs=['bold'])
        cprint('代码数量为：' + str(code_num), 'blue', attrs=['bold'])
        cprint('空格数量为：' + str(blank_num), 'blue', attrs=['bold'])
        cprint('注释数量为：' + str(comment_num), 'blue', attrs=['bold'])

if __name__ == '__main__':
    statistics_file()

'''
思路：首先解析参数，如果没有路径而且无其他参数，则直接打印当前目录下统计的文件总数和文件夹数量
如果有路径则使用该路径，无参数情况下的文件数量和文件夹数量
如果有参数，则当前位置下，所有指定文件的个数，code and comment and blank
无参数同上上
有-v则打印详情
'''
