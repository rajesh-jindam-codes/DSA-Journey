import heapq
def shortestPath(n,m,edges):
    adjList=[[] for _ in range(n+1)]
    for u,v,w in edges:
        adjList[u].append([v,w])
        adjList[v].append([u,w])
    distance=[float('inf')]*(n+1)
    distance[1]=0
    pq=[]
    parent=list(range(n+1))
    heapq.heappush(pq,(0,1))
    while len(pq)!=0:
        currDist,node=heapq.heappop(pq)
        if currDist!=distance[node]:
            continue
        for adjNode,w in adjList[node]:
            newDist=currDist+w
            if newDist<distance[adjNode]:
                distance[adjNode]=newDist
                heapq.heappush(pq,(newDist,adjNode))
                parent[adjNode]=node
    if distance[n]==float('inf'):
        return -1
    path=[]
    node=n
    while parent[node]!=node:
        path.append(node)
        node=parent[node]
    path.append(1)
    path.reverse()
    return path
n = 5
m = 6
edges = [
    [1, 2, 2], [2, 5, 5],
    [2, 3, 1], [1, 4, 1],
    [4, 3, 3], [3, 5, 1]
]
print(shortestPath(n,m,edges))
