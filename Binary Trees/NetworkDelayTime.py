import heapq
from collections import defaultdict
class Solution:
    def networkDelaytime(self,times,n,k):
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist={i:float('inf') for i in range(1,n+1)}
        dist[k]=0
        heap=[(0,k)]
        while heap:
            time,u=heapq.heappop(heap)
            if time>dist[u]:
                continue
            for v,w in graph[u]:
                if time+w<dist[v]:
                    dist[v]=time+w
                    heapq.heappush(heap,(dist[v],v))
        maxTime=max(dist.values())
        return maxTime if maxTime<float('inf') else -1
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
obj=Solution()
print(obj.networkDelaytime(times,n,k))