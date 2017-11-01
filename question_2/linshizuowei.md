

```
import random
def guess_numbers():
    print 'game start'
    target_num = random.randint(1, 100)
    for times in range(5, 0, -1):
        tag = 'you have ' + str(times) + ' chances to get the special number:'
        input_num = raw_input(tag)
        for s in input_num:
            if ord(s) < 48 or ord(s) > 57:
                print 'please input a valid number'
                break
        else:
            guess_num = int(input_num)
            if guess_num == target_num:
                print 'bingo!'
                break
            elif guess_num > target_num:
                print 'too large'
            else:
                print 'too small'
    else:
        print 'What a pity! you did not got the number'
```