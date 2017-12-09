import re


class URL(object):
    '''
    将给定的URL转化为指定的五个部分
    '''

    def __init__(self, url):
        self.url = url
        self.scheme = None
        self.netloc = None
        self.path = None
        self.query_params = dict()
        self.fragment = None

    def parm(self):
        i = self.url.find(':')
        if i > 0:
            self.scheme = self.url[:i]
        url = self.url[i + 3:]
        # 这里借鉴了urllib的写法
        delim = len(url)
        for i in '/?#':
            wdelim = url.find(i)
            if wdelim >= 0:
                delim = min(delim, wdelim)
        self.netloc = url[:delim]
        url = url[delim + 1:]

        # 重复上边的步骤
        # 选出虚拟目录
        # 如果有?或者#
        delim = len(url)
        for i in '?#':
            wdelim = url.find(i)
            if wdelim >= 0:
                delim = min(delim, wdelim)
        self.path = url[:delim]
        url = url[delim + 1:]

        # 假如没有query_params或者fragment直接结束
        if len(url) == 0:
            pass
        else:
            if '?' in url and '#' in url:
                all_query, self.fragment = url.split('#')
                all_query_list = all_query[1:].split('&')
                for i in all_query_list:
                    tmp = i.split('=')
                    self.query_params[tmp[0]] = tmp[1]
            elif '#' in url:
                self.fragment = url[1:]
            else:
                all_query_list = url[1:].split('&')
                for i in all_query_list:
                    tmp = i.split('=')
                    self.query_params[tmp[0]] = tmp[1]

if __name__ == '__main__':
    # test = URL(r'https://www.baidu.com/s?wd=url%E5%AE%8C%E6%95%B4%E6%A0%BC%E5%BC%8F&rsv_spt=1&rsv_iqid=0x8f665dba0005246d&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=url%25E5%25AE%258C%25E6%2595%25B4%25E6%25A0%25BC%25E5%25BC%258F&rsv_t=7bc5WCvKlg4UD6URz5dRyQ2BjEfJobDX9TbRjMMJNYB2TuaYFVxlfXfV9JCvOl0WEpM2&rsv_pq=b49c034700007345&prefixsug=url%25E5%25AE%258C%25E6%2595%25B4%25E6%25A0%25BC%25E5%25BC%258F&rsp=0')
    test = URL(r'https://youtube.com')
    test.parm()
    print(test.scheme, test.netloc, test.path)
    print(test.query_params)
    print(test.fragment)
