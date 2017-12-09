## 第6题 ##

> 题目描述：统计文件数、文件总行数、空行行数、注释行数

```
# 统计文件数、文件总行数、空行行数、注释行数(目前只能统计 Python 文件)
import os

class FileCounter(object):
    def __init__(self, path):
        self.whitelist = ['py', 'java']
        # 文件路径
        self.path = path
        # 文件列表
        self.filelists = []
        # 代码行数
        self.codelines = 0
        # 空行行数
        self.blanklines = 0
        # 注释行数
        self.commentlines = 0

    def get_file(self):
        for parent, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                ext = filename.split('.')[-1]
                if ext in self.whitelist:
                    self.filelists.append(os.path.join(parent, filename))

    def get_file_num(self):
        return len(self.filelists)

    def count_file(self):
        self.codelines = 0
        self.blanklines = 0
        self.commentlines = 0
        # 标记是否开始注释
        is_comment = False
        # 行数(不包括空行和注释)
        lines = 0
        for filename in self.filelists:
            ext = filename.split('.')[-1]
            with open(filename, 'r', encoding='utf-8') as f:
                for index, fileline in enumerate(f, start=1):
                    fileline = fileline.strip()
                    if ext == 'py':
                        if not is_comment:
                            if fileline.startswith("'''") or fileline.startswith('"""'):
                                is_comment = True
                                start_comment_index = index
                            # 注释行
                            elif fileline.startswith("#"):
                                self.commentlines += 1
                            # 空白行
                            elif fileline == '' or fileline == '\n':
                                self.blanklines += 1
                            else:
                                lines += 1
                        else:
                            if fileline.endswith("'''") or fileline.endswith('"""'):
                                is_comment = False
                                self.commentlines += index - start_comment_index + 1
                            else:
                                pass
            self.codelines = lines + self.blanklines + self.commentlines

    def get_codelines(self):
        return self.codelines

    def get_blanklines(self):
        return self.blanklines

    def get_commentlines(self):
        return self.commentlines

if __name__ == "__main__":
    file_counter = FileCounter("D:\\aa")
    file_counter.get_file()
    print("files:%s" % file_counter.get_file_num())
    file_counter.count_file()
    print("code_lines:%s" % file_counter.get_codelines())
    print("blanks:%s" % file_counter.get_blanklines())
    print("comments:%s" % file_counter.get_commentlines())

```

**输出结果：**
> files:1
code_lines:47
blanks:3
comments:11
