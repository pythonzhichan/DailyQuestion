# _*_ coding:utf-8 _*_

import os

'''
第六题，设计一个程序，用于统计一个项目中的代码数，
包括文件个数，代码行数，注释行数，空行行数
'''

#os.remove() 删除文件
#os.rename() 重命名文件
#os.walk() 生成目录树下的所有文件名
#os.chdir() 改变目录
#os.mkdir/makedirs 创建目录/多层目录
#os.rmdir/removedirs 删除目录/多层目录
#os.listdir() 列出指定目录的文件
#os.getcwd() 取得当前工作目录
#os.chmod() 改变目录权限
#os.path.basename() 去掉目录路径，返回文件名
#os.path.dirname() 去掉文件名，返回目录路径
#os.path.join() 将分离的各部分组合成一个路径名
#os.path.split() 返回( dirname(), basename())元组
#os.path.splitext() 返回 (filename, extension) 元组
#os.path.getatime\ctime\mtime 分别返回最近访问、创建、修改时间
#os.path.getsize() 返回文件大小
#os.path.exists() 是否存在
#os.path.isabs() 是否为绝对路径
#os.path.isdir() 是否为目录
#os.path.isfile() 是否为文件

path = '/Users/ssaw/PycharmProjects/untitled/DailyQuestion/'
# 列出指定目录的文件
files = os.listdir(path)
# 打印files
# print(files)

'''
['Fifth.py', 'First.py', 'Fourth.py', 'importthis.txt', 'Second.py', 'Third.py', '__init__.py']
'''


def count(file):
    # 代码行数
    count_total = 0
    # 注释行数
    count_explain = 0
    # 空行数
    count_blank = 0
    # 打开文件file，编码未utf-8
    line = open(file, 'r', encoding='utf-8')
    # readlines一次性读取所有行
    for li in line.readlines():
        # print(li)
        # count_total = count_total + 1
        count_total += 1
        # 判断是否为空行
        if not li.split():
            count_blank += 1
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
        li.strip()
        # 判断起始位置是否为#开头
        # startswith() 方法用于检查字符串是否是以指定子字符串开头
        # 星球第五题也用到了
        if li.startswith('#'):
            count_explain += 1

    print(file)
    #字符串格式化
    print('count_blank:%d' % count_blank)
    print('count_explain:%d' % count_explain)
    print('count_total:%d' % count_total)

for file in files:
    count(path + file)

'''
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/Fifth.py
count_blank:8
count_explain:0
count_total:34
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/First.py
count_blank:4
count_explain:10
count_total:20
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/Fourth.py
count_blank:4
count_explain:9
count_total:30
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/importthis.txt
count_blank:1
count_explain:0
count_total:21
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/Second.py
count_blank:8
count_explain:0
count_total:45
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/Third.py
count_blank:4
count_explain:1
count_total:38
/Users/ssaw/PycharmProjects/untitled/DailyQuestion/__init__.py
count_blank:0
count_explain:0
count_total:0

Process finished with exit code 0
'''

