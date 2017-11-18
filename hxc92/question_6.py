import os


class Project:
    def __init__(self, direct, suffix, one_comment_symbol, inline_comment_symbol, long_comment_symbol):
        self.direct = direct
        self.suffix = suffix
        self.one_comment_symbol = one_comment_symbol
        self.inline_comment_symbol = inline_comment_symbol
        self.long_comment_symbol = long_comment_symbol
        self.codes, self.comments, self.blanks, self.project_files = self.project_check()

    @staticmethod
    def is_blank(line):
        if line == '' or line == '\n':
            return True
        else:
            return False

    def is_codes(self, line):
        if line == '' or line == '\n':
            return False
        if line.startswith(self.one_comment_symbol) or line.startswith(self.long_comment_symbol):
            return False
        if line == ' ' or line == '\n':
            return False
        else:
            return True

    def is_comment(self, line):
        beg, end, flag = False, False, False
        if line.startswith(self.long_comment_symbol):
            beg = True
        if line.endswith(self.long_comment_symbol):
            end = True
        if beg and end:
            flag = True
        if line == self.long_comment_symbol:
            flag = True
        if line.startswith(self.one_comment_symbol) or self.inline_comment_symbol in line:
            flag = True
        return flag

    def file_check(self, path, codecount=0, blankcount=0, commentcount=0):
        with open(path, encoding='utf-8') as f:
            long_comment_flag = False
            for line in f:
                line = line.strip()
                blank_flag = self.is_blank(line)
                code_flag = self.is_codes(line)
                comment_flag = self.is_comment(line)
                if long_comment_flag:  # 多行注释时只需考虑注释何时结束
                    if line == self.long_comment_symbol:
                        long_comment_flag = False
                    commentcount += 1
                else:  # 非多行注释时考虑多行注释是否开始，是否是单行注释，是否是代码段，是否是空行
                    if line == self.long_comment_symbol:
                        long_comment_flag = True
                    if comment_flag:
                        commentcount += 1
                    if code_flag:
                        codecount += 1
                    if blank_flag:
                        blankcount += 1
        return codecount, commentcount, blankcount

    def project_check(self):
        codes = 0
        comments = 0
        blanks = 0
        project_files = dict()
        for dirpath, direc, files in os.walk(self.direct):
            for file in files:
                if self.suffix in file.split('.'):
                    file_path = os.path.join(dirpath, file)
                    code, comment, blank = self.file_check(file_path)
                    codes += code
                    comments += comment
                    blanks += blank
                    project_files.setdefault(file, [code, comment, blank])  # 在project中若出现同名文件则会有问题
        return codes, comments, blanks, project_files

    def file_view(self, filename):
        file = self.project_files[filename]
        print(filename + ':' + '\n' +
              'code' + str(file[0]) + ' ' + 'comment' + str(file[1]) + ' ' + 'blank' + str(file[2]))


class Pyproject(Project):
    def __init__(self, direct, suffix='py', one_comment_symbol='#', inline_comment_symbol='  # ', long_comment_symbol="'''"):
        super(Pyproject, self).__init__(direct, suffix, one_comment_symbol, inline_comment_symbol, long_comment_symbol)

    def is_codes(self, line):
        Project.is_codes(self, line)
        # super(Pyproject, self).is_codes(line)

    def is_comment(self, line):
        Project.is_comment(self, line)
        # super(Pyproject, self).is_comment(line)


project = Project('D:\python', suffix='py', one_comment_symbol='#', inline_comment_symbol='  # ', long_comment_symbol="'''")
print(project.codes, project.comments, project.blanks)
project.file_view('day_6.py')
