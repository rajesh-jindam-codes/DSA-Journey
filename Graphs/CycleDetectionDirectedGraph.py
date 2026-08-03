class Solution:
    def dfs(self,node,visited,pathVisited,adjList):
        visited[node]=1
        pathVisited[node]=1
        for adjNode in adjList[node]:
            if visited[adjNode]==0:
                x=self.dfs(adjNode,visited,pathVisited,adjList)
                if x==True:
                    return True
                elif pathVisited[adjNode]==1:
                    return True
        pathVisited[node]=0
        return False

    def isCycle(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u, v in edges:
            adjList[u].append(v)
        visited=[0]*V
        pathVisited=[0]*V
        for i in range(V):
            if visited[i]==0:
                ans=self.dfs(i,visited,pathVisited,adjList)
                if ans==True:
                    return True
        return False
obj=Solution()
V=4
edges=[[0,1],[1,2],[0,2],[2,3]]
print(obj.isCycle(V,edges))