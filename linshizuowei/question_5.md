问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型
```
import re

class URL(object):
    def __init__(self,url):
        self.url = url
        self.scheme = None
        self.netloc = None
        self.path = None
        self.query_params = {}
        self.fragment = None

    def url_parse(self):
        self.scheme_parse()
        self.netloc_parse()
        self.path_parse()
        self.query_parse()
        self.fragment_parse()

    def scheme_parse(self):
        if self.url:
            self.scheme = re.match(r'.*(?=:)', self.url).group()

    def netloc_parse(self):
        if self.url:
            self.netloc = re.search(r'(?<=//)[a-z]+\.[a-z]+\.[a-z]+\.[a-z]+', self.url).group()

    def path_parse(self):
        if self.url:
            self.path = re.search(r'(?<=\w/).*(?=\?)',self.url).group()

    def query_parse(self):
        if self.url:
            q_str = re.search(r'(?<=\?).*(?=#)',self.url).group()
            for item in re.split(r'&', q_str):
                index = item.find('=')
                self.query_params[item[:index]] = item[index+1:]

    def fragment_parse(self):
        if self.url:
            self.fragment = re.search(r'(?<=#).*', self.url).group()
```