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

import collections
import re

URL = collections.namedtuple('URL', 'schema netloc path query_params fragment')


def url_parse(url):
    url_regex = re.compile(r'''
                    (\w+)         #schema
                    ://([\w./]+)  #netloc
                    (/(\w+))      #path
                    \?(.+)        #query_params
                    \#(.+)        #fragment
                    ''', re.VERBOSE)
    ma = url_regex.search(url)

    params = {
        param_pair.split('=')[0]: param_pair.split('=')[1]
        for param_pair in ma.group(5).split('&')}

    return URL(
        schema=ma.group(1),
        netloc=ma.group(2),
        path=ma.group(3),
        query_params=params,
        fragment=ma.group(6))
