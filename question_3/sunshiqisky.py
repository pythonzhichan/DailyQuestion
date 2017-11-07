# -*- coding: utf-8 -*-
"""
__title__ = 'q3.py'
__author__ = 'sunshiqisky'
__mtime__ = '2017/11/1 0001'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import re
from collections import Counter

filesource = 'import_this.txt'

def getword(checkfile,checknum):
    pattern = r'''[a-zA-z]+'''
    with open(checkfile) as f:
        words = re.findall(pattern, f.read())
        return Counter(words).most_common(checknum)

if __name__ == '__main__':
    print(getword(filesource, 5))
