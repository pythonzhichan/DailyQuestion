# _*_ coding=utf-8 _*_
# author: Lzy
# version: python 2.7
# question:
# '''
# 一个完整的URL由5部分组成，格式为：

# <scheme>://<netloc>/<path>?<query_params>#<fragment>
# 例如
#
# url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
# 解析后得到：
# scheme='http'
# netloc='mp.weixin.qq.com'
# path='/s'
# query_params='__biz=MzA4MjEyNTA5Mw==&mid=2652566513'
# fragment='wechat_redirect'
# 问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型
#
# query_params={'__biz': 'MzA4MjEyNTA5Mw==', 'mid=2652566513'}
# 可以设计一个URL的类，还有一个算法，大概的框架就是下面这样子。
#
# class URL:
# 	....
#     pass
#
# def url_parse(url):
# 	.....
# 	return URL(xxx)
# '''

# 这是我的回答:

# 正常方式实现：

import re

# url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
#
# pattern1 = re.compile(r'(?P<scheme>\w+)://(?P<netloc>.+)/(?P<path>\w+)'
#                      r'\?(?P<query_params>.+)#(?P<fragment>\w+)')
# content1 = pattern1.match(url).groupdict()
#
# for key , value in content1.iteritems():
#     print "%s = %s" % (key, value)
#
# query_params = content1['query_params']
# print query_params
#
# pattern2 = re.compile(r'(.+)&(.+)')
# content2 = pattern2.match(query_params).groups()
# ff = []
# for i in content2:
#     a = re.match(r'(\w+)=(.+)',i).groups()
#     ff.append(a)
#
# print dict(ff)


# 类及函数方法：

class Url(object):
    def __init__(self, url_dict):
        self.url_dict = url_dict
        for key, value in self.url_dict.iteritems():
            print "%s= %s" % (key, value)

def url_paise(url):
    pattern1 = re.compile(r'(?P<scheme>\w+)://(?P<netloc>.+)/(?P<path>\w+)'
                          r'\?(?P<query_params>.+)#(?P<fragment>\w+)')
    content1 = pattern1.match(url).groupdict()
    if 'path' in content1:
        content1['path'] = '/'+content1['path']
    pattern2 = re.compile(r'(.+)&(.+)')
    content2 = pattern2.match(content1['query_params']).groups()
    temp = []
    for i in content2:
        v = re.match(r'(\w+)=(.+)', i).groups()
        temp.append(v)
    # print dict(temp)
    content1['query_params'] = dict(temp)

    return Url(content1)

if __name__=='__main__':

    url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
    url_paise(url)
