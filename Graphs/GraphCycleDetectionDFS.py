V=4
edges=[[0,1],[1,2],[2,3],[3,0]]
class Solution:
    def dfs(self,node,parent,visited,adjList):
        visited[node]=1
        for adjNode in adjList[node]:
            if visited[adjNode]==0:
                ans=self.dfs(adjNode,node,visited,adjList)
                if ans==True:
                    return True
                elif visited[adjNode]==1 and adjNode!=parent:
                    return True
        return False
    def isCycle(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited=[0]*V
        for i in range(V):
            if visited[i]==1:
                continue
            if self.dfs(i,-1,visited,adjList)==True:
                return True
        return False
obj=Solution()
print(obj.isCycle(V,edges))