#!/usr/bin/python3

numbers = [10, 29, 30, 41]

# use enumerate to get the answer
print(list(enumerate(numbers)))

# if the square bracket was unnecessary, then we can strip it.
# send the whole list to str() regardless of the element's data type.
str1 = str(list(enumerate(numbers)))
print(str1.strip('[]'))
