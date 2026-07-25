def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        minIndex=i
        for j in range(i+1,n):
            if nums[j]<nums[minIndex]:
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]
nums=[6,5,2,3,1,9,7,0,8,6,2,1,4]
selectionSort(nums)
print(nums)
