#!usr/bin/python3
#-*- coding:utf-8 -*-

'''
@auter:chenfeng
@date:2017-11-12
@remark:问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型
通过字符串的常用方法实现。实际编码中也可以直接使用内置模块的urllib.parse()快速处理。
'''
from collections import namedtuple
class URL:
    def __init__(self):
        # 定义namedtuple url类
        self.URL = namedtuple('URL','scheme netloc path query_params fragment')

    def url_parse(self, url_str): 
        scheme = netloc = path = fragement ='' 
        query_params = {}
        
        #split url 格式:<scheme>://<netloc>/<path>?<query_params>#<fragment>
        i = url_str.find(':')
        if i > 0:
            if url_str[:i] == 'http':
                scheme = url_str[:i].lower()
                url_str = url_str[i+1:]
            elif not url_str[i+1:] or any(c not in '0123456789' for c in url_str[i+1:]):
                scheme, url_str = url_str[:i].lower(), url_str[i+1:]                
            
            if url_str[:2] == '//':
                netloc, url_str = self.split_netloc(url_str, 2) 
            if '?' in url_str:
                path, url_str = url_str.split('?', 1)
            if '#' in url_str:
                url_str, fragement = url_str.split('#', 1)
            if '=' not in url_str:
                path = url_str
            else:
                query_params = self.gen_dict_query(url_str)
        else:
            return "not a standard url pattern"

        #实例化namedtuple对象
        url = self.URL(scheme=scheme, netloc=netloc, path=path, query_params=query_params, fragment=fragement)
        return url
        
    def split_netloc(self, url, start=0):
        index_len = len(url)
        # 获取主机部分   
        for c in '/?#':
            wdelim = url.find(c, start)        
            if wdelim >= 0: 
                index_len = min(index_len, wdelim) 
        return url[start:index_len], url[index_len:]
    
    def gen_dict_query(self, url):
        #获取key-value键值对
        params_dict = {}
        
        for param in url.split('&'):
            if len(param.split('=',1)) > 1:
                key = param.split('=')[0]
                value = param.split('=',1)[1]
                params_dict[key] = value
        return params_dict

if __name__ == '__main__':

    website_urls = ['https://mp.weixin.qq.com/s/-paroQtl8vtYykLbuQ7w5Q',
    'http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect',
    'www.google.com/search?ei=epYGWp',
    'https://docs.python.org/2.7/library/urlparse.html?highlight=urlparse#module-urlparse'
    ]
    utils = URL()
    for url in website_urls:
        print(utils.url_parse(url))

#output:
'''
URL(scheme='https', netloc='mp.weixin.qq.com', path='/s/-paroQtl8vtYykLbuQ7w5Q', query_params={}, fragment='')
URL(scheme='http', netloc='mp.weixin.qq.com', path='/s', query_params={'__biz': 'MzA4MjEyNTA5Mw==', 'mid': '2652566513'}, fragment='wechat_redirect')
not a standard url pattern
URL(scheme='https', netloc='docs.python.org', path='/2.7/library/urlparse.html', query_params={'highlight': 'urlparse'}, fragment='module-urlparse')
'''
