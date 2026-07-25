def dfs(node,visited,adj,result):
    visited[node]=1
    result.append(node)
    for n in adj[node]:
        if visited[n]==0:
            dfs(n,visited,adj,result)
    return result

n=9
adjMatrix=[
    [],
    [2,8],
    [1,3,4],
    [2],
    [2,5],
    [4,6],
    [5,7],
    [6,8],
    [1,7,9],
    [8]
    
]
visited=[0]*(n+1)
result=[]
dfs(1,visited,adjMatrix,result)
print(result)