刘茂林的回答
``` python
def find_index(list):
    if not list:
        return 'Invalid input'
    length = len(list)
    for index in range(0, length):
        tmp = (index, list[index])
        if index == length - 1:
            print(tmp)
        else:
            print(tmp, end=',')


if __name__ == '__main__':
    numbers = [10, 29, 30, 41]
    find_index(numbers)

```