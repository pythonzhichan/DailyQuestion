import re
class URL:
    def __init__(self,url):
        self.url=url
        self.scheme=''
        self.netloc=''
        self.path=''
        self.query_params={}
        self.fragment=''
    def url_parse(self):
        url=self.url
        scheme=url.split('://')[0]
        netloc=url.split('/')[2]
        path=url.split('com')[1].split('?')[0]
        fragment=url.split('#')[1]
        self.scheme=scheme
        self.netloc=netloc
        self.path=path
        self.fragment=fragment
    def transform(self):
        url=self.url
        query_params=query_params=url.split('?')[1].split('#')[0]
        key=query_params.split('=')[0]
        value1=re.findall(r'_biz=(.*?)&',query_params)[0]
        value2=query_params.split('&')[1]
        data=[(key,(value1,value2))]
        for (key,value) in data:
             self.query_params.setdefault(key,[]).append(value)
    def print_all(self):
        print 'scheme=',self.scheme
        print 'netloc=',self.netloc
        print 'path=',self.path
        print 'fragment=',self.fragment
        print 'query_params=',self.query_params
    def urlparse(self):
        self.url_parse()
        self.transform()
        self.print_all()
        
if __name__=="__main__":
    baseurl='http://mp.weixin.qq.com/s?_biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechart_redirect'
    url=URL(baseurl)
    url.urlparse()
    print '\n'

    
#使用web模块 urlparse
from urlparse import urlparse
from collections import namedtuple
import re

class URL:
    def __init__(self,url,scheme,netloc,path,params,query,fragment):
        self.url=url
        self.scheme=scheme
        self.netloc=netloc
        self.path=path
        self.params=params
        self.query=query
        self.fragment=fragment
        self.list1=[]
        self.list2=[]
    def url_parse(self):
        url=self.url
        self.scheme=urlparse(url).scheme
        self.netloc=urlparse(url).netloc
        self.path=urlparse(url).path
        self.params=urlparse(url).params
        self.query=urlparse(url).query
        self.fragment=urlparse(url).fragment
        self.list1.append([self.scheme,self.netloc,self.path,self.params,self.fragment])
        return self.list1
    def print_all(self):
        self.url_parse()
        print 'scheme=',self.scheme,'netloc=',self.netloc,'path=',self.path,'params=',self.params,'query=',self.query,'fragment=',self.fragment
    def transform(self):
        self.url_parse()
        key=self.query.split('=')[0]
        pattern=re.compile(r'=(.*?)&')
        value1=pattern.findall(self.query)[0]
        value2=self.query.split('&')[1]
        value=[value1,value2]
        self.query={key:value}
        return self.query
        
if __name__=="__main__":
    baseurl='http://mp.weixin.qq.com/s?_biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechart_redirect'
    url_1=URL(baseurl,'','','','','','')
    #使用collections.namedtuple
    URL=namedtuple('URL','scheme netloc path params query  fragment')
    list1=url_1.url_parse()
    list2=url_1.url_parse()[0]
    list3=url_1.transform()
    url=URL(scheme=list2[0],netloc=list2[1],path=list2[2],params=list2[3],fragment=list2[4],query=list3)
    print 'scheme=',url.scheme
    print 'netloc=',url.netloc
    print 'path=',url.path
    print 'params=',url.params
    print 'query=',url.query
    print 'ragment=',url.fragment
    print 'query=',url.query
    print '\n'



#直接使用现成的模板urlparse.urlparse
from urlparse import urlparse
baseurl='http://mp.weixin.qq.com/s?_biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechart_redirect'
scheme,netloc,path,params,query,fragment=urlparse(baseurl)
print 'scheme=',scheme
print 'netloc=',netloc
print 'path=',path
print 'params=',params
print 'query=',query
print 'fragment=',fragment
