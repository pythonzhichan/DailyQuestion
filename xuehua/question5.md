# Python 3

from urllib.parse import urlparse

url = str(input('Please input your URL : \n'))
url = urlparse(url)

print('scheme : ',url.scheme)
print('netloc : ',url.netloc)
print('path : ',url.path)
print('params : ',url.params)
print('query : ',url.query)
print('fragment : ',url.fragment)
