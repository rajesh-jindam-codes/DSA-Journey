class Solution:
    def allPathsSourceTarget(self, graph,src,target):
        n=len(graph)
        result=[]

        def dfs(node,path):
            if node==target:
                result.append(path[:])
                return
            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour,path)
                path.pop()
        dfs(src,[src])
        return result
obj=Solution()
graph=[[1,2],[3],[3],[]]
src=0
target=3
print(obj.allPathsSourceTarget(graph,src,target))