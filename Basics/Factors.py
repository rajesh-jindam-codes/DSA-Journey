from math import sqrt
num=50
result=[]
for i in range(1,int(sqrt(num)+1)):
    if num%i==0:
        result.append(i)
        if num//2!=i:
            result.append(num//i)
result.sort()
print(result)
