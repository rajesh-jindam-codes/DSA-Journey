nums1 = [1,2,3,4,6,9,8,7]
nums2 = [9,8,7,6,5,4,8,3,0,12]
nums3=nums1+nums2
nums3.sort()
n=len(nums3)

if n%2==0:
    median=nums3[n//2]
else:
    median=(nums3[n//2-1]+nums3[n//2])/2
print(median)