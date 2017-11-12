
# 每日一题的第1题：
# 在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，
# 例如 numbers = [10, 29, 30, 41]，
# 要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)

# Answer 1
numbers = [10, 29, 30, 41]
for i in range(len(numbers)):
	print('({0}, {1})'.format(i, numbers[i]))

# Answer 2
numbers = [10, 29, 30, 41]
for n in numbers:
	print('({0}, {1})'.format(numbers.index(n), n))
