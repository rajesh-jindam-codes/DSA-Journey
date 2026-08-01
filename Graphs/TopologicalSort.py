class Solution:
    def dfs(self,currNode,visited,stack,adjList):
        visited[currNode]=1
        for adjNode in adjList[currNode]:
            if visited[adjNode]==-1:
                self.dfs(adjNode,visited,stack,adjList)
        stack.append(currNode)
    def topoSort(self,V,edges):
        adjList=[[] for _ in range(V)]
        visited=[-1 for _ in range(V)] 
        for u,v in edges:
            adjList[u].append(v)
            # adjList[v].append(u)
        stack=[]
        for i in range(V):
            if visited[i]==-1:
                self.dfs(i,visited,stack,adjList)
        return stack[::-1]
obj=Solution()
print(obj.topoSort(6,[[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]))