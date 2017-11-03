numbers=[10,29,30,41]
numbers1=[]
for i,j in enumerate(numbers):
    numbers1.insert(i,(i,j))
print(",".join(str(j) for j in numbers1))    
