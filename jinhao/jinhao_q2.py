'''
第2题：设计一个猜数字的游戏
系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
'''


import random

low = 1
high = 100
times = 5

#随机生成一个数字
goal = random.randrange(low, high)

print('数字已选好，游戏开始。你只有{0}次机会！'.format(times))

while times > 0:
	number = int(input('请输入你猜的数字：'))
	times = times - 1
	if number > goal:
		print('太大了，请重试。你还有{0}次机会！'.format(times))
	elif number < goal:
		print('太小了，请重试。你还有{0}次机会！'.format(times))
	elif number == goal:
		print('猜对了！我想的数字就是{0}！'.format(goal))
		break
