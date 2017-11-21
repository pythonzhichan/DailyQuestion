#-*-coding:utf-8-*-

def fibonaci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonaci(n-1) + fibonaci(n-2)



if __name__ == '__main__':
	n = 10
	numbers = []
	for i in range(n):
		numbers.append(fibonaci(i))
	print(numbers)
