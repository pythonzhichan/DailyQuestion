# python 3
# -*-coding:utf-8-*-

# 问题5：设计一个算法，将URL转换成5部分。
# <scheme>://<netloc>/<path>?<query_params>#<fragment>

import re
from collections import namedtuple

class URL:
	def __init__(self):
		# 定义namedtuple类
		self.URLs = namedtuple('URLs', ['scheme', 'netloc', 'path', 'query_params', 'fragment'])

	def url_parse(self, url):
		#解析url
		scheme = self.get_scheme(url)
		netloc = self.get_netloc(url)
		path = self.get_path(url)
		query_params = self.get_query_param(url)
		fragment = self.get_fragment(url)

		# 用获取的数据初始化namedtuple实例对象
		url = self.URLs(scheme=scheme, netloc=netloc, path=path, query_params=query_params, fragment=fragment)
		return(url)

	def get_scheme(self, url):
		# 获取scheme部分
		if '://' in url:
			return url.split('://')[0]

	def get_netloc(self, url):
		# 获取netloc部分
		pattern = re.compile('[^\/](\w+\.)+\w+')
		return re.search(pattern, url).group()

	def get_path(self, url):
		# 获取path部分
		pattern = re.compile('\w(\/+[\w\.-_]+\w*)\?')
		path = re.search(pattern, url)
		if path:
			return path.group(1)

	def get_query_param(self, url):
		# 获取query param 部分
		if '?' in url:
			if '#' in url:
				params = url[url.find('?')+1 : url.find('#')]
			else:
				params = url[url.find('?')+1 : ]

			query_params = dict()

			for param in params.split('&'):
					key= param[0:param.find('=')]
					value = param[param.find('=') + 1 :]
					query_params[key] = value
			return query_params


	def get_fragment(self, url):
		# 获取fragment部分
		if '#' in url:
			return url.split('#')[1]


if __name__ == '__main__':
	url1 = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
	url2 = "https://search.jd.com/Search.html?keyword=python%E7%BC%96%E7%A8%8B%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%AE%9E%E8%B7%B5&enc=utf-8&suggest=6.his.0.0&wq=&pvid=d8fcb24e53634679a54f4a4cbf35038c"
	url3 = "www.baidu.com"
	u = URL()
	print(u.url_parse(url1))
	print(u.url_parse(url2))
	print(u.url_parse(url3))
	print(u.get_path(url1))
	print(u.get_query_param(url2))

	
# output:

# URLs(scheme='http', netloc='mp.weixin.qq.com', path='/s', query_params={'mid': '2652566513', '__biz': 'MzA4MjEyNTA5Mw=='}, fragment='wechat_redirect')
# URLs(scheme='https', netloc='search.jd.com', path='/Search.html', query_params={'pvid': 'd8fcb24e53634679a54f4a4cbf35038c', 'keyword': 'python%E7%BC%96%E7%A8%8B%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%AE%9E%E8%B7%B5', 'enc': 'utf-8', 'wq': '', 'suggest': '6.his.0.0'}, fragment=None)
# URLs(scheme=None, netloc='www.baidu.com', path=None, query_params=None, fragment=None)
# /s
# {'pvid': 'd8fcb24e53634679a54f4a4cbf35038c', 'keyword': 'python%E7%BC%96%E7%A8%8B%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%AE%9E%E8%B7%B5', 'enc': 'utf-8', 'wq': '', 'suggest': '6.his.0.0'}