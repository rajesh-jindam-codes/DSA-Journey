nums=[2,5,6,4,-1,-2,-50,6,3,9,8,7,4]
n=len(nums)
maximum=float('-inf')
total=0
for i in range(n):
    total+=nums[i]
    if total>maximum:
        maximum=total
    if total<0:
        total=0
print(maximum)