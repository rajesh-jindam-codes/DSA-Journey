from collections import deque
def numberofWeights(edges):
    n=len(edges)+1
    MOD=10**9+7
    adjList=[[] for _ in range(n+1)]
    for u,v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    visited=[0 for _ in range(n+1)]
    queue=deque([(1,0)])
    visited[1]=1
    maxDepth=0
    while queue:
        node,depth=queue.popleft()
        maxDepth=max(maxDepth,depth)
        for nei in adjList[node]:
            if visited[nei]==0:
                visited[nei]=1
                queue.append((nei,depth+1))
    return pow(2,maxDepth-1,MOD)
edges = [[1,2],[1,3],[3,4],[3,5]]
print(numberofWeights(edges))