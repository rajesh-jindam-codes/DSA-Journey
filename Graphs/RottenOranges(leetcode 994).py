from copy import deepcopy
from collections import deque
def oranges(grid):
    rows=len(grid)
    cols=len(grid[0])
    queue=deque()
    freshCount=0
    gridCopy=deepcopy(grid)
    for r in range(rows):
        for c in range(cols):
            if gridCopy[r][c]==2:
                queue.append((r,c))
            elif gridCopy[r][c]==1:
                freshCount+=1
    minutes=0
    while len(queue)!=0 and freshCount>0:
        minutes+=1
        totalRotten=len(queue)
        for _ in range(totalRotten):
            i,j =queue.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                newI,newJ=i+dx,j+dy
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if gridCopy[newI][newJ]==0 or gridCopy[newI][newJ]==2:
                    continue
                freshCount-=1
                gridCopy[newI][newJ]=2
                queue.append((newI,newJ))
    if freshCount>0:
        return -1
    return minutes
grid=[[2,1,1],[1,1,0],[0,1,1]]
print(oranges(grid))