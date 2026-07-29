from collections import deque
class Solution:
    def bfs(self,i,j,visited,grid):
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        queue.append((i,j))
        visited[i][j]=1
        while len(queue)!=0:
            x,y=queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                newI,newJ=x+dx,y+dy
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if grid[newI][newJ]=='0':
                    continue
                if visited[newI][newJ]=='1':
                    continue
                visited[newI][newJ]=1
                queue.append((newI,newJ))
    def numIslands(self,grid):
        count=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and visited[r][c]==0:
                    count+=1
                self.bfs(r,c,visited,grid)
        return count
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj=Solution()
print(obj.numIslands(grid))