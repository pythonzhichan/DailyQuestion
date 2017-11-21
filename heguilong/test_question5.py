#!/usr/bin/env python3


import unittest
from question5 import parse_url


class URLParse(unittest.TestCase):
    def test_with_full_url(self):
        url = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument"
        result = parse_url(url)
        self.assertEqual(result.schema, "http")
        self.assertEqual(result.netloc, "www.example.com:80")
        self.assertEqual(result.path, "/path/to/myfile.html")
        self.assertEqual(result.params, {"key1": "value1", "key2": "value2"})
        self.assertEqual(result.fragment, "SomewhereInTheDocument")

    def test_with_fragment(self):
        url = "http://docs.python.org/2/library/string.html#format-examples"
        result = parse_url(url)
        self.assertEqual(result.schema, "http")
        self.assertEqual(result.netloc, "docs.python.org")
        self.assertEqual(result.path, "/2/library/string.html")
        self.assertEqual(result.params, None)
        self.assertEqual(result.fragment, "format-examples")

    def test_with_params(self):
        url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513"
        result = parse_url(url)
        self.assertEqual(result.schema, "http")
        self.assertEqual(result.netloc, "mp.weixin.qq.com")
        self.assertEqual(result.path, "/s")
        self.assertEqual(result.params, {"__biz": "MzA4MjEyNTA5Mw==", "mid": "2652566513"})
        self.assertEqual(result.fragment, None)

    def test_with_path(self):
        url = "https://www.zhihu.com/topic/19661050/hot"
        result = parse_url(url)
        self.assertEqual(result.schema, "https")
        self.assertEqual(result.netloc, "www.zhihu.com")
        self.assertEqual(result.path, "/topic/19661050/hot")
        self.assertEqual(result.params, None)
        self.assertEqual(result.fragment, None)

    def test_with_only_host(self):
        url = "https://www.zhihu.com"
        result = parse_url(url)
        self.assertEqual(result.schema, "https")
        self.assertEqual(result.netloc, "www.zhihu.com")
        self.assertEqual(result.path, None)
        self.assertEqual(result.params, None)
        self.assertEqual(result.fragment, None)
