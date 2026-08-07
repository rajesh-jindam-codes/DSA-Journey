class Solution:
    def dfs(self,node,adjList,visited,pathVisited,isSafe):
        visited[node]=1
        pathVisited[node]=1
        for adjNode in adjList[node]:
            if visited[adjNode]==0:
                ans=self.dfs(adjNode,adjList,visited,pathVisited,isSafe)
                if ans==False:
                    return False
            elif pathVisited[adjNode]==1:
                return False
        pathVisited[node]=0
        isSafe[node]=1
        return True
    def safeStates(self,graph):
        V=len(graph)
        visited=[0 for _ in range(V)]
        pathVisited=[0 for _ in range(V)]
        isSafe=[0 for _ in range(V)]
        result=[]
        for i in range(V):
            if visited[i]==0:
                self.dfs(i,graph,visited,pathVisited,isSafe)
        for i in range(V):
            if isSafe[i]==1:
                result.append(i)
        return result
obj=Solution()
graph=[[1,2],[2,3],[5],[0],[5],[],[]]
print(obj.safeStates(graph))