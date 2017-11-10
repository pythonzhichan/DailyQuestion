'''
>>> url = url_parse('http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect')
>>> url.schema
'http'
>>> url.netloc
'mp.weixin.qq.com'
>>> url.path
'/s'
>>> url.query_params
{'__biz': 'MzA4MjEyNTA5Mw', 'mid': '2652566513'}
>>> url.fragment
'wechat_redirect'
'''


import re, collections


URL = collections.namedtuple('URL', 'schema netloc path query_params fragment')

def url_parse(url):
    url_regex = re.compile(r'(\w+)://([\w./]+)(/(\w+))\?(.+)#(.+)')
    ma = url_regex.search(url)
    params = {param_pair.split('=')[0]:param_pair.split('=')[1] for param_pair in ma.group(5).split('&')}
    return URL(ma.group(1), ma.group(2), ma.group(3), params, ma.group(6))
