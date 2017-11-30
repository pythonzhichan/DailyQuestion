#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import collections


filename = 'test_for_question3.txt'
words = re.findall(r"[A-Za-z\-']+", open(filename).read().lower())
result = collections.Counter(words).most_common(5)
print(result)
