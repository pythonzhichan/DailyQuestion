

# _*_ coding:utf-8 _*_
'''通过我的努力，下面的代码仅仅能完成对示例中url的解析......期待观摩学习别人的作品~
'''

import re
from collections import namedtuple


url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"

def parse(url):
    url_parse = namedtuple('url_parse', 'scheme netloc path query_params fragment ')
    p = re.split('\://|\/|\?|\#', url)
    p[2]='/'+p[2]
    p[3]=re.split('\&',p[3])
    for i in  range(len(p[3])):
        p[3][i] = re.split('\=', p[3][i],maxsplit=1)
    p[3] = dict(p[3])
    my_url = url_parse(scheme=p[0],netloc=p[1],path=p[2],query_params=p[3],fragment=p[4])
    return my_url

print(parse(url))


