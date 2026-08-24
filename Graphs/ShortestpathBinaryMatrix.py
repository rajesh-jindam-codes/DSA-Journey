from collections import deque
class Solution:
    def shortestPath(self,grid):
        if grid[0][0]==1:
            return -1
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        distance=[[float('inf') for _ in range(cols)] for _ in range(rows)]
        distance[0][0]=1
        queue.append([1,0,0])
        while len(queue)!=0:
            currDist,i,j=queue.popleft()
            directions=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
            for x,y in directions:
                newI,newJ=i+x,j+y
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if grid[newI][newJ]==1:
                    continue
                newDist=currDist+1
                if newDist<distance[newI][newJ]:
                    if newI==rows-1 and newJ==cols-1:
                        return newDist
                    distance[newI][newJ]=newDist
                    queue.append([newDist,newI,newJ])
        if distance[rows-1][cols-1]==float('inf'):
            return -1
        return [rows-1][cols-1]
grid = [[0,0,0],[1,1,0],[1,1,0]]
obj=Solution()
print(obj.shortestPath(grid))