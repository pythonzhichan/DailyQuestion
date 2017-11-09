'''菲波那切数列.'''

def fibonacci(n):
    '''

    >>> fibonacci(10)
    55
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sequence(n):
    '''

    >>> fibonacci_sequence(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    '''
    return [fibonacci(x) for x in range(n)]
