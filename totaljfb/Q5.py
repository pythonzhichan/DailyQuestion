#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jason Zhang
#
# Created:     15/11/2017
# Copyright:   (c) Jason Zhang 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import re

#create a URL class
class URL:
    def __init__(self, url_scheme, url_netloc, url_path, url_query_params, url_fragment):
        self.scheme = url_scheme
        self.netloc = url_netloc
        self.path = url_path
        self.query_params = url_query_params
        self.fragment = url_fragment
    def display_result(self):
        print 'scheme: ' + self.scheme
        print 'netloc: ' + self.netloc
        print 'path: ' + self.path
        print 'query_params: '+ str(self.query_params)
        print 'fragment: '+ self.fragment

#the parsing function to parse the url address
def url_parse(url):
    regex = re.compile(r'''(
                            [^:^\/]*)?          #scheme, group 1, ':' and '/' excluded
                            (:)?                #separator ':', group 2
                            (\/\/)?             #separator '//', group 3
                            ([^\/]*)?           #netloc, '/' excluded, group 4
                            (\/)?               #separator '/'. group 5
                            ([^\?]*)?           #path, '?' excluded, group 6
                            (\?)?               #separator '\', group 7
                            ([^\#]*)?           #query_params, group 8
                            (\#)?               #separator '#', group 9
                            ([^\#]*             #fragment, '#' excluded, group 10
                            )?''',re.VERBOSE)
    result = regex.match(url)
    #deal with the optional sections if any of them are not available
    if result.group(10) == '' or result.group(10) is None:
        fragment = 'NA'
    else:
        fragment = result.group(10)
    if result.group(8) == '' or result.group(8) is None:
        query_params = 'NA'
    else:
        query_params = parse_url_query(result.group(8))
    if result.group(6) == '' or result.group(6) is None:
        path = 'NA'
    else:
        path = '/' + result.group(6)
    if result.group(4) == '' or result.group(4) is None:
        netloc = 'NA'
    else:
        netloc = result.group(4)
    if result.group(1) == '' or result.group(1) is None:
        scheme = 'NA'
    else:
        scheme = result.group(1)
    print result.groups()
    return URL(scheme,netloc,path,query_params,fragment)
#define the function to parse the url query strings
#easier to use string split method than regular expression?
def parse_url_query(query_string):
    query_params = {}
    dic_pair_list = query_string.split('&')
    for each_item in dic_pair_list:
        query_params[each_item.split('=',1)[0]] = each_item.split('=',1)[1]
    return query_params
url = raw_input("Enter an url address to parse: ")
test = url_parse(url)
test.display_result()

