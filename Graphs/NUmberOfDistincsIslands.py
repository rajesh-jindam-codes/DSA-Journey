class Solution:
    def dfs(self,r,c,base_r,base_c,shape,visited,rows,cols,grid):
        visited[r][c]=1
        shape.append((r-base_r,c-base_c))
        for x,y in [(-1,0),(1,0),(0,-1),(0,-1)]:
            newI,newJ=r+x,c+y
            if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                continue
            if grid[newI][newJ]==0:
                continue
            if visited[newI][newJ]==1:
                continue
            self.dfs(newI,newJ,base_r,base_c,shape,visited,rows,cols,grid)
    def countDistincsIslands(self,grid):
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)]for _ in range(rows)]
        uniqueIslands=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    shape=[]
                    self.dfs(r,c,r,c,shape,visited,rows,cols,grid)
                    uniqueIslands.add(tuple(shape))
        return len(uniqueIslands)
obj=Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(obj.countDistincsIslands(grid))