from copy import deepcopy
from collections import deque
def floodFill(sr,sc,image,color):
    if image[sr][sc]==color:
        return image
    visited=deepcopy(image)
    rows=len(visited)
    cols=len(visited[0])
    initialColor=visited[sr][sc]
    queue=deque()
    queue.append((sr,sc))
    while len(queue)!=0:
        i,j=queue.popleft()
        visited[i][j]=color
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            newI=i+dx
            newJ=j+dy
            if newI>=rows or newI<0 or newJ<0 or newJ>=cols:
                continue
            if visited[newI][newJ]!=initialColor:
                continue
            queue.append((newI,newJ))
    return visited
image=[[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(sr,sc,image,color))