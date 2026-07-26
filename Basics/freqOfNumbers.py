nums=[5,6,4,2,3,10,7,8,9,0,4,5,4,7]
freq={}
for i in range(0,len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
print(freq)
