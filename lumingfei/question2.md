路明非的回答

``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

chioce = input('欢迎来到猜数字游戏(输入q退出)')

while True:
    guess_flag = False
    key_num = random.randint(1, 100)
    if chioce == 'q':
        break
    for guess_time in range(5):
        guess_num = 0
        if guess_time == 0:
            guess_num = int(input('数字范围是1-100，你猜的数字是:'))
            if guess_num == key_num:
                print('恭喜你，猜对了！')
                guess_flag = True
                chioce = input('还要继续玩下去吗？(回车继续，输入q退出)')
                break
            else:
                if guess_num < key_num:
                    print('你输入的数字小了')
                else:
                    print('你输入的数字大了')
        else:
            guess_num = int(input('你还有%d次机会哦，你猜的数字是:' % (5-guess_time)))
            if guess_num == key_num:
                print('恭喜你，猜对了！')
                guess_flag = True
                chioce = input('还要继续玩下去吗？(回车继续，输入q退出)')
                break
            else:
                if guess_num < key_num:
                    print('你输入的数字小了')
                else:
                    print('你输入的数字大了')
    if not guess_flag:
        print('很遗憾，你的机会用完了，你输了。')
        chioce = input('还要继续玩下去吗？(回车继续，输入q退出)')
```
