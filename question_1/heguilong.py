#!/usr/bin/python3


# answer 1
numbers = [10, 29, 30, 41]
for index, num in enumerate(numbers):
    print("({}, {})".format(index, num), end=', ')

# answer 2
for pair in list(enumerate(numbers)):
    print(pair, end=', ')
