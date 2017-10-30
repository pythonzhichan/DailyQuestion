# -*- coding: utf-8 -*-

# question 1
# date: 2017-10-27
# author: loongo
# git: https://github.com/loongoo/DailyQuestion

numbers = [10,29,30,41]
j = 0
for i in numbers:
    print('({},{})'.format(j,i))
    j = j + 1
print('\n')

for j,i in enumerate(numbers):
    print('(%d,%d)' % (j,i))
    
print('\nOK')
# 这是叶宪克的第0份作业。
