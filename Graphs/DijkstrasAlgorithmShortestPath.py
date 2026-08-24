import heapq
class Solution:
    def dijkstras(self,V,edges,sec):
        adjList=[[] for _ in range(V)]
        for u,v,w in edges:
            adjList[u].append([v,w])
            adjList[v].append([u,w])
        distance=[float('inf') for _ in range(V)]
        distance[src]=0
        queue=[[0,src]]
        while len(queue)!=0:
            currDist,node=heapq.heappop(queue)
            if currDist>distance[node]:
                continue
            for adjNode,weight in adjList[node]:
                distTrav=currDist+weight
                if distTrav<distance[adjNode]:
                    distance[adjNode]=distTrav
                    queue.append([distTrav,adjNode])
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
