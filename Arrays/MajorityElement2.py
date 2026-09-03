def majorityElement(nums):
    candy1=candy2=None
    count1=count2=0
    for num in nums:
        if candy1==num:
            count1+=1
        elif candy2==num:
            count2+=1
        elif count1==0:
            candy1=num
            count=1
        elif count2==0:
            candy2=num
            count2=1
        else:
            count1-=1
            count2-=1

    result=[]
    if nums.count(candy1)>len(nums)//3:
        result.append(candy1)
    if candy2!=candy1 and nums.count(candy2)>len(nums)//3:
        result.append(candy2)
    return result
nums=[1,1,1,3,3,2,2,2]
print(majorityElement(nums))