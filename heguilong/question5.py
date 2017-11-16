#!/usr/bin/env python3
"""

```
<scheme>://<netloc>/<path>?<query_params>#<fragment>
```

例如
```python
url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
```
解析后得到：
```
scheme='http'
netloc='mp.weixin.qq.com'
path='/s'
query_params='__biz=MzA4MjEyNTA5Mw==&mid=2652566513'
fragment='wechat_redirect'
```

问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型

```
query_params={'__biz': 'MzA4MjEyNTA5Mw==', 'mid=2652566513'}
```

"""
import re


class URL:
    def __init__(self, scheme, netloc, path, query_params, fragment):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.query_params = query_params
        self.fragment = fragment

    def __str__(self):
        return "scheme='{}', netloc='{}', path='{}', query_params={}, fragment='{}'" \
            .format(self.scheme, self.netloc, self.path, self.query_params, self.fragment)


def parse_url(url):
    m = re.match(r'(\w+)://([\w.]+)([\w/]+)\?([\w=&]+)#(\w+)', url)
    query_params = {}
    for query in m.group(4).split('&'):
        q = query.split('=', maxsplit=1)
        query_params[q[0]] = q[1]
    return URL(scheme=m.group(1), netloc=m.group(2), path=m.group(3),
               query_params=query_params, fragment=m.group(5))


if __name__ == "__main__":
    url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
    obj = parse_url(url)
    print(obj)
