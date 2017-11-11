import random

theNumber = int(random.random() * 100)
#print("theNumber: %d" % theNumber)

playTimes = 5
correctFlag = False

for i in range(1, playTimes + 1):
    ans = int(input("Input number:"))
    if ans < theNumber:
        print("Answer will be bigger!")
    elif ans > theNumber:
        print("Answer will be smaller!")
    else:
        correctFlag = True
        break

if correctFlag:
    print("Answer correct! Game end...")
else:
    print("You played excceed %d time, gave over~" % playTimes)