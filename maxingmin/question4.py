'''菲波那切数列.'''


def fib_recr(n):
    '''

    >>> fib_recr(10)
    55
    '''
    if n in (0, 1):
        return n
    return fib_recr(n - 1) + fib_recr(n - 2)


def fib_iter(n):
    '''

    >>> fib_iter(10)
    55
    '''
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fib_matrix(n):
    '''Using matrix to calculate the nth fibonaci number.

    >>> fib_matrix(10)
    55
    '''
    import numpy
    return (numpy.matrix([[1, 1], [1, 0]]) ** (n - 1) * numpy.matrix([[1], [0]]))[0, 0]


def fibonacci_sequence(n):
    '''

    >>> fibonacci_sequence(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    '''
    return [fib_recr(x) for x in range(n)]
