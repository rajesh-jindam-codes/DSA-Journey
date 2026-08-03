from collections import deque
class Solution:
    def bfs(self,V,edges):
        indegrees=[0]*V
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            indegrees[v]+=1
        queue=deque()
        result=[]
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
        return result
V=3
edges=[[0,1],[0,2],[1,2]]
obj=Solution()
print(obj.bfs(V,edges))