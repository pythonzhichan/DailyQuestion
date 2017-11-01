import random
import time
import sys

def compare(x,y):
    if x > y:
        print  'your unmber is bigger'
    elif x < y:
        print 'your number is smaller'
    else:
        print 'you get the crrect number'
        sys.exit()

print '''
  there is a random int between 1 and 100 behide, please guess which is the number.
  you will have 5 chances to get the correct number.
  now enjoy the game 
'''
t = random.randint(1,100)
time.sleep(2)
print 'number generated'
guess_changes = 5
count = 0
while True :
    input_number = int(raw_input('please input your number:'))
    count = count + 1
    compare(input_number,t)
    print 'you have %s time left' % ( guess_changes - count)
    if guess_changes - count == 0:
        print 'your chances are exausted'
        sys.exit()





