from collections import Counter
from typing import List
nums=[1,2,3,2,3,1,4]
freq=Counter(nums)
k=2
bucket=[[] for _ in range(len(nums)+1)]
for num,count in freq.items():
    bucket[count].append(num)
result=[]
for i in range(len(bucket)-1,0,-1):
    for num in bucket[i]:
        result.append(num)
        if len(result)==k:
            print(result)