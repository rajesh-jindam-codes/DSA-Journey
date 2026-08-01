class Solution:
    def dfs(self,currNode,visited,stack,adjList):
        visited[currNode]=1
        for adjNode in adjList[currNode]:
            if visited[adjNode]==0:
                self.dfs(adjNode,visited,stack,adjList)
            stack.append(currNode)
    def topoSort(self,V,edges):
        adjList=[[] for _ in range(V)]
        visited=[0 for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
        stack=[]
        for i in range(V):
            if visited[i]==0:
                self.dfs(i,visited,stack,adjList)
        return stack[::-1]
obj=Solution()
V=6
edges=[[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
print(obj.topoSort(V,edges))
