def findAllPaths(n,edges,distanceThreshold):
    adjList=[[float('inf') for _ in range(n)]for _ in range(n)]
    for u,v,w in edges:
        adjList[u][v]=w
        adjList[v][u]=w
    for i in range(n):
        adjList[i][i]=0
    for via in range(n):
        for i in range(n):
            for j in range(n):
                if adjList[i][via]!=float('inf') and adjList[via][j]!=float('inf'):
                    adjList[i][j]=min(adjList[i][j],adjList[i][via]+adjList[via][j])
    minNeighbours=n
    city=-1
    for i in range(n):
        count=0
        for j in range(n):
            if adjList[i][j]<=distanceThreshold:
                count+=1
        if count<=minNeighbours:
            minNeighbours=count
            city=i
    return city
n=4
edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold=4
print(findAllPaths(n,edges,distanceThreshold))