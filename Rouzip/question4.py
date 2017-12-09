def finonacii():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 测试
if __name__ == '__main__':
    for i in finonacii():
        print(i)
        if i > 50:
            break
