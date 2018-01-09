import random

def init_data(min, max):
    return random.randint(min, max)

def guess(min, max, choice):
    target = init_data(min, max)

    for time in range(1, choice+1):
        try:
            guess_num = int(input(f'请输入{min}到{max}间的整数: '))
        except ValueError:
            print(f'请输入有效数字!, 还剩{choice-time}次机会')
            continue

        if guess_num > target:
            print(f'偏大!, 还剩{choice-time}次机会')
        elif guess_num < target:
            print(f'偏小!, 还剩{choice-time}次机会')
        else:
            print('猜对了!')
            break
    else:
        print(f'正确答案为：{target}')

guess(1, 100, 5)

