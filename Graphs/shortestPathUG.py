from collections import deque
class Solution:
    def shortestPath(self,V,edges,src):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        distance=[-1]*V
        queue=deque()
        queue.append([src,0])
        distance[src]=0
        while queue:
            node,dist=queue.popleft()
            for adjNode in adjList[node]:
                if distance[adjNode]==-1:
                    distance[adjNode]=dist+1
                    queue.append([adjNode,dist+1])
        return distance
obj=Solution()
V=4
edges=[[0,1],[0,2],[1,2],[2,3]]
src=1
print(obj.shortestPath(V,edges,src))

        