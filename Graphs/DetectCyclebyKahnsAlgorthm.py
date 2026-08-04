from collections import deque

def bfs(V,edges):
    adjList=[[] for _ in range(V)]
    indegrees=[0]*V
    for u,v in edges:
        adjList[u].append(v)
        indegrees[v]+=1
    result=[]
    queue=deque()
    for i in range(V):
        if indegrees[i]==0:
            queue.append(i)
    while len(queue)!=0:
        currNode=queue.popleft()
        result.append(currNode)
        for adjNode in adjList[currNode]:
            indegrees[adjNode]-=1
            if indegrees[adjNode]==0:
                queue.append(adjNode)
    if len(result)==V:
        return False
    return True
V=3
edges=[[0,1],[0,2],[1,2]]
print(bfs(V,edges))
