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
    def __init__(self, schema, netloc, path, query_params, fragment):
        self.schema = schema
        self.netloc = netloc
        self.path = path
        self.params = query_params
        self.fragment = fragment

    def __str__(self):
        return "scheme='{}', netloc='{}', path='{}', query_params={}, fragment='{}'".format(
            self.schema, self.netloc, self.path, self.params, self.fragment)


def _params_parse(params):
    if not params:
        return None
    pairs = [s for s in params.split('&')]
    param_dict = dict()
    for pair in pairs:
        k, v = pair.split('=', 1)
        param_dict[k] = v
    return param_dict


# def parse_url(url):
#     rex = r'^(http[s]?)://([^/\s]+)([/\w\-.]+[^#?\s]*)?(\?([^#]*))?(#(.*))?$'
#     schema = netloc = params = fragment = path = ''

#     pattern = re.compile(rex)
#     match = pattern.match(url)
#     if match:
#         schema = match.group(1)
#         netloc = match.group(2)
#         path = match.group(3)
#         params = match.group(5)
#         fragment = match.group(7)
#     return URL(schema=schema, netloc=netloc, path=path,
#             query_params=_params_parse(params), fragment=fragment)


def parse_url(url):
    m = re.match(r'(\w+)://([^/\s]+)([\w\-/.]+)?(\?([^#]*))?(#(.*))?', url)
    query_params = {}
    param_match = m.group(5)
    if param_match:
        for query in param_match.split('&'):
            q = query.split('=', maxsplit=1)
            query_params[q[0]] = q[1]
    else:
        query_params = None
    return URL(
        schema=m.group(1), netloc=m.group(2), path=m.group(3),
        query_params=query_params, fragment=m.group(7))


if __name__ == "__main__":
    url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
    obj = parse_url(url)
    print(obj)
