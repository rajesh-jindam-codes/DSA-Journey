nums=[1,2,-3,4,-5,5,6,-7,-8,2,-1,-9,-8,-7,-6,0,1,3,6,5,4,7,8,5,4,2]
pos=[]
neg=[]
for num in nums:
    if num>=0:
        pos.append(num)
    else:
        neg.append(num)
i=j=0
result=[]
while i<len(pos) and j<len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i+=1
    j+=1
while i<len(pos):
    result.append(pos[i])
    i+=1
while j<len(neg):
    result.append(neg[j])
    j+=1
print(result)
