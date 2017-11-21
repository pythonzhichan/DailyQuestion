#-*- coding:utf-8 -*-
import os


class Codeaccount:
    def __init__(self,path):
        self.path=path  #根目录
        self.account={}  
    def fileaccount(self,type1): 
        fileaccount=0 #文件数目
        if os.path.exists(self.path):
            try:
                for root,dirs,files in os.walk(str(self.path)):
                    for file1 in files:
                        if str(type1) in file1:
                            fileaccount+=1
                            newpath=root+os.sep+file1
                            yield newpath
                print u'文件数目:',fileaccount
            except Exception,e:
                print'None'
        else:
            yield None  #如果输入的目录不存在，使用生成器返回空值，可以让后面函数的for循环为空
            print('目录里不存在你输入的根目录')
    def is_type(self,file1):
        return file1.split('.')[-1]  
           
        
    def codeaccount(self,files):
        flag=False #设置标志，设置的目的:如果输入正确的根目录，文件类型不存在，fileaccount函数返回None会导致函数末尾直接输出(代码行数:None)
        for file1 in files:
            flag=True #for正常执行则可在函数末尾输出代码行数等
            try:      #防止输入的代码类型异常
                if self.is_type(file1)=='py':        #文件是py类型的
                    start_comment_index=0
                    is_comment=False
                    with open(str(file1),'rb') as f:
                        for index,line in enumerate(f,start=1):   #使用index索引为后面计算''' '''这类型的注释记录行数
                            line=line.strip()
                            self.account['lineaccount']=self.account.get('lineaccount',0)+1
                            if not is_comment:
                                if line.startswith("'''") or line.startswith('"""'):
                                    is_comment=True
                                    start_comment_index=index
                                elif line.startswith('#'):
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+1
                                elif line.startswith("'") and line.endswith("'") is True:
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+1
                                elif line.startswith('"') and line.endswith('"') is True:
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+1
                                elif line=='':
                                    self.account['blankaccount']=self.account.get('blankaccount',0)+1
                            else:
                                if line.endswith("'''") or line.endswith('"""'):
                                    is_comment=False
                                    comment_lines=index-start_comment_index+1        #''' ''' 的代码行数
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+comment_lines
                elif self.is_type(file1)=='java':#文件是java类型
                    start_comment_index=0  
                    is_comment=False
                    with open(str(file1),'rb') as f:
                        for index,line in enumerate(f,start=1):
                            line=line.strip()
                            self.account['lineaccount']=self.account.get('lineaccount',0)+1
                            if not is_comment:
                                if line.startswith('/*'):
                                    is_comment=True
                                    start_comment_index=index
                                elif line.startswith('//'):
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+1
                                elif line=='':
                                    self.account['blankaccount']=self.account.get('blankaccount',0)+1
                            else:
                                if line.endswith('*/'):
                                    is_comment=False
                                    comment_lines=index-start_comment_index+1
                                    self.account['commentaccount']=self.account.get('commentaccount',0)+comment_lines
                    
            except Exception,e:
                flag=False
        if flag:
            print u'代码行数:',self.account['lineaccount']
            print u'注释行数:',self.account['commentaccount']
            print u'空行行数:',self.account['blankaccount']

path=raw_input(u'请输入根目录:')
type1=raw_input(u'java提供对 /* */和//注释 支持,请输入你想查询的文件名的后缀(例如:py or java:') #代码类型，只支持py和java
try:
    account=Codeaccount(path)
    files=account.fileaccount(type1)
    account.codeaccount(files)
except KeyError,e:
    print  'None'
