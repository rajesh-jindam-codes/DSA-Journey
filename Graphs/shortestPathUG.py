from collections import deque
V=4
edges=[[0,1],[0,2],[1,2],[2,3]]
src=1
class Solution:
    def shortestPath(self,V,edges,src):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        queue=deque()
        queue.append([src,0])
        distance=[-1]*V
        distance[src]=0
        while len(queue)!=0:
            node,dist=queue.popleft()
            for adjNode in adjList[node]:
                if distance[adjNode]==-1:
                    distance[adjNode]=dist+1
                    queue.append([adjNode,dist+1])
        return distance
obj=Solution()
print(obj.shortestPath(V,edges,src))

        