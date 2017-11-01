import random
start_num,end_num = 1,100
random_number = random.randint(start_num,end_num)
guess_times = 5
guess_flag = False

print('请输入{0}-{1}的数字,你有5次机会:'.format(start_num,end_num))

while guess_times:
    guess = input()
    try:
        guess = int(guess)
    except:
        print('你输入的不是{0}-{1}的整数，请重新输入,你还有{2}次机会'.format(start_num,end_num,guess_times))
        continue
    guess_times =guess_times-1
    if guess==random_number:
        guess_flag = True
        break
    elif guess <random_number:
        print('该数字有点小了,请继续输入,你还有{0}次机会'.format(guess_times))
    else:
        print('该数字有点大了，请继续输入,你还有{0}次机会'.format(guess_times))    
    

if guess_flag:
    print('恭喜你猜中了')
else:   
    print('很遗憾你没有猜中')