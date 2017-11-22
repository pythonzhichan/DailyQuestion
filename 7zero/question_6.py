import re

def count_linenum(filename):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(filename) as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        # 遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            # 检查是否为注释
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match(".*'''$", line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            # 检查是否为空行
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print("在%s中：" % filename)
    print("代码行数：", total_line)
    print("注释行数：", comment_line)
    print("空行数： ", blank_line)


if __name__ == '__main__':
    filename = input("please enter filename:")
    count_linenum(filename)
