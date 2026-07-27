from collections import deque
class Solution:
    def numofEnclaves(self,grid):
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if (r==0 or c==0 or r>=rows-1 or c>=cols-1) and grid[r][c]==1:
                    queue.append((r,c))
                    grid[r][c]='S'
        while len(queue)!=0:
            i,j=queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                newI,newJ=i+dx,j+dy
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if grid[newI][newJ]!=1:
                    continue
                grid[newI][newJ]='S'
                queue.append((newI,newJ))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    count+=1
                elif grid[r][c]=='S':
                    grid[r][c]=1
        return count
grid=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
obj=Solution()
print(obj.numofEnclaves(grid))