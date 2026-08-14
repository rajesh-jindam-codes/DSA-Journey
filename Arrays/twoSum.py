nums=[5,0,1,6,2,7,9,1,8]
class Solution:
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            seen[nums[i]]=i
obj=Solution()
print(obj.twoSum(nums,8))