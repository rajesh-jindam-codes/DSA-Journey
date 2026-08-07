from collections import deque
class Solution:
    def SafeNodes(self,graph):
        V=len(graph)
        adjList=[[] for _ in range(V)]
        indegrees=[0 for _ in range(V)]
        for node in range(V):
            for adjNode in adjList[node]:
                adjList[adjNode].append(node)
        for node in range(V):
            for adjNode in adjList[node]: 
                indegrees[adjNode]+=1
        queue=deque()
        result=[]
        for node in range(0,V):
            if indegrees[node]==0:
                queue.append(node)
        while len(queue)!=0:

            for node in range(0,V):
                currNode=queue.popleft()
                result.append(currNode)
                for adjNode in adjList[currNode]:
                    indegrees[adjNode]-=1
                    if indegrees[adjNode]==0:
                        queue.append(adjNode)
        result.sort()
        return result
# class SOlution
obj=Solution()
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(obj.SafeNodes(graph))