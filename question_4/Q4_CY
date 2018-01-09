def fib():
	now_loop = 0
	the_n_1 = 1
	the_n_2 = 0
	now_number = 1
	
	if now_loop == 0:
		yield 0
		now_loop = now_loop + 1
		
	while True:
		yield now_number
		now_number = the_n_1 + the_n_2
		the_n_2 = the_n_1
		the_n_1 = now_number
		now_loop = now_loop + 1
	return

def get_fib_list(run_time):
	g = fib()
	for i in range(0,run_time):
		print(next(g))

get_fib_list(10)
