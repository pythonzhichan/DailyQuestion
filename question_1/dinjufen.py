#question-1
def foo(L):
    if not L:
        return L
    return list(zip([i for i in range(len(L))], L))
