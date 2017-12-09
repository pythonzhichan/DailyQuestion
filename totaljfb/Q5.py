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
        print 'query_params: '+ self.query_params
        print 'fragment: '+ self.fragment

#the parsing function to parse the url address
def url_parse(url):
    regex = re.compile(r'''(
                            \w*)                 #scheme
                            :\/\/                #://, separator
                            (.*)                 #netloc
                            (\/.*)               #path
                            \?                   #?, separator
                            (.*)                 #query_params
                            \#                   # #, separator
                            (.*                  #fragment
                            )''',re.VERBOSE)
    result = regex.search(url)
    #TODO: parse the query_params to get a dictionary
    return URL(result.group(1),result.group(2),result.group(3),result.group(4),result.group(5))


url = raw_input("Enter an url address to parse: ")
test = url_parse(url)
test.display_result()

