nums=[[1,2,3],[4,0,6],[0,7,8]]
r=len(nums)
c=len(nums[0])
rowTrack=[0 for _ in range(r)]
colTrack=[0 for _ in range(c)]
for i in range(r):
    for j in range(c):
        if nums[i][j]==0:
            rowTrack[i]=float('inf')
            colTrack[j]=float('inf')
for i in range(r):
    for j in range(c):
        if rowTrack[i]==float('inf') or colTrack[j]==float('inf'):
            nums[i][j]=0
        print(nums[i][j],end=" ")
    print(" ")