class Solution:
    def cycleDetection(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            # adjList[v].append(u)
        visited=[-1 for _ in range(V)] 
        queue=[]
        for i in range(V):
            if visited[i]==-1:
                queue.append(i)
                visited[i]=0
                while queue:
                    currNode=queue.pop(0)
                    for adjNode in adjList[currNode]:
                        if visited[adjNode]==-1:
                            queue.append(adjNode)
                            visited[adjNode]=0
                        elif visited[adjNode]==0:
                            return True
                    visited[currNode]=1
        return False
obj=Solution()
V=4
edges=[[0,1],[1,2],[0,2],[2,3]]
print(obj.cycleDetection(V,edges))