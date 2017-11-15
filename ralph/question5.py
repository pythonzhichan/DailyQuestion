#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
问题：设计一个算法，将URL转换成5部分，
例如
url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
解析后得到：
scheme='http'
netloc='mp.weixin.qq.com'
path='/s'
query_params='__biz=MzA4MjEyNTA5Mw==&mid=2652566513'
fragment='wechat_redirect'
注意，query_params 要转换成字典类型
'''


from collections import namedtuple
import re


class URL(object):

    def __init__(self):
        # 定义namedtuple类
        self.URL = namedtuple('URL', ['scheme', 'netloc', 'path', 'query_params', 'fragment'])

    def url_parse(self, url):
        scheme = self.get_scheme(url)
        netloc = self.get_netloc(url)
        path = self.get_path(url)
        query_params = self.get_query_params(url)
        fragment = self.get_fragment(url)
        # 实例化namedtuple对象
        url = self.URL(scheme=scheme, netloc=netloc, path=path, query_params=query_params, fragment=fragment)
        return url

    def get_scheme(self, url):
        # 如果有：//说明写出了scheme，否则默认为http
        if '://' in url:
            return url.split('://')[0]
        return 'http'

    def get_netloc(self, url):
        # 获取netloc
        pat = re.compile('[^\/](\w+\.)+\w+')
        return pat.search(url).group()

    def get_path(self, url):
        # 获取path，如果没有，返回空
        pat = re.compile(r'\w(\/)(.*)\?')
        path = pat.search(url)
        if path:
            return path.group(2)
        return

    def get_query_params(self, url):
        params_dict = {}
        # 如果有？说明有query_params参数 否则返回空{}
        if '?' in url:
            if '#' in url:
                pat = re.compile(r'\?(.*)\#')
                params = pat.search(url).group(1)
            else:
                params = url.split('?')[1]
            for param in params.split('&'):
                key = param.split('=')[0]
                value = param.split('=')[1]
                params_dict[key] = value
        return params_dict

    def get_fragment(self, url):
        # 如果有#,说明有fragment，否则返回空
        if '#' in url:
            return url.split('#')[1]
        return


if __name__ == '__main__':
    url_ps = URL()
    urls = ['http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect',
            'https://www.google.com/search?ei=epYGWpzOF8La0gKe4Kl4&q=dota2&oq=dota2',
            'www.google.com',
            ]
    try:
        for url in urls:
            print(url_ps.url_parse(url))
    except AttributeError:
        print("url不合法")