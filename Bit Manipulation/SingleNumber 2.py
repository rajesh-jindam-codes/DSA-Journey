def singleNumber(nums):
    ones=twos=0
    for x in nums:
        ones=(ones^x)&~twos
        twos=(twos^x)&~ones
    return ones
print(singleNumber([0,0,1,1,2,2,3,3,4,5,5,6,6,7]))