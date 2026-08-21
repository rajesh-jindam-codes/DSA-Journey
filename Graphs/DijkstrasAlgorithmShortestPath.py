import heapq
class Solution:
    def dijkstras(self,V,edges,src):
        adjList=[[] for _ in range(V)]
        for u,v,d in edges:
            adjList[u].append([v,d])
            adjList[v].append([u,d])
        distance=[float('inf') for _ in range(V)]
        distance[src]=0
        prioQueue=[[0,src]]
        while len(prioQueue)!=0:
            currDist,node=heapq.heappop(prioQueue)
            if currDist>distance[node]:
                continue
            for adjNode,weight in adjList[node]:
                distTrav=currDist+weight
                if distTrav<distance[adjNode]:
                    distance[adjNode]=distTrav
                    prioQueue.append([distTrav,adjNode])
        return distance
V = 5

edges = [
    [0, 1, 2],
    [0, 2, 4],
    [1, 2, 1],
    [1, 3, 7],
    [2, 4, 3],
    [3, 4, 1]
]

src = 0
obj=Solution()
print(obj.dijkstras(V,edges,src))
