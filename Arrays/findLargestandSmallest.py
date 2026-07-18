nums=[5,6,3,2,1,0,4,9,7,8,-0,15]
smallest=nums[0]
largest=nums[0]
for num in nums:
    if num>largest:
       
        largest=num
    if num<smallest:
        smallest=num
print('largest',largest)
print('smallest',smallest)
