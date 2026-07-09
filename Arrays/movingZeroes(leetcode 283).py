nums=[2,3,0,1,6,4,0,5,7,90,5,8,7,0]
temp=[]
for i in range(len(nums)):
    if nums[i]!=0:
        temp.append(nums[i])
nz=len(temp)
for i in range(nz):
    nums[i]=temp[i]
for i in range(nz,len(nums)):
    nums[i]=0
print(nums)