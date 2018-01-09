'''
一个完整的URL由5部分组成，格式为：
<scheme>://<netloc>/<path>?<query_params>#<fragment>
设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型
'''


import re


class URL(object):

    def __init__(self, url):
        self.url = url
        self.url_parse = self.url_parse()

    def url_parse(self):
        query_params = {}
        params_key = re.search(r'(?<=\?)[^=]+', self.url)
        if params_key:
            query_params[params_key.group()] = \
                re.findall(r'(?<==|&)[^&^#]+', self.url)

        parse = {
            'scheme': re.match(r'\w+(?=://)', self.url),
            'netloc': re.search(r'(?<=//)[\w.]+', self.url),
            'path': re.search(r'(?<=\w/)\S+(?=\?)', self.url),
            'query_params': query_params,
            'fragment': re.search(r'(?<=#)\S+', self.url)
        }

        for key, val in parse.items():
            if val and key != 'query_params':
                parse[key] = val.group()
        return parse

    def get_result(self):
        return self.url_parse


if __name__ == '__main__':
    url1 = 'http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect'
    url2 = 'http://news.baidu.com/ns?ct=1&rn=20&ie=utf-8&bs=re.search&rsv_bp=1&sr=0&cl=2&f=8&prevct=no&tn=news&word=TEST&rsv_sug3=3&rsv_sug4=121&rsv_sug1=1&rsv_sug2=0&inputT=1409'
    url3 = 'http://github.com'
    url_obj = URL(url1)
    for k, v in url_obj.get_result().items():
        print('%s: %s' % (k, v))
