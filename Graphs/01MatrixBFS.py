from collections import deque
matrix= [[0,0,0],[0,1,0],[1,1,1]]
class Solution:
    def bfs(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        queue=deque()
        visited=[[0 for _ in range(cols)]for _ in range(rows)]
        distance=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    queue.append([r,c,0])
                    visited[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                newI,newJ=i+dx,j+dy
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if visited[newI][newJ]==1:
                    continue
                queue.append([newI,newJ,d+1])
                visited[newI][newJ]=1
        return distance 
obj=Solution()
print(obj.bfs(matrix))