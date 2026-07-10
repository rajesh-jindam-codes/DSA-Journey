nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
rows=len(nums)
cols=len(nums[0])
left=0
top=0
right=cols-1
bottom=rows-1
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j],end="  ")
    print("  ")
while left<=right and top<=bottom:
    for i in range(left,right+1):
        result.append(nums[top][i])
    top+=1
    for i in range(top,bottom+1):
        result.append(nums[i][right])
    right-=1
    if left<=right:
        for i in range(right,left-1,-1):
            result.append(nums[bottom][i])
        bottom-=1
    if top<=bottom:
        for i in range(bottom,top-1,-1):
            result.append(nums[i][left])
        left+=1
print(result)