class UrlParse:
    def __init__(self, url):
        self.url = url
        self.colon_index = url.find(':')
        self.single_smash_index = self.colon_index + 3 + url[self.colon_index+3:].find('/')  # +3是用于去除双斜杆影响
        self.question_mark_index = url.find('?')
        self.hash_index = url.find('#')

        def get_scheme():  # scheme一定是在第一个，并且以冒号结束
            return self.url[:self.colon_index]

        def get_netloc():  # 双斜杆开始，单斜杆结束
            return self.url[self.colon_index+3:self.single_smash_index]

        def get_path():
            return self.url[self.single_smash_index:self.question_mark_index]  # 包括单斜杆

        def get_query_params():  # para有时不止两个
            params = self.url[self.question_mark_index+1:self.hash_index]
            paras = params.split('&')

            def get_para(para):
                equal_index = para.find('=')
                return para[:equal_index], para[equal_index+1:]

            parameters = dict()
            for parameter in paras:
                para_name, para_value = get_para(parameter)
                parameters.setdefault(para_name, para_value)
            return parameters

        def get_fragment():
            return self.url[self.hash_index+1:]

        self.scheme = get_scheme()
        self.netloc = get_netloc()
        self.path = get_path()
        self.query_params = get_query_params()
        self.fragment = get_fragment()


url = UrlParse("http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect")
print(url.scheme)
print(url.netloc)
print(url.path)
print(url.query_params)
print(url.fragment)
