#!usr/bin/python3
#-*- coding:utf-8 -*-

'''
@auter:chenfeng
@date:2017-11-19
@remark:每日一题#  第六题，设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数
尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目
例如：python counter.py --type python [--path usr/bin/python3]
输出：
files:10
code_lines:200
comments:100
blanks:20
===========================================
1. sys.argv 的使用
2. os.walk 文件遍历
3. 装饰器、工厂模式的使用（本文中实现，可优化）
4. 不同语言注释语法的差异
===========================================
'''
import sys,os 

class FileCounter:
  def __init__(self,path,language):
    self.extens = {"c":".c","c++":".cpp","c#":".cs","javascript":".js",
                      "python":".py","java":".java"
                    }
    self.files_count = 0
    self.code_lines_count = 0 
    self.coments_count = 0
    self.blanks_count = 0
    self.path = path
    self.language = language

  def code_files_count(self): 
    if self.language in self.extens:
      postfix = self.extens[self.language]
      #遍历所有目录
      for root,dirs,files in os.walk(self.path):
        for f in files:
          file_fullpath = os.path.join(root,f)
          try:
            ext = f[f.rindex('.'):]
            if self.language == 'python' and postfix == ext:
              #print ('support')
              self.files_count += 1  
              code, comm, space = self.python_code_files_count(file_fullpath)
              self.code_lines_count += code
              self.coments_count += comm
              self.blanks_count += space
            elif postfix == ext:
              self.files_count += 1
              code, comm, space = self.other_code_files_count(file_fullpath)
              self.code_lines_count += code
              self.coments_count += comm
              self.blanks_count += space
          except:
              continue
      print("files:%d code_lines:%d coments:%d blanks:%d"
            %(self.files_count, self.code_lines_count ,self.coments_count, self.blanks_count))                       
    else:
      print(self.language," : not support")  
  
  #python代码统计
  @staticmethod
  def python_code_files_count(file_fullpath):
    code_lines = 0
    comm_lines = 0
    space_lines = 0
    with open(file_fullpath, 'r', encoding='utf-8') as fp:
      while True:
        line = fp.readline()
        if not line:
          #end last line
          break
        elif line.strip().startswith('#'):
          #single line comment
          comm_lines += 1
        elif line.strip().startswith("'''") or line.strip().startswith('"""'):
          comm_lines += 1
          if line.count('"""') ==1 or line.count("'''") ==1:
            while True:
              line = fp.readline()
              #multi line comment
              comm_lines += 1
              if ("'''" in line) or ('"""' in line):
                break
        elif line.strip():
          code_lines += 1
        else:
          space_lines +=1
    return code_lines,comm_lines,space_lines
  
  #其他部分语言统计
  @staticmethod
  def other_code_files_count(file_fullpath):
    code_lines = 0
    comm_lines = 0
    space_lines = 0
    with open(file_fullpath, 'r', encoding='utf-8') as fp:
      while True:
        line = fp.readline()
        if not line:
          #end last line
          break
        elif line.strip().startswith("//"):
          #single line comment
          comm_lines += 1
        elif line.strip().startswith("/*"):
          comm_lines += 1
          if line.count("/*") ==1:
            while True:
              line = fp.readline()
              #multi line comment
              comm_lines += 1
              if ("*/" in line):
                break
        elif line.strip():
          code_lines += 1
        else:
          space_lines +=1
    return code_lines,comm_lines,space_lines

if __name__ == '__main__':
  #验证输入统计的语言参数，目录默认取执行的脚本的所在目录
  if len(sys.argv) > 2 and sys.argv[1].startswith('--'): 
    lan_type = sys.argv[1][2:].lower()
    if lan_type == 'type':
      code_file_counter = FileCounter(sys.path[0],sys.argv[2].lower())
      code_file_counter.code_files_count()
    else: 
      print(lan_type," : not support")
  else:
    code_file_counter = FileCounter(sys.path[0],'python')
    code_file_counter.code_files_count()
