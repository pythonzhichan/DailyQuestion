#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jason Zhang
#
# Created:     17/12/2017
# Copyright:   (c) Jason Zhang 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Q3
import os
import collections
import re
#define a function to read and store the text as a list
def read_text(file):
    #open the file and read as a string
    #need some time to study on encoding...
    f = open(file,encoding="ascii", errors="surrogateescape")
    file_string = f.read()
    #convert the string to a list
    word_list = file_string.split()
    #use regular expression to remove non-word items in the list
    regex = re.compile(r'\w+')
    for item in word_list:
        if not regex.match(item):
            word_list.remove(item)
    f.close()
    return word_list
#define a function to count all the items in the list and get the word whioch has
#the most counts
def count_each_word(input_list):
    #use build-in max() function to get the most counts item
    item = max(input_list, key = input_list.count)
    occurrences = input_list.count(item)
    return {item:occurrences}

#program starts here
#validate the input
text_file = input("Plase enter the text to summarize: ")
while not os.path.isfile(text_file):
    text_file = input("Plase enter a vaild file: ")
in_list = read_text(text_file)
most_count = count_each_word(in_list)
#show result
for k, v in most_count.items():
    print("The most occurrence of the word in file is: ", k)
    print("The occurrences of it is: ", v)
print(most_count)



