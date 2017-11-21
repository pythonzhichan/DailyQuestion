#!usr/bin/python
import re
class extrac_url():
	def __init__(self,url):
		self.url = url
	def pater(self):
		url = self.url
		[scheme1,url_rest] = url.split('//')
		scheme =  re.search(r'(.+)//',url).group(1)
		#print "scheme is %s " % scheme
		netloc = re.search(r'//(.+)/',url).group(1)
		#print "netloc is %s " % netloc
		path = re.search(r'(/.+)\?',url_rest).group(1)
		#print 'path is %s'%path
		#tt =re.compile(r'\?.+')
		query_param =  re.search(r'\?(.+)#',url).group(1)
		query_params={}
		for item in re.split(r'&', query_param):
			#print item
			index = item.find('=')
			query_params[item[:index]] = item[index+1:]
		#print "query_params is %s " %query_params
		fragment = re.search(r'#(.+)',url).group(1)
		#print "fragment is %s " %self.fragment
		return [scheme,netloc,path,query_params,fragment]
		
if __name__=="__main__":
	ttt = extrac_url("http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect").pater()
	print "scheme is %s " % ttt[0]
	print "netloc is %s " % ttt[1]
	print 'path is %s'%ttt[2]
	print 'query_params is %s'%ttt[3]
	print 'fragment is %s'%ttt[4]
