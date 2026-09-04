import heapq
n=7
roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
def countPaths(n,roads):
    adjList=[[] for _ in range(n)]
    MOD=10**9+7
    for u,v,wt in roads:
        adjList[u].append([v,wt])
        adjList[v].append([u,wt])
    distance=[float('inf') for _ in range(n)]
    ways=[0 for _ in range(n)]
    distance[0]=0
    ways[0]=1
    queue=[[0,0]]
    while queue:
        dist,node=heapq.heappop(queue)
        if dist!=distance[node]:
            continue
        for adjNode,weight in adjList[node]:
            newDist=dist+weight
            if newDist<distance[adjNode]:
                distance[adjNode]=newDist
                heapq.heappush(queue,[newDist,adjNode])
                ways[adjNode]=ways[node]
            elif newDist==distance[adjNode]:
                ways[adjNode]+=ways[node]
    return ways[n-1] % MOD

print(countPaths(n,roads))