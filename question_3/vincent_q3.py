#!/usr/bin/env python3
import sys
import re
import collections

def extra_file(file):
    wordlist = {}
    with open(file) as f:
        text = f.read()
        f.close()
        text = text.lower()
        new_text = re.sub("[.!'--\n]", "", text)
        new_text = new_text.split(" ")

        for word in new_text:
            if word not in wordlist:
                wordlist[word] = 0
            wordlist[word] += 1

        return wordlist

def sort_by_count(d):
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

if __name__ == "__main__":
    file = sys.argv[1]

    d = extra_file(file)

    words = sort_by_count(d)

    for key,value in words.items():
        print("{0:>20} : {1}".format(key, value))

        
                                
    
