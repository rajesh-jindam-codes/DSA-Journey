class Solution:
    def dfs(self,node,stack,visited,adjList):
        visited[node]=1
        for adjNode,w in adjList[node]:
            if visited[adjNode]==0:
                self.dfs(adjNode,stack,visited,adjList)
        stack.append(node)
    def shortestPath(self,V,edges):
        adjList=[[] for _ in range(V)]
        for u,v,w in edges:
            adjList[u].append((v,w))
        stack=[]
        visited=[0]*V
        for i in range(V):
            if visited[i]==0:
                self.dfs(i,stack,visited,adjList)
        distance=[float('inf')]*V
        distance[0]=0
        while stack:
            node=stack.pop()
            if distance[node]==float('inf'):
                continue
            for adjNode,w in adjList[node]:
                newD=distance[node]+w
                if newD<distance[adjNode]:
                    distance[adjNode]=newD
        for i in range(V):
            if distance[i]==float('inf'):
                distance[i]=-1
        return distance

V = 4
edges = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 3],
    [2, 3, 4]
]

obj = Solution()
print(obj.shortestPath(V, edges))