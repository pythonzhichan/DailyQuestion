import re
from collections import namedtuple
from unittest import TestCase

URL = namedtuple("URL", ["schema", "netloc", "path", "params", "fragment"])


def url_parse1(url):
    assert url.startswith("http")
    # 初始化每部分为空
    schema = netloc = params = fragment = path = None
    # 从 :// 切分 url，前面部分是shema
    i = url.find('://')
    if i > 0:
        schema = url[:i]
        url = url[i + 3:]

        # 获取netloc
        for c in "/?#":  # 三个分隔符的顺利很重要
            a = url.find(c)
            if a > 0:  # 只要有三个字符中的任意字符，立即切分，前部分就是netloc，剩下的部分进行后续处理
                netloc, url = url[0:a], url[a:]
                break
        else:
            netloc, url = url, ''  # 如果三个分隔符都不在url中，那么这是一个只包含

        # 同样的方式获取path
        for c in "?#":

            a = url.find(c)
            if a > 0:
                path, url = url[0:a], url[a:]
                break
        else:
            path, url = url or None, ''

        if "#" in url:
            url, fragment = url.split("#", 1)

        if '?' in url:
            url, params = url.split('?', 1)

    return URL(schema=schema, netloc=netloc, path=path, params=_params_parse(params), fragment=fragment)


def _params_parse(params):
    if not params:
        return None
    pairs = [s for s in params.split('&')]
    param_dict = dict()
    for pair in pairs:
        k, v = pair.split('=', 1)
        param_dict[k] = v
    return param_dict


def url_parse2(url):
    rex = r'^(http[s]?):\/\/([^\/\s]+)([\/\w\-\.]+[^#?\s]*)?(\?([^#]*))?(#(.*))?$'
    schema = netloc = params = fragment = path = ''

    pattern = re.compile(rex)
    match = pattern.match(url)
    if match:
        schema = match.group(1)
        netloc = match.group(2)
        path = match.group(3)
        params = match.group(5)
        fragment = match.group(7)
    return URL(schema=schema, netloc=netloc, path=path, params=_params_parse(params), fragment=fragment)


def url_parse2(url):
    m = re.match(r'(\w+)://([\w.]+)([\w/]+)\?([\w=&]+)#(\w+)', url)
    query_params = {}
    for query in m.group(4).split('&'):
        q = query.split('=', maxsplit=1)
        query_params[q[0]] = q[1]
    return URL(scheme=m.group(1), netloc=m.group(2), path=m.group(3),
               query_params=query_params, fragment=m.group(5))

url = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument"
print(url_parse2(url))


class URLParse(TestCase):
    def test_with_full_url(self):
        url = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument"
        for fun in (url_parse1, url_parse2):
            result = fun(url)
            self.assertEqual(result.schema, "http")
            self.assertEqual(result.netloc, "www.example.com:80")
            self.assertEqual(result.path, "/path/to/myfile.html")
            self.assertEqual(result.params, {"key1": "value1", "key2": "value2"})
            self.assertEqual(result.fragment, "SomewhereInTheDocument")

    def test_with_fragment(self):
        url = "http://docs.python.org/2/library/string.html#format-examples"
        for fun in (url_parse1, url_parse2):
            result = fun(url)
            self.assertEqual(result.schema, "http")
            self.assertEqual(result.netloc, "docs.python.org")
            self.assertEqual(result.path, "/2/library/string.html")
            self.assertEqual(result.params, None)
            self.assertEqual(result.fragment, "format-examples")

    def test_with_params(self):
        url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513"
        for fun in (url_parse1, url_parse2):
            result = fun(url)
            self.assertEqual(result.schema, "http")
            self.assertEqual(result.netloc, "mp.weixin.qq.com")
            self.assertEqual(result.path, "/s")
            self.assertEqual(result.params, {"__biz": "MzA4MjEyNTA5Mw==", "mid": "2652566513"})
            self.assertEqual(result.fragment, None)

    def test_with_params(self):
        url = "https://www.zhihu.com/topic/19661050/hot"
        for fun in (url_parse1, url_parse2):
            result = fun(url)
            self.assertEqual(result.schema, "https")
            self.assertEqual(result.netloc, "www.zhihu.com")
            self.assertEqual(result.path, "/topic/19661050/hot")
            self.assertEqual(result.params, None)
            self.assertEqual(result.fragment, None)

    def test_with_only_host(self):
        url = "https://www.zhihu.com"
        for fun in (url_parse1, url_parse2):
            result = fun(url)
            self.assertEqual(result.schema, "https")
            self.assertEqual(result.netloc, "www.zhihu.com")
            self.assertEqual(result.path, None)
            self.assertEqual(result.params, None)
            self.assertEqual(result.fragment, None)
