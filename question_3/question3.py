from collections import Counter

filename = 'import_this.txt'
top_number = 5

with open(filename,'r+',encoding='utf-8') as f:
    content = f.read().replace('.','').replace(',','').split()
    top_words=Counter(content).most_common(top_number)
    for item in top_words:
        print(item[0])
