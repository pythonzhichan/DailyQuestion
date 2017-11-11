file_object = open('import_this.txt', 'r')

count_dict = {}
try:
  while True:
      read_line = file_object.readline()

      if read_line:
          line = ""
          for c in read_line:
              if c.isalpha():
                  line += c
              else:
                  line += " "

          strAry = line.split()
          for word in strAry:
              word = word.lower()
              if word in count_dict:
                  count_dict[word] += 1
              else:
                  count_dict[word] = 1
          #print(strAry)
      else:
          break
finally:
    file_object.close()

print(count_dict)

listWord = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)#用value排序

topX = 5

for i in range(0, 5):
    print("word: %s, count: %s" % (listWord[i][0], listWord[i][1]))#0 是key， 1 是value