def singleNumber(nums):
    xor=0
    for x in nums:
        xor^=x
    diff=xor&-xor
    a=b=0
    for x in nums:
        if x&diff:
            a^=x
        else:
            b^=x
    return [a,b]
print(singleNumber([2,1,1,2,3,4,5,6,6]))