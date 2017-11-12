from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_list = list(islice(fib(), 10))
print(fib_list)
