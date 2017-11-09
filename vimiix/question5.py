#coding=utf-8
__author__ = 'vimiix'

class URL(object):
    
    def __init__(self, url):
        self.url = url
        self.scheme = None
        self.netloc = None
        self.path = None
        self.query_params = {}
        self.fregment = None

    def parse(self):
        if self.url.find('://') != -1:
            self.scheme, tail = self.url.split('://')
        else:
            tail = self.url
        if tail.find('/') != -1:
            sep = tail.find('/')
            self.netloc = tail[:sep]
            tail = tail[sep:]
        else:
            self.netloc = tail
        if tail.find('#') != -1:
                tail, fregment = tail.split('#')
                self.fregment = fregment if fregment else None
        if tail.find('?') != -1:
            self.path, tail = tail.split('?')
            if not tail:
                self.query_params = None
            else:
                params = tail.split('&') if tail.find('&') else [tail]
                for item in params:
                    sep = item.find('=')
                    key = item[:sep]
                    val = item[sep+1:]
                    self.query_params.update({key : val})
        else:
            self.path = tail

    def pack_result(self):
        return '''
            scheme={scheme}\n
            netloc={netloc}\n
            path={path}\n
            query_params={query_params}\n
            fregment={fregment}\n
        '''.format(
            scheme = self.scheme,
            netloc=self.netloc,
            path = self.path,
            query_params = self.query_params,
            fregment = self.fregment
        )


def parse_url(url):
    url_instance = URL(url)
    url_instance.parse()
    result = url_instance.pack_result()
    return result


if __name__ == "__main__":
    src_url = raw_input("Please input url:").strip()
    print parse_url(src_url)