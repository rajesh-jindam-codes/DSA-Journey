class Solution:
    def __init__(self, nums):
        self.prefix = []

        total = 0

        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]


nums = [-2, 0, 3, -5, 2, -1]

obj = Solution(nums)

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))