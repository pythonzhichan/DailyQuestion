import collections

def find_words(path,number):
    with open(path) as f:
        str = f.read().split(' ')
    str_conter = collections.Counter(str).most_common(number)

    for str in str_conter:
        print(str[0])



if __name__ == '__main__':
    path = 'import_this.txt'
    number = 5
    find_words(path,number)
