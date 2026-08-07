from collections import deque
class Solution:
    def safeNodes(self,graph):
        V=len(graph)
        adjList=[[] for _ in range(V)]
        indegrees=[0 for _ in range(V)]
        for node in range(0,V):
            for adjNode in graph[node]:
                adjList[adjNode].append(node)
        for node in range(V):
            for adjNode in adjList[node]:
                indegrees[adjNode]+=1
        queue=deque()
        result=[]
        for node in range(V):
            if indegrees[node]==0:
                queue.append(node)
        while len(queue)!=0:
            node=queue.popleft()
            result.append(node)
            for adjNode in adjList[node]:
                indegrees[adjNode]-=1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        result.sort()
        return result
obj=Solution()
graph=[[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(obj.safeNodes(graph))