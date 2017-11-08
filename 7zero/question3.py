import collections

filename = 'import_this.txt'
with open(filename) as f:
    list_str = f.read().split()
    data_dict = collections.Counter(list_str)
    new_list = (sorted(data_dict.items(), key=lambda x: x[1], reverse = True))
    for i in new_list[0:5]:
        print(i)
