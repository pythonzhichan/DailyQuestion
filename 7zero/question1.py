numbers = [10, 29, 30, 41]

for i in list(enumerate(numbers)):
    print(i, end=' ')


for index, value in enumerate(numbers):
    print(index, value)
    
    
for i in range(len(numbers)):
    print('{},{}'.format(i, numbers[i]))
