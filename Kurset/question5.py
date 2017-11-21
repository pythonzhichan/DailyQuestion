class URL:
    def __init__(self, url):
        self.url = url
        self.scheme = ''
        self.netloc = ''
        self.path = ''
        self.query_params = ''
        self.fragment = ''

        self.__url_parse()

    def print_all_parts(self):
        print(self.url)
        print(self.scheme)
        print(self.netloc)
        print(self.path)
        print(self.query_params)
        print(self.fragment)

    def __url_parse(self):
        if (self.url.find('://') == -1):
            raise Exception('url not legal')

        # find scheme
        self.scheme = self.url.split('://')[0]

        # find netloc
        after_scheme_url = self.url.split('://')[1]
        self.netloc = after_scheme_url.split('/')[0]

        if (self.netloc == ''):
            raise Exception('url not legal')

        #find path
        _after_netloc_url = self.url.split(self.netloc)[1]
        self.path = _after_netloc_url.split('?')[0]

        #find query
        _query_str = ''
        if (self.url.find('?') != -1):
            _after_path_url = self.url.split('?')[1]
            _query_str = _after_path_url.split('#')[0]

        self.query_params = {}
        if (self.url.find('&') != -1):
            for _params_item in _query_str.split('&'):
                key = _params_item.split('=')[0]
                self.query_params[key] = _params_item.split('=')[1]

        # find fragment
        self.fragment = ''
        if (self.url.find('#') != -1):
            self.fragment = self.url.split('#')[1]


test_url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
new_url = URL(test_url)
new_url.print_all_parts()
