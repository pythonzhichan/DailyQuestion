numbers = [10, 29, 30, 41]

new_dic = {}
for keys,item in enumerate(numbers):
    new_dic[keys] = numbers[keys]

print new_dic.items()