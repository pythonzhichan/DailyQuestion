# 刘茂林的第二次回答
``` python
import random

guess = random.randint(1, 100)
answer = int(input('猜猜这个数，共5次机会：'))
for i in range(5):
    if answer == guess:
        print("恭喜！猜对了。")
        break
    elif answer > guess:
        print("大了！猜对了。")
    else:
        print("小了！猜对了。")
    answer = int(input('重新猜下吧，还剩{0}次机会：'.format(4 - i)))

```