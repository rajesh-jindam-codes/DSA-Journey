from collections import deque
V=4
edges=[[0,1],[0,2],[1,2],[2,3]]
class Solution:
    def isCycle(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited=[0]*V
        for i in range(V):
            if visited[i]==1:
                continue
            queue=deque()
            queue.append((i,-1))
            visited[i]=1
            while len(queue)!=0:
                node,parent=queue.popleft()
                for adjNode in adjList[node]:
                    if visited[adjNode]==0:
                        visited[adjNode]=1
                        queue.append((adjNode,node))
                    else:
                        if adjNode!=parent:
                            return True
        return False
obj=Solution()
print(obj.isCycle(V,edges))