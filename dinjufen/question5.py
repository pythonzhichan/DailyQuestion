import re
class URL:
    def __init__(self, url_dict):
        self.url_dict = url_dict
        self.scheme = url_dict['scheme']
        self.netloc = url_dict['netloc']
        self.path = url_dict['path']
        self.query_params = url_dict['query_params']
        self.fragment = url_dict['fragment']

    @property
    def params(self):
        print(self.url_dict)

    #将url参数拼接成完整url
    @property
    def url(self):
        url = ''
        if self.scheme:
            url = url + self.scheme + '://'
        url = url + self.netloc + self.path
        if self.query_params:
            url = url + '?'
            for query in self.query_params:
                url = url + query + '=' + self.query_params[query] + '&'
            url = url[:-1]
        if self.fragment:
            url = url + '#' + self.fragment
        print(url)
        
#考虑一些缺省情况下的url解析
def url_parse(url):
    url_dict = {}

    scheme = re.findall(r"(.*?)://", url)
    #考虑缺省协议的情况下的匹配,无法匹配域名后不包含/的url,待改进
    netloc = re.findall(r"://(.*?)/" if scheme else r"(.*?)/", url)

    # 匹配path,考虑缺省后边query和params参数情况下的匹配
    if '?' in url or '#' in url:
        path = re.findall(r"\w(/.*?)[\?#]", url)
    else:
        path = re.findall(r"\w(/.*)", url)

    #匹配query_params和fragment,考虑缺省fragment情况下的匹配
    if '#' in url:
        query_params = re.search(r"\?(.*?)[#]", url)
        fragment = re.findall(r"#(.*)", url)
    else:
        query_params = re.search(r"\?(.*)", url)
        fragment = []
    query_dict = {}
    if query_params:
        split_querys = re.split('&', query_params.groups()[0])
        for query in split_querys:
            kv = re.split('=', query)
            query_dict[kv[0]] = kv[1]

    url_dict['scheme'] = scheme[0] if scheme else ''
    url_dict['netloc'] = netloc[0] if netloc else ''
    url_dict['path'] = path[0] if path else ''
    url_dict['query_params'] = query_dict
    url_dict['fragment'] = fragment[0] if fragment else ''
    return URL(url_dict)

url0 = "http://mp.weixin.qq.com/s/df/g?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
url1 = "http://mp.weixin.qq.com/s/df/g?__biz=MzA4MjEyNTA5Mw==&mid=2652566513"
url2 = "https://github.com/dinjufen/DailyQuestion"
url3 = "https://www.google.com/?gfe_rd=cr&dcr=0&ei=GU2pWaqFNtTU8AeNhqGYBA"
url4 = "https://www.cnblogs.com/dky20155212/p/6821634.html?utm_source=itdadao&utm_medium=referral"
url5 = "https://www.baidu.com/s?wd=url%E5%AE%8C%E6%95%B4%E6%A0%BC%E5%BC%8F&rsv_spt=1&rsv_iqid=0x8f665dba0005246d&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=url%25E5%25AE%258C%25E6%2595%25B4%25E6%25A0%25BC%25E5%25BC%258F&rsv_t=7bc5WCvKlg4UD6URz5dRyQ2BjEfJobDX9TbRjMMJNYB2TuaYFVxlfXfV9JCvOl0WEpM2&rsv_pq=b49c034700007345&prefixsug=url%25E5%25AE%258C%25E6%2595%25B4%25E6%25A0%25BC%25E5%25BC%258F&rsp=0"
url6 = "www.youtube.com/"
url7 = "http://www.w3school.com.cn/h.asp"


#一些例子
=======
#验证

urls = [url0,url1, url2, url3, url4, url5, url6, url7]
for url in urls:
    tmp_url = url_parse(url)
    tmp_url.params
    tmp_url.url
