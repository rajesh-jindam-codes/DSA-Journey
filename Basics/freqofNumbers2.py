nums1=[2,1,3,6,5,4,7,9,9,6,5,4,1,32,3,8,5]
nums2=[0,1,2,3]
freq={}
for num in nums1:
    if num in nums2:
        freq[num]=freq.get(num,0)+1
print(freq)
