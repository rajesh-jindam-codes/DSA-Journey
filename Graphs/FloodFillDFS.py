from copy import deepcopy
def dfs(i,j,newColor,initialColor,visited,rows,cols):
    if i<0 or i>=rows or j<0 or j>=cols:
        return
    if visited[i][j]!=initialColor:
        return
    if visited[i][j]==initialColor:
        visited[i][j]=newColor
    dfs(i-1,j,newColor,initialColor,visited,rows,cols)
    dfs(i+1,j,newColor,initialColor,visited,rows,cols)
    dfs(i,j-1,newColor,initialColor,visited,rows,cols)
    dfs(i,j+1,newColor,initialColor,visited,rows,cols)
def floodFill(image,sr,sc,color):
    if image[sr][sc]==color:
        return image
    visited=deepcopy(image)
    rows=len(visited)
    initialColor=visited[sr][sc]
    cols=len(visited[0])
    dfs(sr,sc,color,initialColor,visited,rows,cols)
    return visited
image=[[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(image,sr,sc,color))