#-*-codeing:utf-8-*-
import io
import re

class Counter:
    def __init__(self,path):
        """
        :param path: file path
        """
        self.mapping = dict()
        with io.open(path,encoding="utf-8")as f:
            data = f.read()
            print data
            words= [s.lower() for s in re.findall("\w+",data)]
            for word in words:
                print word
                self.mapping[word]=self.mapping.get(word,0)+1

    def most_common(self,n):
        assert n>0,"n should be large than 0"
        return sorted(self.mapping.items(),key=lambda item:item[1],reverse=True)[:n]

if __name__=='__main__':
    most_common_5 = Counter("import_this.txt").most_common(10)
    for item in most_common_5:
        print(item)
