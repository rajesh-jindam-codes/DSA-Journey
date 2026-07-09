nums1 = [2,0,3,5,0,1,4,6,0,9,7,8,5,1,2,3,6,4]
nums2 = [5,6,9,0,3,7,0,8,4,0,2,6,5,2,0,1,4,8,7,9,7]
nums1.sort()
nums2.sort()
n=len(nums1)
m=len(nums2)
i, j = 0, 0
result=[]
while i<n and j<m:
    if nums1[i]<nums2[j]:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    elif nums1[i]>nums2[j]:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1
    else:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
        j+=1
while i<n:
    if result[-1]!=nums1[i]:
        result.append(nums1[i])
    i+=1
while j<m:
    if result[-1]!=nums2[j]:
        result.append(nums2[j])
    j+=1
print(result)