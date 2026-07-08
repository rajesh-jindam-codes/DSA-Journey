def mergeArray(left,right):
    result=[]
    i=j=0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left=mergeSort(nums[:mid])
    right=mergeSort(nums[mid:])
    return mergeArray(left,right)
nums=[6,9,7,5,1,0,10,14,15,9,20,18]
print(mergeSort(nums))