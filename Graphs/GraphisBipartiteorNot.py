class Solution:
    def isBipartite(self,graph):
        totalNodes=len(graph)
        visited=[-1]*totalNodes
        for index in range(0,totalNodes):
            if visited[index]==-1:
                ans=self.dfs(index,visited,graph,0)
                if ans==False:
                    return False
        return True
    def dfs(self,currentNode,visited,graph,color):
        visited[currentNode]=color
        for adjNode in graph[currentNode]:
            if visited[adjNode]!=-1:
                if visited[adjNode]==color:
                    return False
            else:
                ans=self.dfs(adjNode,visited,graph,1-color)
                if ans==False:
                    return False
        return True
obj=Solution()
print(obj.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
