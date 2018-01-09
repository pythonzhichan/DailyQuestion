#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re


class URL:
    def __init__(self, schema, netloc, path, query_params, fragment):
        self.schema = schema
        self.netloc = netloc
        self.path = path
        self.params = query_params
        self.fragment = fragment

    # print时要转成str
    def __str__(self):
        return "scheme='{}', netloc='{}', path='{}', query_params={}, fragment='{}'".format(
            self.schema, self.netloc, self.path, self.params, self.fragment)


def url_parse(url):
    match_obj = re.match(r'(\w+)://([^/\s]+)([^\s?#&]+)?(\?([^#\s]+))?(#(.+))?', url)
    schema = match_obj.group(1)
    netloc = match_obj.group(2)
    path = match_obj.group(3)
    fragment = match_obj.group(7)
    query_params = {}
    params = match_obj.group(5)
    if params:
        for query in params.split('&'):
            q = query.split('=', maxsplit=1)
            query_params[q[0]] = q[1]
    return URL(schema, netloc, path, query_params, fragment)


if __name__ == "__main__":
    url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
    parsed_url = url_parse(url)
    print(parsed_url)

