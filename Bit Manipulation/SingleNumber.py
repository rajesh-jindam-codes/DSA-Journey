def singleNumber(nums):
    res=0
    for x in nums:
        res^=x
    return res
print(singleNumber([1,1,2,3,3]))