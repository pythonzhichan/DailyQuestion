###靠着搜索，实现了一部分功能:
####统计一个文件夹里的文件数以及某个文件里的代码行等情况

    import os

    files = 0
    code_lines = 0
    blanks = 0
    comments = 0
    my_path = os.getcwd()
    my_file = open('2.py', 'r')

    for root, dirs, file_ in os.walk(my_path):
        for each in file_:
        files += 1
    print('files=', files)
    for line in my_file:
        code_lines += 1
        line = line.strip()
        if len(line) == 0:
            blanks += 1
        elif line.startswith("#"):
            comments += 1
    print('code_lines=', code_lines, '\n', 'blanks=', blanks, '\n', 'comments=', comments)