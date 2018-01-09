import os
import re
import sys
class Statistics_project():
        # 默认 Python 语言
        def __init__(self, Languages=["python"]):
                self.Languages = Languages
                self.all_dir_path, self.all_file_path, self.all_code_file = [], [], []
                # 不同语言的代码文件对应不同的文件类型
                self.Language_dict={
                        'python': {
                                'filetype': ['.py'],
                                # 注释 #、"""、'''
                                # 单行注释正则
                                'Single_line_comment': r"^\s*#.*",
                                # 多行注释正则（必须成对出现 """ 或 '''）
                                'Multi_line_comment':r"^\s*([\'\"]{3})[\W\w]*?\1",
                                # 空行正则（如果 ^\s* 后面没有问号?，那么它将连续的多行当作一行匹配）
                                'Regular_blanks': r"^\s*?\n"}, 
                        # 单行与多行注释的正则要通过逻辑或 "|" 进行字符串合并来匹配注释的行数，所以若没有单行注释，就让单行注释的正则表达式和多行注释一致
                        'html': {
                                'filetype': ['.html', '.htm'], 
                                'Single_line_comment': r"^\s*(<\!--)[\W\w]*?(?(1)\-\->)", 
                                'Multi_line_comment': r"^\s*(<\!--)[\W\w]*?(?(1)\-\->)", 
                                'Regular_blanks': r"^\s*?\n"}, 
                        # 因为多个文件格式要进行迭代操作，所以文件格式是以列表形式存在，不然会迭代文件格式字符串中的每个字符
                        'css': {
                                'filetype': ['.css'], 
                                'Single_line_comment': r"^\s*(\/\*)[\W\w]*?(?(1)\*\/)", 
                                'Multi_line_comment': r"(\/\*)[\W\w]*?(?(1)\*\/)", 
                                'Regular_blanks': r"^\s*?\n"}, 
                        'js': {
                                'filetype': ['.js'], 
                                'Single_line_comment': r"^\s*(\/\/).*", 
                                'Multi_line_comment': r"(\/\*)[\W\w]*?(?(1)\*\/)", 
                                'Regular_blanks': r"^\s*?\n"}
                }
 
        # 遍历所有目录和文件
        def all_dir_file(self):
                dir_lists = os.walk(self.path)
                for root, dirs, files in dir_lists:
                        # for d in dirs:
                                # 将目录的路径与目录名合并成目录的绝对路径，然后添加进目录路径列表 all_dir_path
                                # self.all_dir_path.append(os.path.join(root, d))
                        for f in files:
                                self.all_file_path.append(os.path.join(root, f))
 
        # 统计文件数 files，返回整数
        def files(self):
                return len(self.all_file_path)
 
        # 筛选某语言的代码文件
        def code_files(self):
                self.all_code_file = []
                for f in self.all_file_path:
                        for filetype in self.Lang_attr["filetype"]:
                                # 文件格式符合就文件路径添加进代码文件列表
                                if f.endswith(filetype):
                                        self.all_code_file.append(f)
 
        # 读取文件内容
        def read_file_content(self, file_path):
                self.filecontent, self.file_line_count = "", 0
                try:
                        with open(file_path, encoding="utf8") as f:
                                for line in f:
                                        self.file_line_count += 1
                                        self.filecontent += line
                except UnicodeDecodeError as e:
                        print("该文件解码时出错，请手动保存该文件的编码格式为UTF-8： %s \n" % e)
 
        # 返回代码行数 = 总行数 - 空行数 - 注释数（没有加上单行注释位于代码语句后的情况）
        def code_lines(self):
                return self.file_line_count - self.comments() - self.blanks()
        
        # 返回注释数
        def comments(self):
                m = re.search(self.Lang_attr["Multi_line_comment"], self.filecontent, re.M)
                if m:
                        # 存在多行注释就加上多行注释所占的行数减1；
                        # self.Lang_attr["Single_line_comment"]+"|"+self.Lang_attr["Multi_line_comment"] 是通过逻辑或 "|" 合并单行、多行注释的正则表达式
                        return len(re.findall(self.Lang_attr["Single_line_comment"]+"|"+self.Lang_attr["Multi_line_comment"], self.filecontent, re.M)) + len(re.findall(r"^[\s\S]*?", m.group(), re.M)) - 1
                else:
                        return len(re.findall(self.Lang_attr["Single_line_comment"]+"|"+self.Lang_attr["Multi_line_comment"], self.filecontent, re.M))
     
        # 返回空行数
        def blanks(self):
                return len(re.findall(self.Lang_attr["Regular_blanks"], self.filecontent, re.M))
        
        # 打印统计结果，默认统计当前目录
        def statis_results(self, path = "."):
                self.path = path
                self.all_dir_file()
                print("files: %d" % (self.files()))
                # 迭代多个编程语言
                for Language in self.Languages:
                        try:
                                # 语言的属性列表
                                self.Lang_attr = self.Language_dict[Language.casefold()]
                                # 筛选一种编程语言的代码文件到列表all_code_file中
                                self.code_files()
                                print("code files( %s ): %d" % (self.Lang_attr["filetype"], len(self.all_code_file)))
                                # 从代码文件列表 all_code_file 中逐个读取并打印分析结果
                                for file_path in self.all_code_file:
                                        print(file_path)
                                        self.read_file_content(file_path)
                                        # print("\t总行数: %d" % (len(re.findall(r".*\n", self.filecontent, re.M))+1))
                                        print("\t总行数: %d" % self.file_line_count)
                                        print("\tcode lines: %d" % self.code_lines())
                                        print("\tcomments: %d" % self.comments())
                                        print("\tblanks: %d\n" % self.blanks())
                        except KeyError as e:
                                print("对不起，暂不支持您的输入的 %s 语言" % e)

if __name__ == '__main__':
        # 至少指定 1 种编程语言
        if sys.argv[2:]:
                stat_pro = Statistics_project(sys.argv[2:])
                stat_pro.statis_results(sys.argv[1])
        # 只指定路径，统计默认编程语言
        elif sys.argv[1:]:
                stat_pro = Statistics_project()
                stat_pro.statis_results(sys.argv[1])
        # 路径和编程语言都没指定，统计默认路径和默认编程语言
        else:
                stat_pro = Statistics_project()
                stat_pro.statis_results()