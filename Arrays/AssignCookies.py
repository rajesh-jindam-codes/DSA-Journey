greed=[1,3,2,4,5,6]
cookie=[2,4,6,3,1,2,5,9,7]
greed.sort()
cookie.sort()
n=len(greed)
m=len(cookie)
left=0
right=0
count=0
while left<n and right<m:
    if greed[left]<=cookie[right]:
        count+=1
        left+=1
        
    right+=1
print(count)