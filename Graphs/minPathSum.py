def minPathSum(grid):
    rows=len(grid)
    cols=len(grid[0])
    def solve(i,j):
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return float('inf')
        up=solve(i-1,j)
        left=solve(i,j-1)
        return grid[i][j]+min(up,left)
    return solve(rows-1,cols-1)
grid=[[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
