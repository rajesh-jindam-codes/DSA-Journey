from collections import deque
def shortestPath(grid):
    if grid[0][0]==1:
        return -1
    rows=len(grid)
    cols=len(grid[0])
    distance=[[float('inf') for _ in range(cols)]for _ in range(rows)]
    distance[0][0]=1
    queue=deque()
    queue.append([1,0,0])
    while len(queue)!=0:
        dist,i,j=queue.popleft()
        for x,y in [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]:
            newI,newJ=i+x,j+y
            if newI<0 and newJ<0 or newI>=rows or newJ>=cols:
                continue
            if grid[newI][newJ]==1:
                continue
            newDist=dist+1
            if newDist<distance[newI][newJ]:
                if newI==rows-1 and newJ==cols-1:
                    return newDist
                distance[newI][newJ]=newDist
                queue.append([newDist,newI,newJ])
    if distance[rows-1][cols-1]==float('inf'):
        return -1
    return distance[rows-1][cols-1]
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPath(grid))
