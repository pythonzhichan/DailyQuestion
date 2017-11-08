# encoding: utf-8

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return Fib(n - 1) + Fib(n - 2)

def sequence(n):
    seq = []
    for num in range(n + 1):
        seq.append(Fib(num))
    print seq


if __name__== "__main__":
    sequence(20)